score = 0
def provjeri_pitanje(odgovor, tačan_odgovor):
    global score 
    pokušaj = 3
    while pokušaj > 0:
      if(odgovor.upper() == tačan_odgovor.upper()):
        print("Tačan odgovor")
        score += 1
        break
      else:
          print ("Netačan odgovor")
          break
      
pitanje_1 = "Koliko igrača čini jedan tim u košarci?"
pitanje_2 = "Ko je naslikao Mona Lisu?"
pitanje_3 = "Koje su tri osnovne boje?, a=plava, crvena, žuta. b=plava, žuta, zelena. c=crvena, žuta, ljubičasta?"
pitanje_4 = "Koja je najveća planeta u sunčevom sistemu?"
pitanje_5 = "Koja životinja može spavati naopako?"
pitanje_6 = "Zašto astronauti lebde u svemiru? a=nema kisika, b=nema gravitacije, c=previše gravitacije"
pitanje_7 = "Koji je hemijski simbol za vodu?"
pitanje_8 = "Koji je najtvrđi materijal na svijetu?"
pitanje_9 = "Koja je formula za izračunavanje gustine tijela?"
pitanje_10 = "Koji kontinent ima najviše država?"
pitanje_11 = "Ko se smatra osnivačem dinastije Kotromanića?"
pitanje_12 = "Ko je napisao ¨Pinokija¨?"
Pitanje_13 = "Koji je najpoznatiji web pretraživač?"
pitanje_14 = "Koliko iznosi pi(π)(bar 5 brojeva)?"
pitanje_15 = "Ko je najbolji šahista?"
lista_pitanja = (pitanje_1, pitanje_2, pitanje_3, pitanje_4, pitanje_5, pitanje_6, pitanje_7, pitanje_8, pitanje_9, pitanje_10, pitanje_11, pitanje_12, Pitanje_13, pitanje_14, pitanje_15)
odgovor_1 = "5"
odgovor_2 = "LEONARDO DA VINCI"
odgovor_3 = "A"
odgovor_4 = "JUPITER"
odgovor_5 = "SISMIS"
odgovor_6 = "B"
odgovor_7 = "H2O"
odgovor_8 = "DIJAMANT"
odgovor_9 = "M/V"
odgovor_10 = "AFRIKA"
odgovor_11 = "STJEPAN KOTROMANIC"
odgovor_12 = "KARLO KOLODI"
odgovor_13 = "GOOGLE CHROME"
odgovor_14 = "3.1415"
odgovor_15 = "MAGNUS CARLSEN"

lista_odgovora = (odgovor_1, odgovor_2, odgovor_3, odgovor_4, odgovor_5, odgovor_6, odgovor_7, odgovor_8, odgovor_9, odgovor_10, odgovor_11, odgovor_12, odgovor_13, odgovor_14, odgovor_15)

for i in range(15):
    ulaz = input(lista_pitanja[i])
    provjeri_pitanje(ulaz.upper(), lista_odgovora[i])
print("Osvojili ste %s poena " % score)

if score == 0:
    print ("Igra preporučena za tebe je iks oks")

if score > 0 and score < 6:
    print ("Igra preporučena za tebe je fortnite")

if score > 5 and score < 11:
    print ("Igra preporučena za tebe je roblox")

if score > 10 and score < 16:
    print ("Igra preporučena za tebe je šah")


