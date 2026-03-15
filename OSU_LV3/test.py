import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
'''
s1 = pd . Series (['crvenkapica','baka ', ' majka ', ' lovac ',  'vuk' ])
print ( s1 )
s2 = pd . Series ( 5, index = ['a ','b' ,'c' ,'d' ,'e' ], name =  'ime_objekta' )
print ( s2 )
print ( s2['b' ])
s3 = pd . Series ( np . random . randn ( 5 ) )
print ( s3 )
print ( s3[3])

data1 = {'country' : [ 'Italy' , 'Spain' , 'Greece' , 'France' , 'Portugal' ],
'population' : [59 , 47 , 11 , 68 , 10 ],
'code' : [39 , 34 , 30 , 33 , 351 ] }
countries = pd . DataFrame ( data1 , columns = [ 'country' , 'population', 'code' ]
)
print ( countries )


data = pd . read_csv (  'data_C02_emission.csv' )
# konvertiranje kategorickih velicina u tip category
#print ( len ( data ))
#print ( data )
#print ( data . head ( 5 ) )
#print ( data . tail ( 3 ) )
#print ( data . info () )
#print ( data . describe () )
#print ( data . max () )
#print ( data . min () )

# izdvajanje pojedinog stupca
print ( data [ 'Cylinders' ])
print ( data.Cylinders )

# izdvajanje vise stupaca
print ( data [[ 'Model' , 'Cylinders' ]])

# izdvajanje redaka koristenjem iloc metode
print ( data . iloc [2:8 , :11])
print ( data . iloc [ :, 2:5])
print ( data . iloc [ :, [0 ,4 , 7] ])


print ( data .Cylinders > 6 )
print ( data [ data .Cylinders > 6])
#print ( data [( data [ 'Cylinders' ] == 4 ) & ( data ['Engine Size ( L ) '] > 2.4 )]. Model)
# dodavanje novih stupaca
data [ 'jedinice' ] = np.ones ( len ( data ))
data ['large' ] = ( data [ 'Cylinders' ] > 10 )

data = pd .read_csv ( 'data_C02_emission.csv ')
plt.figure()
data ['Fuel Consumption City (L/100km)']. plot ( kind = 'hist' , bins = 20 )
plt.figure()
#data ['Fuel Consumption City (L/100km)']. plot ( kind ='box' )
plt.show()''''''
data = pd .read_csv ( 'data_C02_emission.csv')
data.plot.scatter ( x='Fuel Consumption City (L/100km)',y='Fuel Consumption Hwy (L/100km)',c='Engine Size (L)', cmap ="hot", s=50 )
plt.show ()
'''
data = pd . read_csv ( 'data_C02_emission.csv')
print ( data . corr ( numeric_only = True ) )
pri