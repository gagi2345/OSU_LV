# Skripta zadatak_1.py ucitava podatkovni skup iz  data_C02_emission.csv.
#Potrebno je izgraditi i vrednovati model koji procjenjuje emisiju C02 plinova na temelju ostalih numerickih ulaznih velicina.
#Detalje oko ovog podatkovnog skupa mogu se pronaci u 3. 
#laboratorijskoj vježbi.
#a) Odaberite željene numericke velicine specificiranjem liste s nazivima stupaca. Podijelite
#podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%. 
#b) Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova 
#o jednoj numerickoj velicini. Pri tome podatke koji pripadaju skupu za ucenje oznacite 
#plavom bojom, a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom. 
#c) Izvršite standardizaciju ulaznih velicina skupa za ucenje. Prikažite histogram vrijednosti 
#jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja 
#transformirajte ulazne velicine skupa podataka za testiranje. 
#d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
#povežite ih s izrazom 4.6.
#e) Izvršite procjenu izlazne velicine na temelju ulaznih velicina skupa za testiranje. Prikažite 
#pomocu dijagrama raspršenja odnos izmedu stvarnih vrijednosti izlazne velicine i procjene 
#dobivene modelom.
#f) Izvršite vrednovanje modela na nacin da izracunate vrijednosti regresijskih metrika na 
#skupu podataka za testiranje.
#g) Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj 
#ulaznih velicina?
import pandas as pd
from sklearn.model_selection import train_test_split
#a)
data = pd.read_csv("data_C02_emission.csv")

features = [
    'Engine Size (L)',
    'Cylinders',
    'Fuel Consumption City (L/100km)',
    'Fuel Consumption Hwy (L/100km)',
    'Fuel Consumption Comb (L/100km)',
    'Fuel Consumption Comb (mpg)'
]

X = data[features]
y = data['CO2 Emissions (g/km)']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

#b)
import matplotlib.pyplot as plt

plt.scatter(X_train['Engine Size (L)'], y_train, color='blue', label='Train')
plt.scatter(X_test['Engine Size (L)'], y_test, color='red', label='Test')

plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('CO2 vs Engine Size')
plt.legend()
plt.show()

#c)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

# Prije skaliranja
plt.hist(X_train['Engine Size (L)'], bins=20)
plt.title("Prije skaliranja")
plt.show()

# Skaliranje
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Nakon skaliranja
plt.hist(X_train_scaled[:, 0], bins=20)
plt.title("Nakon skaliranja")
plt.show()

#d)
import sklearn.linear_model as lm

model = lm.LinearRegression()
model.fit(X_train_scaled, y_train)

print("Koeficijenti (θ1, θ2, … θm):", model.coef_)
print("Presjek (bias  θ0):", model.intercept_)


#e)
y_pred = model.predict(X_test_scaled)

plt.scatter(y_test, y_pred)
plt.xlabel("Stvarne CO2 emisije")
plt.ylabel("Predviđene CO2 emisije")
plt.title("Stvarne vs Predviđene vrijednosti")
plt.show()

#f)
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R^2:", r2)

#g)
#Povećanjem broja ulaznih veličina model obično postiže bolje rezultate (manji MSE i veći R²),
#ali prevelik broj veličina može dovesti do prenaučenosti modela (overfitting).
#Smanjenjem broja ulaznih veličina model postaje jednostavniji, ali se povećava pogreška predikcije.
