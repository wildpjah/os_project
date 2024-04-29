Miner Game
The Miner Game Simulator project aims to create a simulation environment where users can explore concurrency management and deadlock prevention concepts. Deadlocks in asynchronous threading occur when two or more threads are blocked forever, waiting for each other to release resources they need to proceed. In asynchronous programming, this deadlock scenario typically arises due to the way threads interact with shared resources or synchronize their execution. 
Asynchronous threading means that threads can execute independently and concurrently. They may not wait for each other explicitly, as in synchronous programming, but instead may continue execution and perform tasks in a non-blocking manner. To mitigate deadlocks in asynchronous threading, developers can employ strategies such as proper resource management, using asynchronous primitives that minimize resource contention, careful design of thread interactions, and thorough testing to uncover potential deadlock scenarios. Additionally, adopting programming patterns that reduce the need for shared mutable state can also help minimize the risk of deadlocks. 
The Miner game will simulate what happens inside CPU by using twenty miners and ten games to simulate multiple processes happening at once and waiting for their turn on the queue. The game is more complicated since instead of the default 1 room per level, we have three rooms in our simulation. However, if one thread acquires a lock or resource and then needs access to another resource held by a second thread, and vice versa, a deadlock can occur. Each thread is waiting for the other to release the resource it needs before it can proceed, leading to a standstill.


Rules of the Game:
1. Miners drop gold and Gamers collect gold.
2. There can only be one miner and gamer in the room at the same time.
3. The miner randomly drops from 0 - 5 gold coins per room. They have 10ms per room.
4. There are 10 levels, and in order to make it to the next level the gamer needs to collect 20 coins.
5. The gamer has a small amount of time (100ms) to search for gold coins. Can only collect one coin per room. If they don’t collect 20 coins by the end of their turn they go back into the queue.
6. There are 3 rooms per level.
7. Gamers are chosen at random. They cannot be chosen again until 3 other players had their turn and they can be randomly chosen again.
8. Each gamer and miner will have their own thread and run at the same time asynchronously. 
9. They will be deadlocked based on how much time they have to wait and how they are randomly chosen.
10.  Miners will have a 100ms head start, to go into rooms and drop coins.
11. Miners will randomly choose the rooms they will enter regardless of level. With 20 miners and 30 rooms in total they can simultaneously be in 20 and 10 are empty.






Design:
1. Main.py – creates random seed based off of the current time.
   1. Creates a track list of miners and gamers. 
   2. Creates a task list for asyncio, gamers, and miners.
      1. For Asyncio to understand what to run concurrently. 
         1. await.asyncio.gather runs tasks concurrently
2. helperfunctions.py – it has a new game function that creates a new game.
3. Game.py – holds the levels rooms, keeps track of gamers and miners, keeps track of rooms that are unoccupied. 
   1. Check_win – determines the winner
   2. Level_from_game – tracks what level a room is on.
   3. Print_coins_per_room – used for testing, just prints how many coins are in the room. 
4. Objects:
   1. level.py – Hold the rooms, miners, and gamers. Its an aggregator for rooms. 
      1. Keeps track of gamers and holds gamers when rooms are occupied.
   2. room.py – holds coins, one miner and one gamer.
   3. person.py - abstract class, describes and defines what miners and gamers do.
      1. Makes it easier to create miners and gamers.
         1. miner.py – Class contains the class miner that contains game, id, name, coins, and room. Contains Asynchronous loop functions to continue entering rooms and dropping coins until someone wins
            1. Functions:
               1. enter_room – allows miners into room
               2. find_room – checks the game for empty rooms. When it picks a room, it uses the find_room function.
                  1. Updates the game on which rooms are unoccupied or not.
               3. leave_room – updates the game and the room.
                  1. This is asynchronous with a timer.
               4. mine_coins – generates a random number between 0 – 5.
                  1. Updates the coins for the miners.
               5. add_coin – adds coins to the room.
               6. set_coin – randomly generates coins
         2. gamer.py – gamer class extends person, game, contains the game, id, name, coins, and room. It’s the main loop for the gamer.
            1. Functions:
            2. loop_for_win an asynchronous function that checks to see if the game has been won yet. 
               1. find_room – finds a room that is unoccupied.
               2. If there’s empty rooms on the same level and pick a random pick a random, if occupied nothing happens.
               3. Collect _coin is asynchronous, if inside room it will count how many coins there are in the room. 
                  1. It takes 10ms to collect one coin
                  2. 100ms allotted time the gamer has to search the room. (With allotted time the gamer can only collect 10 coins per room in total.)
                  3. If the room has less than 10 coins, the gamer will not stay the whole 100ms 
                  4. self.level_up checks to see if gamer has the 20 coin s need to level up.
                     1. If < 20 coins, the gamer stays in the same level.
                     2. If coins = 20 then the Gamer moves on to the next level.
                  5. game_win – checks what level the level is currently in.
                     1. activated when the self.level_up function checks for then coin amount the gamer contains.
                     2. If the gamer is in the last level they win if not the self.Level_up function moves the gamer to the next level.
                  6. Leave_room – activated when leveling up, makes gamer leave room.
                     1. if the gamer levels up they move on to the next level otherwise they wait until their turn.
                     2. Level.get.gamers – retrieves list of gamers in previous level and uses the level.set_gamers function to update the list and add gamers to the next level.
5. Modules/Libraries:
   1. Random – generates a random number of coins, room, miner, and gamer.
   2. Asyncio – asynchronous programming, simulating multithreading, deadlocks, lock mechanism.
   1. Pygame or Tkinter - Used for designing the user interface and providing visual representation of the game simulation, including the grid layout, miners, gamers, rooms, and levels.
Challenges: 
1. Locks: deadlocks are difficult because of waiting causing the program to gridlock. It causes each process to wait for each other instead of moving asynchronously. 
   1. Multiple rooms with multiple levels – a lot of objects to work with simultaneously. Its hard to get so many things to interact with each other. 
   2. Global Interpreter Locks – can only use one CPU core.
   3. Changed the loop for loop_for_win function finds a room, enter, collect the room, and leave the room. Leave is explicitly called in the loop. 
   4. Before it was an asynchronous function, it would acquire the lock during the function, and now all functions run with the same lock.
2. Animation: We will have to create an animation class, and have the miners and gamers interact with that class. We have to do more research on different python modules that can animate the asynchronous multithreading. We will attempt to try two python tools, tkinter and pygame. So far pygame has been a failure, the problem could be the short about of time that the gamers and miners have per room.