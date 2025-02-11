import numpy 
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
print(backLegSensorValues)
print("")
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, linewidth = 6.0, label = 'BackLeg')
matplotlib.pyplot.plot(frontLegSensorValues, linewidth = 2.0, label = 'FrontLeg')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()


