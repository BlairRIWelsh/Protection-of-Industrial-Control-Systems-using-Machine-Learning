
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np
import pandas as pd
import sys

fileName = 'IanArffDataset.arff'

def loadDataset():
    # Tried loading in the dataset as an arff but sparce values did not work so just coverted it to csv and imported it here
    df = pd.read_csv ("arffcsv.csv",header=0, na_values = "?")
    df.columns = ['Address', 'Function', 'Length', 'Setpoint', 'Gain','Reset Rate','Deadband','Cycle Time', 'Rate','System Mode','Control Scheme','Pump','Solenoid','Pressure Measurement','CRC Rate','Command Response','Time','Binary Result','Categorized Result','Specific Result']
    print("Dataset loaded: "+ fileName + "\n")
    return df

def preProcessDataset(dataset):
    print("Preprocessing Dataset...\n")
    
    # treatedDataset
    
    # search whole table for null values
    nullValsInTable = dataset.isnull().sum().sum()
    nullValsInTablePercentage = round((nullValsInTable / (dataset.shape[0] * dataset.shape[1])) * 100,2)
    columnsWithNullVals = dataset.isnull().sum().astype(bool).sum()
    
    # leave if no nulls are found
    if nullValsInTable == 0:
        print("No Null values found.")
        print("Pre-processing finished.")
        return dataset
    
    # if found ask to deal with them all as one or sperately
    print(nullValsInTable,"(",nullValsInTablePercentage,"% )", "null values found in ",columnsWithNullVals,"/",dataset.shape[1]," collumns")
    print("What would you like to do?")
    
    # print menu
    print ("""
      1.Leave all Null values
      2.Deal with all Null values at once
      3.Deal with Null values collumn by collumn
      9.Exit/Quit""")
    while True:
      ans=input("Choice: ") 
      print("")
      # Leave all Null values
      if ans=="1":
          print("Pre-processing finished.")
          return dataset
      
      # Deal with all Null values at once
      elif ans=="2":
          print("Selection: Deal with all Null values at once") 
          temp = treatMissingValuesInGivenDF(dataset)
          return temp
         
      # Deal with Null values Column by Column
      elif ans=="3":
          print("e") 
          
      # Quit
      elif ans=="9":
          print("\nGoodbye.")
          sys.exit(0)
      else:
          print("\r\n[ERROR] Not Valid Choice. Please try again.") 
    
# def treatMissingValues:
    
    
def treatMissingValuesInGivenDF(df):
    if df.shape[0] == 1:
        print("How would you like to remove Null values?") 
        print ("""
            1.Imputation - Mean
            2.Imputation - Median
            3.Imputation - Mode
            4.Imputation - All Zeros
            9.Exit/Quit""")
        while True:
            ans=input("Choice: \r") 
            print("")
            if ans=="1":
                print("Selection: Imputation - Mean")
                imp = SimpleImputer(missing_values=np.nan, strategy='mean')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="2":
                print("Selection: Imputation - Median")
                imp = SimpleImputer(missing_values=np.nan, strategy='median')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="3":
                print("Selection: Imputation - Mode")
                imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="4":
                print("Selection: Imputation - All Zeros")
                imp = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value = 0)
                imp.fit(df)
                return imp.transform(df)
    else:
        print("How would you like to remove Null values?") 
        print ("""
            1.Imputation - Mean
            2.Imputation - Median
            3.Imputation - Mode
            4.Imputation - All Zeros
            5.Imputation - Multivariate
            6.Deletion - Delete Rows
            7.Deletion - Delete Collumns
            9.Exit/Quit""")
        while True:
            ans=input("Choice: \r") 
            print("")
            if ans=="1":
                print("Selection: Imputation - Mean")
                imp = SimpleImputer(missing_values=np.nan, strategy='mean')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="2":
                print("Selection: Imputation - Median")
                imp = SimpleImputer(missing_values=np.nan, strategy='median')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="3":
                print("Selection: Imputation - Mode")
                imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                imp.fit(df)
                return imp.transform(df)
            elif ans=="4":
                print("Selection: Imputation - All Zeros")
                imp = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value = 0)
                imp.fit(df)
                return imp.transform(df)
            elif ans=="5":
                print("Selection: Imputation - Multivariate")
                print("[ERROR] Feature not working yet. Please choose again.")
                # iters = input("How many iterations do you want to go through?: ")
                
                # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
                # imp.fit(df)
                # df = imp.transform(df)
                
                # imp = IterativeImputer(missing_values=np.nan,max_iter=iters,initial_strategy = 'mean')
                # imp.fit(df)
                # return imp.transform(df)
            elif ans=="6":
                print("Selection: Deletion - Delete Rows")
                return df.dropna(how='any',axis=0) 
                # should i have a check here in case this returns no columns
            elif ans=="7":
                print("Selection: Deletion - Delete Collumns")
                return df.dropna(how='any',axis=1) 
            elif ans=="9":
                print("\nGoodbye.")
                sys.exit(0)
            else:
                print("\r\n[ERROR] Not Valid Choice. Please try again.")
    
###############################################################################

print()
dataset = loadDataset()
orig = dataset
# dataset.info()
dataset = preProcessDataset(dataset)