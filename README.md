## Pacman

Pacman peli sokkelopeli, jossa Pac-Man pallo (pelin pelaaja) syö pisteitä . Hänen täytyy vältellä haamuja pelatessaan. Haamuun osuessa hän menettää elämän ja elämien loppuessa peli päättyy. Tavoite on kerätä kaikki pisteet


*Dokumentaatiot*
- [release](https://github.com/tuovinenemma/ot-harjoitustyo1/releases/tag/viikko5)


- [vaatimusmaarittely.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/tuntikirjanpito.md)

- [arkkitehtuuri.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/arkkitehtuuri.md)

- [changelog.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```


2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start

```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```
Muistathan suorittaa komennon poetry shell ympäristössä!
```bash
poetry shell
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

