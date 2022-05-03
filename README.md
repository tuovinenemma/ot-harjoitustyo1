## Pacman

Pacman peli sokkelopeli, jossa Pac-Man pallo (pelin pelaaja) syö pisteitä . Hänen täytyy vältellä haamuja pelatessaan. Haamuun osuessa hän menettää elämän ja elämien loppuessa peli päättyy. Tavoite on kerätä kaikki pisteet


*Dokumentaatiot*
- [release](https://github.com/tuovinenemma/ot-harjoitustyo1/releases/tag/viikko5)

- [käyttöohje](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/kayttoohje.md)

- [vaatimusmaarittely.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/tuntikirjanpito.md)

- [arkkitehtuuri.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/arkkitehtuuri.md)

- [changelog.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/changelog.md)

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

