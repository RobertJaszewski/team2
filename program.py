wiek = input("Podaj wiek użytkownika: ")
plec = input("Podaj płeć użytkownika: \n 'k'-kobieta \n 'm'-mężczyzna \n")
#Sprawdzamy czy użytkownik dobrze wpisał symbol płci według instrukcji,
#przy wpisaniu nieprawidłowych znaków program się kończy.
if plec == "k":
    print("Użytkownik jest kobietą.")
elif plec == "m":
    print("Użytkownik jest mężczyzną.")
else:
    exit("Źle wpisany symbol płci.")

#Sprawdzamy czy wiek jest złożony z cyfr
region = input ("Jesli jestes z Chin, wpisz 0, jesli nie 1")
if region.isdigit() == False:
    exit("Podano nieprawidlowa")
if wiek.isdigit() == False:
    exit("Wiek mosi być podany jako liczba")
wiek = int(wiek)
if wiek >= 18 and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50 and wiek <= 120:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
elif wiek > 120:
    print("Maksmylany wiek to 120 lat")
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
płeć = input("Jaka jest Twoja płeć?")
wiek = input("Podaj swój wiek: ")
#Sprawdzamy płeć oraz wiek użytkownika
wiek = int(wiek)
płeć = int(płeć)
płeć = input("Podaj płeć użytkownika: \n 'k'-kobieta \n 'm'-mężczyzna \n")
if wiek <= 120:
    print("Specjalna usługa dla kobiet pełnoletnich!")
if płeć == "k":
    print("Dostajesz od nas APEROLA!")
else:
    exit("Jesteś pełnoletni ale nie jesteś kobietą")

