# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:41:10 2020

@author: Blair
"""
import pandas as pd
import numpy as np
import seaborn as sns

def makeHelpDataFrame():
    
    helpDataFrame = dataset.copy() # Create a copy of the dataset
    
    if splitModbusFrame == True:
        # Rename headings so they are easier to understand
        helpDataFrame.columns = ['Slave Address', 'Function Code', 'Register Address', 'Value', 'CRC','Categorization','Specific Attack','Source','Destination', 'Time Stamp']
        
        # Convert all Hex values to Int.
        helpDataFrame["Slave Address"] = helpDataFrame["Slave Address"].apply( lambda x: int(x,16))
        helpDataFrame["Function Code"] = helpDataFrame["Function Code"].apply( lambda x: int(x,16) )
        helpDataFrame["Register Address"] = helpDataFrame["Register Address"].apply(lambda x: int(x,16) + 40001) # Registers start at 40000
        helpDataFrame["CRC"] = helpDataFrame["CRC"].apply( lambda x: int(x,16) )
        
        helpDataFrame = helpDataFrame.replace(
        {
        'Slave Address': { 0x04: "Gas(04)"}, 
        "Function Code": {
            3: "Read Holding Register(0x03)",
            2: "Read Discrete Input(0x02)",
            4: "Read input Register(0x04)",
            16: "Write Holding Register(0x10)",
            6: "Write Single Register(0x06)",
            144: "Exception for Write Multiple Registers(0x90)",
            20: "Read File Record(0x14)"
            
            }})
    else:
            helpDataFrame.columns = ['Modbus Frame','Categorization','Specific Attack','Source','Destination', 'Time Stamp']
    
    helpDataFrame = helpDataFrame.replace(
        {'Categorization': {
            0: "Normal(0)", 
            1: "NMRI(1)",
            2: "CMRI(2)",
            3: "MSCI(3)",
            4: "MPCI(4)",
            5: "MFCI(5)",
            6: "DoS(6)",
            7: "Recon(7)",},
        "Specific Attack": {
            0: "Normal(0)", 
            1: "Setpoint Attack - Outside Range(1)",
            2: "Setpoint Attack - Inside Range(2)",
            3: "PID Gain Attack - Outside Range(3)",
            4: "PID Gain Attack - Inside Range(4)",
            5: "PID Reset Rate Attack - Outside Range(5)",
            6: "PID Reset Rate Attack - Inside Range(6)",
            7: "PID Rate Attack - Outside Range(7)",
            8: "PID Rate Attack - Inside Range(8)", 
            9: "PID Deadband Attack - Outside Range(9)", 
            10: "PID Deadband Attack - Inside Range(10)", 
            11: "PID Cycle Time Attack - Outside Range(11)",
            12: "PID Cycle Time Attack - Inside Range(12)",
            13: "Pump Attack(13)", 
            14: "Solenoid Attack(14)", 
            15: "System Mode Attack(15)",
            16: "Critical Condition Attack(16)", 
            17: "Critical Condition Attack(17)", 
            18: "Bad CRC Attack(18)", 
            19: "Clean Registers Attack(19)", 
            20: "Device Scan Attack(20)", 
            21: "Force Listen Attck(21)", 
            22: "Restart Attack(22)", 
            23: "Read ID Attack(23)", 
            24: "Function Code Scan Attack(24)", 
            25: "Rise/Fall Attack(25)",
            26: "Rise/Fall Attack(26)", 
            27: "Slope Attack - Increase(27)", 
            28: "lope Attack - Decrease(28)", 
            29: "Random Value Attack(29)", 
            30: "Random Value Attack(30)", 
            31: "Random Value Attack(31)", 
            32: "Negative Pressure Attack(32)", 
            33: "Fast Attack(33)", 
            34: "Fast Attack(34)", 
            35: "Slow Attack(35)"},
        "Source" : {
            1: "Master(1)",
            2: "Man-in-the-Middle(2)",
            3: "Slave(3)"},
        "Destination" : {
            1: "Master(1)",
            2: "Man-in-the-Middle(2)",
            3: "Slave(3)"},
        })    
    return helpDataFrame

def displayHelpDatasetInformation():
    # Describe data set object types and collumns
    helpDataFrame.describe()
    print()
    
    # Mathematical Infromation about Int Collumns
    helpDataFrame.info()
    print()
    
    print("% Slave Address")
    print(helpDataFrame["Slave Address"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    print("% Function Code")
    print(helpDataFrame["Function Code"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    print("% Register Addresses")
    print(helpDataFrame["Register Address"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    print("% Values")
    print(helpDataFrame["Value"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    # % of Cateogrization attacks
    print("% of Cateogization Attacks")
    print(helpDataFrame["Categorization"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    # % Of specfic attacks
    print("% Specific Attacks")
    print(helpDataFrame["Specific Attack"].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
    
    print("% Direction of Attacks")
    print((helpDataFrame["Source"] + " - " + helpDataFrame["Destination"]).value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
    print()
 

fileName = "dataset.txt"
splitModbusFrame = True
createHelpDataFrame = True
displayDataSetInfo = True

dataset = pd.read_csv (fileName,header=None)
if splitModbusFrame == True:
    # 
    temp = pd.DataFrame()
    temp[0] = dataset[0].str.slice(0,2)
    temp[1] = dataset[0].str.slice(2,4)
    temp[2] = dataset[0].str.slice(4,8)
    temp[3] = dataset[0].str[8:-4] # 8th to the 4th last digit is the value to write
    temp[4] = dataset[0].str[-4:] # Last 4 digits of Modbus Frame are CRC
    temp = pd.concat([temp, dataset.drop(columns = 0)], axis=1, sort=False, ignore_index=True) # Drop Modbus frame and concat tables
    dataset = temp
    
if createHelpDataFrame == True:
        helpDataFrame = makeHelpDataFrame()

if displayDataSetInfo == True:
    displayHelpDatasetInformation()