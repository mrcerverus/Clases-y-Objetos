class Te_artesanal():
    duracion = "365 dias o 1 año"
        
    @staticmethod
    def obt_preparacion_recomendacion(n):
        menu =  {
        1 : ['Té negro' , '3 min' , 'Desayuno'] ,
        2 : ['Té verde' , '5 min' , 'Medio Dia'] ,
        3 : ['Agua de hierbas' , '6 min' , 'Atardecer']
        }
        return tuple(menu[n])
    
    @staticmethod
    def obt_precio_formato(precio):
        menu =  {
        300 : 3000 ,
        500 : 5000
        }
        return menu[precio]
