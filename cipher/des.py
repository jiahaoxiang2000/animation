from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class DESExplanation(VoiceoverScene):
    def construct(self):
        # Set up the voice service
        self.set_speech_service(GTTSService(language='en'))

        # Title
        title = Text("Data Encryption Standard (DES)", font_size=48)
        with self.voiceover("Welcome to this explanation of the Data Encryption Standard, or DES."):
            self.play(Write(title))
        with self.voiceover("DES is a symmetric-key block cipher that was once widely used for data encryption."):
            self.play(title.animate.to_edge(UP))

        # Overview of DES
        des_overview = BulletedList(
            "Developed in the 1970s",
            "Block size: 64 bits",
            "Key size: 56 bits (with 8 parity bits)",
            "16 rounds of processing",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)

        with self.voiceover("DES was developed in the 1970s. It uses a 64-bit block size and a 56-bit key, although the key is typically represented as 64 bits with 8 bits used for parity checking."):
            self.play(FadeIn(des_overview[:3]))

        with self.voiceover("The algorithm processes data through 16 rounds of encryption operations."):
            self.play(FadeIn(des_overview[3]))

        # Clear screen for the next section
        with self.voiceover("Let's take a closer look at how DES works."):
            self.play(FadeOut(title), FadeOut(des_overview))

        # DES structure diagram
        des_structure = self.create_des_structure()

        with self.voiceover("DES is a Feistel network that consists of an initial permutation, followed by 16 rounds of encryption, and finally a final permutation."):
            self.play(Create(des_structure))

        # Key schedule explanation
        with self.voiceover("The DES key schedule generates 16 48-bit subkeys from the original 56-bit key."):
            key_schedule = Text(
                "Key Schedule: 56-bit → 16 × 48-bit subkeys", font_size=36)
            self.play(FadeIn(key_schedule.to_edge(UP)))

        # Round function explanation
        round_function = self.create_round_function()

        with self.voiceover("In each round, the data block is split into left and right halves. The right half goes through the F function, which includes expansion, key mixing, S-box substitution, and permutation."):
            self.play(FadeOut(des_structure), FadeIn(round_function))

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
            self.play(FadeOut(round_function), FadeOut(key_schedule),
                      FadeIn(security_text), FadeIn(security_points[:2]))

        with self.voiceover("Triple DES was developed to extend DES's security life, but most modern applications now use AES instead."):
            self.play(FadeIn(security_points[2:]))

        # Conclusion
        conclusion = Text(
            "DES was a groundbreaking cipher that influenced modern cryptography", font_size=36)

        with self.voiceover("Despite its limitations, DES was a groundbreaking cipher that greatly influenced the field of modern cryptography."):
            self.play(FadeOut(security_text), FadeOut(
                security_points), FadeIn(conclusion))

        with self.voiceover("Thanks for watching this explanation of the Data Encryption Standard."):
            self.play(FadeOut(conclusion))

    def create_des_structure(self):
        # Create a simple diagram showing DES structure
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

    def create_round_function(self):
        # Create a diagram of the DES round function
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
