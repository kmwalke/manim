from manim import *
import random

class Arctic(Scene):
  def construct(self):
  

### Setup Initial Square
    squares=[]
    square = Square(color=BLUE, side_length=1)
    self.add(square)

### Draw Starting Grid
    for i in range(0, 4):
      for j in range(0, 4):
        new_square = square.copy().shift([i, j, 0])
        self.add(new_square)

### Draw Domino
    domino = Group(
      Rectangle(color=RED, height=2, width=1),
      Arrow(start=[-0.6, 0.5, 0], end=[0.6, 0.5, 0])
    )
    domino[0].set_fill(RED, opacity=1.0)
    domino[0].shift([0,0.5,0])
    self.play(Create(domino[0]))
    self.play(Create(domino[1]))
    
### Show Domino Position
    x_coor = Variable(0, 'x', num_decimal_places=1)
    y_coor = Variable(0, 'y', num_decimal_places=1)

    x_coor.shift(LEFT * 4)
    y_coor.shift(LEFT * 4, DOWN)

    self.play(Write(x_coor), Write(y_coor))


### Move Domino
    directions = [LEFT, RIGHT, UP, DOWN]

    for i in range(10):
      direction = random.choice(directions)
      x_val = x_coor.tracker.get_value()
      y_val = y_coor.tracker.get_value()
      new_x_val = x_val + direction[0]
      new_y_val = y_val + direction[1]
      if new_x_val < 0 or new_x_val > 3:
        direction[0] = direction[0] * -1
      if new_y_val < 0 or new_y_val > 2:
        direction[1] = direction[1] * -1
      self.play(
        x_coor.tracker.animate.set_value(x_val + direction[0]),
        y_coor.tracker.animate.set_value(y_val + direction[1]),
        domino.animate.shift(direction),
        run_time = 2
      )

### Wait
    self.wait()

