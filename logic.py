#!/usr/bin/env python3
import keyboard
import time
# player health counter default value

playerLife = 3

# something for the player to want

gold = 0

# current game state

gameOver = False

# keyboard directions
keys = [
    "down",
    "up",
    "left",
    "right",
    "w",
    "s",
    "a",
    "d"
]

# list of directions
playerMoves = ["return", "forward!", "left", "right"]

# dictionary of places with answers
rooms = {"Room1": ["orcs! lose 1 health",
    "healing fountain! gain 1 health", "empty! choose next door"]}

def chooseDirection(keyPressed):
    global gameOver
    #print("Key pressed = "+keyPressed.name)
    try:
        if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                print("left!")
                gameOver = True
        elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                print("right!")
        elif keyboard.is_pressed("up") or keyboard.is_pressed("w"):
                print("up!")
        elif keyboard.is_pressed("down") or keyboard.is_pressed("s"):
                print("return!")
                gameOver = True
    except:
        print("wrong key pressed...")
        print("please use w,a,s,d or up,left,down,right arrows for movement selection")
        





print("Game starting....")
while gameOver==False:
        time.sleep(1)
        keyboard.on_press(chooseDirection)
        time.sleep(1)

print("Game Over")
    