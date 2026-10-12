class Prestito:
    def __init__(self,codice,data,id_strumento,cognome_allievo):
        self.__codice = codice
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo


    @property
    def codice(self):
        return self.__codice

    @property
    def data(self):
        return self.__data

    @property
    def id_strumento(self):
        return self.__id_strumento

    @property
    def cognome_allievo(self):
        return self.__cognome_allievo

    def __str__(self):
        return f'codice:{self.__codice}, strumento:{self.__id_strumento}, allievo:{self.__cognome_allievo},data:{self.__data}'

