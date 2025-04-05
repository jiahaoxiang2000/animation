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

    def keep_and_move_to_top(self, *objects_to_keep, animate_duration=1.0, spacing=0.5):
        """
        Keeps specified objects visible while fading out everything else,
        then moves the kept objects to the top position.
        
        Parameters:
        -----------
        *objects_to_keep : Mobject
            The objects that should remain visible
        animate_duration : float, optional
            Duration of the animation in seconds, defaults to 1.0
        spacing : float, optional
            Horizontal spacing between objects, defaults to 0.5
        
        Returns:
        --------
        VGroup
            A group containing all kept objects in their new positions
        """
        # Collect all objects that need to be removed
        all_mobjects = self.mobjects.copy()
        objects_to_remove = []
        
        # Identify objects to remove (those not in objects_to_keep)
        for mob in all_mobjects:
            if mob not in objects_to_keep:
                objects_to_remove.append(mob)
        
        # Fade out objects that aren't being kept
        if objects_to_remove:
            self.play(
                *[FadeOut(obj) for obj in objects_to_remove],
                run_time=animate_duration
            )
        
        # Create a group for the kept objects for easier positioning
        kept_group = VGroup(*objects_to_keep)
        
        # Move kept objects to top position while preserving their vertical relationship
        self.play(
            kept_group.animate.to_edge(UP).shift(DOWN * 1),
            run_time=animate_duration
        )
        
        return kept_group

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

        # Split into C and D blocks using LaTeX with clearer visuals
        c0_title = MathTex(r"C_0 = K_{56}[0:28]", font_size=26, color=RED)
        d0_title = MathTex(r"D_0 = K_{56}[28:56]", font_size=26, color=BLUE)

        self.keep_and_move_to_top(
           c0_bits, d0_bits,
            spacing=0.5
        )
        
        
        with self.voiceover("The 56-bit key is then split into two 28-bit halves, called C-zero and D-zero."):
            # Position titles to the left of their respective bit groups
            c0_title.next_to(c0_bits, LEFT, buff=0.5)
            d0_title.next_to(d0_bits, LEFT, buff=0.5)
            
            self.play(
            Write(c0_title),
            Write(d0_title)
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

        # Rotation title positioned using absolute coordinates instead of relative to specific objects
        rotation_title = Tex(r"\textbf{Key Rotation}", font_size=32, color=YELLOW_D).next_to(self.mobjects[0], DOWN, buff=0.5)
        
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
        
        # Position C1 and D1 below the kept elements
        c1_bits.arrange_in_grid(rows=1, buff=0.2).next_to(rotation_title, DOWN*2, buff=0.7)
        d1_bits.arrange_in_grid(rows=1, buff=0.2).next_to(c1_bits, DOWN, buff=0.7)
        
        # Add labels for C1 and D1
        c1_title = MathTex(r"C_1", font_size=26, color=RED_B).next_to(c1_bits, LEFT, buff=0.5)
        d1_title = MathTex(r"D_1", font_size=26, color=BLUE_B).next_to(d1_bits, LEFT, buff=0.5)
        
        with self.voiceover("Let's see what happens in round one. Since it's round one, we shift each half by one bit to the left."):
            # First, highlight the first bit that will wrap around
            self.play(
                Indicate(c0_bits[0], color=YELLOW, scale_factor=1.5),
                Indicate(d0_bits[0], color=YELLOW, scale_factor=1.5),
            )
            
            # Show the bits rotating to their new positions
            self.play(
                FadeIn(c1_title),
                FadeIn(d1_title),
                *[TransformFromCopy(c0_bits[i], c1_bits[(i-1) % 28]) for i in range(28)],
                *[TransformFromCopy(d0_bits[i], d1_bits[(i-1) % 28]) for i in range(28)],
                run_time=2
            )
            
        self.keep_and_move_to_top(
            c1_bits, d1_bits,
            c1_title, d1_title,
            spacing=0.5
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
        pc2_title.next_to(d1_bits, DOWN, buff=0.5)
        
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
    
            # Then write the new elements
            self.play(
            Write(pc2_title),
            Write(pc2_formula),
            Write(pc2_description),
            run_time=1
            )

        self.keep_and_move_to_top(
            pc2_formula,
            spacing=0.5
        )
        
        # Create the final subkey K1 by the VGroup, also use the arrange_in_grid to show one two row, 
        k1_subkey = VGroup(c1_bits, d1_bits).arrange_in_grid(rows=2, buff=0.2)
        k1_subkey.next_to(pc2_formula, DOWN, buff=0.5)
        
        with self.voiceover("We combine C1 and D1 to form a 56-bit value that will be input to PC-2."):
            self.play(Write(k1_subkey))

        # Create the final K1 subkey, here we need the animate to show the permutation 2 transformation
        k1_output = "101011001000110111110011000010101111000001010111"
        k1_bits = VGroup(*[Text(bit, font_size=20, color=GREEN) for bit in k1_output])
        k1_bits.arrange_in_grid(rows=2, buff=0.2).next_to(k1_subkey, DOWN, buff=0.5)
        
        k1_title = MathTex(r"K_1 \text{ (48-bit subkey)}", font_size=28, color=GREEN_D).next_to(k1_bits, LEFT, buff=0.5)
        
        with self.voiceover("PC-2 selects and permutes 48 bits from the 56-bit combined key to create the round subkey. Watch how the bits are rearranged according to the PC-2 permutation table.") as tracker:
            # First show the PC-2 selection with animated paths from source to destination
            animations = []
            for i in range(48):
                # Use a random source bit position for visual effect (in a real implementation, this would follow the actual PC-2 table)
                source_idx = i % 56
                source_row = 0 if source_idx < 28 else 1
                source_col = source_idx % 28
                
                # Get the source mobject (either from c1_bits or d1_bits)
                source_mob = c1_bits[source_col] if source_row == 0 else d1_bits[source_col % 28]
                
                # Create a copy and transform it to the destination
                animations.append(
                    TransformFromCopy(
                        source_mob,
                        k1_bits[i],
                        path_arc=PI/3,
                        run_time=min(2, tracker.duration * 0.8/48)
                    )
                )
            
            # Play all transformations with a slight lag for visual appeal
            self.play(
            LaggedStart(*animations, lag_ratio=0.02),
            run_time=min(3, tracker.duration * 0.8)
            )
            self.play(Write(k1_title), run_time=min(1, tracker.duration * 0.2))
        
        with self.voiceover("This 48-bit subkey K1 is now ready to be used in the first round of DES encryption. The process repeats for all 16 rounds, with different rotation amounts to generate unique subkeys for each round."):
            self.play(
            Indicate(k1_bits, color=GREEN_D, scale_factor=1.2),
            run_time=2
            )
        
      
class DESRoundScene(VoiceoverScene):
    """Illustrates a single round of the DES encryption process in detail"""

    def keep_and_move_to_top(self, *objects_to_keep, animate_duration=1.0, spacing=0.5):
        """
        Keeps specified objects visible while fading out everything else,
        then moves the kept objects to the top position.
        
        Parameters:
        -----------
        *objects_to_keep : Mobject
            The objects that should remain visible
        animate_duration : float, optional
            Duration of the animation in seconds, defaults to 1.0
        spacing : float, optional
            Horizontal spacing between objects, defaults to 0.5
        
        Returns:
        --------
        VGroup
            A group containing all kept objects in their new positions
        """
        # Collect all objects that need to be removed
        all_mobjects = self.mobjects.copy()
        objects_to_remove = []
        
        # Identify objects to remove (those not in objects_to_keep)
        for mob in all_mobjects:
            if mob not in objects_to_keep:
                objects_to_remove.append(mob)
        
        # Fade out objects that aren't being kept
        if objects_to_remove:
            self.play(
                *[FadeOut(obj) for obj in objects_to_remove],
                run_time=animate_duration
            )
        
        # Create a group for the kept objects for easier positioning
        kept_group = VGroup(*objects_to_keep)
        
        # Move kept objects to top position while preserving their vertical relationship
        self.play(
            kept_group.animate.to_edge(UP).shift(DOWN * 1),
            run_time=animate_duration
        )
        
        return kept_group

    def construct(self):
        self.set_speech_service(GTTSService())

        # Title for the scene
        title = Text("DES Round Function", font_size=48, color=BLUE_D).to_edge(UP)
        
        with self.voiceover("Let's examine a single round of the DES algorithm in detail."):
            self.play(Write(title))
            self.wait(0.5)
        
        # Show the Feistel structure diagram
        feistel_title = Text("Feistel Network Structure", font_size=32, color=BLUE).shift(UP * 2)
        
        with self.voiceover("DES uses a Feistel network structure, which processes data in halves and provides the valuable property that encryption and decryption operations are nearly identical."):
            self.play(Write(feistel_title))
        
        # Create input blocks for the round
        left_block = "10101010" * 4  # 32 bits represented as a binary string
        right_block = "01010101" * 4  # 32 bits represented as a binary string
        
        # Labels for the input blocks
        li_label = MathTex(r"L_{i-1}", font_size=32, color=RED_D)
        ri_label = MathTex(r"R_{i-1}", font_size=32, color=BLUE_D)
        
        # Create visual representation of the 32-bit blocks (we'll use simplified representations)
        li_block = Rectangle(height=1, width=2, color=RED_D).set_fill(RED_E, opacity=0.3)
        ri_block = Rectangle(height=1, width=2, color=BLUE_D).set_fill(BLUE_E, opacity=0.3)
        
        # Position them side by side
        input_group = VGroup(li_block, ri_block).arrange(RIGHT, buff=1).shift(UP * 0.5)
        
        # Add the labels above the blocks
        li_label.next_to(li_block, UP, buff=0.2)
        ri_label.next_to(ri_block, UP, buff=0.2)
        
        # Create sample bits inside the blocks (just a few to keep it manageable)
        li_bits_text = Text(left_block[:8] + "...", font_size=16, color=RED).move_to(li_block)
        ri_bits_text = Text(right_block[:8] + "...", font_size=16, color=BLUE).move_to(ri_block)
        
        with self.voiceover("Each round begins with two 32-bit halves from the previous round, typically labeled L and R."):
            self.play(
                Create(li_block), 
                Create(ri_block),
                Write(li_label),
                Write(ri_label)
            )
            self.play(
                Write(li_bits_text),
                Write(ri_bits_text)
            )
        
        # Create the F-function box
        f_box = Rectangle(height=1.5, width=2, color=GREEN_D).set_fill(GREEN_E, opacity=0.3)
        f_box.next_to(ri_block, DOWN, buff=1.5)
        
        # Position the F-box below the right block with an arrow connecting them
        f_label = MathTex(r"F", font_size=40, color=GREEN_D).move_to(f_box)
        r_to_f_arrow = Arrow(ri_block.get_bottom(), f_box.get_top(), buff=0.1, color=WHITE)
        
        with self.voiceover("The core of each round is the F function, which takes the right half as input."):
            self.play(
                Create(f_box)
            )
            self.play(
                Write(f_label),
                GrowArrow(r_to_f_arrow)
            )
        
        # Add the round key input to the F-function
        key_box = Rectangle(height=0.8, width=1.5, color=YELLOW_D).set_fill(YELLOW_E, opacity=0.3)
        key_box.next_to(f_box, RIGHT, buff=1)
        
        # Position the key to the right of the F-box
        key_label = MathTex(r"K_i", font_size=32, color=YELLOW_D).move_to(key_box)
        key_arrow = Arrow(key_box.get_left(), f_box.get_right(), buff=0.1, color=YELLOW)
        
        with self.voiceover("The F function also takes the round subkey as input. Each round uses a different subkey derived from the key schedule."):
            self.play(
                Create(key_box)
            )
            self.play(
                Write(key_label),
                GrowArrow(key_arrow)
            )
        
        # Show the XOR operation between L_{i-1} and F(R_{i-1}, K_i)
        xor_symbol = MathTex(r"\oplus", font_size=60).move_to(li_block.get_center() + DOWN * 1.5)
        
        # Draw arrow from F-box output to XOR
        f_to_xor_arrow = Arrow(f_box.get_left(), xor_symbol.get_right(), buff=0.1,color=WHITE)
        
        # Draw arrow from L_{i-1} to XOR
        l_to_xor_arrow = Arrow(li_block.get_bottom(), xor_symbol.get_top(), buff=0.1, color=WHITE)
        
        with self.voiceover("The output of the F function is then combined with the left half using an XOR operation."):
            self.play(
                Write(xor_symbol),
                GrowArrow(f_to_xor_arrow),
                GrowArrow(l_to_xor_arrow)
            )
        
        # Show the result of the XOR operation which becomes the new right half
        output_right = Rectangle(height=1, width=2, color=PURPLE_D).set_fill(PURPLE_E, opacity=0.3)
        output_right_label = MathTex(r"R_i", font_size=32, color=PURPLE_D)
        
        # Position the new right half at the bottom
        output_right.next_to(xor_symbol, DOWN, buff=1)
        output_right_label.move_to(output_right)
        
        # Arrow from XOR to the new right half
        xor_to_r_arrow = Arrow(xor_symbol.get_bottom(), output_right.get_top(), buff=0.1, color=WHITE)
        
        with self.voiceover("The result of this XOR operation becomes the new right half for the current round."):
            self.play(
                GrowArrow(xor_to_r_arrow),
                Create(output_right),
                Write(output_right_label)
            )
        
        # The new left half is simply the previous right half
        output_left = Rectangle(height=1, width=2, color=GREEN_B).set_fill(GREEN_C, opacity=0.3)
        output_left_label = MathTex(r"L_i", font_size=32, color=GREEN_B)
        
        # Position the new left half next to the new right half
        output_left.next_to(ri_block, RIGHT, buff=1)
        output_left_label.move_to(output_left)
        
        # Arrow showing R_{i-1} becomes L_i
        r_to_l_arrow = Arrow(
            ri_block.get_right(), 
            output_left.get_left(), 
            color=BLUE
        )
        
        with self.voiceover("Meanwhile, the new left half is simply a copy of the previous right half. This completes the structure of a single round."):
            self.play(
                GrowArrow(r_to_l_arrow),
                Create(output_left),
                Write(output_left_label)
            )
        
        # Add the round number indicator
        round_indicator = Text("Round i of 16", font_size=28, color=YELLOW).to_edge(UP).shift(DOWN * 0.7)
        
        with self.voiceover("This process is repeated for all sixteen rounds of DES, with each round using a different subkey from the key schedule."):
            self.play(Write(round_indicator))
  
        # Title for the F function details
        f_function_title = Text("Inside the F Function", font_size=36, color=GREEN_D).to_edge(UP)
        
        with self.voiceover("The F function consists of several operations that add confusion and diffusion to the cipher."):
            self.play(
                *[FadeOut(mob) for mob in self.mobjects],
                run_time=1.5
            )
            self.play(Write(f_function_title))
        
        # Inside the DESRoundScene class, modify the F function animation section
        
        # Create a detailed diagram of the F function with bit-level visualizations
        # Sample initial 32-bit input for R_{i-1}
        initial_bits = "10101010101010101010101010101010"
        
        # 1. Expansion (E)
        expansion_box = Rectangle(height=0.8, width=1.8, color=TEAL).shift(UP * 1.5)
        expansion_label = Text("Expansion (E)", font_size=20, color=TEAL).move_to(expansion_box)
        
        # Show actual bits for input to expansion
        input_bits_group = self.create_bit_group(initial_bits, font_size=16, color=WHITE)
        input_bits_group.scale(0.8).next_to(expansion_box, UP, buff=0.3)
        input_label = MathTex(r"R_{i-1} (32 \text{ bits})", font_size=18).next_to(input_bits_group, UP, buff=0.2)
        
        # Text explaining the expansion
        expansion_text = MathTex(r"32 \text{ bits} \rightarrow 48 \text{ bits}", font_size=24).next_to(expansion_box, RIGHT, buff=0.5)
        
        with self.voiceover("First, the 32-bit right half is expanded to 48 bits using an expansion permutation, which duplicates some of the bits."):
            self.play(
                Create(expansion_box),
                Write(expansion_label),
                Write(expansion_text),
                Write(input_bits_group),
                Write(input_label)
            )
        
        # Show expanded bits (48-bit output) - duplicating some bits from the original
        expanded_bits = self.get_expanded_bits(initial_bits)
        expanded_bits_group = self.create_bit_group(expanded_bits, font_size=16, color=TEAL)
        expanded_bits_group.scale(0.8).next_to(expansion_box, DOWN, buff=0.3)
        
        # Animate bits being duplicated and rearranged
        with self.voiceover("The expansion permutation takes each 4-bit block and creates a 6-bit block by duplicating edge bits, creating a total of 48 bits."):
            self.play(
                Write(expanded_bits_group),
                run_time=1.5
            )
        
        # 2. XOR with round key
        key_xor_box = Rectangle(height=0.8, width=1.8, color=YELLOW).next_to(expansion_box, DOWN, buff=2.0)
        key_xor_label = Text("XOR with Key", font_size=20, color=YELLOW).move_to(key_xor_box)
        
        # Keep expanded bits and move to top before continuing
        kept_group = self.keep_and_move_to_top(expansion_label, expanded_bits_group)
        
        # Arrow from Expansion to XOR
        key_xor_box.next_to(expanded_bits_group, DOWN, buff=0.7)
        key_xor_label.move_to(key_xor_box)
        e_to_xor_arrow = Arrow(kept_group.get_bottom(), key_xor_box.get_top(), buff=0.1, color=WHITE)

        # Key arrow pointing to the XOR operation
        key_input = MathTex(r"K_i \text{ (48 bits)}", font_size=24, color=YELLOW)
        key_input.next_to(key_xor_box, RIGHT, buff=0.2)
        
        with self.voiceover("The expanded 48-bit output is then combined with the 48-bit round subkey using an XOR operation."):
            self.play(
                GrowArrow(e_to_xor_arrow),
                Create(key_xor_box),
                Write(key_xor_label),
                Write(key_input)
            )

        # XOR result (showing actual bits)
        xor_result = "1011101101110101000110100110111001101101111110000"  
        xor_result_bits = self.create_bit_group(xor_result, font_size=16, color=GREEN_C)
        xor_result_bits.scale(0.8).next_to(key_xor_box, DOWN, buff=0.3)
        
        with self.voiceover("Each bit of the expanded data is XORed with the corresponding bit from the round key.") as tracker:
            # Show full XOR result
            self.play(Write(xor_result_bits), run_time=tracker.duration)
        
        # 3. S-Boxes
        # Keep XOR result and move to top
        kept_group = self.keep_and_move_to_top(key_xor_label, xor_result_bits)

        sbox_box = Rectangle(height=0.8, width=1.8, color=PURPLE).next_to(xor_result_bits, DOWN, buff=2.0)
        sbox_label = Text("S-Boxes (8×)", font_size=20, color=PURPLE).move_to(sbox_box)
        
        # Arrow from XOR to S-Boxes
        xor_to_s_arrow = Arrow(kept_group.get_bottom(), sbox_box.get_top(), buff=0.1, color=WHITE)
        
        # S-Box explanation
        sbox_text = MathTex(r"48 \text{ bits} \rightarrow 32 \text{ bits}", font_size=24).next_to(sbox_box, RIGHT, buff=0.5)
        
        # Divide the 48-bit XOR result into 8 groups of 6 bits each
        bit_groups = []
        for i in range(0, min(48, len(xor_result)), 6):
            if i + 6 <= len(xor_result):
                group = xor_result[i:i+6]
                bit_groups.append(group)
        
        # Create visual representation of bit groups
        bit_group_visuals = []
        for i, group in enumerate(bit_groups[:]):
            group_rect = Rectangle(height=0.4, width=0.8, color=PURPLE_A)
            group_text = Text(group, font_size=14, color=WHITE)
            group_text.move_to(group_rect)
            group_label = Text(f"Group {i+1}", font_size=12).next_to(group_rect, UP, buff=0.1)
            
            group_visual = VGroup(group_rect, group_text, group_label)
            bit_group_visuals.append(group_visual)
        
        # Arrange bit groups horizontally
        bit_group_row = VGroup(*bit_group_visuals).arrange(RIGHT, buff=0.3)
        bit_group_row.next_to(sbox_box, DOWN, buff=0.5)
        
        with self.voiceover("Next, the 48-bit result is divided into eight 6-bit blocks. Each block is processed by a different S-Box."):
            self.play(
                GrowArrow(xor_to_s_arrow),
                Create(sbox_box),
                Write(sbox_label),
                Write(sbox_text)
            )
            
            # Show bit groups
            self.play(
                *[FadeIn(group) for group in bit_group_visuals],
                run_time=1.5
            )
        self.keep_and_move_to_top(
            sbox_label, bit_group_row,
            spacing=0.5
        )

        # S-Box outputs (4 bits each)
        sbox_outputs = []
        for i, group in enumerate(bit_groups[:]):
            # Simplified S-Box substitution (in real DES this would use lookup tables)
            # Just take first 4 bits for demonstration
            output = self.simplified_sbox(group, i)
            sbox_outputs.append(output)
        
        # Create visual representation of S-Box outputs
        output_visuals = []
        for i, output in enumerate(sbox_outputs):
            output_rect = Rectangle(height=0.4, width=0.6, color=GREEN)
            output_text = Text(output, font_size=14, color=WHITE)
            output_text.move_to(output_rect)
            output_label = Text(f"Output {i+1}", font_size=12).next_to(output_rect, DOWN, buff=0.1)
            
            output_visual = VGroup(output_rect, output_text, output_label)
            output_visuals.append(output_visual)
        
        # Arrange S-Box outputs horizontally
        output_row = VGroup(*output_visuals).arrange(RIGHT, buff=0.3)
        output_row.next_to(bit_group_row, DOWN, buff=1.0)
       
        # Focus on the first S-box to explain the lookup process in detail
        first_group = bit_group_visuals[0]
        
        # Create a copy of the first group that we'll focus on
        focused_group = first_group.copy()
        
        with self.voiceover("Let's examine how one S-Box operates by looking at the first group of 6 bits."):
            # Highlight and scale up the first group to focus attention
            self.play(
                focused_group.animate.move_to(ORIGIN+UP*2).scale(1.5),
                FadeOut(bit_group_row),  # Temporarily hide other groups
                FadeOut(sbox_label),  # Hide S-Box label
                run_time=1.0
            )
        
        # Show how the 6 bits are divided into row and column selectors
        first_bit = focused_group[1][0].copy()  # First bit
        last_bit = focused_group[1][5].copy()   # Last bit
        middle_bits = VGroup(*[focused_group[1][i].copy() for i in range(1, 5)])  # Middle 4 bits
        
        # Create row/column labels
        row_label = Text("Row selector", font_size=18, color=YELLOW)
        col_label = Text("Column selector", font_size=18, color=BLUE)
        
        # Position labels
        row_label.next_to(VGroup(first_bit, last_bit), DOWN+LEFT, buff=0.3)
        col_label.next_to(middle_bits, DOWN+RIGHT, buff=0.3)
        
        with self.voiceover("The first and last bits together determine which row of the S-box to use."):
            # Highlight the bits used for row selection
            self.play(
                first_bit.animate.set_color(YELLOW),
                last_bit.animate.set_color(YELLOW),
                FadeIn(row_label),
                run_time=1.5
            )
        
        with self.voiceover("The middle four bits determine which column of the S-box to use."):
            # Highlight the bits used for column selection
            self.play(
                middle_bits.animate.set_color(BLUE),
                FadeIn(col_label),
                run_time=1.5
            )
        
        # Create S-box table visual using the real S-box 1 values (showing just part of the table for clarity)
        with self.voiceover("Let's look at the actual S-Box 1 table from the DES standard."):
            # Real S-Box 1 values (all 16 columns)
            real_sbox1 = [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ]
            
            # Show first 8 columns only to fit on screen
            visible_cols = 8
            sbox_table = VGroup()
            for i in range(4):  # 4 rows
                row = VGroup()
                for j in range(visible_cols):  # First 8 columns
                    cell = Rectangle(height=0.5, width=0.5, color=WHITE)
                    value = Text(str(real_sbox1[i][j]), font_size=16)
                    value.move_to(cell)
                    cell_group = VGroup(cell, value)
                    row.add(cell_group)
                row.arrange(RIGHT, buff=0)
                sbox_table.add(row)
            sbox_table.arrange(DOWN, buff=0)
            
            # Add table headers
            row_headers = VGroup()
            for i in range(4):
                header = Text(f"{i:02b}", font_size=14, color=YELLOW)  # Binary representation
                header.next_to(sbox_table[i], LEFT, buff=0.2)
                row_headers.add(header)
            
            col_headers = VGroup()
            for i in range(visible_cols):
                header = Text(f"{i:04b}", font_size=14, color=BLUE)  # Binary representation
                header.next_to(sbox_table[0][i], UP, buff=0.2)
                col_headers.add(header)
            
            # Add table title and "more columns" indicator
            table_title = Text("S-Box 1 (First 8 columns shown)", font_size=24, color=PURPLE)
            table_title.next_to(sbox_table, UP, buff=0.4)
            more_cols = Text("+ 8 more columns →", font_size=16, color=GRAY)
            more_cols.next_to(sbox_table, RIGHT, buff=0.3)
            
            # Show the table with a fade-in effect
            table_group = VGroup(sbox_table, row_headers, col_headers, table_title, more_cols)
            table_group.next_to(focused_group, DOWN, buff=1.0)
            
            self.play(
                FadeIn(table_group),
                run_time=2.0
            )
        
        # Calculate the row and column from the example bit group
        example_group = bit_groups[0]
        row_value = int(example_group[0] + example_group[5], 2)
        col_value = int(example_group[1:5], 2)  # Middle 4 bits determine column
        
        with self.voiceover(f"For our input value, the first and last bits {example_group[0]} and {example_group[5]} give us row {row_value} in binary."):
            # Create row indicator
            row_indicator = Arrow(row_headers[row_value].get_right(), sbox_table[row_value][0].get_left(), buff=0.05, color=YELLOW)
            self.play(
                GrowArrow(row_indicator),
                Indicate(row_headers[row_value], color=YELLOW, scale_factor=1.2),
                run_time=1.5
            )
        
        with self.voiceover(f"The middle bits {example_group[1:5]} give us column {col_value} in decimal. But since we're only showing 8 columns, we'll use column {min(col_value, 7)} for our demonstration."):
            # Use min(col_value, 7) to ensure we stay within our visible columns
            visible_col = min(col_value, 7)
            
            # Create column indicator
            col_indicator = Arrow(col_headers[visible_col].get_bottom(), sbox_table[0][visible_col].get_top(), buff=0.05, color=BLUE)
            self.play(
                GrowArrow(col_indicator),
                Indicate(col_headers[visible_col], color=BLUE, scale_factor=1.2),
                run_time=1.5
            )
        
        # Get the actual selected cell value from S-box 1
        selected_value = real_sbox1[row_value][col_value]
        binary_value = format(selected_value, '04b')
        
        # If the actual column is beyond what we're showing, indicate that
        if col_value >= visible_cols:
            pass
        else:
            # Highlight the selected cell
            selected_cell = sbox_table[row_value][visible_col]
            
            with self.voiceover(f"We look up the value at the intersection of row {row_value} and column {col_value}, which is {selected_value}."):
                self.play(
                    selected_cell.animate.set_fill(YELLOW, opacity=0.3),
                    Flash(selected_cell, color=YELLOW, line_length=0.1, flash_radius=0.3),
                    run_time=1.5
                )
        
        with self.voiceover(f"This decimal value {selected_value} is converted to a 4-bit binary value {binary_value}."):
            # Show the binary conversion
            value_text = Text(f"{selected_value}", font_size=24, color=GREEN_D)
            binary_text = Text(f"= {binary_value} (binary)", font_size=24, color=GREEN_D)
            
            conversion_group = VGroup(value_text, binary_text).arrange(RIGHT, buff=0.3)
            conversion_group.next_to(table_group, RIGHT, buff=0.5)
            
            self.play(
                Write(conversion_group),
                run_time=1.5
            )
        
       
        
        with self.voiceover("This process is repeated for all eight 6-bit groups in parallel, with each group using a different S-box."):
            self.keep_and_move_to_top(
                bit_group_row,
                sbox_label,
                spacing=0.5
            ) 
           
            # Now show all S-Box transformations with arrows
            all_arrows = []
            for i in range(len(bit_group_visuals)):
                src = bit_group_visuals[i]
                dest = output_visuals[i]
                all_arrows.append(
                    Arrow(src.get_bottom(), dest.get_top(), buff=0.1, color=WHITE)
                )
            
            self.play(
                *[GrowArrow(arrow) for arrow in all_arrows],
                run_time=1.5
            )
            
            # Show S-Box outputs
            self.play(
                *[FadeIn(output) for output in output_visuals],
                FadeOut(*all_arrows),
                run_time=1.5
            )
        
        with self.voiceover("The eight 4-bit outputs are then combined to form the 32-bit result that will proceed to the final permutation step."):
            # Combine all S-Box outputs into one 32-bit result
            sbox_combined = "".join(sbox_outputs)
            sbox_combined_bits = self.create_bit_group(sbox_combined, font_size=16, color=PURPLE_B)
            sbox_combined_bits.scale(0.8).next_to(output_row, DOWN, buff=0.7)
            sbox_combined_label = Text("Combined S-Box Output (32 bits)", font_size=18).next_to(sbox_combined_bits, UP, buff=0.2)
            
            # Show the combined output
            self.play(
                Write(sbox_combined_label),
                Write(sbox_combined_bits),
                run_time=1.5
            )

        self.keep_and_move_to_top(
            sbox_combined_label, sbox_combined_bits,
            spacing=0.5
        )

        # Starting from the kept combined S-Box output
        
        # 4. Permutation (P)
        perm_box = Rectangle(height=0.8, width=1.8, color=ORANGE).next_to(sbox_combined_bits, DOWN, buff=1.0)
        perm_label = Text("Permutation (P)", font_size=20, color=ORANGE).move_to(perm_box)
        
        # Arrow from S-Box combined output to Permutation
        s_to_p_arrow = Arrow(sbox_combined_bits.get_bottom(), perm_box.get_top(), buff=0.1, color=WHITE)
        
        # Permutation explanation
        perm_text = MathTex(r"32 \text{ bits} \rightarrow 32 \text{ bits}", font_size=24).next_to(perm_box, RIGHT, buff=0.5)
        
        with self.voiceover("The final step in the F function is the P permutation, which rearranges the 32-bit output from the S-boxes."):
            self.play(
                Create(perm_box),
                Write(perm_label),
                GrowArrow(s_to_p_arrow),
                Write(perm_text),
                run_time=2.0
            )
        
        with self.voiceover("Unlike the expansion permutation which changed the number of bits, this permutation simply reorders the bits to increase diffusion."):
            # Highlight the permutation box
            self.play(
                Indicate(perm_box, color=ORANGE, scale_factor=1.1),
                run_time=1.5
            )
        
        # Create the permuted output
        permuted_bits = self.get_permuted_bits(sbox_combined)
        permuted_bits_group = self.create_bit_group(permuted_bits, font_size=16, color=ORANGE)
        permuted_bits_group.scale(0.8).next_to(perm_box, DOWN, buff=0.3)
        
        with self.voiceover("The permutation spreads the influence of each S-box output across the entire result, strengthening the cipher against differential cryptanalysis."):
            # Show bit movement with paths to visualize the permutation
            # Create several sample arrows showing bits moving to new positions
            bit_arrows = []
            for i in range(8):  # Show 8 sample bit movements
                src_idx = i * 4  # Sample source indices spread across the input
                # In real DES, the destination would be according to the P-table
                # For visualization, we'll use a simplified formula
                dest_idx = (src_idx * 7) % 32
                
                if src_idx < len(sbox_combined_bits) and dest_idx < len(permuted_bits_group):
                    start_point = sbox_combined_bits[src_idx].get_center()
                    end_point = permuted_bits_group[dest_idx].get_center()
                    
                    # Create curved path for better visualization
                    path = CubicBezier(
                        start_point,
                        start_point + DOWN * 0.5 + LEFT * (0.3 * (i % 4 - 1.5)),
                        end_point + UP * 0.5 + RIGHT * (0.3 * (i % 4 - 1.5)),
                        end_point
                    )
                    
                    bit_arrows.append(
                        VMobject().set_points_as_corners([path.point_from_proportion(j/20) for j in range(21)])
                        .set_stroke(color=YELLOW, width=2)
                    )
            
            # Animate the bit movement paths
            self.play(
                *[Create(arrow) for arrow in bit_arrows],
                run_time=2.0
            )
            
            # Fade out the arrows and show the permuted bits
            self.play(
                *[FadeOut(arrow) for arrow in bit_arrows],
                Write(permuted_bits_group),
                run_time=1.5
            )
        
        # Final F function output - this is what gets XORed with L_{i-1}
        final_output_box = Rectangle(height=0.8, width=2.2, color=GREEN_D).set_fill(GREEN_E, opacity=0.2)
        final_output_box.next_to(permuted_bits_group, DOWN, buff=0.7)
        final_output_label = Text("F Function Output", font_size=20, color=GREEN_D).move_to(final_output_box)
        
        # Arrow from permutation to final output
        p_to_final_arrow = Arrow(permuted_bits_group.get_bottom(), final_output_box.get_top(), buff=0.1, color=WHITE)
        
        with self.voiceover("The output of the P permutation becomes the final result of the F function, which is then XORed with the left half from the previous round."):
            self.play(
                GrowArrow(p_to_final_arrow),
                Create(final_output_box),
                Write(final_output_label),
                run_time=2.0
            )
        
        # Create a mathematical representation of the F function
        f_function_formula = MathTex(
            r"F(R_{i-1}, K_i) = P(S(E(R_{i-1}) \oplus K_i))",
            font_size=32,
            color=GREEN_D
        )
        f_function_formula.next_to(final_output_box, DOWN, buff=0.5)
        
        with self.voiceover("The complete F function can be mathematically represented as a composition of these operations: expansion, XOR with the round key, S-box substitution, and final permutation."):
            self.play(
                Write(f_function_formula),
                run_time=2.0
            )
        
        
        # Conclude the F function explanation
        with self.voiceover("Understanding the F function is crucial to grasping how DES achieves encryption security through repeated application across multiple rounds.") as tracker:
            self.play(
                Circumscribe(f_function_formula, color=YELLOW, fade_in=True, fade_out=True),
                run_time=tracker.duration
            )

       
    
    # Helper methods for bit manipulation 
    def create_bit_group(self, bit_string, font_size=16, color=WHITE):
        """Create a group of mobjects representing individual bits"""
        bits = VGroup(*[Text(bit, font_size=font_size, color=color) for bit in bit_string])
        bits.arrange(RIGHT, buff=0.15)
        return bits
    
    def get_expanded_bits(self, bits):
        """Simulate the expansion permutation (simplified)"""
        # In a real implementation, this would use the E-bit selection table
        # For demonstration, we'll just duplicate some bits to get 48 from 32
        expanded = ""
        for i in range(0, len(bits), 4):
            if i+4 <= len(bits):
                block = bits[i:i+4]
                # Duplicate first and last bit of each block
                expanded += block[3] + block + block[0]
        
        # Ensure we have exactly 48 bits
        return expanded[:48].ljust(48, "0")
    
    def perform_xor(self, bits1, bits2):
        """Perform bitwise XOR on two bit strings"""
        result = ""
        for i in range(min(len(bits1), len(bits2))):
            result += "1" if bits1[i] != bits2[i] else "0"
        
        return result
    
    def simplified_sbox(self, bits, box_index):
        """Simplified S-Box implementation for demonstration"""
        # In real DES, this would use the S-Box lookup tables
        # For demonstration, we'll just use a simple transformation
        if len(bits) >= 6:
            # Use first and last bit to select row, middle 4 bits for column
            row = int(bits[0] + bits[5], 2)
            col = int(bits[1:5], 2)
            
            # Simple demonstration value based on row, col and box index
            value = (row + col + box_index) % 16
            
            # Convert to 4-bit binary
            return format(value, '04b')
        
        return "0000"  # Default fallback
    
    def get_permuted_bits(self, bits):
        """Simulate the P permutation (simplified)"""
        # In a real implementation, this would use the P permutation table
        # For demonstration, we'll just shuffle the bits in a consistent way
        if len(bits) >= 32:
            # Simple shuffle algorithm for demonstration
            permuted = list(bits[:32])
            for i in range(32):
                new_pos = (i * 7) % 32  # A simple permutation formula
                permuted[new_pos] = bits[i]
            
            return "".join(permuted)
        
        return bits  # Default fallback
        
         
