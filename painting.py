from turtle import *  # importerer turtle til python programmet

speed(0)

bgcolor("olive")

penup()               # penup commandoen som tar opp pennen og lager ingen spor
print(pos())          #printer posisjonen
goto(-640.00, 0.00)   #går til start posisjonen ved bruk av goto kommandoen til kordinatene
pendown()             # pendown, motsatte av penup.
color("orangered")    # skifter farge til første figuren "orangered"
begin_fill()          # "begin_fill" commandoen som starter å fylle figuren fra punkt til punkt til figuren er ferdig og satt sammen.
right(90)             # figuren går til venstre fra den sitt perspektiv
forward(355)          # pennen går fram ned mot venstre hjørne
left(90)              # figuren skifter rettning 90 grader til venstre
forward(540)          # figuren går fram



left(130)             # første punkt med løkke der figuren skifter rettning 130 grader mot venstre
for i in range(20):   # løkke som lager en kant
    forward(2)
    left(1)

for i in range(15):   # en del av den andre løkken bare med mindre gjentakelser
    forward(1)
    left(2)

forward(230)          # går fram til kanten som skal være det siste punktet av den gule firkanten

for i in range(9):    # løkke som lager bøyd kant
    forward(1)
    right(10)

forward(183)          # går fram fra kanten til starten av den store buen som er siste punkt av den første figuren

for i in range(90):   # løkke som gjør buen
    forward(5)
    left(1)

end_fill()            # endfill som stopper fill commandoen og da er den oransje figuren nr 1 ferdig.

penup()               # penup som tar pennen opp

backward(286)         # figuren går bakover over punktet der den løkken over startet
left(90)              # snur mot venstre fra figuren sitt perspektiv
forward(270)          # går fram til startpunktet av firkanten
left(180)             # snur rundt 180 grader

color("yellow")       # skifter farge til gul
begin_fill()          # begynner den andre fyllen som er gul
pendown()             # pendown som starter å lage en linje

for i in range(9):    # løkke som lager kant nr1
    forward(1)
    right(10)

forward(200)          # går fram 200 og starter på løkke nr2

for i in range(9):    # løkke nr2 starter å lage kant nr2
    forward(1)
    right(10)
forward(200)          # samme som over, går fram til neste løkke

for i in range(9):    # løkke nr3 som lager kant nr3
    forward(1)
    right(10)

forward(200)          # samme som over, går fram til neste løkke

for i in range(9):    # løkke nr 4 som er den siste kanten på figuren (kant nr4)
    forward(1)
    right(10)

forward(200)          # går fram til startpunktet
end_fill()            # slutter fill
penup()               # pennen går opp

backward(200)         # pennen går bakover

right(90)             # snur 90 grader


forward(350)          # går 350 grader framover
right(90)             # snur mot høyre
forward(23)           # går ned fram til startpunktet til balong tråen
print(pos())          # printer posisjonen

pendown()             # pennen går ned for å tegne tråen
color("black")        # skifter farge til svart som skal være fargen på tråen til balongen.
begin_fill()          # starter å fylle med svart som er fyllen på tråen og knuten/sirkelen som tråden går fra
for i in range(123):  # starer på løkke på sirkelen som tråen skal gå ut av
    left(5)
    forward(1)

right(75)             # snur 75 grader mot høyre fra slutten på sirkelen som er startpunket på tråen
forward(430)          # går framover, dette er lengen på tråen
left(90)              # snur 90 grader for å starte på den andre linjen som er en del av tråen
forward(5)            # går fram mot neste startpunkt
left(90)              # snur mot start av neste linje
forward(430)          # går ned mot sirkelen som lager et rektangel sammen med den andre linjen som skaper tråen
end_fill()            # slutter fyllen

backward(430)         # går bakover 430 for å starte på balongen
right(90)             # snur 90 grader for å starte på sirkelen
color("orangered")    # skifter farge til "orangred" oransje rød som er fargen på balongen
begin_fill()          # begynner fyllen
for i in range(220):  # løkken som lager balongen.
    forward(6)
    right(3)
end_fill()            # stopper fyllen, balongen er ferdig.

penup()               # pennen går opp for å starte på den 3 delen av malingen
color("black")
pos1 = 632.94, 160.69 #lager en variabel som heter pos1 som holder kordinatene som brukes til å skifte pos ved å bruke goto
goto(pos1)            #går til variablet, altså posisjonen som er holdt inni en variabel (pos1)
print(pos())          #printer posisjonen
pendown()             #pennen går ned for å begynne på den første trekanten

#FIGUR: TREKANT PÅ HØYRE SIDE AV MALERIET

color("orangered")    #skifter farge til oransje
begin_fill()          #begynner fillen
left(30)              #snur 30 grader for å lage den ene siden av trekanten
forward(260)          #sideflaten
right(90)             #sidekant trekant
forward(100)          #fram 100

print(pos())          #printer posisjonen
pos2 = pos()          #en annen vei for å bruke variabel på posisjonen. Hvis kordinatene skifter så gjør det seg automatisk inni variabelen, altså variablen = pos() som er kommando for den aktuelle posisjonen.

for i in range(9):    #løkke som lager kantene for trekanten
    forward(1)
    right(10)

forward(130)          #går framover
right(20)
for i in range(9):    #løkke som lager en til kant.
    forward(1)
    right(3)
forward(170)          #framover igjen
end_fill()            #slutten på fillen på trekanten. trekanten er nå ferdig.
penup()

