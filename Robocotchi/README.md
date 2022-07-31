## In this game, you will care for a robogotchi pet, play with, and oil every so often.
## Robopet requires care and attention: only instead of feeding it you charge it,
## instead of putting it to bed you switch it to the sleeping mode, and instead of meds it needs oil.
### Here are the robot's basic features: name, level of battery, level of overheat, 
### skills, boredom, level of rust.
## There are a few ways that the user can interact with their robopet and improve its well-being parameters:
- play allows the user to play one of the two possible games. Playing decreases the level of boredom by 20 and increases the level of overheat by 10
You have two games to choose: Numbers and rock-scissor-paper.  
Rules of the game numbers: first, a random number is generated in the interval from 0 to 1,000,000. 
Then, the robot player and the human player each provide a number. The player whose number is closer to the generated number wins. 
- recharge gives the robot a chance to boost its energy. The option Recharge increases the level of battery by 10, decreases the level of overheat by 5, and increases the level of boredom by 5.
- sleeping mode gives the robot a well-deserved break and allows it to cool off. Sleeping mode decreases the level of overheat by 20. 
- learning increases the level of skill by 10, decreases the level of the battery by 10, increases the level of overheat by 10, and increases the level of boredom by 5. 
- working decreases the level of battery by 10, and increases the level of boredom and overheat by 10 each. It also might increase the level of rust, but it depends on unpleasant events. 
- info prints all the information about the robopet and its vitals.
- oil is the robot's medicine that helps with rust. Oiling decreases the rust level by 20.
### An unpleasant event could happen during working, learning and playing. One of the following events may take place: 
### stepping into a puddle (increases the level of rust by 10), or falling into the pool (increases the level of rust by 50).
### if rust level or overheat reaches 100 you lose 