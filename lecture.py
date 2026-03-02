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

name = "Petr"
position = "traktorista"
grade = 4
is_student = False
name_size = len(name)

   # Petr je traktorista
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

age = 2005
age2 = int("2005") + 18
sentence = "Petr se narodil roku " + str(age)
sentence2 = "Kdyz Petr mel 18, byl rok " + str(age2)
print(sentence)
print(sentence2)

number1 = 1.1
number2 = int(number1)
print(number2)
print(str(number2))

num1 = 1
num2 = 0
n1 = bool(number1)
n2 = bool(number2)
print(n1)
print(n2)

name1 = ""
is_empty = len(name1) == 0
print(is_empty)

brand = ""
brand = brand + "H"
brand = brand + "P"
print(brand)