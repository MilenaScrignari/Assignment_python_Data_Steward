#importing libraries
import csv
import numpy as np
import matplotlib.pyplot as plt

# ------------------MAIN FUNCTION-------------------
# loading data frome CSV
def load_data(filename):
    years = []
    lengths = []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')  #adapting the code to make sure that it takes in account different tabulations (my CSV file as a ; tabulation)
                
        # ignoring the 10 first line
        for _ in range(10):
            next(reader)

        # extracting data after the 10 first lines
        for row in reader:
            # extracting "end date of observation" (row 5) + integer conversion
            year = int(row[4].split('.')[2])  # 'end date' est en row 5 (index 4 - py starts row counting at 0) for year format DD.MM.YYYY
            #year = int(row[4].split('-')[0]) # if the year format is YYYY-MM-DD
            
            # adding "length change" + float (data type) conversion
            length_change = float(row[6])  # 'length change' est en colonne 7 (index 6)

# values verification "length change" 
            if length_change < -1000 or length_change > 1000:
                print(f"Ligne ignorée (valeur anormale de 'length change'): {row}")
                continue  # go to the next line of the value is out of range
            if year < 1700 or year > 2024:
                print(f"Ligne ignorée (valeur anormale de 'length change'): {row}")
                continue  #  go to the next line of the value is out of range
            
            # Adding data
            years.append(year)
            lengths.append(length_change)

   # Controlling if data have been correctly downloaded
    if len(years) == 0 or len(lengths) == 0:
        print("Erreur : no valid data in filr.")
        return None, None  # None if invalid or inexisting data

    return years, lengths
#-----------------------------FUNCTION TO CALCULATE LINEAR REGRESSION--------------------
# calculating linear regression (régression linéaire)
def calculate_trend(years, lengths):
    slope, intercept = np.polyfit(years, lengths, 1)
    return slope, intercept

#-----------------------------FUNCTION TO DISPLAY DATA--------------------
# displaying data + regression
def display_data(years, lengths, slope, intercept):
    plt.plot(years, lengths, 'o', label='Données réelles', color='green')
    plt.plot(years, slope * np.array(years) + intercept, label='Régression linéaire', color='red')

    plt.title('Évolution de la longueur du glacier de Silvretta')
    plt.xlabel('Année')
    plt.ylabel('Changement de longueur du glacier (m)')
    plt.legend()
    plt.grid(True) #grid activation
    plt.show()

# downloading data from our CSV file
#**************COMMENT FOR TEACHER: The actual path where the csv lengthchange_swissglaciers.csv is stored has to be copy paste here:******************
filename = r'c:\Users\Milena\OneDrive\Bureau\Data Steward Module 2\2.7\CoursePackage\lengthchange_swissglaciers.csv' 
years, lengths = load_data(filename)

# calculating regression
slope, intercept = calculate_trend(years, lengths)

print(f"Regression linéaire : Slope = {slope:.3f}, Intercept = {intercept:.3f}")

 # Prediction using slope /intercept
year_prediction = 2035
predicted_length_change = slope * year_prediction + intercept
print(f"Prédiction pour l'année 2035 : {predicted_length_change:.2f} mètres")

# displaying data and regression
display_data(years, lengths, slope, intercept)