#FIRKANT UNDER TREKANTEN TIL HØYRE SIDE AV MALERIET.

goto(pos2)            #går til lagret pos av variablet som er over. Denne inneholder kordinatene til det forrige punktet som vi skal tilbake til for å starte på firkanten.
color("yellow")       #skifter farge til gul.
begin_fill()          #begynner å fylle alle punktene fram til endfill kommando.
pendown()             #pennen går ned og starter å tegne.
right(43)             #snur fra start pos til posisjonen som er fram.
pos3 = pos()          #lagrer den aktuelle posisjonen som en variabel som vi bruker etterpå.
forward(100)          #går framover for å starte på firkanten
goto(pos3)            #går tilbake til den start posisjonen altså pos3 som er variablet over.
left(180)             #snur 180 grader rundt fordi variablet er lagret med motsatt rettning.

for i in range(9):    #løkken som starter på den første kanten, kant 1/4.
    forward(1)
    left(10)

forward(100)          #går fram 100 til neste kant.

for i in range(9):    #løkken som lager kant nr2 altså kant 2/4
    forward(1)
    left(10)

forward(100)          #går fram igjen til neste kant.

pos4 = pos()          #lagrer posisjonen i en variabel igjen.

for i in range(9):    #løkke til kant nr3 altså 3/4
    forward(1)
    left(10)

forward(100)          #går framover til neste kant.

for i in range(9):    #siste kant i figuren, nå er alle kantene på firkanten ferdig.
    forward(1)
    left(10)

penup()               #pennen går opp for å flytte til neste posisjon.
end_fill()            #stopper fyllen på firkanten.
goto(pos4)            #går til pos4 som ble lagret som variabel over.

#DEL NR1 AV FØRSTE REKTANGEL MEST TIL HØYRE SOM ER SATT SAMMEN AV TO DELER, DEL BLÅ OG GUL. VI STARTER PÅ BLÅ

color("lightblue")    #skifter farge til blå for å starte på den ene delen av rektanglet.
begin_fill()          #begynner fyllet.
pendown()             #pennen går ned og vi starter.

forward(100)          #går fram for å lage den første sideflaten

for i in range(9):    #første kant på rektanglet, kant 1/4. Løkke.
    forward(1)
    left(10)

forward(135)         #går fram for å lage den andre sideflaten.

pos5 = pos()         #lagrer posisjonen igjen inni en variabel.

for i in range(9):   #løkken som lager den andre kanten på figuren, kant 2/4
    forward(1)
    left(10)

forward(50)          #går framover 50 på underflaten der figuren tar slutt og den blå trekanten inni rektangelet altså den blå delen er ferdig.

end_fill()           #slutter fyllen.

#DEN GULE DELEN INNI REKTANGELET

color("yellow")     #skifter farge til gul
begin_fill()        #begynner fyllet.

forward(50)         #går framover til venstre kant av figuren, 50 fordi den andre halvdelen er blå. Så til sammen 100.
left(90)            #snur 90 grader
forward(141)        #går fram for å avslutte figuren, nå er den gule delen ferdig og hele rektanglet nr 1 er ferdig.

end_fill()          #stopper å fylle.
penup()             #pennen går opp
goto(pos5)          #går til pos som er lagret i variablet pos 5.

left(180)           #snur helt rundt fordi variablet har motsatt vei lagret.
pendown()           #pennen går ned og vi starter på det andre rektangelet som er helt gult, altså rektangelet mest til høyre på venstre siden av maleriet

#SISTE REKTANGEL, ALTSÅ REKTANGEL NR 1 MEST TIL VENSTRE PÅ HØYRE SIDE AV MALERIET.

begin_fill()        #Begynner å fylle figuren i gul, skriver ikke color("yellow") igjen fordi vi allerede har den på.
for i in range(9):  #løkke som starter på den første kanten.
    forward(1)
    right(10)

forward(100)        #går framover på underflaten. vi bruker sideflaten til det første rektangelet så vi trenger bare 3 sideflater tegnet for å fylle figuren.

for i in range(9):  #neste kant løkke
    forward(1)
    right(10)

forward(135)        #neste sideflate på rektangelet.

for i in range(9):  #en til løkke
    forward(1)
    right(10)

pos6 = pos()        #lagrer posisjonen igjen i en variabel som vi går tilbake til

forward(100)        #går fram mot siste kant.

for i in range(9):  #siste kant løkke i rektangelet som kommer i kontakt med flaten til det andre rektangelet.
    forward(1)
    right(10)

end_fill()          #vi slutter å fylle gul
penup()

goto(pos6)

right(90)
backward(100)
left(180)
for i in range(9):
    forward(1)
    left(10)
goto(pos6)
color("orangered")
begin_fill()

pendown()
left(90)

for i in range(9):
    forward(1)
    right(13.5)
forward(190)
for i in range(10):
    forward(3)
    right(15)
goto(pos6)
left(92.5)
forward(100)
for i in range(9):
    forward(1)
    left(9)
forward(150)

end_fill()

#EKSTRA KODE OM CREDITS

input1 = input("credits (y/n)")        #variablet input lagrer det personen skriver altså y eller n og vi kan bruke det med if eller else eller elif
if input1 == "y":                      #If som betyr hvis, hvis personen skriver str y så vil det printe ut mitt navn som credits på slutten av koden.
    print("made by kamil podgorni")
else:                                  #else som betyr ellers, så hvis personen skriver noe annet eller n så vil det bare si "thanks for playing" og avslutte koden.
    print("thanks for trying")
