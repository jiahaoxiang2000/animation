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

        with self.voiceover("The input plaintext is divided into 64-bit blocks, and each block is encrypted separately using the same key to produce 64-bit blocks of ciphertext."):
            self.play(
                Indicate(plaintext, color=GREEN),
                Indicate(key_text, color=YELLOW),
                Indicate(block_cipher_diagram, color=BLUE),
                Indicate(ciphertext, color=RED),
                run_time=4
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
        self.set_speech_service(GTTSService(language='en'))

        # DES structure diagram
        des_structure = DESComponents.create_des_structure()

        with self.voiceover("DES is a Feistel network that consists of an initial permutation, followed by 16 rounds of encryption, and finally a final permutation."):
            self.play(Create(des_structure))

        self.wait(1)

        # Key schedule explanation
        with self.voiceover("The DES key schedule generates 16 48-bit subkeys from the original 56-bit key."):
            key_schedule = Text(
                "Key Schedule: 56-bit → 16 × 48-bit subkeys", font_size=36)
            self.play(FadeIn(key_schedule.to_edge(UP)))

        self.wait(1)
        self.play(FadeOut(des_structure), FadeOut(key_schedule))


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
