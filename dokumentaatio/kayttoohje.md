# Käyttöohje

## Konfigurointi

Ohjelma käyttää tallennukseen kahta eri tiedostoa. Näiden nimiä voit muokana ohjelman .env -tiedostossa:
![env]()

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

![create user](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2018-16-17.png)

Jos käyttäjän luominen onnistuu, sovellus ilmoittaa siitä ilmoituksella:

![created succesfully](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-07.png)

Jos salasana ei vastaa vaatimuksia, sovellus ilmoittaa siitä ilmoituksella:

![not succesfull](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-21.png)

## Sisäänkirjautuminen
Syötä käyttäjätiedot tekstikenttiin ja klikkaa login

![login view](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-44-05.png)

Jos käyttäjää ei löydy tietokannasta, sovellus ilmoittaa siitä:

![invalid](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-59-14.png)

Käyttäjätunnuksen ja salasanan ollessa oikein siirrytään roolin mukaiseen näkymään

## Työnantajan rooli

Työnantajana voit valita haluatko nähdä kaikki vuorot vai luoda uuden. Tietokanta ei sisällä valmiiksi yhtään vuoroa.

![Employer_view](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-28-22.png)

### Luo uusi vuoro

Klikkaamalla "Create a new shift" voit luoda uuden vuoron

![new shift](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-28-28.png)

Syötä haluamasi tiedot, voit jättää "Employee" kentän tyhjäksi jos et halua määrittää sitä tietylle työntekijälle, vaan se on vapaana kenelle tahansa.
Luo vuoro klikkaamalla "Create"

![creation](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-29-01.png)

Jos tiedot ovat oikein, tulee ilmoitus:

![successfull](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-29-05.png)

Jos jokin vaadituista tiedoista puuttuu, tulee ilmoitus:

![unsuccessful](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-29-14.png)

### Kaikkien vuorojen tarkastelu

Voit nähdä kaikki luomasi vuorot taulukossa klikkaamalla "Show all shifts":

![all shifts](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-43-12.png)

Voit kirjautua ulos ja palata kirjautumisnäkymään "Log out" painikkeesta.
 
## Työntekijän rooli

Klikkaamalla Show available shifts voit nähdä vapaat vuorot:

![available](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-43-12.png)

Voit valita vapaan vuoron itsellesi klikkaamalla sitä ja painamalla "Choose selected shift":

![choice](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-42-06.png)

Sovellus ilmoittaa onnistuneesta toiminnosta:

![success](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-42-09.png)

Nyt klikkaamalla Show my shifts voit nähdä omat vuorosi:

![my shifts](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2017-42-19.png)

Log out napista pääset kirjautumaan sovelluksesta ulos

![employee view](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-03%2014-57-55.png)

## Lopetus

Voit sulkea ohjelman yläkulman rastista. 
