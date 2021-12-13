#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!
szam = int(input('Kérek egy számot!'))
szám = int(input('Kérek egy másik számot!'))
if szam < szám:
  print(szám, 'a nyagyobb!')
if szám < szam:
  print(szam, 'a nagyobb!')
else:
  print('Egyenlőek!')