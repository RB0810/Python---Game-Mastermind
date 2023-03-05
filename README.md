# Python : Game-Mastermind

**Background of Game:**<br>
Our game is called mastermind. The inspiration comes from a board game most of us
played as children (especially in India).<br>
It is a game that involves mathematical permutation and combinations, without actual
theoretical solutions. Hence, the player unknowingly puts his knowledge to test whilst
having fun, developing critical thinking.<br>
The game is basically to guess the combination/sequence of colours as chosen by the
computer using hints and indicators being provided from time to time.

**Game Play:**<br>
The code generates a random row of four colours which is supposed to be decoded by
the player in a maximum of 9 guesses or tries. The code generated can comprise any
four colours out of the 7 colour list.<br>
The player starts by guessing, trying to duplicate exact colours and positions of the
pegs. After every guess, the code outputs white, red or black indicators which represent
the player’s progress.<br>
A red peg describes that the position as well as colour of the peg is correct.<br>
A white peg describes that the colour of the peg is correct.<br>
A black peg describes that neither the position nor the colour of the peg is correct.<br>
Example:<br>
A player guesses a sequence of four colours that he/she thinks might be correct.<br>
➢ If the player has two pegs that are the correct colors but are in the wrong
positions, the Code outputs two white pegs and two black pegs.<br>
➢ If the player has one peg of the correct color and in the correct position, the
Code outputs one red peg and three black pegs.<br>
➢ If the player has one peg of the correct colour in the wrong position and one
peg of the correct colour in the correct position, the Code outputs one white
peg, one red peg and two black pegs.<br>
With these pegs as indicators and hints, the player gets 9 guesses to crack the
correct combination, if he/she does that he/she wins, else they can try again.<br>


