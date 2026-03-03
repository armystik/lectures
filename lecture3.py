books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]
print(books)
# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
# 2. Změň cenu jedné libovolné knihy. Vypiš list.
# 3. Odstraň nějakou knihu. Vypiš list.
# 4. Vypiš celkový počet knih v listu.
# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)

books.append({
    "name": "Pivo Plzeň",
    "price": 1399,
    "author": "Kuba",
    "publication_year": 1969,
})
books.append({
    "name": "Hladový psycholog",
    "price": 2544,
    "author": "Lubomir Kratochvil",
    "publication_year": 2006,
})
print(f"Po přidání: {books}")

books[1]["price"] = 1550 # dal jsem změnu ceny u druhé knihy
print(f"Po změně ceny: {books}")

books.pop(0) # smazal jsem první knihu
print(f"Po odstranění: {books}")

print(f"Celkový počet knih: ", len(books))

print("--- Přidání nové knihy v příkazovém řádku---")

name = input("Zadej název knihy: ")
author = input("Zadej autora: ")
price = int(input("Zadej cenu: "))
publication_year = int(input("Zadej rok vydání: "))

books.append({
    "name": name,
    "author": author,
    "price": price,
    "publication_year": publication_year
})

print(f"Po přidání knihy přes input: {books}")