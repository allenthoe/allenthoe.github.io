# Allen's Cool Python Program
# This program will take in user input and use that input to draw designs.
# PLTW CORE TRAINING - 2017 San Diego State University

import turtle
import time

# Greeting
print ('Hello! This program is going to show you a module called \"turtle\".')
time.sleep(1)                    # This line allows for a 1 second delay between print statements
print() 
print ('Would you like me to draw a regular polygon? (yes or no)')
answer = input()

# Set up  
window = turtle.Screen()         # Creates a window to draw in
window.title('PLTW 2017')        # Rename the window
allen=turtle.Turtle()            # Creates a turtle can be created and set to any name.
s = 500                          # Initialize a variable 's' to determine the total distance
window.colormode(255)            # Change to RGB Colormode so we can use numbers to change
allen.speed(9)                   # Makes the turtle go really fast

#Define the functions I will call in my program


def initialize():

    if answer == 'yes':
        print ('Ok, how many sides should it have? (only INTEGERS please)')
        n = int(input())
        if n > 1:
            RegularPoly(n)
        else:
            print ('Please enter an integer greater than 1')
            initialize()
        print ('Would you like me to draw another one? (\'yes\' or \'no\')')
        response = input()
        if response == 'yes':
            initialize()
            
    elif answer == 'no':
        print (' :( ')
        print()
        time.sleep(1)
        
    else:
        print ('I\'m sorry, I can only interpret the responses \'yes\' or \'no\'.')
        initialize()

def RegularPoly(n):         # This function takes the parameter 'n' and makes
                            # a regular polygon with that many sides.
        for i in range (n):
            allen.forward(s/n)
            allen.right(360/n)

# Nested Loops (with and without user control)
def control():
    r = 0
    g = 255
    b = 0
    for i in range (3,12):
        print ('Presee ENTER to proceed each time through the loop')
        input()         # This line pauses the loop and waits for input() from the user
        r = r + 25
        g = g - 20
        b = b + 10
        allen.color(r, g, b)
        RegularPoly(i)  # As you recall, this function is a loop.  So this loop is nested

def nocontrol():
    r = 0
    g = 255
    b = 100
    for i in range (3,12):

        r = r + 25
        g = g - 20
        b = b + 10
        allen.color(r, g, b)
        RegularPoly(i)  # As you recall, this function is a loop.  So this loop is nested

def nested():
    
    print ('Would you like to control when I go through the loop eaxch time?')
    choice4 = input()
    if choice4 == 'yes':
        print ('Ok.')
        control()
    else:
        nocontrol()

# User input to make their own shapes using loops        

def shapes():
    window.clear()
    window.bgcolor("Blue")
    allen.color("White")
    allen.goto(0,0)
    print ('Enter a value for how far to go first, call it x: ')
    x = int(input())
    print ('Enter an angle to turn, call it theta: ' )
    theta = int(input())        
    print ('Enter a value to more foward the second time, y: ')
    y = int(input())
    print ('Enter the second turn, phi :')
    phi = int(input())        
    print ('Enter the number of times to go through the loop, n: ')
    n = int(input())
    for i in range (n):
        allen.forward(x)
        allen.right(theta)
        allen.forward(y)
        allen.right(phi)
    print ("Do you want to try it again with new numbers?")
    choice6 = input()
    if choice6 == 'yes':
        shapes()
    else:
        print ('Goodbye!')

"""Begin the Program"""  # Now it is time to start calling functions

initialize()
print ('OK.  Let\'s move on.')
time.sleep(1)
window.clear()
window.colormode(255)

print ('Would you like me to change the background color to black?')
choice3 = input()
if choice3 == 'yes':
    window.bgcolor("Black")     # Changes bg color IFF the user types 'yes'

print ('Would you like to draw a series of regular polygons by going through some loops.')
choice5 = input()
if choice5 == 'yes':
    nested()          

    print ('Would you like to do it again?')
    choice4 = input()
    if choice4 == 'yes':
        nested()

print ('Ok, last thing.  How about you make your own shapes?')
shapes()                # Calls the final function

# Finish
print ('That is ALL I have in this program.')
time.sleep(.5)
print ('I hopoe you enjoyed it.')
time.sleep(2)
print ('email me at:  allenthoe@gmail.com ')
time.sleep(1)
print ('TTFN')
window.mainloop()     # This holds the turtle graphics window open till the user closes it
