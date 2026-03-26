numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh","0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

def vypis_kladna_cisla(cisla):
    print("kladná čísla:")
    for cislo in cisla:
        if cislo >= 0:
            print(cislo)
    print()


def vypis_jmena_do_alice(seznam_jmen):
    print("jména (ukončení při 'Alice'):")
    index = 0
    while index < len(seznam_jmen):
        if seznam_jmen[index] == "Alice":
            break
        print(seznam_jmen[index])
        index += 1
    print()

def kody_s_nulou(kody):
    print("kódy obsahující znak '0':")
    vysledek = [kod for kod in kody if "0" in kod]
    print(vysledek)
    print()

def kody_se_stejnymi_znaky(kody):
    print("kódy obsahující alespoň 3 stejné znaky po sobě:")
    for kod in kody:
        for i in range(len(kod) - 2):
            if kod[i] == kod[i + 1] == kod[i + 2]:
                print(kod)
                break
    print()

def main():
    print("cykly\n")
    vypis_kladna_cisla(numbers)
    vypis_jmena_do_alice(names)
    kody_s_nulou(random_codes)
    kody_se_stejnymi_znaky(random_codes)
main()