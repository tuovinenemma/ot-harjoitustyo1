```mermaid
classDiagram
  Aloita_peli--|>Vihollinen
  Aloita_peli--|>Pacman
  Aloita_peli--|>Taso

  class Pacman{
    move_pacman()

  }

  class Vihollinen{
    move_ghost()

  }

  class Aloita_peli{
    nayton_luominen()
    handle_events()

  }

  class Taso{


  }



```
