from te import Te_artesanal

eleccion1 = Te_artesanal.obt_preparacion_recomendacion(1)
eleccion2 = Te_artesanal.obt_preparacion_recomendacion(3)

print(type(eleccion1) , type(eleccion2))

if type(eleccion1) == type(eleccion2):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")