from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class DESComponents:
    """Helper class that provides DES-related visual components"""

    @staticmethod
    def create_des_structure():
        """Create a simple diagram showing DES structure"""
        diagram = VGroup()

        # Initial permutation box
        ip_box = Rectangle(height=1, width=2).set_stroke(WHITE)
        ip_text = Text("Initial Permutation", font_size=24).scale(
            0.7).move_to(ip_box)
        ip = VGroup(ip_box, ip_text)

        # Rounds
        rounds_box = Rectangle(height=2, width=2).set_stroke(
            WHITE).next_to(ip, DOWN, buff=0.5)
        rounds_text = Text("16 Rounds", font_size=24).scale(
            0.8).move_to(rounds_box)
        rounds = VGroup(rounds_box, rounds_text)

        # Final permutation
        fp_box = Rectangle(height=1, width=2).set_stroke(
            WHITE).next_to(rounds, DOWN, buff=0.5)
        fp_text = Text("Final Permutation", font_size=24).scale(
            0.7).move_to(fp_box)
        fp = VGroup(fp_box, fp_text)

        # Arrows
        arrow1 = Arrow(ip.get_bottom(), rounds.get_top())
        arrow2 = Arrow(rounds.get_bottom(), fp.get_top())

        # Input and output labels
        input_label = Text("64-bit input", font_size=20).next_to(ip, UP)
        output_label = Text("64-bit output", font_size=20).next_to(fp, DOWN)

        diagram = VGroup(ip, rounds, fp, arrow1, arrow2,
                         input_label, output_label)
        return diagram

    @staticmethod
    def create_round_function():
        """Create a diagram of the DES round function"""
        round_group = VGroup()

        # Split input to L and R
        split_text = Text(
            "Split 64-bit block into L and R (32 bits each)", font_size=24)
        round_group.add(split_text)

        # F function box
        f_box = Rectangle(height=1.5, width=2).set_stroke(
            WHITE).next_to(split_text, DOWN, buff=0.5)
        f_text = Text("F Function", font_size=24).move_to(f_box)
        f_function = VGroup(f_box, f_text)
        round_group.add(f_function)

        # F function details
        f_details = BulletedList(
            "Expansion (32 → 48 bits)",
            "XOR with round key",
            "S-box substitution (48 → 32 bits)",
            "Permutation",
            font_size=20
        ).next_to(f_function, DOWN, buff=0.5)
        round_group.add(f_details)

        # XOR and swap
        xor_text = Text("XOR and Swap halves for next round",
                        font_size=24).next_to(f_details, DOWN, buff=0.5)
        round_group.add(xor_text)

        return round_group.arrange(DOWN, center=True, buff=0.4)


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
            Tex("Permuted Choice 1 ($PC$-$1$)", font_size=20),
            Text("Key Rotation", font_size=20),
            Tex("Permuted Choice 2 ($PC$-$2$)", font_size=20)
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
        
        self.wait(1)
        
        # Update the fade-out voiceover to indicate what's coming next
        with self.voiceover("Now that we've seen the overall structure of DES, let's explore the details of both the encryption process and the key schedule.") as tracker:
            # Clean up for next scene with a nice fade out effect
            self.play(
                *[FadeOut(mob, run_time=1.5) for mob in self.mobjects],
                run_time=tracker.duration
            )


class DESRoundFunctionScene(VoiceoverScene):
    """Details of the DES round function"""

    def construct(self):
        self.set_speech_service(GTTSService(language='en'))

        # Round function explanation
        round_function = DESComponents.create_round_function()

        with self.voiceover("In each round, the data block is split into left and right halves. The right half goes through the F function, which includes expansion, key mixing, S-box substitution, and permutation."):
            self.play(FadeIn(round_function))

        self.wait(1)
        self.play(FadeOut(round_function))


class DESSecurityScene(VoiceoverScene):
    """Discussion of DES security considerations"""

    def construct(self):
        self.set_speech_service(GTTSService(language='en'))

        # Security discussion
        security_text = Text("Security Considerations",
                             font_size=42).to_edge(UP)
        security_points = BulletedList(
            "56-bit key is too small by modern standards",
            "Vulnerable to brute force attacks",
            "Triple DES (3DES) extends security",
            "Replaced by AES for most applications",
            font_size=36
        ).next_to(security_text, DOWN, buff=0.5)

        with self.voiceover("Today, DES is considered insecure due to its small key size. A 56-bit key can be brute-forced with modern computing power."):
            self.play(FadeIn(security_text), FadeIn(security_points[:2]))

        with self.voiceover("Triple DES was developed to extend DES's security life, but most modern applications now use AES instead."):
            self.play(FadeIn(security_points[2:]))

        self.wait(1)
        self.play(FadeOut(security_text), FadeOut(security_points))


class DESConclusionScene(VoiceoverScene):
    """Conclusion scene for the DES explanation"""

    def construct(self):
        self.set_speech_service(GTTSService(language='en'))

        # Conclusion
        conclusion = Text(
            "DES was a groundbreaking cipher that influenced modern cryptography", font_size=36)

        with self.voiceover("Despite its limitations, DES was a groundbreaking cipher that greatly influenced the field of modern cryptography."):
            self.play(FadeIn(conclusion))

        with self.voiceover("Thanks for watching this explanation of the Data Encryption Standard."):
            self.play(FadeOut(conclusion))


class DESExplanation(VoiceoverScene):
    """Main scene that coordinates all the DES explanation subscenes"""

    def construct(self):
        self.set_speech_service(GTTSService(language='en'))

        # Introduction
        intro_scene = DESIntroScene()
        intro_scene.construct()

        # Structure explanation
        structure_scene = DESStructureScene()
        structure_scene.construct()

        # Round function details
        round_scene = DESRoundFunctionScene()
        round_scene.construct()

        # Security considerations
        security_scene = DESSecurityScene()
        security_scene.construct()

        # Conclusion
        conclusion_scene = DESConclusionScene()
        conclusion_scene.construct()
