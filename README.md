------------------------------------------------------------
IDENTIFICATION OF SIMILAR CATCHMENTS (HADES)
------------------------------------------------------------

INTRO
------------------------------------------------------------
The main script (HADES_script_final.py) was developed for the "Hydrological Atlas of Switzerland" (HADES) to enhance the user experience on their website. This is a tool for interactive selection of similar catchments based on different catchment characteristics. The main idea is that when the user selects a catchment area, similar areas should be displayed.

DOCUMENT "DATA_200"
------------------------------------------------------------
All data for our project are taken from the database of the Hydrological Atlas of Switzerland. The document contains the individual characteristics of the catchment areas, which have a size of 200 square meters. The script is based on the data from this Excel file. The catchment area sizes of 100 and 300 square meters were also used to test the script.

SCRIPT DESCRIPTION
------------------------------------------------------------
The data frames "pandas" and "numpy" are used in this script for analyzing the data. The script allows the user to select a catchment as well as the catchment characteristics he/she wants to compare the catchments among each other (like slope and aspect). The script works with quantiles to detect the similarity between catchments. Therefore the script also asks for a quantile-number input. The higher the chosen number the higher is the similarity between the characteristics of the chosen catchment and the catchments presented in the output list "ergebnisliste".
