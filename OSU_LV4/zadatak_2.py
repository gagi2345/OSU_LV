 #Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoricku 
#varijable „Fuel Type“ kao ulaznu velicinu. Pri tome koristite 1-od-K kodiranje kategorickih 
#velicina. Radi jednostavnosti nemojte skalirati ulazne velicine. Komentirajte dobivene rezultate. 
#kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu
#vozila radi?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("data_C02_emission.csv")

# One-hot encoding (1_od-K) za Fuel Type
data_encoded = pd.get_dummies(data, columns=['Fuel Type'])


features = [
    'Engine Size (L)',
    'Cylinders',
    'Fuel Consumption City (L/100km)',
    'Fuel Consumption Hwy (L/100km)',
    'Fuel Consumption Comb (L/100km)',
    'Fuel Consumption Comb (mpg)',
    'Fuel Type_D',
    'Fuel Type_E',
    'Fuel Type_X',
    'Fuel Type_Z'
]

X = data_encoded[features]
y = data_encoded['CO2 Emissions (g/km)']

# Podjela 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Linearni model (bez skaliranja!)
model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)




errors = abs(y_test - y_pred)

max_error = errors.max()
index_max = errors.idxmax()

print("Maksimalna pogreška:", max_error)

print("Vozilo s najvećom pogreškom:")
print(data.loc[index_max, ['Make', 'Model']])