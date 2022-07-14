import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

steps = 3
while steps < 10:
    for _ in range(steps):
        tim.forward(100)
        tim.right(360/steps)
    steps += 1