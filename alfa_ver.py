from datetime import datetime
from datetime import date

class Alkohol:
    def __init__(self, id, data, nazwa, waga_pusta, waga_zwazona, ilosc_pelnych_butelek):
        self.id = id
        self.data = data
        self.nazwa = nazwa
        self.waga_pusta = waga_pusta
        self.waga_zwazona = waga_zwazona
        self.ilosc_pelnych_buetelek = ilosc_pelnych_butelek
        self.waga_plynu = self.wylicz_wage_plynu()#komentarz------------------------------------------------

    def wylicz_wage_plynu(self):
        return round(self.waga_zwazona - self.waga_pusta, 2)

    def __str__(self):
        return (f"ID: {self.id}, Data: {self.data}, Nazwa: {self.nazwa}, "
                f"Waga płynu: {self.waga_plynu} kg + {self.ilosc_pelnych_buetelek} pełnych butelek")


class BazaAlkoholi:
    def __init__(self):
        self.rekordy = []

    def dodaj_alkohol(self, alkohol):
        self.rekordy.append(alkohol)

    def usun_alkohol(self, alkohol):
        self.rekordy.remove(alkohol)

    def pokaz_wszystkie(self):
        for alkohol in self.rekordy:
            print(alkohol)
#dodawanie do bazy w excelu jak potraficie łatwiej to dawać to jest moj pomysł
def dodawanie_alkoholi_do_bazy(id, data, nazwa, waga_pusta, waga_zwazona, ilosc_pelnych_butelek):
    dane=str(id)+";"+str(data)+";"+str(nazwa)+";"+str(waga_pusta)+";"+str(waga_zwazona)+";"+str(ilosc_pelnych_butelek)+"\n"
    baza_tekstowa=open("baza_alko_excel.csv","w")
    baza_tekstowa.write(dane)
#przy zczytywaniu trzeba pamietac zeby zmienac to co  trzeba na inty oraz usuwav \n z koncow.


# === Przykładowe użycie ===================================================================
if __name__ == "__main__":
    baza = BazaAlkoholi()
#JESLI CHCEMY BAZE TO TRZEBA BEZ POLSKICH ZNAKOW!!!!!
    data= date.today()
    alkohol1 = Alkohol(1, data, "Woda Zubrowka", 0.5, 1.2, 0)
    dodawanie_alkoholi_do_bazy(1, data, "Woda Zubrowka", 0.5, 1.2, 0)
    
    alkohol2 = Alkohol(2, data, "Whisky Jack Daniels", 0.7, 1.9, 3)
    alkohol3 = Alkohol(3, data, "Piwo Heineken", 0.3, 0.85, 4)
    alkohol4 = Alkohol(3, data, "Piwo Warka Strong", 0.3, 0.85, 7)

    baza.dodaj_alkohol(alkohol1)
    baza.dodaj_alkohol(alkohol2)
    baza.dodaj_alkohol(alkohol3)
    baza.dodaj_alkohol(alkohol2)
    baza.dodaj_alkohol(alkohol2)
    baza.dodaj_alkohol(alkohol2)
    baza.dodaj_alkohol(alkohol2)

    baza.usun_alkohol(alkohol3)

    baza.pokaz_wszystkie()
#===================================================================================================s