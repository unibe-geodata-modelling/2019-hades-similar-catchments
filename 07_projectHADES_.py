import pandas as pd
import numpy as np

###Import data
data_200 = pd.read_csv("/Users/Flavia/PycharmProjects/projectHADES/Einzugsgebiete_200m.csv", sep=";")
#print(data_200)

##################### Auswahl durch USER ######################

#ID auswählen
#featureID = int(input("Choose your feature ID: "))
#print("You choose the id" + " " + str(featureID))
featureID = 164454

###Auswahl Quantils durch Benutzer
#quantile = int(input("Choose your quantile: "))
quantile = 6

#Achtung quantile funktionieren nur bis und mit 6 --> WIESO????
# und bei 5 quantile gibt es eine ähnliche ID aus, bei 4 quantilen aber keine --> macht das Sinn??


################ Abfrage der gewünschten Variabeln durch USER ##########################


# display the list the user needs to see in order to choose some values
print('\n' + 'A catchment has many different variables that are used to describe it:')
display_liste = ['middle Hight', 'slope', 'aspect', 'D', 'E']
for i, display_name in enumerate(display_liste, start=1):
    print('{}. {}'.format(i, display_name))

# the real list the programm is going to use to be able to choose the right headers in the file data_200
db_list = ['mH_04', 'N20slp8_12', 'asp8smm_14', 'Icecream', 'Bananasplit']

criteriachosenbyuser = []
criteria_for_display = []

print('\n' + 'Please select a variable that you want your catchment to compare with. Keep in mind that there might '
             'not be similar catchments to your chosen ID {} if you choose '
             'to many variables.'.format(featureID))
additional_variable = 'YES'
while additional_variable == 'YES':
    try:
        selected = int(input('Select a variable (1-{}): '.format(i)))
        # add the selected variable to the list "criteriachosenbyuser"
        new_element = db_list[selected - 1]
        criteriachosenbyuser.append(new_element)

        # present the right variable name to the user:
        new_element_for_show_only = display_liste[selected - 1]
        criteria_for_display.append(new_element_for_show_only)
        print('You have selected {}'.format(criteria_for_display))

        # follow up question:
        additional_variable = input('Do you want to select another variable? (write YES or NO)')

    except (ValueError, IndexError):
        print('This is not a valid selection. Please enter number between 1 and {}!'.format(i))
else:
    print('You ended the selection of possible variables correctly. You have chosen the following variables: ')
    print(str(criteria_for_display) + ' or in other words:' + str(criteriachosenbyuser))


###################################################################

###Berechnung Quantile der ausgewählten Kriterien
for x in criteriachosenbyuser:
    data_200['Quantile_rank_'+ str(x)] = pd.qcut(data_200[x], quantile, labels=False)
print(data_200)

############################# Quantile vergleichen und ähnliche IDs auswählen #################################

quantilliste=[]
for x in criteriachosenbyuser:
    ###Gib die Quantile der ausgewählten ID aus (der ausgewählten Kriterien)
    quantilliste.append(int(data_200.loc[data_200.id==featureID]['Quantile_rank_' + str(x)]))
    print('the quantilliste is:')
    print(quantilliste)

ergebnisliste=[]
for i in data_200.index:
    tempquantilliste = []
    for x in criteriachosenbyuser:
        # Quantile der gerade prozessierenden Zeile auswählen (und in die Liste 'tempquantilliste' speichern)...
        tempquantilliste.append(int(data_200.iloc[i]['Quantile_rank_' + str(x)]))
        #** Werte Ausgeben (nur um Prozess zu veranschaulichen)**
        print('the tempquantilliste is:')
        print(tempquantilliste)
        # ...wenn die Quantile mit den Quantilen der vom User ausgewählten ID ('quantilliste') übereinstimmen,
        # und in die Liste 'ergebnisliste' speichern
        if quantilliste == tempquantilliste:
            ergebnisliste.append(data_200.iloc[i]['id'])

# die vom USER gewählte ID aus der Ergebnisliste entfernen
ergebnisliste.remove(featureID)

###################################################################################################

print('\033[1m' + "the following catchments are similar to your chosen catchment {} "
                  "in regard to the variable(s) {} as well as your quantile {}:"
                 .format(featureID, criteria_for_display, quantile))
print(ergebnisliste)


print('\n' + '\033[0m' + 'the feeling when you finally have been successful :)')