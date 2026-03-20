    # x = 5
    # y = 64
    # print(x + y)
    # z = 20
    # print(x - z)

    # x = 6 + 2
    # y = 6 - 2
    # z = 6 * 2
    # c = 6 / 2
    # v = 6 // 2
    # b = 6 ** 2
    # n = 6 % 2
    # print(x)
    # print(y)
    # print(z)
    # print(c)
    # print(v)
    # print(b)
    # print(n)

name = "Kuba"
position = "programator"
grade = 4
is_student = False
name_size = len(name)

    # Petr je programator
    # x = name + " je " + position + " a dostal" + grade
    # string s integer hodí error u tohohle zápisu
    # print(x)

r = f"{name} je {position} a dostal {grade}"
print(r)
print(f"Jmeno {name} ma {name_size} znaku")

    # x = 7
    # y = 7
    # z = x == y
    # t = 3
    # e = t > x
    # print(z)
    # print(e)

k = name_size >= 5
print(f"Jmeno ma vice znaku nez 5: {k}")

sentence_mesto = "Ahoj jsem Petr a bydlim v meste Praha"
b = "Brno" in sentence_mesto
p = "Praha" in sentence_mesto
print(f"V teto vete je slovo Brno: {b}")
print(f"V teto vete je slovo Praha: {p}")

age = 1997
age2 = int("1997") + 18
sentence = "Kuba se narodil roku " + str(age)
sentence2 = "Kdyz Kuba mel 18, byl rok " + str(age2)
print(sentence)
print(sentence2)

    # number1 = 1.1
    # number2 = int(number1)
    # print(number2)
    # print(str(number2))

    # num1 = 1
    # num2 = 0
    # n1 = bool(number1)
    # n2 = bool(number2)
    # print(n1)
    # print(n2)

    # name1 = ""
    # is_empty = len(name1) == 0
    # print(is_empty)

    # brand = ""
    # brand = brand + "H"
    # brand = brand + "P"
    # print(brand)

names = ["Radek", "Jakub", "Michal"]
jakub = names[1]
radek = names[0]
names[1] = "Kuba" # Předělání hodnoty na jinou
names.append("Adam") #Přidání do listu další jméno

    # print(names)
    # print(jakub + " a " + radek)

print("List:", *names, sep=", ")

names_size = len(names)
print(f"Pocet jmen v listu: {names_size}")

books = ["Srdcervaci", "Pan Prstenu", "Zaklinac", "5 jazyku lasky", "10 pravidel lasky"]
    # books.remove("Pan Prstenu")
    # Odebrání vybraného prvku
removed_book = books.pop(-1) # Odstraní prvek a vrátí ho
books.insert( 2, "Lví Král")
print(f"Seznam knih:", *books, sep=", ")
print(f"Prodane knihy: {removed_book}")

    # numbers = [1,2,3,4,-1,100]
    # print(numbers)
    # numbers.sort() # Seřadí prvky
    # numbers.clear() # Smaže prvky z listu
    # print(numbers)
    # del numbers[1] # Odstraní prvek z listu

user = {
    "name": "Kuba",
    "age": 28,
    "address": "Praha",
    "nakup": [
        {"name": "Pivo", "count": 2, "price": 39},
        {"name": "Maso", "count": 1, "price": 89},
        {"name": "Brambory", "count": 8, "price": 44},
    ]
}
    # print(user["address"])

user["age"] = 29
user["email"] = "kuba@gmail.com"
print(f"Slozka: {user}")

    # user_phone = user.get("phone", "774584555") # Přidá prvek
    # print(user_phone) # Hodí to "None"

    # print(user.keys()) # Dictionary

    # user_list = []
    # user_list.append(user)
    # print(user_list)

    # m1 = {1, 10, 2, 3, 4, -4, 4}
    # m1 = set(m1)
    # m1 = list(m1)
    # m1.sort()
    # print(m1)

m2 = {1,3,4,5}
m3 = {10,3,4,7}
prunik = m2.intersection(m3)
sjednoceni = m2.union(m3)
rozdil = m2.difference(m3)
print(prunik)
print(sjednoceni)
print(rozdil)

    # t = tuple([1,2,3]) # tuple

    # FUNKCE

    # print("ahoj") # funkce se zavolá díky ()
    # j = ["A", "B"]
    # k = len(j)

def hodnoceni(osloveni: str, vek: int) -> None:
    # Tato funkce žádá o hodnocení

    print(f"{osloveni} ({vek}), doufáme, že se ti v programu líbí! Kdyžtak zanech hodnocení.")

    # for i in range(3):  # Vypíše 3x
    #     hodnoceni()

hodnoceni("Kubo", "28")
hodnoceni("Alexi", "21")

    # def soucet():
    #     pass

def soucet(cislo4: float, cislo5: float) -> float:
    res = cislo4 + cislo5
    return res
a5 = 1.251
b5 = 2.32
c5 = soucet(a5, b5)
print(c5)

user = {
    "name": "Kuba",
    "age": 28,
    "work": "IT",
    "hair_color": "brown",
}

def change_work(user: dict, new_work: str):
    user["work"] = new_work
    # nemusim dávat: return user, protože se vrací v paměti
print(user)
change_work(user, "programator") # zde taky nemusim psát: user =
print(user)
###### Podminky #######
speed = 120
limit = 140
lower_limit = 100
if (speed > limit):
    print("Překročen limit rychlosti.")
elif (speed < lower_limit):
    print("Rychlost v pořádku.")
else:
    print("Rychlost fajn.")
name = "admin"
if (name == "admin"):
    print("Vítej admine")
