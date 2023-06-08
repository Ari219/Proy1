import pandas as pd 
import numpy as np 

pastelería={"Nombre Producto":["vainilla", "chocolate", "red velvet", "marmoleado"], 
"Cantidad de Ventas":[25,15,20,10], 
"Costo de Produccion":[187500, 112500, 160000, 75000],
"Margen de Beneficio":[187500, 112500, 160000, 75000],  
"Precio de Venta": [375000, 225000, 360000, 150000]}
pt = pd.DataFrame(pastelería)

nuevos_datos={"Pago":["Transferencia","Transferencia", "Transferencia", "Transferencia"], 
"Envío":["Retiro en local","Retiro en local", "Retiro en local", "Retiro en local"]}

pt["Pago"] = nuevos_datos["Pago"]
pt["Envío"] = nuevos_datos["Envío"]
print(pt)
