from strumento import Strumento
from prestito import Prestito
import csv
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome=nome
        self.__responsabile=responsabile
        self.__strumenti=[]
        self.__prestiti=[]
        self.__prossimo_id_prestito=1 #permette di assegnare codici progressivi,senza riutilizzare quelli dei prestiti terminati


    # definiamo getter e setter per il responsabile
    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile=responsabile





    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r",encoding='utf-8',newline='') as file:
                lettore=csv.reader(file)

                for riga in lettore:
                    codice=riga[0]
                    tipo=riga[1]
                    marca=riga[2]
                    anno=int(riga[3])
                    valore=float(riga[4])
                    strumento=Strumento(codice, tipo, marca, anno, valore)
                    self.__strumenti.append(strumento)


        except FileNotFoundError:
            raise


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice='S'+str(len(self.__strumenti)+1)
        strumento=Strumento(codice,tipo, marca, anno_acquisto, valore)
        self.__strumenti.append(strumento)
        return strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        strumenti_ordinati=sorted(self.__strumenti, key=lambda x: x.marca)
        return strumenti_ordinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato=False
        for s in self.__strumenti:
            if s.codice==id_strumento:
                trovato=True
                break
        if trovato==False:
            raise Exception('strumento non presente nel deposito')

        # verifica che lo strumento non sia gia in prestito
        for prestito in self.__prestiti:
            if prestito.id_strumento==id_strumento:
                raise Exception('lo strumento è gia in prestito')

        #crea il prestito
        codice='P'+str(self.__prossimo_id_prestito)
        prestito=Prestito(codice,data,id_strumento,cognome_allievo)
        self.__prestiti.append(prestito)
        self.__prossimo_id_prestito+=1
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.__prestiti:
            if prestito.codice==id_prestito:
                self.__prestiti.remove(prestito)
                return

        raise Exception('prestito non trovato')


