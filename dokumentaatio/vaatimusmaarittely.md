#Vaatimusmäärittely
##Sovelluksen tarkoitus
Sovellus on työvuorosovellus, jossa työntekijä voi nähdä vapaat työvuorot ja valita ne itselleen sekä nähdä omat vuoronsa. Työnantaja pystyy lataamaan sovellukseen avoimia työvuoroja työntekijöiden vastaanotettavaksi. Sovelluksen tarkoitus on sopia erityisesti yritykselle joka tarjoaa usealle eri työntekijälle keikkaluontoisia töitä.

##Käyttäjät
Sovelluksella on kaksi käyttäjäroolia: Työntekijä ja työnantaja. Työntekijä voi valita listasta itselleen työvuoroja ja nähdä omat työvuoronsa. Työntekijä ei nää muiden työntekijöiden vuoroja, vain omat ja vapaat. Työnantaja pystyy lisäämään vapaita vuoroja ja tarkastelemaan kaikkia vuoroja.

##Käyttöliittymäluonnos
todo

##Perusversion tarjoama toiminnallisuus
###Ennen kirjautumista
-Käyttäjä voi luoda käyttäjätunnuksen
  -Salasanan täytyy olla yli 8 merkkiä ja sisältää:
    -Vähintään yksi iso kirjain
    -Vähintään yksi pieni kirjain
    -Vähintään yksi numero
    -Vähintään yksi erikoismerkki (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.)
   -Tunnusta luodessa valitaan rooli työntekijän ja työnantajan välillä
-Käyttäjä voi kirjautua sisään tunnuksella ja salasanalla
  -Jos käyttäjätunnus tai salasana on väärin, järjestelmä ilmoittaa siitä
###Kirjautumisen jälkeen
####Työntekijän rooli
-Käyttäjä voi valita haluaako nähdä omat vuorot vai vapaat vuorot
  -Vapaissa vuoroissa näkyy vapaat vuorot ja siitä tiedot:
    -Päivämäärä
    -Aika
    -Paikka
    -"Choose shift" -nappula jolloin vuoro siirtyy omiin vuoroihin
  -Omissa vuoroissa näkyy valitut vuorot
-Käyttäjä voi kirjautua ulos
####Työnantajan rooli
-Käyttäjä voi luoda uuden vuoron
  -Uusi vuoro -lomake kysyy tiedot
    -Päivämäärä
    -Aika
    -Paikka
   -"Create Shift" -nappulalla uusi vuoro siirtyy vapaisiin vuoroihin
-Käyttäjä voi nähdä kaikki vuorot
  -Käyttäjä voi poistaa vuoron
-Käyttäjä voi kirjautua ulos

##Jatkokehitysideoita
-Työnantaja pystyy muokata olemassaolevia vuoroja
-Lisätietojen lisääminen työvuoroon
-Omien työvuorojen organisointi tehtyihin ja tuleviin
-Työvuorojen lajittelu ja järjestys eri kriteereillä
-Käyttäjän ja tietojen poistaminen


  
