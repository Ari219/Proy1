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
pelicula={"Nombre": ["Super Mario Bros", "The Whale", "Spiderman: Across", "Notting Hill", "Kiki:entregas a domicilio", "Green Book"], 
"Género":["animada", "drama", "animada", "romance", "anime", "Drama" ],
"Duración": ["1h32m", "1h57m", "2h20m", "2h04m", "1h42m", "2h10m"],
"Puntaje Rotten Tomatoes": [60, 65, 96, 85, 99, 77]}
pl= pd.DataFrame(pelicula)
print(pl)