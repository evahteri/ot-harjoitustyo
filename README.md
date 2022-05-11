# Work Shift App
Tämä sovellus on työvuorosovellus, jolla työnantaja voi luoda työvuoroja ja tarkastella niitä. Työntekijä voi valita vapaista vuoroista itselleen vuoroja ja tarkastella omia vuorojaan. Sovellukseen on mahdollista luoda useampi käyttäjä.

Tämä sovellus on tehty Helsingin Yliopiston Ohjelmistotekniikkakurssilla harjoitustyönä.

# Dokumentaatio

[Käyttöohje](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Työaikakirjanpito](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[Viikon 5 Release](https://github.com/evahteri/ot-harjoitustyo/releases/tag/viikko5)

[Viikon 6 Release](https://github.com/evahteri/ot-harjoitustyo/releases/tag/viikko6)

## Asennus

### Asenna riippuvuudet komennolla 

```bash
poetry install
```
### Alusta ohjelma

```bash
poetry run invoke build
```
### Käynnistä ohjelma

```bash
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman käynnistys

```bash
poetry run invoke start
```
### Testaus

```bash
poetry run invoke test
```
### Testikattavuusraportti

```bash
poetry run invoke coverage-report
```
Kattavuutta toi tarkastella htmlcov-hakemistosta löytyvästä index.html tiedostosta

### Pylint

Pylint tarkistus:

```bash
poetry run invoke lint
```
