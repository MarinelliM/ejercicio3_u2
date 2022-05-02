class Menuop:
    __opcion = None
    __lista = None

    def __init__(self, list, op):
        self.__opcion = op
        self.__lista = list

    def menor(self, var):
        if var == "Humedad":
            a = 100000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getHumedad() < a:
                        a = self.__lista[i][j].getHumedad()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Temperatura":
            b = 100000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getTemperatura() < b:
                        b = self.__lista[i][j].getTemperatura()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Presion":
            c = 100000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getPresion() < c:
                        c = self.__lista[i][j].getPresion()
                        dia = i+1
                        hora = j+1
            return dia, hora
        else:
            return "Error"

    def mayor(self, var):
        if var == "Humedad":
            d = -1000000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getHumedad() > d:
                        d = self.__lista[i][j].getHumedad()
                        dia = i+1
                        hora = j+1
            return dia,hora
        elif var == "Temperatura":
            e = -10000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getTemperatura() > e:
                        e = self.__lista[i][j].getTemperatura()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Presion":
            f = -1000000
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getPresion() > f:
                        f = self.__lista[i][j].getPresion()
                        dia = i+1
                        hora = j+1
            return dia,hora
        else:
            return "Error"

    def mostrar(self):
        variables=["Humedad", "Temperatura", "Presion"]
        for variable in variables:
            print("Para la variable {} el dia y hora de menor valor es {} y el dia y hora de mayor valor es {}".format(variable, self.menor(variable), self.mayor(variable)))

    def promedio(self):
        for i in range(30):
            x = 0
            for j in range(24):
                x += self.__lista[i][j].getTemperatura()
            print("El promedio del dia {} por cada hora es {}".format(i+1, x/30))

    def Listado(self):
        x=int(input("Ingrese un numero de Dia para indicar las variables:"))
        print("Hora      Temperatura      Humedad      Presion")
        for i in range(24):
            print("  {}            {}             {}           {}".format(i+1, self.__lista[x][i].getTemperatura(), self.__lista[x][i].getHumedad(), self.__lista[x][i].getPresion()))

    def menu(self):
        if self.__opcion == 1:
            self.mostrar()
        elif self.__opcion == 2:
            self.promedio()
        elif self.__opcion == 3:
            self.Listado()
        else: print("Error al ingresar el codigo ")
