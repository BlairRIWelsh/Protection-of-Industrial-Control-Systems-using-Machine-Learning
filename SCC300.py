import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing


fileName = "dataset.txt"
splitModbusFrame = True
detectCategorizationOrSpecificAttack = True
imputationTechnique = 'zeroes'
normalisationTechnique = 'constant factor'
testSize = 0.30

def loadDataSet():
    dataset = pd.read_csv (fileName,header=None)
    if splitModbusFrame == True:
        temp = pd.DataFrame()
        temp[0] = dataset[0].str.slice(0,2).apply(int, base=16)
        temp[1] = dataset[0].str.slice(2,4).apply(int, base=16)
        temp[2] = dataset[0].str.slice(4,8).apply(int, base=16)
        temp[3] = dataset[0].str[8:-4] # 8th to the 4th last digit is the value to write
        temp[4] = dataset[0].str[-4:].apply(int, base=16) # Last 4 digits of Modbus Frame are CRC
       
        # temp[3] = temp[3].apply(int, base=16).astype(int) # convert the hex string to write to an int - OVERFLOW 
       
        temp = pd.concat([temp, dataset.drop(columns = 0)], axis=1, sort=False, ignore_index=True) # Drop Modbus frame and concat tables
        dataset = temp
    
    return dataset

def cleanDataSet(dataset):
    # deal with spurious lines
      
    # find and deal with missing data
    
    if splitModbusFrame == True:
      # imputation choice goes here
      dataset[3] = dataset[3].replace(r'^\s*$', "0", regex=True) # Replace blank values with a 0 string
      
    # remove any unwanted columns
      
    # find anddeal with bad numeric data
    
    ## FIND AND DEAL WITH BAD CATEGORICAL DATA
    # If we have split the data ValueToWrite is a String, else the ModbusFrame is a String so Encode them with labels
    if splitModbusFrame == True: val = 3 
    else: val = 1
    le = preprocessing.LabelEncoder()
    le.fit(dataset[val])
    dataset[val] = le.transform(dataset[val])
    
    return dataset
    
# def normaliseDataset():
#     # normalise numeric predictors
#     if (normalisationTechnique == 'min-max'):
        
#     else if (normalisationTechnique == 'z-score'):
        
#     else if (normalisationTechnique == 'constant factor'):
    
#     else:
#         print("Normalisation technique not recognised.")
            
#     # encode categorical predictors
#     # encode categorical dependant variable
    
# def selectTypeOfAlgorithm():
#     True
    
def splitDataSet(dataset):
    if splitModbusFrame == False:
        # separate the data from the target attributes
        if detectCategorizationOrSpecificAttack == True:
            y = dataset[1]
        else:
            y = dataset[2]
        x = dataset.drop([1,2],axis=1)
    else:
        # separate the data from the target attributes
        if detectCategorizationOrSpecificAttack == True:
            y = dataset[5]
        else:
            y = dataset[6]
        x = dataset.drop([5,6],axis=1)
    return x, y

    
############################################################################################################################################################


# dataset = cleanDataSet(dataset)

# valToWrite = pd.get_dummies(dataset[3],drop_first = True)
# dataset[3] = valToWrite

dataset = loadDataSet()
dataset = cleanDataSet(dataset)

X,y = splitDataSet(dataset)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = testSize)
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))


# normalize the data attributes
# normalized_X = preprocessing.normalize(x)

# normaliseDataset()

# selectTypeOfAlgorithm()
