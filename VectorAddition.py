import math

class DirectionMapping:

  def direc(self, vectorInput):
        global direction
        global magnitude
        global theta
        direction = [vectorInput[2], vectorInput[4]]
        magnitude = float(vectorInput[0])
        theta = float(vectorInput[1]) * math.pi/180
        default = "N"
        return getattr(self, 'case_' + str(direction[0]), lambda: default)()

  def case_N(self):
    if(direction[1] == "E"):
      xComp = math.cos(theta)
      yComp = math.sin(theta)
    else :
      xComp = -1 * math.cos(theta)
      yComp = math.sin(theta)
    return (magnitude * xComp, magnitude * yComp)

  def case_S(self):
    if(direction[1] == "E"):
      xComp = math.cos(theta)
      yComp = -1 * math.sin(theta)
    else :
      xComp = -1 * math.cos(theta)
      yComp = -1 * math.sin(theta)
    return(magnitude * xComp, magnitude * yComp)

  def case_E(self):
    if(direction[1] == "N"):
      xComp = math.sin(theta)
      yComp = math.cos(theta)
    else:
      xComp = math.sin(theta)
      yComp = -1 * math.cos(theta)
    return(magnitude * xComp, magnitude * yComp)

  def case_W(self):
    if(direction[1] == "N"):
      xComp = -1 * math.sin(theta)
      yComp = math.cos(theta)
    else:
      xComp = -1 * math.sin(theta)
      yComp = -1 * math.cos(theta)
    return(magnitude * xComp, magnitude * yComp)




vector1 = input("Enter the vector with magnitude then direction(North = N, South = S, and so on) \n Ex: 5.6(magnitude) 7.73(degrees) N of E \n ").split(" ")
vector2 = input("Enter the second vector: \n").split(" ")

directionMapper = DirectionMapping()
xComp1, yComp1 = directionMapper.direc(vector1)
xComp2, yComp2 = directionMapper.direc(vector2)

x = xComp1 + xComp2
y = yComp1 + yComp2

finalAngle = math.atan(y/x) * 180/math.pi

print("\nVector 1: " + str(xComp1) + ", " + str(yComp1))
print("Vector 2: " + str(xComp2) + ", " + str(yComp2))
print("Final Vector: " + str(x) + ", " + str(y))

print("Magnitude: " + str(math.pow(math.pow(x,2) + math.pow(y,2), 0.5)))



if(x > 0):
  if(y > 0):
    print("Direction: " + str(abs(finalAngle)) + " degrees N of E")
  else:
    print("Direction: " + str(abs(finalAngle)) + " degrees S of E")
else:
  if(y > 0):
    print("Direction: " + str(abs(finalAngle)) + " degrees N of W")
  else:
    print("Direction: " + str(abs(finalAngle)) + " degrees S of W")
