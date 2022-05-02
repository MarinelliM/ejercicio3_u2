class Registro:
    __temperatura=""
    __humedad=""
    __presion=""

    def __init__(self,temp,hum,pres):
        self.__temperatura=temp
        self.__humedad=hum
        self.__presion=pres

    def getTemperatura(self):
        return self.__temperatura

    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presion
