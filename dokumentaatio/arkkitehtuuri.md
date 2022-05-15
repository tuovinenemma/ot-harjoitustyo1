# Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Aloitusnäyttö
- Pelaaminen
- Lopetusnäyttö

Näitä eri osa-alueita pelissä kuvaa sen "state".
- Start
- Playing
- Game over

```mermaid
classDiagram
  Aloitusnaytto--|>Peli
  Peli--|>Lopetus
  
  class Aloitusnaytto{
    aloita_peli()
    state = start
    
   }
  class Peli{
    pelaa()
    state = playing
  }
  
  class Lopetus{
    lopeta_peli()
    state = game over
  }
```

# Pelin rakenne jakautuu eri rakenteisiin

```mermaid
classDiagram
  main<|--Game
  Game<|--Maze
  Game<|--Game_events
  Game<|--Pacman
  Game<|--Ghosts
  Game<|--Start
  Game<|--Gameover

  class main{
    Pacman()
    
    Game_events()
    start_game()

  }

  class Maze{
    create_maze()
    

  }

  class Game_events{
    aloita_peli()
    handle_events()

  }

 

   class Game{
  move_pacman()
  move_ghost()
  update()
  create_maze()

  }
  class Pacman{

  }
  
  class Ghosts{
   

  }
  
  class Start{
   

  }
  class Gameover{
   

  }
 
```
# Pelin kulku
 
 Peli aloitetetaan alkunäytöstä jossa painamalla SPACE-nappia päästään pelin seuraavaan tasoon: pelinäkymään.


```mermaid

sequenceDiagram
participant Main
participant Game
participant Handle_events
participant Game_events

Main->>Game: Game()
activate Game
Game->>Game: Game.run()
Game->>Game: Game.start_events()
Game->>Game: Game.start_update()
Game->>Game: Game.teksti()
Game->>Game: Game.start_playing()
Game->>Handle_events: get()
activate Handle_events
Handle_events->>Game: 
deactivate Handle_events
Game->>Game_events: aloita_peli()
activate Game_events
Game_events->>Game: 
deactivate Game_events
Game->>Main: exit()
deactivate Game







```

