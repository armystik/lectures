def nacti_soubor():
    nazev = input("\nzadej název souboru: ")

    try:
        with open(nazev, "r", encoding="utf-8") as soubor:
            print("\n--- obsah ---")
            for radek in soubor:
                print(radek.strip())
    except FileNotFoundError:
        print("chyba: soubor nebyl nalezen.")
    except PermissionError:
        print("chyba: nedostatečná oprávnění k otevření souboru.")
    except Exception as e:
        print("neočekávaná chyba:", e)
    finally:
        print("pokus o načtení souboru byl dokončen.\n")

def deleni():
    try:
        a = float(input("\nzadej první číslo: "))
        b = float(input("zadej druhé číslo: "))
        vysledek = a / b
    except ValueError:
        print("chyba: je nutné zadat platná čísla.")
    except ZeroDivisionError:
        print("chyba: nelze dělit nulou.")
    else:
        print(f"výsledek: {vysledek}")
    finally:
        print("operace dělení byla dokončena.\n")


def bezpecny_vstup_int(vyzva):
    while True:
        try:
            return int(input(vyzva))
        except ValueError:
            print("chyba: neplatný vstup, zkuste to znovu.")


def menu():
    while True:
        print("1 - načíst soubor")
        print("2 - dělení čísel")
        print("3 - konec")

        volba = bezpecny_vstup_int("vyber možnost: ")

        if volba == 1:
            nacti_soubor()
        elif volba == 2:
            deleni()
        elif volba == 3:
            print("program bude ukončen.")
            break
        else:
            print("chyba: neplatná volba.\n")

if __name__ == "__main__":
    print("Program ukazuje, jak dělá vyjímky přes try-except.\n")
    menu()