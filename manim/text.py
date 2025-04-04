from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
from manim import *


class HelloWorld(Scene):
    def construct(self):
        text1 = Text("Hello world", font_size=144,
                     color=RED)
        text2 = Text("Hello isomo", font_size=144)
        self.add(text1)
        self.play(Transform(text1, text2))


class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)


class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{
                YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)


class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)


class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex(r'你好 \LaTeX \\ $a+b=c$',
                  tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)


# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class RecorderExample(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        # self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="我们将去画一个圆") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="将它向左移动2个单位") as tracker:
            self.play(circle.animate.shift(2 * LEFT),
                      run_time=tracker.duration)
