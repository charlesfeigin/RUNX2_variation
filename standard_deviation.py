import sys
import numpy as np
from scipy import stats

###################Function Definitions#######################
def listToFile(file):

	f = open(file, 'rU')

	x = f.readline().strip()

#	print (x)

	myList = x.split(',')
#	print (myList)
	for i, s in enumerate(myList):

		#print(type(myList[i]))

		myList[i] = float(s)

	myArray = np.array(myList)
	
#	print (myArray)

	return myArray

def standardDeviationTest(listOne):

	stdev = np.std(listOne, dtype=np.float64);

	return stdev

#############################################################

# Collect arguments
inFileOne= sys.argv[1]

# Open input files
#inOne = open(inFileOne, 'rU')
#inTwo = open(inFileTwo, 'rU')

listOne = listToFile(inFileOne)
#listTwo = listToFile(inFileTwo)


stdev = standardDeviationTest(listOne)

print ("{}".format(stdev))





