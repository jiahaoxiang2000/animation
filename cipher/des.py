from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.openai import OpenAIService

class DESIntroScene(VoiceoverScene):
    """Introduction to DES with basic overview"""

    def construct(self):
        self.set_speech_service(GTTSService())

        # Title
        title = Text("Data Encryption Standard (DES)",
                     font_size=48, color=BLUE_D)
        with self.voiceover("Welcome to this explanation of the Data Encryption Standard, or DES."):
            self.play(Write(title))
            self.play(title.animate.to_edge(UP).shift(DOWN * 0.3))

        # Overview of DES - Show this immediately after the title
        des_overview = BulletedList(
            "Developed in the 1970s",
            "Block size: 64 bits",
            "Key size: 56 bits (with 8 parity bits)",
            "16 rounds of processing",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)

        with self.voiceover("DES was developed in the 1970s as the first publicly available encryption algorithm standardized by the US government. It quickly became one of the most widely used encryption methods worldwide."):
            self.play(FadeIn(des_overview[0]))

        with self.voiceover("Let's understand the basic parameters of DES as an encryption algorithm. It has a block size of 64 bits and a key size of 56 bits with 8 parity bits."):
            self.play(FadeIn(des_overview[1:3]))

        with self.voiceover("The algorithm processes data through 16 rounds of encryption operations, making it highly secure for its time."):
            self.play(FadeIn(des_overview[3]))

        # Mathematical explanation of symmetric-key cipher
        symmetric_key_formula = MathTex(
            r"C = E_K(P)", r"\quad", r"P = D_K(C)"
        ).scale(0.9)

        symmetric_key_labels = VGroup(
            Text("Encryption", font_size=24),
            Text("Decryption", font_size=24)
        )
        symmetric_key_labels[0].next_to(
            symmetric_key_formula[0], DOWN, buff=0.2)
        symmetric_key_labels[1].next_to(
            symmetric_key_formula[2], DOWN, buff=0.2)

        mathematical_group = VGroup(
            symmetric_key_formula, symmetric_key_labels)
        mathematical_group.next_to(des_overview, DOWN, buff=0.6)

        with self.voiceover("DES is a symmetric-key cipher, which means the same key is used for both encryption and decryption. We can represent this mathematically."):
            self.play(
                des_overview.animate.scale(0.8).to_edge(
                    LEFT).shift(RIGHT * 0.5),
                Write(symmetric_key_formula),
                Write(symmetric_key_labels)
            )

        # Block cipher diagram
        block_cipher_diagram = VGroup(
            Rectangle(height=1, width=1.5, stroke_color=BLUE).set_fill(
                BLUE_E, opacity=0.3),
            Text("Block\nCipher", font_size=20)
        )
        block_cipher_diagram[1].move_to(block_cipher_diagram[0])

        arrows = VGroup(
            Arrow(LEFT * 3, block_cipher_diagram[0].get_left(), buff=0.2),
            Arrow(block_cipher_diagram[0].get_right(), RIGHT * 3, buff=0.2)
        )

        plaintext = Text("Plaintext\n(64 bits)",
                         font_size=20).next_to(arrows[0], LEFT)
        ciphertext = Text("Ciphertext\n(64 bits)",
                          font_size=20).next_to(arrows[1], RIGHT)

        key_arrow = Arrow(
            UP * 1.5, block_cipher_diagram[0].get_top(), buff=0.2)
        key_text = Text("Key (56 bits)", font_size=20).next_to(key_arrow, UP)

        cipher_diagram = VGroup(
            block_cipher_diagram, arrows, plaintext, ciphertext, key_arrow, key_text
        )
        cipher_diagram.scale(0.8).to_edge(RIGHT).shift(LEFT * 0.5 + UP * 0.3)

        with self.voiceover("As a block cipher, DES processes fixed-size blocks of data - specifically 64 bits at a time - using a 56-bit key."):
            self.play(Create(cipher_diagram))

        with self.voiceover("The input plaintext is divided into 64-bit blocks, and each block is encrypted separately using the same key to produce 64-bit blocks of ciphertext.") as track:
            self.play(
                Indicate(plaintext, color=GREEN),
                Indicate(key_text, color=YELLOW),
                Indicate(block_cipher_diagram, color=BLUE),
                Indicate(ciphertext, color=RED),
                run_time=track.duration
            )

        with self.voiceover("Let's take a closer look at how DES works internally.") as track:
            self.play(
                FadeOut(title),
                FadeOut(des_overview),
                FadeOut(mathematical_group),
                FadeOut(cipher_diagram),
                run_time=track.duration
            )


