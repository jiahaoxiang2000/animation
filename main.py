from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # noqa: F405
        square.rotate(PI / 4)  # rotate a certain amount noqa

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the circle
        self.play(FadeOut(square))  # fade out animation
