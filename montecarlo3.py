import random
import math

print("Monte Carlo Quadrant Method for Approximating π")
inCircle = 0
outCircle = 0
pointRatio = 0.0 #Will be set to inCircle/outCircle
approximation = 0.0 #Will be set to pointRatio * 4
localPi = 3.1415926535
difference = 0 #Will be set to Math.abs(approximation - localPi)
for i in range(10):
	x = random.random();
	y = random.random();
	if math.pow(x,2) + math.pow(y,2) < 1:
		inCircle += 1
	else:
		outCircle += 1

pointRatio = float(inCircle/10)
approximation = float(pointRatio * 4)
difference = float(math.fabs(approximation - localPi))

print("In the Circle: " , inCircle)
print("Out of Circle: " , outCircle)
print("Ratio: " , pointRatio)
print("Pi = " , approximation)
print("Difference:" , difference)

print("\n\n\n")	

inCircle = 0
outCircle = 0
pointRatio = 0.0 #Will be set to inCircle/outCircle
approximation = 0.0 #Will be set to pointRatio * 4
localPi = 3.1415926535
difference = 0 #Will be set to Math.abs(approximation - localPi)
for i in range(100):
	x = random.random();
	y = random.random();
	if math.pow(x,2) + math.pow(y,2) < 1:
		inCircle += 1
	else:
		outCircle += 1

pointRatio = float(inCircle/100)
approximation = float(pointRatio * 4)
difference = float(math.fabs(approximation - localPi))

print("In the Circle: " , inCircle)
print("Out of Circle: " , outCircle)
print("Ratio: " , pointRatio)
print("Pi = " , approximation)
print("Difference:" , difference)

print("\n\n\n")

inCircle = 0
outCircle = 0
pointRatio = 0.0 #Will be set to inCircle/outCircle
approximation = 0.0 #Will be set to pointRatio * 4
localPi = 3.1415926535
difference = 0 #Will be set to Math.abs(approximation - localPi)
for i in range(1000):
	x = random.random();
	y = random.random();
	if math.pow(x,2) + math.pow(y,2) < 1:
		inCircle += 1
	else:
		outCircle += 1

pointRatio = float(inCircle/1000)
approximation = float(pointRatio * 4)
difference = float(math.fabs(approximation - localPi))

print("In the Circle: " , inCircle)
print("Out of Circle: " , outCircle)
print("Ratio: " , pointRatio)
print("Pi = " , approximation)
print("Difference:" , difference)

print("\n\n\n")

inCircle = 0
outCircle = 0
pointRatio = 0.0 #Will be set to inCircle/outCircle
approximation = 0.0 #Will be set to pointRatio * 4
localPi = 3.1415926535
difference = 0 #Will be set to Math.abs(approximation - localPi)
for i in range(10000):
	x = random.random();
	y = random.random();
	if math.pow(x,2) + math.pow(y,2) < 1:
		inCircle += 1
	else:
		outCircle += 1

pointRatio = float(inCircle/10000)
approximation = float(pointRatio * 4)
difference = float(math.fabs(approximation - localPi))

print("In the Circle: " , inCircle)
print("Out of Circle: " , outCircle)
print("Ratio: " , pointRatio)
print("Pi = " , approximation)
print("Difference:" , difference)

print("\n\n\n")

inCircle = 0
outCircle = 0
pointRatio = 0.0 #Will be set to inCircle/outCircle
approximation = 0.0 #Will be set to pointRatio * 4
localPi = 3.1415926535
difference = 0 #Will be set to Math.abs(approximation - localPi)
for i in range(100000):
	x = random.random();
	y = random.random();
	if math.pow(x,2) + math.pow(y,2) < 1:
		inCircle += 1
	else:
		outCircle += 1

pointRatio = float(inCircle/100000)
approximation = float(pointRatio * 4)
difference = float(math.fabs(approximation - localPi))

print("In the Circle: " , inCircle)
print("Out of Circle: " , outCircle)
print("Ratio: " , pointRatio)
print("Pi = " , approximation)
print("Difference:" , difference)

print("\n\n\n")
print("End of program")
