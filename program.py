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
