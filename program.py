wiek = input("Podaj wiek użytkownika: ")
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

**********************************************

płeć = input("Jaka jest Twoja plec?")
wiek = input("Podaj swoj wiek: ")
#Sprawdzamy płeć oraz wiek użytkownika
wiek = int(wiek)
płeć = int(plec)
płeć = input("Podaj płeć użytkownika: \n 'k'-kobieta \n 'm'-mężczyzna \n")
if wiek >= 18:
    print(Specjalna usługa dla kobiet pełnoletnich!)
if płeć = 'k':
    print(Dostajesz od nas APEROLA!)
else:
    exist("Jesteś pełnoletni ale nie jesteś kobietą")
