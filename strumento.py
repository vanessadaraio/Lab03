class Strumento:
    def __init__(self,codice,tipo,marca,anno_acquisto,valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = int(anno_acquisto)
        self.__valore = float(valore)

    @property
    def codice(self):
        return self.__codice

    @property
    def tipo(self):
        return self.__tipo

    @property
    def marca(self):
        return self.__marca

    @property
    def anno_acquisto(self):
        return self.__anno_acquisto

    @property
    def valore(self):
        return self.__valore

    def __str__(self):
        return (f'Codice: {self.codice}, Tipo:{self.tipo}, Marca:{self.marca},'
                f'Anno:{self.anno_acquisto}, Valore:{self.valore:.2f} euro')


