class Carro:
    def __init__(self,nom,mod,color,precio): #CONSTRUCTOR CLASE PADRE
        self.nom=nom
        self.mod=mod
        self.color=color
        self.precio=precio
    def descripcion(self): #FUNCION QUE MUESTRA LOS VALORES DE LOS ATRIBUTOS
        print(f"Nombre:{self.nom} Modelo:{self.mod} color:{self.color} Precio:{self.precio}")
class Chevrolet(Carro): #CLASE HIJA QUE HEREDA ATRIBUTOS Y COMPORTAMIENTO DE LA CLASE PADRE
    def __init__(self,nom,mod,color,precio,marca): #CONSTRUCTOR CLASE HIJA
        super().__init__(nom,mod,color,precio) #LE DIGO QUE EL CONSTRUCTOR DE LA CLASE PADRE Y LE AGREGA ESPECIFICIDAD
        self.marca=marca 
    def descripcion(self): #HEREDA LA FUNCION DESCIPCION DE LA CLASE PADRE Y LE AGREGA ESPECIFICIDAD
        super().descripcion()
        print(f"Marca {self.marca}")
class Fiat(Carro): #CLASE HIJO QUE HEREDA ATRIBUTOS Y COMPORTAMIENTO DE LA CLASE PADRE
    def __init__(self,nom,mod,color, precio): #CONSTRUCTOR CLASE HIJO
        super().__init__(nom,mod,color,precio) #LE DIGO QUE EL CONSTRUCTOR DE LA CLASE HIJO HEREDA DEL CONSTRUCTOR DE LA CLASE PADRE

    def descripcion(self): #HEREDA LA FUNCION DESCRIPCION  DE LA CLASE PADRE Y LE AGREGA ESPECIFIDIAD
        super().descripcion()

c1=Carro("Versa",2021,"Negro",150000) #CREAMOS O INSTANCIAMOS EL OBJETO C1 Y LE INDICAMOS QUE ES DE LA CLASE CARRO
#LLMANDO A LA FUNCION CONSTRUCTORA Y LE PASAMOS ARGUMENTOS, ESTOS RECIBIRA COMO PARAMETROS EN LA FUNCION
c1.descripcion() #LLAMAMOS A LA FUNCION DESCRIPCION PRA EL OBJETO C1
c2=Chevrolet("Aveo",2022,"Rojo",100000,"Chevrolet")#CREAMOS O INSTANCIAMOS EL OBJETO C2 Y LE INDICAMOS QUE ES DE LA CLASE CHEVROLET
#LLAMANDO A LA FUNCION CONSTRUCTORA Y LE PASAMOS ARGUMENTOS AGREGANDO UNO ESPECIFICO DE ESTA CLASE QUE ES MARCA
# ESTOS RECIBIRA COMO PARAMETROS EN LA FUNCION 
c2.descripcion() #LLAMAMOS A LA FUNCION DESCRIPCION PARA EL OBJETO C2
c3=Chevrolet("Onix",2022,"Rojo",140000,"Chevrolet")
c3.descripcion()
c4=Fiat("Corsa",2023,"Azul",45999) ##CREAMOS O INSTANCIAMOS EL OBJETO C2 Y LE INDICAMOS QUE ES DE LA CLASE FIAT
c4.descripcion()#LLAMAMOS A LA FUNCION DESCRIPCION PARA EL OBJETO C4