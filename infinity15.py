import turtle
import time
import math
from svg_turtle import SvgTurtle

myPen = SvgTurtle(15000, 15000)

myPen.speed(0)
myPen.color("#000000")

size = 1
stop = 17

angle = 5
degree = 360 / angle
degree2 = degree * 2


def calculate_distance(first, second):
    A, C = first, second
    # Distance formula
    distance = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)
    return distance

def calculate_angle(first, second, third):
    A, B, C = first, second, third
    # Calculate vectors AB and BC
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    
    # Dot product
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    
    # Magnitudes
    magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
    magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)

    if magnitude_AB == 0 or magnitude_BC == 0:
        return 0
    
    # Cosine of the angle
    cos_theta = dot_product / (magnitude_AB * magnitude_BC)
    
    # Calculate the angle in degrees
    angle = math.degrees(math.acos(cos_theta))
    return angle

def zero():
    output.append("+1")
    output.append("-1")
    readable.append("Top")
def posone():
    output.append("+2")
    output.append("-1")
    readable.append("Left")
    myPen.left(degree)
    myPen.forward(size)
def negone():
    output.append("+1")
    output.append("-2")
    readable.append("Right")
    myPen.right(degree)
    myPen.forward(size)
def postwo():
    output.append("+1")
    output.append("+1")
    readable.append("Up")
    myPen.left(degree2)
    myPen.forward(size)
def negtwo():
    output.append("-1")
    output.append("-1")
    readable.append("Down")
    myPen.right(degree2)
    myPen.forward(size)

oldoutput = ["0"]
output = []
readable = []

counting = [0, 0, 0, 0, 0]

data = []

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
    data.append(myPen.pos())
    print("Iterations left: " + str(stop))

print("Done!")


raw_distances = []

counter = 0
while (counter + 1) < len(data):
    distance = calculate_distance(data[counter], data[counter + 1])
    raw_distances.append(distance)
    counter += 1

raw_distance_ratios = []

counter = 0
while (counter + 1) < len(raw_distances):
    ratio = raw_distances[counter + 1] / raw_distances[counter]
    raw_distance_ratios.append(ratio)
    counter += 1

raw_angles = []

counter = 0
while (counter + 2) < len(data):
    angle = 180 - calculate_angle(data[counter], data[counter + 1], data[counter + 2])
    raw_angles.append(angle)
    counter += 1
    
raw_angle_ratios = []

counter = 0
while (counter + 1) < len(raw_angles):
    ratio = raw_angles[counter] / raw_angles[counter + 1]
    raw_angle_ratios.append(ratio)
    counter += 1

angles_from_origin = []

counter = 0
while (counter + 1) < len(data):
    angle = 180 - calculate_angle(data[counter], (0.00, 0.00), data[counter + 1])
    angles_from_origin.append(angle)
    counter += 1

origin_angle_ratios = []

counter = 0
while (counter + 1) < len(angles_from_origin):
    ratio = angles_from_origin[counter] / angles_from_origin[counter + 1]
    origin_angle_ratios.append(ratio)
    counter += 1

distances_from_origin = []

for i in data:
    distance = calculate_distance((0.00, 0.00), i)
    distances_from_origin.append(distance)

origin_distances_ratios = []

counter = 1
while (counter + 1) < len(data):
    ratio = distances_from_origin[counter + 1] / distances_from_origin[counter]
    origin_distances_ratios.append(ratio)
    counter += 1

origin_triangles = []

counter = 0
while (counter + 2) < len(data):
    triangle = []
    triangle.append(180 - calculate_angle(data[counter], data[counter + 1], (0.00, 0.00)))
    triangle.append(180 - calculate_angle(data[counter + 1], data[counter], (0.00, 0.00)))
    triangle.append(180 - calculate_angle(data[counter], (0.00, 0.00), data[counter + 1]))
    origin_triangles.append(triangle)
    counter += 1

sequential_triangles = []

counter = 0
while (counter + 2) < len(data):
    triangle = []
    triangle.append(180 - calculate_angle(data[counter], data[counter + 1], data[counter + 2]))
    triangle.append(180 - calculate_angle(data[counter + 1], data[counter], data[counter + 2]))
    triangle.append(180 - calculate_angle(data[counter], data[counter + 2], data[counter + 1]))
    sequential_triangles.append(triangle)
    counter += 1

print(" ")
print("-----")
print("DATA: ")
print(data)
print(" ")
print("-----")
print("SEQUENTIAL ANGLES: ")
print(raw_angles)
print("-----")
print("SEQUENTIAL ANGLE RATIOS: ")
print(raw_angle_ratios)
print("-----")
print(" ")
print("-----")
print("SEQUENTIAL DISTANCES: ")
print(raw_distances)
print("-----")
print("SEQUENTIAL DISTANCE RATIOS: ")
print(raw_distance_ratios)
print("-----")
print(" ")
print("-----")
print("ANGLES FROM ORIGIN: ")
print(angles_from_origin)
print("-----")
print("ANGLES FROM ORIGIN RATIOS: ")
print(origin_angle_ratios)
print("-----")
print(" ")
print("-----")
print("DISTANCES FROM ORIGIN: ")
print(distances_from_origin)
print("-----")
print("DISTANCES FROM ORIGIN RATIOS: ")
print(origin_distances_ratios)
print("-----")
print(" ")
print("-----")
print("ORIGIN TRIANGLES: ")
for i in origin_triangles:
    print(" -- ")
    print(i)
print("^^^ GOLDEN GNOMON")
print("-----")
print(" ")
print("-----")
print("SEQUENTIAL TRIANGLES: ")
for i in sequential_triangles:
    print(" -- ")
    print(i)
print("-----")
print("^^^ B/C = GOLDEN RATIO")

save = input("Save? y/n - ")
if save == "y":
    myPen.save_as("infinity15.svg")
