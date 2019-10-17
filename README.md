------------------------------------------------------------
IDENTIFICATION OF SIMILAR CATCHMENTS (HADES)
------------------------------------------------------------

INTRO
------------------------------------------------------------
This script was developed for the "Hydrological Atlas of Switzerland" (HADES) to enhance the user experience on their website. This is a tool for interactive selection of similar catchments based on different catchment characteristics. The main idea is that when the user selects a catchment area, similar areas should be displayed.

DOCUMENT "DATA_200"
------------------------------------------------------------
All data for our project are taken from the database of the Hydrological Atlas of Switzerland. The document contains the individual characteristics of the catchment areas, which have a size of 200 square meters. The script is based on the data from this Excel file. The catchment area sizes of 100 and 300 square meters were also used to test the script.

VARIABLES
------------------------------------------------------------


SCRIPT DESCRIPTION
------------------------------------------------------------
As a first step we wrote a small script for a classification of only one property (middle hight). After that we tested it several times and expanded the script for classification considering multiple features. In the end, we applied the script to the properties "middle height", "slope" and "aspect".
