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



