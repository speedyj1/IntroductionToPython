"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jack Speedy.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle=rg.SimpleTurtle('turtle')
blue_turtle.pen=rg.Pen('blue',5)
blue_turtle.speed= 7

yellow_turtle=rg.SimpleTurtle('turtle')
yellow_turtle.pen=rg.Pen('yellow',3)
yellow_turtle.speed= 5

blue_size=350
yellow_size=-200

for k in range(11):
    blue_turtle.draw_regular_polygon(3,blue_size)
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)
    blue_turtle.pen_down()
    blue_size=blue_size - 15

    yellow_turtle.draw_circle(yellow_size)
    yellow_turtle.pen_up()
    yellow_turtle.right(45)
    yellow_turtle.forward(10)
    yellow_turtle.left(45)
    yellow_turtle.pen_down()
    yellow_size-yellow_size+ 10
