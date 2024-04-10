So far, this is just the framework for our project.
We have a class object for each of the important categories in the game.

Miner, Gamer, Room which contains 1 miner and 1 gamer, and Level which contains a list of rooms, a list of miners, and a list of gamers.

These need to be expanded so that they cannot break any of the requirements and they perform the required actions.
We also need to implement parallel computing to simulate players and miners moving at the same time.
Our main file will run all of the actual operations.

PJW



Project plan:

Gamers = 10

Miners = 20

Levels: 10

Amount of time to collect gold per round = 10ms -1 per level

Amount of time miners stay in room = 10ns

Order of arrival - random

Rules:

1. Gamers have 10ms (-1 per level) to search for gold. If they don’t collect 20 coins by the end of their turn they go back into the queue.

2. Gamers are chosen at random. They cannot be chosen again until 3 other players had their turn and they can be randomly chosen again.

3. Miners bring a random number of coins but are less than or equal to 5.

4. Miners have 10ns to stay in the room and drop gold. Then randomly pop up in another room leaving gold.

5. As the gamer move up a level search time will decrease by one millisecond.

6. A gamer can only move up a level if they collect 20 coins.

Possible rules:

1. Number of Rooms per level = 3?

2. If multiple rooms are permitted, miners will randomly choose the rooms they will enter regardless of level. With 20 miners and 30 rooms in total they can simultaneously be in 20 and 10 are empty.

Now if there’s any thing else you would like to add, feel free to add and email this back to me.