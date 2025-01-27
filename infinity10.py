import turtle
import time
import math
from svg_turtle import SvgTurtle

myPen = SvgTurtle(15000, 15000)

myPen.speed(0)
myPen.color("#000000")

size = 1

def zero():
    output.append("-1")
    output.append("+1")
    readable.append("Top")
def posone():
    output.append("-1")
    output.append("+2")
    readable.append("Left")
    myPen.left(72)
    myPen.forward(size)
def negone():
    output.append("+1")
    output.append("-2")
    readable.append("Right")
    myPen.left(288)
    myPen.forward(size)
def postwo():
    output.append("+1")
    output.append("+1")
    readable.append("Up")
    myPen.left(144)
    myPen.forward(size)
def negtwo():
    output.append("-1")
    output.append("-1")
    readable.append("Down")
    myPen.left(216)
    myPen.forward(size)

oldoutput = ["0"]
output = []
readable = []

counting = [0, 0, 0, 0, 0]

stop = 18

while stop != 0:
    length = len(oldoutput)
    lencounter = 0
    for i in oldoutput:
        if i == "0":
            zero()
            counting[0] += 1
            lencounter += 1
            if lencounter == ( len(oldoutput) / 2 ):
                myPen.dot(5, "blue")
            elif ( (lencounter == ( len(oldoutput) / 4 )) | (lencounter == ( len(oldoutput) * 0.75 ) ) ) & (lencounter != ( len(oldoutput) / 2 )):
                myPen.dot(5, "green")
        elif i == "+1":
            posone()
            counting[1] += 1
            lencounter += 1
            if lencounter == ( len(oldoutput) / 2 ):
                myPen.dot(5, "blue")
            elif ( (lencounter == ( len(oldoutput) / 4 )) | (lencounter == ( len(oldoutput) * 0.75 ) ) ) & (lencounter != ( len(oldoutput) / 2 )):
                myPen.dot(5, "green")
        elif i == "-1":
            negone()
            counting[2] += 1
            lencounter += 1
            if lencounter == ( len(oldoutput) / 2 ):
                myPen.dot(5, "blue")
            elif ( (lencounter == ( len(oldoutput) / 4 )) | (lencounter == ( len(oldoutput) * 0.75 ) ) ) & (lencounter != ( len(oldoutput) / 2 )):
                myPen.dot(5, "green")
        elif i == "+2":
            postwo()
            counting[3] += 1
            lencounter += 1
            if lencounter == ( len(oldoutput) / 2 ):
                myPen.dot(5, "blue")
            elif ( (lencounter == ( len(oldoutput) / 4 )) | (lencounter == ( len(oldoutput) * 0.75 ) ) ) & (lencounter != ( len(oldoutput) / 2 )):
                myPen.dot(5, "green")
        elif i == "-2":
            negtwo()
            counting[4] += 1
            lencounter += 1
            if lencounter == ( len(oldoutput) / 2 ):
                myPen.dot(5, "blue")
            elif ( (lencounter == ( len(oldoutput) / 4 )) | (lencounter == ( len(oldoutput) * 0.75 ) ) ) & (lencounter != ( len(oldoutput) / 2 )):
                myPen.dot(5, "green")
        length -= 1
        if length == 0:
            break
    readable = []
    #print(counting)
    #print(readable)
    #print(output)
    #for i in output:
    #    print(i + ",")
    oldoutput = output
    output = []
    stop -= 1
    #time.sleep(0.5)
    myPen.dot(5, "red")
    print("Iteration completed:" + str(stop))

print("Done!")

save = input("Save? y/n - ")
if save == "y":
    myPen.save_as("infinity10.svg")
