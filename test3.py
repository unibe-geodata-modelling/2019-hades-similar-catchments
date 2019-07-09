import pandas as pd
import numpy as np

###Import data
data_200 = pd.read_csv("/Users/eileenschilliger/Documents/Studium/01_Geografie/Master_neu2/Geodata analysis and modelling/Eigenes Projekt/pyCharm/Einzugsgebiete_200mB.csv", sep=";")
#print(data_200)


###Test Spaltenauswahl, einfache Berechnungen
#mean_H = data_200['mH_04'].mean()
#print ('The middle high of ' + 'str(id) ' + 'is ' + str(mean_H) + ' m ü.M.')
#min_H = data_200['Hmin_06'].min()
#print ('The lowest high of ' + 'str(id) ' + 'is ' + str(min_H) + ' m ü.M.')

###Berechnung der Grenzwerte
#quantile = data_200.quantile([0,0.25,0.5,0.75,1], axis=0)
#print(quantile['mH_04'])


#ID auswählen und gesuchte Variable extrahieren
featureID = int(input("Choose your feature ID: "))
print("You choose the id" + " " + str(featureID))
chosenID = data_200.loc[data_200.id==featureID, 'mH_04']
print("The middle high of your chosen id is " + str(chosenID))

###Auswahl Quantils durch Benutzer
quantile = int(input("Choose your quantile: "))

###Berechnung Quantile mittlere Höhe
data_200['Quantile_rank_mH'] = pd.qcut(data_200['mH_04'], quantile, labels=False)
print(data_200)



#while (chosenID != quantile):
 #   if (chosenID )