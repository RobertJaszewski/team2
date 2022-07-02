wiek = input("Podaj wiek użytkownika: ")
#Sprawdzamy czy wiek jest złożony z cyfr
region = input ("Jesli jestes z Chin, wpisz 0, jesli nie 1")
if region.isdigit() == False:
    exit("Podano nieprawidlowa")
if wiek.isdigit() == False:
    exit("Wiek mosi być podany jako liczba")
wiek = int(wiek)
if wiek >= 18 and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
else:
    exit("Jesteś za młody na alkohol")
if region.isdigit() == False:
    exit("Podano nieprawidlowa wartosc")
region = int(region)
if region == 0:
    print("Uzytkownicy z Chin dostaja darmowa butelke whiskey")
elif region == 1:
    print("Uzytkownicy z poza Chin nie dostaja darmowej butelki whiskey")
else:
    exit("Podaj 0 lub 1")
