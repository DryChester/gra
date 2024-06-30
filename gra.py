print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Witaj na Wyspie Skarbów!")
print("Twoją misją jest znaleźć skarb. Powodzenia! :)") 

rozwidlenie = input("Masz przed sobą rozwidlenie. Idziesz w [L]ewo czy w [P]rawo?\n")

if not rozwidlenie == "L":
 wyjście = input("Dwa dni temu Gae się tutaj przewrócił i zostawił wielką dziurę.\nWpadasz w nią, skręcasz sobie kark i giniesz. Koniec gry!") 
else:
 print("Omijasz koczujących w lasach Orleanu i idziesz dalej!\n")
 
 kierunek = input ("Dopływasz do morza słonych łez Popcia.\nCzy chcesz przez nie przepłynąć? [T]ak lub [N]ie? \n")
 if not kierunek == "N":
  print ("Z morza wychodzi Popcio. Zaczyna shillować Touhou i narzekać na Pokemony.\nGiniesz. Koniec gry!")
 else:
  print ("Nie ufasz tym szalonym wodom i obchodzisz je naookoło.\n")
  
  drzwi = input ("Po drodze znajdujesz małą chatkę na kaczej stopie. Wchodzisz do niej. Są tam trzy rodzaje drzwi.\n[C]zerwone, [Z]ielone oraz [N]iebieskie. Które wybierasz?\n")
  if drzwi == "C":
   print ("Napotykasz Nessa, który właśnie zginął 200 razy w Dark Soulsach.\nGiniesz. Koniec gry!")
  elif drzwi == "N":
   print ("Spotykasz Shya, który zaczyna gadać Ci o swoich ulubionych grach.\nUmierasz z nudów. Koniec gry!")
  elif drzwi == "Z":
   print ("Znalazłeś skarb. Wygrałeś! Brawo Anon!\n(tylko uważaj na urząd skarbowy)")
  else:
   print ("Nie wybierasz żadnych drzwi. Wychodzisz z chatki. Przychodzi Tateusz i wlepia Ci blachę w potylicę za tchórzostwo.\nGiniesz. Koniec gry!")