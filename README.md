## Pacman

Pacman peli sokkelopeli, jossa Pac-Man pallo (pelin pelaaja) syö pisteitä . Hänen täytyy vältellä haamuja pelatessaan. Haamuun osuessa hän menettää elämän ja elämien loppuessa peli päättyy. Tavoite on kerätä kaikki pisteet


*Dokumentaatiot*
- [release](https://github.com/tuovinenemma/ot-harjoitustyo1/releases)

- [käyttöohje](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/kayttoohje.md)

- [vaatimusmaarittely](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/tuntikirjanpito.md)

- [arkkitehtuuri](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/arkkitehtuuri.md)

- [changelog](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Mene ot-harjoitustyo tiedostosta pacman tiedostoon komennolla:
```bash
cd pacman
```


3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start

```
Muistathan suorittaa komennon poetry shell ympäristössä!
```bash
poetry shell
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```


### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
```bash
install coverage
```
```bash
install invoke
```

```bash
poetry run invoke coverage-report
```
### Pylint

Pylint suoritetaan komennolla:

```bash
poetry run invoke pylint
```
