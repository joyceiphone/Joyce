import numpy as np 
import operator
from math import log
from Collections import Counter

def createDataSet():
	dataSet = [[1, 1, 'yes'],[1, 1, 'yes'],[1, 0, 'no'],[0, 1, 'no'],[0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	
	return dataSet, labels

def calShannonEnt(dataSet):
	labelCounts = {}
	total = len(dataSet)

	for data in dataSets:
		currLabel = data[-1]
		labelCounts[currLabel] = labelCounts.get(currLabel, 0) + 1

	shannonEnt = 0.0

	for key in labelCounts:
		prob = float(labelCounts[key])/total
		shannonEnt = -prob*math.log(prob, 2)

	return shannonEnt

def splitDataSet(dataSet, index, value):
	retDataSet = []

	for data in dataSet:
		if data[index] == value:
			reducedData = data[:index]
		    reducedData.extend(data[index + 1:])
		    retDataSet.append(reducedData)
    
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet) - 1
	baseEntropy = calShannonEnt(dataSet)

	bestInfoGain, bestFeature = 0.0, -1

	for i in range(numFeatures):
		featList = [group[i] for group in dataSet]
		uniqueVals = np.unique(featList)
		newEntropy = 0.0

		for value in uniqueVals:
			subDataSet = split(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calShannonEnt(subDataSet)
    
    	infoGain = baseEntropy - newEntropy
    	if infoGain > bestInfoGain:
    		bestInfoGain = infoGain
    		bestFeature = i

    return bestFeature

def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]

	if classList.count(classList[0])== len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	bestFeature = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeature]

	myTree = {bestFeatLabel: {}}

































