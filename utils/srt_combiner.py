#!/usr/bin/env python3
"""
SRT Combiner Utility

This script combines multiple SRT subtitle files in a user-specified order
with proper timestamp adjustments based on either manual durations or
automatically extracted durations from corresponding video files.
"""

import os
import sys
import argparse
from typing import List, Optional


class SubtitleEntry:
    """Represents a single subtitle entry in an SRT file."""
    def __init__(self, index: int, start_time: str, end_time: str, text: str):
        self.index = index
        self.start_time = start_time
        self.end_time = end_time
        self.text = text

    def shift_time(self, offset_ms: int) -> None:
        """Shift the start and end times by the given offset in milliseconds."""
        self.start_time = self._add_time_offset(self.start_time, offset_ms)
        self.end_time = self._add_time_offset(self.end_time, offset_ms)

    def _add_time_offset(self, time_str: str, offset_ms: int) -> str:
        """Add milliseconds offset to a timestamp in format HH:MM:SS,mmm."""
        h, m, s = time_str.replace(',', '.').split(':')
        seconds = int(h) * 3600 + int(m) * 60 + float(s)
        new_seconds = seconds + (offset_ms / 1000)
        
        hours = int(new_seconds // 3600)
        minutes = int((new_seconds % 3600) // 60)
        seconds = new_seconds % 60
        
        return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}".replace('.', ',')

    def __str__(self) -> str:
        return f"{self.index}\n{self.start_time} --> {self.end_time}\n{self.text}\n"


def parse_srt_file(srt_file_path: str) -> List[SubtitleEntry]:
    """Parse an SRT file into a list of SubtitleEntry objects."""
    if not os.path.exists(srt_file_path):
        print(f"Warning: SRT file not found: {srt_file_path}")
        return []
    
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    
    entries = []
    blocks = content.split('\n\n')
    
    for block in blocks:
        if not block.strip():
            continue
        
        lines = block.split('\n')
        if len(lines) < 3:
            continue
            
        index = int(lines[0])
        time_line = lines[1]
        text = '\n'.join(lines[2:])
        
        start_time, end_time = time_line.split(' --> ')
        
        entries.append(SubtitleEntry(index, start_time, end_time, text))
    
    return entries


def write_srt_file(entries: List[SubtitleEntry], output_file: str) -> None:
    """Write a list of SubtitleEntry objects to an SRT file."""
    # Re-index the entries
    for i, entry in enumerate(entries, 1):
        entry.index = i
        
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(str(entry) for entry in entries))


def get_srt_duration(srt_file_path: str) -> int:
    """
    Get the duration of an SRT file in milliseconds.
    Returns the timestamp of the last subtitle's end time.
    """
    entries = parse_srt_file(srt_file_path)
    if not entries:
        return 0
    
    last_entry = entries[-1]
    h, m, s = last_entry.end_time.replace(',', '.').split(':')
    duration_seconds = int(h) * 3600 + int(m) * 60 + float(s)
    return int(duration_seconds * 1000)


def extract_video_duration(video_file: str) -> Optional[int]:
    """
    Extract duration from video file in milliseconds.
    Returns None if video file doesn't exist or if moviepy is not available.
    """
    if not os.path.exists(video_file):
        return None
    
    try:
        # Import here to make it optional
        from moviepy.video.io.VideoFileClip import VideoFileClip
        with VideoFileClip(video_file) as clip:
            return int(clip.duration * 1000)
    except ImportError:
        print("Warning: moviepy not installed. Cannot extract video duration.")
        return None
    except Exception as e:
        print(f"Error extracting video duration: {e}")
        return None


def combine_subtitles(srt_files: List[str], durations: List[int], output_file: str) -> None:
    """
    Combine multiple SRT files, adjusting timestamps based on durations.
    
    Args:
        srt_files: List of SRT file paths
        durations: List of durations for each subtitle segment (in milliseconds)
        output_file: Output SRT file path
    """
    if len(srt_files) != len(durations):
        raise ValueError("Number of SRT files must match number of duration values")
    
    all_entries = []
    time_offset = 0
    
    for i, srt_file in enumerate(srt_files):
        entries = parse_srt_file(srt_file)
        
        # Shift time for all entries in this file
        for entry in entries:
            entry.shift_time(time_offset)
        
        all_entries.extend(entries)
        time_offset += durations[i]
    
    write_srt_file(all_entries, output_file)


def main():
    parser = argparse.ArgumentParser(description='Combine multiple SRT subtitle files with proper timing adjustments')
    parser.add_argument('-s', '--subtitles', nargs='+', required=True, 
                        help='List of SRT files in the desired order')
    parser.add_argument('-d', '--durations', nargs='+', type=int, 
                        help='List of durations in milliseconds for each subtitle segment')
    parser.add_argument('-v', '--videos', nargs='+', 
                        help='List of video files to extract durations from')
    parser.add_argument('-o', '--output', required=True, 
                        help='Output SRT file path')
    parser.add_argument('--use-srt-duration', action='store_true',
                        help='Use the last subtitle time as the duration of each segment')
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.durations and len(args.durations) != len(args.subtitles):
        parser.error("If durations are provided, there must be one for each SRT file")
        
    if args.videos and len(args.videos) != len(args.subtitles):
        parser.error("If videos are provided, there must be one for each SRT file")
    
    # Determine durations based on provided options
    durations = []
    
    if args.durations:
        durations = args.durations
    elif args.videos:
        print("Extracting durations from videos...")
        for video in args.videos:
            duration = extract_video_duration(video)
            if duration is None:
                print(f"Error: Could not extract duration from {video}")
                return 1
            durations.append(duration)
    elif args.use_srt_duration:
        print("Using SRT end times as durations...")
        for srt in args.subtitles:
            durations.append(get_srt_duration(srt))
    else:
        parser.error("Please specify either --durations, --videos, or --use-srt-duration")
    
    try:
        print(f"Combining {len(args.subtitles)} SRT files...")
        combine_subtitles(args.subtitles, durations, args.output)
        print(f"Combined SRT file written to: {args.output}")
        print("Done!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    return 0


if __name__ == "__main__":
    sys.exit(main())