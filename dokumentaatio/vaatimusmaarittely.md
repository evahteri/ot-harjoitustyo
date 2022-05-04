# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus on työvuorosovellus, jossa työntekijä voi nähdä vapaat työvuorot ja valita ne itselleen sekä nähdä omat vuoronsa. Työnantaja pystyy lataamaan sovellukseen avoimia työvuoroja työntekijöiden vastaanotettavaksi. Sovelluksen tarkoitus on sopia erityisesti yritykselle joka tarjoaa usealle eri työntekijälle keikkaluontoisia töitä.

## Käyttäjät
Sovelluksella on kaksi käyttäjäroolia: Työntekijä ja työnantaja. Työntekijä voi valita listasta itselleen työvuoroja ja nähdä omat työvuoronsa. Työntekijä ei nää muiden työntekijöiden vuoroja, vain omat ja vapaat. Työnantaja pystyy lisäämään vapaita vuoroja ja tarkastelemaan kaikkia vuoroja.

## Käyttöliittymäluonnos
![Käyttöliittymäluonnos](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/IMG_20220329_175616.jpg)

## Perusversion tarjoama toiminnallisuus
### Ennen kirjautumista
- Käyttäjä voi luoda käyttäjätunnuksen _tehty_
  - Salasanan täytyy olla yli 8 merkkiä ja sisältää: _tehty_
    - Vähintään yksi iso kirjain _tehty_
    - Vähintään yksi pieni kirjain _tehty_
    - Vähintään yksi numero _tehty_
    - Vähintään yksi erikoismerkki (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.) _tehty_
   - Tunnusta luodessa valitaan rooli työntekijän ja työnantajan välillä _tehty_
- Käyttäjä voi kirjautua sisään tunnuksella ja salasanalla _tehty_
  - Jos käyttäjätunnus tai salasana on väärin, järjestelmä ilmoittaa siitä _tehty_
### Kirjautumisen jälkeen
#### Työntekijän rooli
- Käyttäjä voi valita haluaako nähdä omat vuorot vai vapaat vuorot _tehty_
  - Vapaissa vuoroissa näkyy vapaat vuorot ja siitä tiedot: _tehty_
    - Päivämäärä 
    - Aika 
    - Paikka 
    - "Choose shift" -nappula jolloin vuoro siirtyy omiin vuoroihin
  - Omissa vuoroissa näkyy valitut vuorot _tehty_
- Käyttäjä voi kirjautua ulos _tehty_
#### Työnantajan rooli
- Käyttäjä voi luoda uuden vuoron _tehty_
  - Uusi vuoro -lomake kysyy tiedot _tehty_
    - Päivämäärä
    - Aika
    - Paikka
   - "Create Shift" -nappulalla uusi vuoro luodaan _tehty_
- Käyttäjä voi nähdä kaikki vuorot _tehty_
  - Käyttäjä voi poistaa vuoron
- Käyttäjä voi kirjautua ulos _tehty_

## Jatkokehitysideoita
- Työnantaja pystyy muokata olemassaolevia vuoroja
- Lisätietojen lisääminen työvuoroon
- Omien työvuorojen organisointi tehtyihin ja tuleviin
- Työvuorojen lajittelu ja järjestys eri kriteereillä
- Käyttäjän ja tietojen poistaminen
- Työnantaja voi suoraan määrätä työntekijälle vuoroja _tehty_


  
