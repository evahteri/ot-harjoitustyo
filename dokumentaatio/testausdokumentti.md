# Testausdokumentti

Ohjelmaa on testattu käyttöliittymän kautta laajasti eri tilanteiden luomisella ja automaattisilla yksikkö- ja integraatiotesteillä unittestillä.
Huom! Ohjelma on kehitetty ja testattu ainoastaan Python -versiolla 3.8.10.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Kaikki sovelluslogiikka testataan TestShiftAppService, koska ohjelman ShiftAppService vastaa sovelluslogiikasta. 
Testille luodaan ympäristöksi testaamiseen ShiftAppService -luokka ja luodaan sen avulla käyttäjä testejä varten.
Luokka testaa laajasti ShiftAppServicen metodeja eri funktioilla.

### Repositoriot

Kumpaakin Repository -luokkaa testataan erillisissä testitiedostoissa. Kummallekin luodaan testejä varten omat tietokannat varsinaisen ohjelman tietokannoista erilleen, joiden nimet on konfiguroitu .env.test -tiedostossa.
Tiedostot testaavat laajasti Repository -luokkien metodeja eri funktioilla.

### Testauskattavuus

Ohjelman testikattavuus on 98%, kun käyttöliittymää ei testata.

![kattavuus](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202022-05-12%2007-20-41.png)

Kattavuuden ulkopuolelle näistä jäivät initialize-database tiedoston kutsu, configin FileNotFoundError ja build -tiedoston kutsu.
Nämä puutteet eivät jätä mitään kriittistä toiminnallisuutta testien ulkopuolelle.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on toteutettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on ladattu ja se on asennettu sekä suoritettu useissa eri Linux -ympäristöissä sekä macOs ympäristössä. 
Sovellusta on testattu virheellisillä käyttöliittymän syötteillä ja eri yhdistelmillä vuoroja sekä käyttäjiä.

### Toiminnallisuudet

Kaikki määrittelydokumentin vaativat toiminnallisuudet on toteutettu ja ne toimivat virheettömästi lopullisessa ohjelmaversiossa. Myös virheelliset syötteet on otettu huomioon, eikä ohjelma kaadu millään syötteellä.

## Sovellukseen jääneet laatuongelmat

- Käyttäjä voi muokata ikkunan kokoa, eikä se muutu välttämättä takaisin normaaliin kokoon, tälle ratkaisu olisi ollut määrittää jokaiselle ikkunalle tietty koko, jota ei voi muuttaa.
