# Testausdokumentti

## Asennus ja testaus

Sovellusta on testattu eri ympäristöissä, kuten macOS, Linux ja Windows. Käyttöjärjestelmän ja liittymän testaus on suoritettu manuaalisesti eri tekijöiden avulla. Täten sovelluksen käyttöliittymä parannettu toimivaksi.

## Toiminnallisuudet

Sovelluksen eri vaatimusmäärittelyn toiminnallisuudet ja sen käyttöohjeet löytyvät linkeistä [käyttöohje](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/kayttoohje.md) ja [vaatimusmaarittely](https://github.com/tuovinenemma/ot-harjoitustyo1/blob/main/dokumentaatio/vaatimusmaarittely.md).

## Testauskattavuus

Testauskattavuuden voi nähdä komennoilla:

```bash
install coverage
```
```bash
install invoke
```

```bash
poetry run invoke coverage-report
```
