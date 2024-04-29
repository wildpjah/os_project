# Miner Game
The Miner Game Simulator project aims to create a simulation environment where users can explore concurrency management and deadlock prevention concepts. Deadlocks in asynchronous threading occur when two or more threads are blocked forever, waiting for each other to release resources they need to proceed. In asynchronous programming, this deadlock scenario typically arises due to the way threads interact with shared resources or synchronize their execution. 

Asynchronous threading means that threads can execute independently and concurrently. They may not wait for each other explicitly, as in synchronous programming, but instead may continue execution and perform tasks in a non-blocking manner. To mitigate deadlocks in asynchronous threading, developers can employ strategies such as proper resource management, using asynchronous primitives that minimize resource contention, careful design of thread interactions, and thorough testing to uncover potential deadlock scenarios. Additionally, adopting programming patterns that reduce the need for shared mutable state can also help minimize the risk of deadlocks. 

The Miner game will simulate what happens inside CPU by using twenty miners and ten games to simulate multiple processes happening at once and waiting for their turn on the queue. The game is more complicated since instead of the default 1 room per level, we have three rooms in our simulation. However, if one thread acquires a lock or resource and then needs access to another resource held by a second thread, and vice versa, a deadlock can occur. Each thread is waiting for the other to release the resource it needs before it can proceed, leading to a standstill.

Rules of the Game:
1. Miners drop gold and Gamers collect gold.
There can only be one miner and gamer in the room at the same time.
2. The miner randomly drops from 0 - 5 gold coins per room. They have 10ms per room.
3. There are 10 levels, and in order to make it to the next level the gamer needs to collect 20 coins.
4. The gamer has a small amount of time (100ms) to search for gold coins. Can only collect one coin per room. If they don’t collect 20 coins by the end of their turn they go back into the queue.
5. There are 3 rooms per level.
6. Gamers are chosen at random. They cannot be chosen again until 3 other players had their turn and they can be randomly chosen again.
7. Each gamer and miner will have their own thread and run at the same time asynchronously. 
8. They will be deadlocked based on how much time they have to wait and how they are randomly chosen.
9. Miners will have a 100ms head start, to go into rooms and drop coins.
10. Miners will randomly choose the rooms they will enter regardless of level. With 20 miners and 30 rooms in total they can simultaneously be in 20 and 10 are empty.



Design:
- Main.py – creates random seed based off of the current time.
	- Creates a track list of miners and gamers. 
	- Creates a task list for asyncio, gamers, and miners.
		- For Asyncio to understand what to run concurrently. 
		- await.asyncio.gather runs tasks concurrently
- helperfunctions.py – it has a new game function that creates a new game.
- Game.py – holds the levels rooms, keeps track of gamers and miners, keeps track of rooms that are unoccupied. 
	- Check_win – determines the winner
	- Level_from_game – tracks what level a room is on.
	- Print_coins_per_room – used for testing, just prints how many coins are in the room. 
- Other Objects:
	- Level.py – Hold the rooms, miners, and gamers. Its an aggregator for rooms. 
		- Keeps track of gamers and holds gamers when rooms are occupied.
		- Room.py – holds coins, one miner and one gamer.
		- Person.py - abstract class, describes and defines what miners and gamers do.
		- Makes it easier to create miners and gamers.
	- Miner.py – Class contains the class miner that contains game, id, name, coins, and room. Contains Asynchronous loop functions to continue entering rooms and dropping coins until someone wins
		- Functions:
			- enter_room – allows miners into room
			- find_room – checks the game for empty rooms. When it picks a room, it uses the find_room function.
			- Updates the game on which rooms are unoccupied or not.
			- leave_room – updates the game and the room.
			- This is asynchronous with a timer.
			- mine_coins – generates a random number between 0 – 5.
			- Updates the coins for the miners.
			- add_coin – adds coins to the room.
			- set_coin – randomly generates coins
	- gamer.py – gamer class extends person, game, contains the game, id, name, coins, and room. It’s the main loop for the gamer.
		- Functions:
			- loop_for_win an asynchronous function that checks to see if the game has been won yet. 
			- find_room – finds a room that is unoccupied.
			- If there’s empty rooms on the same level and pick a random pick a random, if occupied nothing happens.
			- Collect _coin is asynchronous, if inside room it will count how many coins there are in the room. 
				- It takes 10ms to collect one coin
				- 100ms allotted time the gamer has to search the room. (With allotted time the gamer can only collect 10 coins per room in total.)
				- If the room has less than 10 coins, the gamer will not stay the whole 100ms 
			- self.level_up checks to see if gamer has the 20 coin s need to level up.
				- If < 20 coins, the gamer stays in the same level.
				- If coins = 20 then the Gamer moves on to the next level.
			- game_win – checks what level the level is currently in.
				- activated when the self.level_up function checks for then coin amount the gamer contains.
				- If the gamer is in the last level they win if not the self.Level_up function moves the gamer to the next level.
			- Leave_room – activated when leveling up, makes gamer leave room.
				- if the gamer levels up they move on to the next level otherwise they wait until their turn.
				- Level.get.gamers – retrieves list of gamers in previous level and uses the level.set_gamers function to update the list and add gamers to the next level.
- Modules/Libraries:
	- Random – generates a random number of coins, room, miner, and gamer.
	- Asyncio – asynchronous programming, simulating multithreading, deadlocks, lock mechanism.
	- Pygame or Tkinter - Used for designing the user interface and providing visual representation of the game simulation, including the grid layout, miners, gamers, rooms, and levels.
Challenges: 
- Locks: deadlocks are difficult because of waiting causing the program to gridlock. It causes each process to wait for each other instead of moving asynchronously. 
	- Multiple rooms with multiple levels – a lot of objects to work with simultaneously. Its hard to get so many things to interact with each other. 
	- Global Interpreter Locks – can only use one CPU core.
	- Changed the loop for loop_for_win function finds a room, enter, collect the room, and leave the room. Leave is explicitly called in the loop. 
	- Before it was an asynchronous function, it would acquire the lock during the function, and now all functions run with the same lock.
- Animation: We will have to create an animation class, and have the miners and gamers interact with that class. We have to do more research on different python modules that can animate the asynchronous multithreading. We will attempt to try two python tools, tkinter and pygame. Eventually, pygame ended up being easier to use. There were some major issues that made it difficult though:
	- It needs to be run in a separate process
		- Separate processes do not share memory and as such the animation would not be able to “see” the game.
		- A manager and proxies need to be set up to copy the original object.
		- These proxies then need to be updated every time the original is changed.
- When information is shared between processes in Python, it needs to be Picklable. 
	- The asyncio functions cause the objects involved to not be Picklable. 
	- In order to resolve this, each object needs functions such that they can be translated into a dictionary and rebuilt from that dictionary.
