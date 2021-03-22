#KOLEKCJE DANYCH
li = [-2, 2, 20]
print(len(li))          #ZADANIE 1

li1 = li.copy()
li1.append(2)
print(li)
print(li1)              #ZADANIE 2

list3 = li + li1
print(sum(list3))       #ZADANIE 3

zbior1 = {"zielone", "czerwone"}
zbior2 = {2, "2", "zielone"}
x = zbior1 & zbior2
y = zbior1 | zbior2
z = zbior1 ^ zbior2
print(x, y, z)          #ZADANIE 4

zbior3 = zbior1.union(zbior2)
print(zbior3)           #ZADANIE 5

koszyk = {"gruszka" : 12,
        "jablko" : 2,
        "banan" : 5}
print(koszyk["banan"])    #ZADANIE 6

li = [3,4,'pies', 1,2]
if "kot" in li:
    print(bool(1))
else:
    print(bool(0))      #ZADANIE 7

#STRUKTURY KONTROLNE

#ZADANIE 1 -> lab1
#ZADANIE 2 -> lab1

li = ["pies", "kot", "chomik"]
x = input("Podaj zwierzę domowe: ")
if x in li:
    print("Gratulacje")
else:
    print("Podane zwierzę nie znajduje się na liście") #ZADANIE 3

list1 = [-3, 0, 2]
for i in list1:
    if i < 0:
        print(i, "jest mniejsze od 0")
    elif i == 0:
        print(i, "jest równe 0")
    elif i > 0:
        print(i, "jest większe od 0")
    i += 1                  #ZADANIE 4

for i in koszyk.items():
    print(i)                #ZADANIE 5

set1 = set()
for i in range(0, 5):
    set1.add(input("Podaj wartość: "))
print(set1)                 #ZADANIE 6
