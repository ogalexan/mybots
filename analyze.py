import numpy 
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
targetAngleValues = numpy.load('data/targetAngles.npy')
print(backLegSensorValues)
print("")
print(frontLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 6.0, label = 'BackLeg')
#matplotlib.pyplot.plot(frontLegSensorValues, linewidth = 2.0, label = 'FrontLeg')
matplotlib.pyplot.plot(targetAngleValues, linewidth = 2.0)

#matplotlib.pyplot.legend()
matplotlib.pyplot.show()

