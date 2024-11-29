from manim import *
import random

class Arctic(Scene):
  def construct(self):
  
### Global Vars
    a_n_max = 10
    animation_speed = 1

### Setup arctic array
    for a_n in range(1, a_n_max):
      arctic=[[None] * a_n] * a_n
      square = Square(color=BLUE, side_length=1)
      corner = Group()

      for i in range(0, a_n):
        for j in range(0, a_n):
          if i + j < a_n:
            arctic[i][j] = 0
            new_square = square.copy().shift([i, j, 0])
            #corner.add(Integer(j).next_to(new_square, RIGHT, -0.9))
            #corner.add(Integer(i).next_to(new_square, RIGHT, -0.5))
            corner.add(new_square)

      self.play(
        FadeIn(
          Group(
            corner,
            corner.copy().shift([-a_n, 0, 0]).flip([0, 1, 0]),
            corner.copy().shift([-a_n, -a_n, 0]).flip([-1, 1, 0]),
            corner.copy().shift([0, -a_n, 0]).flip([1, 0, 0])
          )
        )
      )


### Wait
      self.wait(animation_speed)
      self.clear()

