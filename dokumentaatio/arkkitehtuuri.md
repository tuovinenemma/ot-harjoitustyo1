```mermaid
classDiagram
  main<|--Pacman
  main<|--jono
  main<|--pelinhallinta
  main<|--naytto
  pelinhallinta<|--Pacman

  class main{
    Pacman()
    Naytto()
    Jono()
    pelinhallinta._aloita_peli()

  }

  class jono{
    

  }

  class pelinhallinta{
    aloita_peli()
    handle_events()

  }

  class naytto{
    lataa()

  }

   class Pacman{
  move_pacman()
  move_ghost()
  update()
  lataa_naytto()

  }


```
