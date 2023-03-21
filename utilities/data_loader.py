import pandas as pd
import os
import numpy as np
import csv
from tqdm import tnrange

def loader(start,end,csv_files,dir_path):
    Array=[]

    for i in tnrange(start,end, desc='Processing CSV files'):
        filename = csv_files[i]
        if i%1000==0:
            print(filename)

        A=[]
        if filename.endswith(".csv"):
        # Open the CSV file and read the contents\
            print(csv_files[i])
            data_frame = pd.read_csv(dir_path+csv_files[i])
            data_frame = data_frame.reset_index(drop=True)
            data_frame = data_frame.drop(index=[0,1]).reset_index(drop=True)
            # Print the data frame to verify the contents
            #print(csvfile)
            A.append(list(map(float, data_frame['Time'].values)))
            A.append(list(map(float, data_frame['Channel A'].values)))
            B_values=data_frame['Channel B'].values
            B_values=[float(val)if val!='-∞'and val!='∞' else 0 if val=='∞' else float('-inf') for val in B_values]
            A.append(B_values)
            Array.append(A)
    # print("reshaping : ",(3, np.shape(Array)[1], int((np.shape(Array)[0])/3)))
    # Array2 = np.reshape(Array, (3, np.shape(Array)[1], int((np.shape(Array)[0])/3)))
    # Array2.shape
    return(Array)