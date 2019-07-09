import pandas as pd
import numpy as np

data_200 = pd.read_csv("/Users/eileenschilliger/Documents/Studium/01_Geografie/Master_neu2/Geodata analysis and modelling/Eigenes Projekt/pyCharm/Einzugsgebiete_200mB.csv", sep=";")
#print(data_200)

mean_H = data_200['mH_04'].mean()
print ('The middle high of ' + 'str(id) ' + 'is ' + str(mean_H) + ' m ü.M.')


min_H = data_200['Hmin_06'].min()
print ('The lowest high of ' + 'str(id) ' + 'is ' + str(min_H) + ' m ü.M.')



#mean_H = data_200.mean()
#print("The mean H is:" + " "  + str(mean_H))