class DESStructureScene(VoiceoverScene):
    """Shows the overall structure of the DES algorithm"""

    def construct(self):
        # self.set_speech_service(
        #     OpenAIService(
        #         voice="fable",
        #         model="tts-1-hd",
        #     )
        # )
        self.set_speech_service(GTTSService())
        
        title = Text("DES Algorithm Structure", font_size=48, color=BLUE_D).to_edge(UP)
        
        with self.voiceover("Let's look at the overall structure of the DES algorithm.") as tracker:
            self.play(Write(title), run_time=2)
        
        # First introduce the encryption/decryption structure
        encryption_box = Rectangle(height=4, width=3.5, color=BLUE_C)
        encryption_title = Text("Encryption/Decryption", font_size=28, color=BLUE_C).next_to(encryption_box, UP, buff=0.2)
        encryption_group = VGroup(encryption_box, encryption_title).move_to(ORIGIN)
        
        with self.voiceover("First, let's examine the encryption and decryption structure, which processes the data.") as tracker:
            self.play(
                Create(encryption_box, run_time=1.5),
                FadeIn(encryption_title, run_time=1.5),
                run_time=tracker.duration
            )
        
        # Encryption/Decryption structure details - Using LaTeX for IP and IP^-1
        enc_structure = VGroup(
            Tex("Initial Permutation ($IP$)", font_size=20),
            Text("16 Feistel Rounds", font_size=20),
            Tex("Final Permutation ($IP^{-1}$)", font_size=20)
        ).arrange(DOWN, buff=0.5).scale(0.9).move_to(encryption_box)
        
        with self.voiceover("The encryption structure consists of an initial permutation, followed by sixteen Feistel rounds, and finally a final permutation. The decryption process is simply the reverse, using the subkeys in opposite order.") as tracker:
            # Stagger the appearance of each component for better visual flow
            self.play(
                AnimationGroup(
                    Write(enc_structure[0]),
                    Write(enc_structure[1]),
                    Write(enc_structure[2]),
                    lag_ratio=0.3  # Creates staggered effect
                ),
                run_time=min(tracker.duration * 0.8, 3)
            )
        
        # Now move encryption to the left to make room for key schedule
        with self.voiceover("However, to complete the DES algorithm, we need another essential component.") as tracker:
            self.play(
                encryption_group.animate.shift(LEFT * 3.5),
                enc_structure.animate.shift(LEFT * 3.5),
                run_time=tracker.duration
            )
        
        # Now introduce the key schedule
        key_schedule_box = Rectangle(height=4, width=3.5, color=YELLOW_C)
        key_schedule_title = Text("Key Schedule", font_size=28, color=YELLOW_C).next_to(key_schedule_box, UP, buff=0.2)
        key_schedule_group = VGroup(key_schedule_box, key_schedule_title).shift(RIGHT * 3.5)
        
        with self.voiceover("The second main component is the key schedule, which generates subkeys for each round.") as tracker:
            self.play(
                Create(key_schedule_box, run_time=1.5),
                FadeIn(key_schedule_title, run_time=1.5),
                run_time=tracker.duration
            )
        
        # Key Schedule details - Using LaTeX for PC-1 and PC-2 
        key_structure = VGroup(
            Tex("Permuted Choice 1 ($PC_{1}$)", font_size=20),
            Text("Key Rotation", font_size=20),
            Tex("Permuted Choice 2 ($PC_{2}$)", font_size=20)
        ).arrange(DOWN, buff=0.5).scale(0.9).move_to(key_schedule_box)
        
        with self.voiceover("The key schedule transforms the original 56-bit key through permutation and bit rotations to generate sixteen 48-bit subkeys, one for each round.") as tracker:
            # Stagger the appearance of each component
            self.play(
                AnimationGroup(
                    Write(key_structure[0]),
                    Write(key_structure[1]),
                    Write(key_structure[2]),
                    lag_ratio=0.3
                ),
                run_time=min(tracker.duration * 0.8, 3)
            )
        
        # Connection between the two components
        connection_arrow = Arrow(key_schedule_box.get_left(), encryption_box.get_right(), 
                                color=GREEN, buff=0.1).shift(UP * 1)
        connection_text = Text("Subkeys", font_size=24, color=GREEN).next_to(connection_arrow, UP, buff=0.1)
        
        with self.voiceover("These components work together. The key schedule generates subkeys that are fed into each round of the encryption process.") as tracker:
            # Animate the connection with growing arrow effect
            self.play(
                GrowArrow(connection_arrow, run_time=1.5),
                Write(connection_text, run_time=1.2),
                run_time=min(tracker.duration, 2.5)  # Ensure animation doesn't exceed voiceover
            )
        
        # Highlight components when discussing them
        with self.voiceover("Let's examine these components in more detail, starting with the initial permutation.") as tracker:
            self.play(
                Indicate(enc_structure[0], color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        with self.voiceover("The heart of DES is its Feistel round structure, which is executed sixteen times.") as tracker:
            self.play(
                Indicate(enc_structure[1], color=YELLOW, scale_factor=1.1),
                Flash(enc_structure[1], color=YELLOW, line_length=0.2, flash_radius=0.5),
                run_time=tracker.duration
            )
        
        with self.voiceover("After the rounds, a final permutation is applied, which is the exact inverse of the initial permutation.") as tracker:
            self.play(
                Indicate(enc_structure[2], color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        with self.voiceover("The key schedule begins with Permuted Choice 1, which selects 56 bits from the original 64-bit key.") as tracker:
            self.play(
                Indicate(key_structure[0], color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        with self.voiceover("Next, these bits are rotated according to a predefined schedule, with different rotation amounts for each round.") as tracker:
            self.play(
                Indicate(key_structure[1], color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        with self.voiceover("Finally, Permuted Choice 2 selects 48 bits from the rotated key to form each round's subkey.") as tracker:
            self.play(
                Indicate(key_structure[2], color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        # Emphasize the connection again
        with self.voiceover("The generated subkeys are crucial as they provide the cryptographic strength to each round of encryption.") as tracker:
            self.play(
                Indicate(connection_arrow, color=YELLOW, scale_factor=1.1),
                Indicate(connection_text, color=YELLOW, scale_factor=1.1),
                run_time=tracker.duration
            )
        
        # Update the fade-out voiceover to indicate what's coming next
        with self.voiceover("Now that we've seen the overall structure of DES, let's explore the details of both the encryption process and the key schedule.") as tracker:
            # Clean up for next scene with a nice fade out effect
            self.play(
                *[FadeOut(mob, run_time=1.5) for mob in self.mobjects],
                run_time=tracker.duration
            )


class DESKeyScheduleScene(VoiceoverScene):
    """Illustrates the DES key schedule process with bit-level transformations"""

    def construct(self):
        self.set_speech_service(GTTSService())

        # Title
        title = Text("DES Key Schedule", font_size=48, color=YELLOW_D).to_edge(UP)
      
        with self.voiceover("Let's explore the DES key schedule process in detail, showing how the bits are transformed at each step."):
            self.play(Write(title))
            self.wait(0.5)

        # Initial 64-bit key visualization
        initial_key = "0001001100110100010101110111100110011011101111001101111111110001"
        key_text = Tex(r"\textbf{Original 64-bit Key:}", font_size=24).shift(UP * 2 + LEFT * 5)
        key_bits = VGroup(*[Text(bit, font_size=20) for bit in initial_key])
        key_bits.arrange_in_grid(rows=2, buff=0.2).next_to(key_text, RIGHT)
        
        with self.voiceover("We start with a 64-bit key. Here's an example key shown in binary."):
            self.play(
                Write(key_text),
                LaggedStartMap(FadeIn, key_bits, lag_ratio=0.1)
            )

        # PC-1 Transformation
        pc1_title = Text("Permuted Choice 1 (PC-1)", font_size=32, color=YELLOW).shift(UP)
        pc1_formula = MathTex(
            r"K_{56} = \text{PC}_1(K_{64})", r"\text{ (Selects 56 bits, drops 8 parity bits)}"
        ).next_to(pc1_title, DOWN)
        
        with self.voiceover("First, Permuted Choice 1 selects 56 bits from the original key, dropping the 8 parity bits."):
            self.play(
                Write(pc1_title),
                Write(pc1_formula)
            )

        # Visualize PC-1 transformation with bit movement
        pc1_output = "11110000110011001010101011110101010101100110011110001111"
        pc1_bits = VGroup(*[Text(bit, font_size=20, color=YELLOW) for bit in pc1_output])
        pc1_bits.arrange_in_grid(rows=2, buff=0.2).shift(DOWN)
        
        # Create separate groups for C0 and D0 for highlighting
        c0_bits = pc1_bits[:28]  # First 28 bits
        d0_bits = pc1_bits[28:]  # Last 28 bits
        
        with self.voiceover("Watch as the bits are rearranged according to the PC-1 permutation table.") as track:
            self.play(
                *[Transform(
                    key_bits[i].copy(),
                    pc1_bits[j],
                    path_arc=PI/2
                ) for i, j in zip(range(64), range(56))],
                run_time=track.duration
            )
            
            # Clean up the initial key display to reduce clutter
            self.play(
                FadeOut(key_text),
                FadeOut(key_bits)
            )

        # Split into C and D blocks using LaTeX with clearer visuals
        c0_title = MathTex(r"C_0 = K_{56}[0:28]", font_size=26, color=RED)
        d0_title = MathTex(r"D_0 = K_{56}[28:56]", font_size=26, color=BLUE)
        
        
        with self.voiceover("The 56-bit key is then split into two 28-bit halves, called C-zero and D-zero."):
            # Position titles to the left of their respective bit groups
            c0_title.next_to(c0_bits, LEFT, buff=0.5)
            d0_title.next_to(d0_bits, LEFT, buff=0.5)
            
            self.play(
            Write(c0_title),
            Write(d0_title)
            )
            
            # No need to move the bits, just indicate them
            self.play(
            FadeOut(pc1_title),
            FadeOut(pc1_formula)
            )
            
            # Highlight each half
            self.play(
            Indicate(c0_bits, color=RED, scale_factor=1.2),
            run_time=1
            )
            self.play(
            Indicate(d0_bits, color=BLUE, scale_factor=1.2),
            run_time=1
            )

         # Rotation visualization - improved with better visual representation and position handling

        rotation_title = Tex(r"\textbf{Key Rotation}", font_size=32, color=YELLOW_D).to_edge(UP).shift(DOWN * 1)
        
        with self.voiceover("For each round, both halves are rotated left by a specific number of positions based on the round number."):
            self.play(
                Write(rotation_title)
            )
            
            # Show rotation schedule in a more compact form
            schedule_text = Tex(
                r"\text{Rounds 1, 2, 9, 16: Shift 1 bit}\\", 
                r"\text{All other rounds: Shift 2 bits}",
                font_size=24
            ).next_to(rotation_title, DOWN)
            
            self.play(Write(schedule_text))
        
        # Demonstrate the rotation for Round 1 (1-bit shift)
        # Extract bits for better visualization
        c0_bit_values = [mob.text for mob in c0_bits]
        d0_bit_values = [mob.text for mob in d0_bits]
        
        # Create rotated versions (1-bit left shift for round 1)
        c1_bit_values = c0_bit_values[1:] + c0_bit_values[0:1]  # Rotate left by 1
        d1_bit_values = d0_bit_values[1:] + d0_bit_values[0:1]  # Rotate left by 1
        
        # Create C1 and D1 mobjects
        c1_bits = VGroup(*[Text(bit, font_size=20, color=RED_B) for bit in c1_bit_values])
        d1_bits = VGroup(*[Text(bit, font_size=20, color=BLUE_B) for bit in d1_bit_values])
        
        # Position C1 and D1 above C0 and D0
        c1_bits.arrange_in_grid(rows=1, buff=0.2).next_to(c0_bits, UP, buff=0.7)
        d1_bits.arrange_in_grid(rows=1, buff=0.2).next_to(d0_bits, UP, buff=0.7)
        
        # Add labels for C1 and D1
        c1_title = MathTex(r"C_1", font_size=26, color=RED_B).next_to(c1_bits, LEFT, buff=0.5)
        d1_title = MathTex(r"D_1", font_size=26, color=BLUE_B).next_to(d1_bits, LEFT, buff=0.5)
        
        with self.voiceover("Let's see what happens in round one. Since it's round one, we shift each half by one bit to the left."):
            # First, highlight the first bit that will wrap around
            self.play(
                Indicate(c0_bits[0], color=YELLOW, scale_factor=1.5),
                Indicate(d0_bits[0], color=YELLOW, scale_factor=1.5),
            )
            
            # Create rotation arrows to indicate circular shift
            c_rotation_arrow = CurvedArrow(
                c0_bits[0].get_center() + UP*0.2, 
                c0_bits[-1].get_center() + UP*0.2, 
                angle=-TAU/4,
                color=RED_B
            ).scale(0.8)
            
            d_rotation_arrow = CurvedArrow(
                d0_bits[0].get_center() + UP*0.2, 
                d0_bits[-1].get_center() + UP*0.2, 
                angle=-TAU/4,
                color=BLUE_B
            ).scale(0.8)
            
            self.play(
                Create(c_rotation_arrow),
                Create(d_rotation_arrow)
            )
            
            # Show the bits rotating to their new positions
            self.play(
                FadeIn(c1_title),
                FadeIn(d1_title),
                *[TransformFromCopy(c0_bits[i], c1_bits[(i-1) % 28]) for i in range(28)],
                *[TransformFromCopy(d0_bits[i], d1_bits[(i-1) % 28]) for i in range(28)],
                run_time=2
            )
            
            # Remove the arrows
            self.play(
                FadeOut(c_rotation_arrow),
                FadeOut(d_rotation_arrow)
            )
        
        with self.voiceover("After rotation, we get new C-one and D-one values that will be used to create the subkey for round one."):
        # Highlight the new C1 and D1 groups
            self.play(
                Indicate(c1_bits, color=RED_B, scale_factor=1.1),
                Indicate(d1_bits, color=BLUE_B, scale_factor=1.1),
                run_time=2
            )
        
        # PC-2 Transformation with visually appealing effects
        pc2_title = Tex(r"\textbf{Permuted Choice 2 (PC-2)}", font_size=32, color=GREEN_D)
        pc2_title.to_edge(UP).shift(DOWN * 1)
        
        # Mathematical formulation with LaTeX
        pc2_formula = MathTex(
            r"K_1 = \text{PC}_2(C_1 \parallel D_1)", 
            font_size=28
        )
        pc2_description = Tex(
            r"\text{(Selects 48 bits from the 56-bit concatenated key)}", 
            font_size=24, 
            color=GRAY
        )
        
        formula_group = VGroup(pc2_formula, pc2_description).arrange(DOWN, buff=0.2)
        formula_group.next_to(pc2_title, DOWN, buff=0.3)
        
        with self.voiceover("Now we apply Permuted Choice 2, which selects 48 specific bits from the combined C-one and D-one values."):
            # First fade out the previous elements
            self.play(
            FadeOut(rotation_title),
            FadeOut(schedule_text),
            FadeOut(pc1_bits),
            FadeOut(c1_bits),
            FadeOut(d0_bits),
            FadeOut(c0_title),
            FadeOut(d0_title),
            run_time=1
            )
            
            # Then write the new elements
            self.play(
            Write(pc2_title),
            Write(pc2_formula),
            Write(pc2_description),
            run_time=1
            )
        
        # # Create a combined C1||D1 visualization
        # combined_bits_title = MathTex(r"C_1 \parallel D_1", font_size=28, color=PURPLE_B)
        
        # # Move and reorganize C1 and D1 bits to show concatenation
        # combined_c1d1_group = VGroup()
        
        # with self.voiceover("First, we concatenate C-one and D-one to form a 56-bit value."):
        #     # Prepare concatenated bit array
        #     self.play(
        #         # Create title for combined bits
        #         Write(combined_bits_title.to_edge(LEFT).shift(RIGHT * 3 + UP * 0.5)),
                
        #         # Keep the titles visible but move them
        #         c1_title.animate.scale(0.8).to_edge(LEFT).shift(RIGHT * 1.5 + UP * 0.5),
        #         d1_title.animate.scale(0.8).to_edge(LEFT).shift(RIGHT * 4.5 + UP * 0.5),
                
        #         # Move bit groups to show concatenation
        #         c1_bits.animate.scale(0.8).arrange(RIGHT, buff=0.1).next_to(c1_title, RIGHT, buff=0.2),
        #         d1_bits.animate.scale(0.8).arrange(RIGHT, buff=0.1).next_to(d1_bits, RIGHT, buff=0.2),
                
        #         # Fade out the original C0 and D0 groups to reduce visual clutter
                
                
        #         run_time=2.5
        #     )
            
        #     # Highlight the concatenated bits with a surrounding rectangle
        #     combined_rect = SurroundingRectangle(
        #         VGroup(c1_bits, d1_bits), 
        #         color=PURPLE_B, 
        #         buff=0.15,
        #         stroke_width=2,
        #         corner_radius=0.2
        #     )
        #     self.play(
        #         Create(combined_rect),
        #         Flash(combined_rect, color=PURPLE_B, line_length=0.1, flash_radius=0.2)
        #     )
        
        # # Create K1 (48-bit subkey) using a visually distinct pattern
        # # Using a Manim-compatible bit selection to demonstrate PC-2
        # k1_string = "101100101111001100001010010101100110111100001010"  # Example 48-bit subkey
        
        # # Create the destination for K1 bits
        # k1_bits = VGroup(*[Text(bit, font_size=18, color=GREEN_D) for bit in k1_string])
        # k1_bits.arrange(RIGHT, buff=0.1).shift(DOWN * 1.5)
        
        # # Create a visually appealing box for K1
        # k1_box = RoundedRectangle(
        #     height=k1_bits.height + 0.4,
        #     width=k1_bits.width + 0.4,
        #     corner_radius=0.2,
        #     color=GREEN_D,
        #     fill_opacity=0.1
        # ).move_to(k1_bits)
        
        # # Add a label for K1
        # k1_label = MathTex(r"K_1", font_size=30, color=GREEN_D).next_to(k1_box, LEFT, buff=0.3)
        
        # # Mathematical formulation specifically for K1
        # k1_formula = MathTex(
        #     r"K_1 = \text{PC}_2(C_1 \parallel D_1)",
        #     r"= \text{Selected 48 bits}",
        #     font_size=24
        # ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).shift(LEFT * 2 + UP * 2)
        
        # with self.voiceover("Permuted Choice 2 selects 48 specific bits from the combined 56-bit key to create the round subkey K1."):
        #     # Display the K1 formula
        #     self.play(
        #         Write(k1_formula),
        #         Create(k1_box),
        #         Write(k1_label),
        #         run_time=1.5
        #     )
        
        # # Define source bit indices (these would normally come from the PC-2 table)
        # # We'll use some example indices for illustration
        # source_indices = [
        #     9, 17, 23, 31, 13, 28, 2, 18, 
        #     24, 16, 30, 6, 26, 20, 10, 1, 
        #     8, 14, 25, 3, 4, 29, 11, 19, 
        #     32, 12, 22, 7, 5, 27, 15, 21, 
        #     38, 48, 54, 35, 45, 56, 37, 39, 
        #     46, 50, 42, 33, 51, 47, 44, 49
        # ]
        
        # # Adjust indices to be 0-based
        # source_indices = [i-1 for i in source_indices]
        
        # # Create more realistic transformation with PC-2 pattern
        # with self.voiceover("Let's watch as specific bits are selected from the combined key according to the permutation table.") as track:
        #     # Animate selection of individual bits with staggered timing for visual appeal
        #     animations = []
            
        #     # Group animations to show multiple bits transforming simultaneously
        #     for i in range(0, 48, 6):  # Process in groups of 6 for better visualization
        #         group_anims = []
        #         for j in range(6):  # 6 bits per group
        #             if i+j < 48:  # Ensure we don't go beyond 48 bits
        #                 source_idx = source_indices[i+j]
        #                 source_bit = c1_bits[source_idx] if source_idx < 28 else d1_bits[source_idx-28]
                        
        #                 # Create a copy animation with path arc for better visual effect
        #                 transform = TransformFromCopy(
        #                     source_bit,
        #                     k1_bits[i+j],
        #                     path_arc=PI/3,
        #                     rate_func=smooth
        #                 )
                        
        #                 # Flash the source bit for emphasis
        #                 flash = Flash(
        #                     source_bit, 
        #                     color=YELLOW_A, 
        #                     line_length=0.1, 
        #                     flash_radius=0.2,
        #                     line_stroke_width=2
        #                 )
                        
        #                 group_anims.append(AnimationGroup(flash, transform, lag_ratio=0.2))
                
        #         # Play each group with slight stagger for visual appeal
        #         self.play(
        #             AnimationGroup(*group_anims, lag_ratio=0.15),
        #             run_time=min(1.2, track.duration/8)  # Adjust timing based on voiceover
        #         )
        
        # # Emphasize the final K1
        # with self.voiceover("And thus, we have our first round subkey, K1, which will be used in the first round of the DES encryption process."):
        #     self.play(
        #         Indicate(k1_bits, color=GREEN, scale_factor=1.1),
        #         Flash(k1_box, color=GREEN_D, line_length=0.2, flash_radius=0.5),
        #         run_time=2
        #     )
        
        # # Show the key schedule continuation
        # key_schedule_text = Tex(
        #     r"\textbf{For each round $i$ from 1 to 16:}",
        #     r"1. $C_i = \text{LeftShift}(C_{i-1}, \text{shift}_i)$",
        #     r"2. $D_i = \text{LeftShift}(D_{i-1}, \text{shift}_i)$",
        #     r"3. $K_i = \text{PC}_2(C_i \parallel D_i)$",
        #     font_size=24
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=0.8)
        
        # with self.voiceover("This entire process repeats for all sixteen rounds, with each round using different rotation amounts to create sixteen unique subkeys."):
        #     self.play(
        #         Write(key_schedule_text),
        #         run_time=2.5
        #     )
        
        
        
        
        # # PC-2 Transformation with simplified and clearer visuals
        # pc2_title = Tex(r"\textbf{Permuted Choice 2 (PC-2)}", font_size=32, color=GREEN_D).to_edge(UP).shift(DOWN * 0.5)
        # pc2_formula = MathTex(
        #     r"K_1 = \text{PC}_2(C_1 \parallel D_1)", r"\text{ (Selects 48 bits from 56)}"
        # ).next_to(pc2_title, DOWN)
        
        # with self.voiceover("Now we combine C1 and D1 and apply Permuted Choice 2 to form a 48-bit subkey for the first round."):
        #     # Clear the rotation visuals
        #     self.play(
        #         FadeOut(rotation_title),
        #         FadeOut(schedule_text),
        #         FadeOut(c0_title),
        #         FadeOut(d0_title),
        #         Write(pc2_title),
        #         Write(pc2_formula)
        #     )
            
        #     # Move C1 and D1 bits to center for concatenation
        #     self.play(
        #         c0_bits.animate.arrange(RIGHT, buff=0.2).move_to(LEFT * 2),
        #         d0_bits.animate.arrange(RIGHT, buff=0.2).move_to(RIGHT * 2)
        #     )
        
        # # Create K1 (48-bit subkey) from PC-2
        # k1_string = "110100101011000011001101001111010101100110011110"  # Example 48-bit subkey
        # k1_bits = VGroup(*[Text(bit, font_size=20, color=GREEN) for bit in k1_string])
        # k1_bits.arrange(RIGHT, buff=0.2).shift(DOWN * 1.5)
        
        # k1_label = MathTex(r"K_1 \text{ (48-bit subkey)}", font_size=28, color=GREEN_D).next_to(k1_bits, UP, buff=0.5)
        
        # # Show bits being selected to form K1
        # with self.voiceover("Permuted Choice 2 selects 48 bits from the combined 56 bits to produce the round subkey K1. Each round generates a different subkey using the same process but with different rotations.") as track:
        #     self.play(Write(k1_label), run_time=1)
            
        #     # Show bits being selected with transform animation
        #     sample_indices = [3, 8, 12, 18, 22, 27, 31, 36, 42, 45, 50, 53]
            
        #     for i, target_index in zip(sample_indices, range(0, 48, 4)):
        #         source_bit = c0_bits[i % 28].copy() if i < 28 else d0_bits[i - 28].copy()
                
        #         self.play(
        #             TransformFromCopy(source_bit, k1_bits[target_index]), 
        #             Flash(source_bit, color=YELLOW_A, line_length=0.1, flash_radius=0.2),
        #             run_time=0.2
        #         )
            
        #     # Fade in the rest of K1 bits
        #     self.play(
        #         FadeIn(VGroup(*[k1_bits[i] for i in range(48) if i % 4 != 0])),
        #         run_time=min(track.duration - 3, 2)
        #     )
        
        # # Emphasize the complete key schedule process
        # process_text = Tex(r"\textbf{This process repeats for all 16 rounds, generating 16 unique subkeys}", 
        #                    font_size=28, color=YELLOW_D).to_edge(DOWN, buff=0.8)
        
        # with self.voiceover("This process repeats for all sixteen rounds, with each round's rotation producing a unique subkey that strengthens DES's security."):
        #     self.play(Write(process_text))
        
        # # Clean up
        # with self.voiceover("This completes our detailed look at the DES key schedule process."):
        #     self.play(*[FadeOut(mob) for mob in self.mobjects])
