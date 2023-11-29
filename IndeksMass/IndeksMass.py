
print("Tere! Olen sinu uus sõber - Python!")

nimi = input("Sisesta oma nimi: ")

print(nimi + ", oi kui ilus nimi!")

try:
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
except ValueError:
    print("Palun sisestage arv (0 või 1)!")
    exit()

if vastus == 1:
    try:
        
        pikkus = int(input("Sisesta pikkus (cm): "))
        mass = float(input("Sisesta kaal (kg): "))
    except ValueError:
        print("Palun sisestage kehtivad numbrid!")
        exit()

    indeks = mass / (0.01 * pikkus) ** 2
    
    print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
   
    if indeks < 16:
        print("Tervisele ohtlik alakaal")
    elif 16 <= indeks < 19:
        print("Alakaal")
    elif 19 <= indeks < 25:
        print("Normaalkaal")
    elif 25 <= indeks < 30:
        print("Ülekaal")
    elif 30 <= indeks < 35:
        print("Rasvumine")
    elif 35 <= indeks < 40:
        print("Tugev rasvumine")
    else:
        print("Tervisele ohtlik rasvumine")

else:
    print("Kahju! See on väga kasulik info!")


print()

print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
