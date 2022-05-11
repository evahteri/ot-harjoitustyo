# Arkkitehtuurikuvaus

## Rakenne

Sovellus rakentuu neljästä pääkomponentista: ui, services, entities ja repositories.

Ui hakemisto sisältää kaiken graafisen käyttöliittymän toiminnallisuuden. Se ei itsessään sisällä sovelluslogiikkaan kuuluvia komponentteja vaan vain kutsuu toimintoja muista luokista. Käyttöliittymään sisältyy useampi näkymä, ne ovat kuvailtu tarkemmin myöhemmin.
Services hakemistossa on yksi tiedosto ja luokka, joka vastaa sovelluslogiikasta. Sitä kautta suurin osa sovelluksen toiminnallisuudesta suoritetaan.
Repositories sisältää toiminnallisuudet molempiin tietokantoihin eli shift databaseen ja user databaseen. Näiden luokkien kautta toimii kaikki pysyväistallennukseen liittyvät toiminnallisuudet.
Entities sisältää sovelluksen kaksi tietomuotoa koostavat komponentit User ja Shift.

## Sovelluslogiikka
Luokat User ja Shift muodostavat sovelluksen loogisen tietomallin, jotka sisältävät tietoja käyttäjistä ja vuoroista.

Sovelluksen toiminnallisuus toteutuu luokassa ShiftAppService, joka tarjoaa sovelluksen perustoiminnoille omat metodit, esim:

- `create_user(username, password, role)`
- `create_shift(date, time, location, employee)`
- `login(username, password)`

Kaikki pysyväistallennukseen liittyvät metodit on toteutettu repositories hakemistoon, jota kautta niitä käytetään. Alla näkyy tarkemmin luokkien suhteet pakkauskaaviossa.

![Arkkitehtuurikaavio](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuurikaavio_shift_app.drawio(1).svg)

## Tietojen pysyväistallennus

Sovelluksessa käytetään pysyväistallennukseen kahta eri .db tyyppistä tiedostoa, joihin on tallennettu SQLite tietokanta. Luokat ShiftRepository ja UserRepository kommunikoivat tietokannan kanssa ja sisältävät metodit tallennukseen sekä hakemiseen.
Nämä metodit ovat esimerkiksi:

- `find_user_shifts(user)`
- `find_all_shifts()`
- `find_user(username)`
- `login(username,password)`

Molemmissa db tiedostoissa on yksi taulu, shift_database sisältää kolumnit date, time, location, employee. User_database sisältää kolumnit username, password, role.

## Käyttöliittymä

Lopullisen sovelluksen käyttöliittymä sisältää kuusi eri näkymää:

- login näkymä, josta kirjaudutaan sisään
- create user näkymä, josta luodaan uusi käyttäjä
- employee näkymä, joka näyttää työntekijän näkymän
- employer näkymä, joka näyttää työnantajan näkymän
- shift näkymä, joka näyttää halutut vuorot
- create shift näkymä, josta luodaan uusi vuoro (vain työnantajan roolissa)

Edelliseen näkymään voi aina palata back -painikkeella.

## Toiminnalliisuus

### Päätoiminnallisuudet


#### Käyttäjän kirjautuminen

Käyttäjä näkee näkymässä kentät käyttäjätunnukselle ja salasanalle. Nämä syötettyään käyttäjän painaessa login nappia, seuraavat asiat tapahtuvat:

![Sekvenssikaavio](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio.png)

UI käyttää ShiftAppServicen login-funktiota, joka taas käyttää user repositoryn login -funktiota, joka hakee tietokannasta käyttäjän. Tässä vaiheessa nostetaan error jos käyttäjää ei löydy tai salasana ei täsmää. User repository palauttaa user -olion ShiftAppServicelle, joka edelleen palauttaa sen UI:lle ja UI:n näkymä siirtyy roolin mukaiseen näkymään.

### Käyttäjän luominen

Käyttäjä syöttää käyttöliittymän kenttiin käyttäjätunnuksen ja salasanan, sekä valitsee itselleen sopivan roolin. Tämän jälkeen käyttäjän painaessa "Create user" tapahtuu seuraavat asiat:

![create user](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2020-03-27.png)

UI Käyttää ShiftAppServiceä, joka taas käyttää UserRepositoryn funktiota käyttäjän luomiseen. Jos jokin virhe ei esiinny, funktiot palauttavat user -olion takaisin ja käyttäjälle ilmoitetaan onnistuneesta käyttäjän luomisesta.

### Vuoron luominen

Käyttäjä kirjoittaa käyttöliittymän kenttiin tarvittavat tiedot ja painaa "Create shift". Sitten ohjelma toimii seuraavalla tavalla:

![create shift](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-11%2020-06-18.png)

UI Käyttää ShiftAppServiceä, joka taas käyttää ShiftRepositoryn funktiota vuoron luomiseen. Jos jokin virhe ei esiinny, funktiot palauttavat shift -olion takaisin ja käyttäjälle ilmoitetaan onnistuneesta vuoron luomisesta.

### Muu toiminnallisuus

Loput ohjelman toiminnallisuudesta koostuu samalla tavalla. Muut luokat kutsuvat muiden luokkien metodeja tarpeen mukaan ja näin ohjelman vastuualueet ovat selkeät.


