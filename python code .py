# Welcome to your Python project!
import os
import time
import random
highscore_file = "highscore.txt"
if os.path.exists(highscore_file):
    with open(highscore_file, "r") as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
else:
    highscore = 0
playerName = ""
gameDifficulty = -1
os.system('clear')
while gameDifficulty < 1 or gameDifficulty > 3:
    print ("select a difficulty level (1, 2, or 3):")
    gameDifficulty = int(input(">"))
    if gameDifficulty <1 or gameDifficulty > 3:
        print("invalid difficulty, please try again.\n")
print("difficulty successfully set to:",gameDifficulty)
while len(playerName) < 3:
    print("\nEnter your n=username (minimum 3 charcters): ")
    playerName = input(">")
    if len(playerName) < 3:
        print("invalid name. must be at least three characters.")
print("\nWelcome", playerName + "!")
print("the game will begin shortly")
time.sleep(2)
os.system('clear')
GRID_SIZE = 20
player_x = random.randint(0, GRID_SIZE - 1)
player_y = random.randint(0, GRID_SIZE - 1)
goal_x = random.randint(0, GRID_SIZE - 1)
goal_y = random.randint(0, GRID_SIZE - 1)
playerHealth = 100
score = 0
enemies_x = [5, 10, 3, 15, 7]
enemies_y = [5, 10, 12, 4, 16]
if gameDifficulty == 1:
    move_damage = 1
    enemy_damage = 5
elif gameDifficulty == 2:
    move_damage = 2
    enemy_damage = 10
elif gameDifficulty == 3:
    move_damage = 3
    enemy_damage = 15
debug = False
while True:
    os.system('clear')
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if x == player_x and y == player_y:
                row += "P "
                continue
            if x == goal_x and y == goal_y and debug:
                row += "G "
                continue
            enemy_found = False
            for i in range(5):
                if enemies_x[i] == x and enemies_y[i] == y and debug:
                    row += "E "
                    enemy_found = True
                    break
            if not enemy_found:
                row += "# "
        print(row)
    print("Health:", playerHealth)
    print("Move with W A S D (type 'debug' to toggle enemy/goal visibility):")
    move = input(">> ") .lower ()
    if move == "debug":
        debug = not debug
        print("Debug mode", debug)
        time.sleep(1)
        continue
    if move in ["w", "a", "s", "d"]:
        new_x = player_x
        new_y = player_y
        if move == "w":
            new_y -= 1
        if move == "s":
            new_y += 1
        if move == "a":
            new_x -= 1
        if move == "d":
            new_x += 1
        if 0 <=new_x < GRID_SIZE:
            player_x = new_x
        if 0 <=new_y < GRID_SIZE:
            player_y = new_y
        playerHealth -= move_damage
        for i in range(5):
            if player_x == enemies_x[i] and player_y == enemies_y[i]:
                playerHealth -= enemy_damage
                print ("OH NO! You hit an enemy! YOU LOST", enemy_damage, "5 HEALTH POINTS!")
                time.sleep(1)
    if player_x == goal_x and player_y == goal_y:
        print("WOOP WOOP! You reached the goal! YOU WIN")
        score = playerHealth
        print("Your score:", score)
        print("Highscore:", highscore)
        if score > highscore:
            print("WOAH YOU BEAT YOUR HIGHSCORE!")
            with open(highscore_file, "w") as f:
                f.write(str(score))
        break
    if playerHealth <= 0:
        print("Oh no. You ran out of health! GAME OVER LOSER!")
        print("Highscore:", highscore)
        break


