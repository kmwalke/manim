from manim import *


class CreateCircle(Scene):
  def construct(self):
    circle = Circle()  # create a circle
    circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
    self.play(Create(circle))  # show the circle on scree

class SquareToCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(PINK, opacity=0.5)

    square = Square()
    square.rotate(PI / 4)

    self.play(Create(square))
    self.play(Transform(square, circle))
    self.play(FadeOut(square))

class SquareAndCircle(Scene):
  def construct(self):
    circle = Circle()  # create a circle
    circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

    square = Square()  # create a square
    square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

    square.next_to(circle, RIGHT, buff=0.5)  # set the position
    self.play(Create(circle))
    self.play(Create(square))  # show the shapes on screen

    self.play(FadeOut(square), FadeOut(circle))

class AnimatedSquareToCircle(Scene):
  def construct(self):
    circle = Circle()
    square = Square()

    self.play(Create(square))
    self.play(square.animate.rotate(PI / 2))
    self.play(Transform(square, circle))
    self.play(
            square.animate.set_fill(BLUE, opacity=0.5)
    )
    self.play(square.animate.flip(axis=[0., 1., 0.]))
    self.play(square.animate.shift(RIGHT))
    self.play(FadeOut(square))

class DifferentRotations(Scene):
  def construct(self):
    left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
    right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
    angle = PI / 2

    self.play(
      left_square.animate.rotate(angle), Rotate(right_square, angle=angle), run_time=4
    )
    self.wait()

class TwoTransforms(Scene):
	def transform(self):
		a = Circle()
		b = Square()
		c = Triangle()

		self.play(Transform(a, b))
		self.play(Transform(a, c))
		self.play(FadeOut(a))

	def replacement_transform(self):
		a = Circle()
		b = Square()
		c = Triangle()

		self.play(ReplacementTransform(a, b))
		self.play(ReplacementTransform(a, c))
		self.play(FadeOut(a))

	def construct(self):
		self.transform()
		self.wait(0.5)
		self.replacement_transform()

class TransformCycle(Scene):
  def construct(self):
    a = Circle()
    t = [ Square(), Triangle(), Circle(), Square(), Triangle() ]

    self.play(Create(a))

    self.wait(1)
    for shape in t:
      self.play(Transform(a,shape), run_time=1)

    self.play(FadeOut(a))
