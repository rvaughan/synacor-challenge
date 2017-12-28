#!/usr/bin/expect -f

spawn "./challenge.py"

expect "What do you do\?"

send "take tablet\r"
send "look tablet\r"
send "use tablet\r"
send "doorway\r"
send "north\r"
send "north\r"
send "bridge\r"
send "continue\r"
send "down\r"
send "east\r"
send "take empty lantern\r"
send "look empty lantern\r"
send "west\r"
send "west\r"
send "passage\r"
send "ladder\r"
send "west\r"
send "south\r"
send "north\r"
send "take can\r"
send "look can\r"
send "use can\r"
send "use lantern\r"
send "west\r"
send "ladder\r"
send "darkness\r"
send "continue\r"
send "west\r"
send "west\r"
send "west\r"
send "west\r"
send "north\r"
send "take red coin\r"
send "look red coin\r"
send "north\r"
# Reached the central hall
send "east\r"
send "take concave coin\r"
send "look concave coin\r"
send "down\r"
send "take corroded coin\r"
send "look corroded coin\r"
send "up\r"
send "west\r"
send "west\r"
send "take blue coin\r"
send "look blue coin\r"
send "up\r"
send "take shiny coin\r"
send "look shiny coin\r"
send "down\r"
send "east\r"
# Back at the central hall

# Now you need to solve the math problem using the collected coins. Each
# coin has a number of dots on it, these are the numbers that need to be
# plugged into the math equation. Coins are inserted at the left and move
# to the right when the next one is placed in the puzzle. If you fail to
# solve the problem then all of the coins fall out.
# Run the solve_coin_puzzle.py script
send "use blue coin\r"
send "use red coin\r"
send "use shiny coin\r"
send "use concave coin\r"
send "use corroded coin\r"

send "north\r"
send "take teleporter\r"
send "look teleporter\r"
send "use teleporter\r"

send "take business card\r"
send "look business card\r"
send "take strange book\r"
send "look strange book\r"

# At this point you see some text which essentially indicates that you need
# to put a specific value in the 8th register to use the teleporter to get
# somewhere interesting.
# The exact value needs to be calculated by extracting the teleportation
# algorithm and re-implementing it in an optimal manner.

interact
