# Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email
#
# Vytvoř následující funkce:
#
# is_adult: Funkce ověří zda je uživatel dospělý
# is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
# create_user:
#   Funkce vytvoří slovník reprezentujícího uživatele.
#  Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
# Pokud je vše v pořádku, create_user vrátí následující slovník:
# {
# "success": True,
# "user": {"username": "...", "age": ..., "email": "..."}
# }
#  Pokud validace selže, create_user vrátí:
# {
# "success": False,
# "error": "Chybová zpráva..."
# }
#
# print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#
# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.
#
# Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.

user = {
    "username": "Kuba",
    "age": 28,
    "email": "jakub1@seznam.cz",
}

def is_adult(age):
    return age >= 18

def is_name_valid(username):
    return len(username) >= 4

def create_user(username, age, email):
    if not is_name_valid(username):
        return {
            "success": False,
            "error": "Uzivatelske jmeno musi mit alespon 4 znaky."
        }
    if not is_adult(age):
        return {
            "success": False,
            "error": "Uzivatel musi být starsi 18 let."
        }
    return {
        "success": True,
        "user": {
            "username": username,
            "age": age,
            "email": email
        }
    }
def print_user_info(info):
    if info["success"]:
        user = info["user"]
        print(user)
    else:
        print("CHYBA:", info["error"])

users = [
    create_user("Petr", 29, "petr@gmail.com"),
    create_user("Ondra", 17, "ondra@gmail.com"),
    create_user("Jan", 30, "jan@email.cz"),
    create_user("Radek", 22, "radek@email.cz")
]
for user in users:
    print_user_info(user)