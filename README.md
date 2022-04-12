# Tämä on Ohjelmistotekniikan kurssin harjoitustyö
[Työaikakirjanpito](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

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
