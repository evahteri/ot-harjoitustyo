# Käyttöohje

## Ohjelman käynnistäminen

### Alkutoimet

Asenna riippuvuudet komennolla 

```bash
poetry install
```
Sitten suorita alustus komennolla

```bash
poetry run invoke build
```

## Käynnistäminen

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```
Sovellus aukaisee login näkymän

(kuva)

## Uuden käyttäjän luominen

Klikkaa Create new user nappia

Syötä tekstikenttiin haluamasi käyttäjätunnus ja salasana

Huom! Salasanan täytyy olla yli 8 merkkiä pitkä ja sisältää:
- Vähintään yksi iso kirjain
- Vähintään yksi pieni kirjain 
- Vähintään yksi numero 
- Vähintään yksi erikoismerkki (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.)

Valitse itsellesi relevantti rooli valintanappulasta

Luo käyttäjä painamalla Create

(kuva)

## Työntekijän rooli

Klikkaamalla Show available shifts voit nähdä vapaat vuorot

Klikkaamalla Show my shifts voit nähdä omat vuorosi

Log out napista pääset kirjautumaan sovelluksesta ulos

### Vuorojen näkymä

Available shifts näkymässä, valitse haluamasi vuorot ja paina Choose selected shifts

(kuva)

### Työnantajan rooli

__TODO__

## Lopetus

Voit sulkea ohjelman yläkulman rastista. 
