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

![login](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-55-04.png)

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

![create user](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-00.png)

Jos käyttäjän luominen onnistuu, sovellus ilmoittaa siitä ilmoituksella:

![created succesfully](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-07.png)

Jos salasana ei vastaa vaatimuksia, sovellus ilmoittaa siitä ilmoituksella:

![not succesfull](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-21.png)

## Sisäänkirjautuminen
Syötä käyttäjätiedot tekstikenttiin ja klikkaa login

![login view](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-50.png)

Jos käyttäjää ei löydy tietokannasta, sovellus ilmoittaa siitä:

![invalid](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-59-14.png)

Käyttäjätunnuksen ja salasanan ollessa oikein siirrytään roolin mukaiseen näkymään

 
## Työntekijän rooli

Klikkaamalla Show available shifts voit nähdä vapaat vuorot

Klikkaamalla Show my shifts voit nähdä omat vuorosi

Log out napista pääset kirjautumaan sovelluksesta ulos

![employee view](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-55.png)


### Vuorojen näkymä

Available shifts näkymässä, valitse haluamasi vuorot ja paina Choose selected shifts

![shifts](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-58-03.png)

### Työnantajan rooli

__TODO__

## Lopetus

Voit sulkea ohjelman yläkulman rastista. 
