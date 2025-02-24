import numpy

iterations = 1000

backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)
angles = [i * (2* numpy.pi) / (iterations - 1) for i in range(iterations)]
targetAngles = numpy.sin(numpy.array(angles))
targetAngles = targetAngles * (numpy.pi / 4)


BackLegAmplitude = numpy.pi/4
BackLegFrequency = 40
BackLegPhaseOffset = 0
BackLegMotorVectors = [BackLegAmplitude * numpy.sin(BackLegFrequency * j + BackLegPhaseOffset) for j in targetAngles]

FrontLegAmplitude = numpy.pi/4
FrontLegFrequency = 40
FrontLegPhaseOffset = 0
FrontLegMotorVectors = [FrontLegAmplitude * numpy.sin(FrontLegFrequency * k + BackLegPhaseOffset) for k in targetAngles]


maxForce = 500 


