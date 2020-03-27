class Samochod:
    def __init__(self):
        self.__marka = "NA"
        self.__rok_produkcji = 0
        self.__pojemnosc_silnika = 0
        self.__numer_rejestracyjny="NA"

    def __init__(self, marka, rok_produkcji, pojemnosc_silnika, numer_rejestracyjny):
        self.set_marka(marka)
        self.set_rok_produkcji(rok_produkcji)
        self.set_pojemnosc_silnika(pojemnosc_silnika)
        self.set_numer_rejestracyjny(numer_rejestracyjny)

    def __str__(self):
        return "Marka: {}, Rok produkcji: {}, Pojemność silnika: {}, numer rejestracyjny: {}".format(
            self.__marka, self.__rok_produkcji, self.__pojemnosc_silnika, self.__numer_rejestracyjny)

    def set_marka(self, marka):
        self.__marka = marka

    def set_rok_produkcji(self, rok_produkcji):
        if not rok_produkcji.isnumeric():
            raise ValueError("Blad! Rok produkcji musi byc liczbą")
        else:
            self.__rok_produkcji = rok_produkcji

    def set_pojemnosc_silnika(self, pojemnosc_silnika):
            self.__pojemnosc_silnika = pojemnosc_silnika

    def set_numer_rejestracyjny(self, numer_rejestracyjny):
        self.__numer_rejestracyjny = numer_rejestracyjny

    def get_marka(self):
        return self.__marka

    def get_rok_produkcji(self):
        return self.__rok_produkcji

    def get_pojemnosc_silnika(self):
        return self.__pojemnosc_silnika

    def get_numer_rejestracyjny(self):
        return self.__numer_rejestracyjny


Samochody = [Samochod("Toyota", "1999", "3 l", "WX99999"),
             Samochod("Fiat", "2000", "1,0 l", "WOT3000"),
             Samochod("Mercedes", "2015", "4,0 l", "WG7018P"),
             Samochod("Volvo", "1984", "1,5 l", "111111"),
             Samochod("Mitsubishi", "2007", "2,3 l", "KR78004")]

for i in Samochody:
    print(i)

posortowane_samochody = sorted(Samochody, key=lambda x: int(x.get_rok_produkcji()))
print("\nPosortowane wzgledem roku produkcji")
for i in posortowane_samochody:
    print(i)
