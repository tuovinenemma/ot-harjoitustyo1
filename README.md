## Pacman

Pacman peli sokkelopeli, jossa Pac-Man pallo (pelin pelaaja) syö pisteitä . Hänen täytyy vältellä haamuja pelatessaan. Haamuun osuessa hän menettää elämän ja elämien loppuessa peli päättyy. Tavoite on kerätä kaikki pisteet


*Dokumentaatiot*

- [gitlog.txt](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/laskarit/viikko1/gitlog.txt)


- [vaatimusmaarittely.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito.md](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```


2. Käynnistä sovellus komennolla:

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
poetry run invoke coverage-report
```

