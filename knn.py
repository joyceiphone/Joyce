import numpy as np

def file2Matrix():
    data = np.loadtxt('datingTestSet2.txt')
    returnMat = data[:, :3]
    classLabelVector = data[:,-1]
    return returnMat, classLabelVector
def euclideanDist(inX, inY):
    length = 0
    for i in len(inX):
        diff = inX[i] - inY[i]
        sqDiff = pow(diff, 2)
        length+= sqDist
    return length^(0.5)
def classify(inX, dataSet, labels, k):
    distances = []
    for i in len(dataSet.shape[0]):
        distance.append(euclideanDist(inX, dataSet[i]))
    
    sortedDistIndices = distances.argsort()
    classCount = {}
    
    for i in range(k):
        voterLabel = labels[sortedDistIndices[i]]
        classCount[voterLabel] = classCount.get(voterLabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2Matrix()
    nRow = datingDataMat.shape[0]
    numTestVecs = int(hoRatio*nRow)
    
    count = 0.0

datingClassTest()
