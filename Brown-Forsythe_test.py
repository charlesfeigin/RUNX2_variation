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

def leveneTest(listOne, listTwo):

	#pval = stats.levene(listOne, listTwo, center="trimmed", proportiontocut = .05);
	pval = stats.levene(listOne, listTwo, center="median");

	return pval

#############################################################

# Collect arguments
inFileOne, inFileTwo = sys.argv[1:]

# Open input files
#inOne = open(inFileOne, 'rU')
#inTwo = open(inFileTwo, 'rU')

listOne = listToFile(inFileOne)
listTwo = listToFile(inFileTwo)


pval = leveneTest(listOne, listTwo)

print ("pvalue = {}".format(pval))





