from math import pi, sqrt

class Rettangolo:
    def __init__(self, base, altezza):
        self.base       = base
        self.altezza    = altezza

    def imposta_base(self, valore):
        self.base       = valore

    def ottieni_base(self):
        return self.base

    def imposta_altezza(self, valore):
        self.altezza    = valore

    def ottieni_altezza(self):
        return self.altezza

    def calcola_perimetro(self):
        return 2*(self.base + self.altezza) 

class Quadrato(Rettangolo):
    def __init__(self, lato):
        super().__init__(lato, lato)

    def imposta_lato(self, valore):
        self.imposta_base(valore)
        self.imposta_altezza(valore)

    def ottieni_lato(self):
        return self.base

class Cerchio:
    def __init__(self, raggio):
        self.raggio     = raggio

    def ottieni_raggio(self):
        return self.raggio

    def calcola_perimetro(self):
        return 2*pi*self.raggio

class Personalizzato:
    def __init__(self):
        self.perimetro      = 0

    def calcola_distanza(self, primo: tuple, secondo: tuple):
        return sqrt((primo[0] - secondo[0]) ** 2 + (primo[1] - secondo[1]) ** 2)

    def loop_personalizzato(self):
        print("x1 y1, x2 y2, ... , xN yN (a) per indicare le coordinate dei vertici della figura (lasciare la figura aperta)")
        ver     = input("INPUT: ").split(',')
        aperto  = False

        prime_coord     = None
        ultime_coord    = None

        for v in ver:
            if (v == 'a'):
                aperto  = True
                break

            x,y = float(v.split()[0]), float(v.split()[1])

            if (prime_coord == None):
                prime_coord = (x, y)

            if (ultime_coord != None):
                self.perimetro += self.calcola_distanza((x, y), ultime_coord)
                
            ultime_coord   = (x, y)

        if (not aperto):
            self.perimetro      += self.calcola_distanza(prime_coord, ultime_coord)

        print(self.perimetro)

            
class Main:
    def __init__(self):
        self.prosegui   = True
    def loop(self):
        print("1 - Quadrato")
        print("2 - Rettangolo")
        print("3 - Cerchio")
        print("4 - Personalizzato")
        print("q - Esci")

        scelta          = input("Inserisci il numero corrispondente alla figura geometrica di cui vuoi calcolare il perimetro. ")
        if (scelta == 'q'):
            self.prosegui   = False
            return

        scelta  = int(scelta)

        if (scelta == 1):
            lato        = float(input("Inserisci il valore della base: "))
            quadrato    = Quadrato(lato)
            print(f"Il perimetro di un quadrato di lato {quadrato.ottieni_lato()} è {quadrato.calcola_perimetro()}")
        elif (scelta == 2):
            base        = float(input("Inserisci il valore della base: "))
            altezza     = float(input("Inserisci il valore dell'altezza: "))
            rettangolo  = Rettangolo(base, altezza)
            print(f"Il perimetro di un rettangolo di base {rettangolo.ottieni_base()} e altezza {rettangolo.ottieni_altezza()} è {rettangolo.calcola_perimetro()}")
        elif (scelta == 3):
            raggio      = float(input("Inserisci il raggio del cerchio: "))
            cerchio     = Cerchio(raggio)
            print(f"Il perimetro di un cerchio di raggio {cerchio.ottieni_raggio()} è {cerchio.calcola_perimetro()}")
        elif (scelta == 4):
            personalizzato  = Personalizzato()
            personalizzato.loop_personalizzato()
        else:
            self.prosegui   = False

    def main(self):
        while (self.prosegui):
            self.loop()

if (__name__ == "__main__"):
    main                = Main()
    main.main()

