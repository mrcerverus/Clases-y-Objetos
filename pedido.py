from te import Te_artesanal

tipo_te = int(input('''
    Por favor elije un sabor de te:
1. Té negro
2. Té verde
3. Agua de hierbas.
    >>
'''))

formato = int(input('''
    Por favor elije un tamano de te:
300 gr
500 gr.
'''))

sabor , tiempo , recomendacion = Te_artesanal.obt_preparacion_recomendacion(tipo_te)
precio = Te_artesanal.obt_precio_formato(formato)

print(f'''
    Tu pedido es el siguiente:
a. Sabor del tipo de té: {sabor}.
b. Formato: {formato} gr.
c. Precio: ${precio}.
d. Tiempo: {tiempo} min.
e. Recomendación: {recomendacion}
''')