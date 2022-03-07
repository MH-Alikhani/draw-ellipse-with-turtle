import turtle

def draw_ellipse(rad):
  '''
  This is a function to draw ellipse
  It divide the ellipse into four arcs
  '''
  for i in range(2):
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)

# Make the ellipse to stay in a good state
turtle.seth(-45)


draw_ellipse(100)


# If you wanna not close the window after it's done, use: turtle.done()