```mermaid

  classDiagram
    Pelilauta <|-- Pelaaja
    Pelilauta <|-- Noppa1
    Pelilauta <|-- Noppa2
    Pelilauta <|-- Aloitusruutu
    Pelilauta <|-- Vankila
    Pelilauta <|-- Sattumaruutu
    Pelilauta <|-- Yhteismaaruutu
    Pelilauta <|-- Kadut
    Pelilauta <|-- Asema
    Pelilauta <|-- Laitos
    Sattumaruutu <|-- Sattumakortit
    Yhteismaaruutu <|-- Yhteismaakortit
    Pelaaja <|-- Pankkitili

    class Pelaaja{
      nimi
      pelinappula
      liikuta()
      ruutu

    }

    class Pelilauta{
           
    }

      class Noppa1{
        heita()
      }

      class Noppa2{      
        heita()
      }
      
      class Aloitusruutu{
        sijainti_x_y
        aloita()
      }
      
      class Vankila{
        sijainti_x_y
        vankila()
      }
      class Sattumaruutu{
        toiminto()
      }
      
      class Yhteismaaruutu{
        toiminto()
      }
      
     
      class Sattumakortit{
        toiminto()
      }
      
      class Yhteismaakortit{
        toiminto()
      }
      
      class Kadut{
        nimi
        omistaja
        rakenna_talo()
        rakenna_hotelli()
      }
      
      class Asema{
        toiminto()
      }
      
      class Laitos{
        toiminto()
      }
      
      class Pankkitili{
        saldo
        lisaa_rahaa()
        nosta_rahaa()
      }
      
```
    
   
