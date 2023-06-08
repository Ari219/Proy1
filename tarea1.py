import pandas as pd 
import numpy as np 

pastelería={"Nombre Producto":["vainilla", "chocolate", "red velvet", "marmoleado"], 
"Cantidad de Ventas":[25,15,20,10], 
"Costo de Produccion":[187500, 112500, 160000, 75000],
"Margen de Beneficio":[187500, 112500, 160000, 75000],  
"Precio de Venta": [375000, 225000, 360000, 150000]}
df = pd.DataFrame(pastelería)
print(df)