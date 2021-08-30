
import random

randomPO = 0
randomSM = 0

while randomPO == randomSM:
    randomPO = random.randint(0,4)
    randomSM = random.randint(0,4)

team1 = ["Bryan Soh","Bryan Thum","Amanda","Jun Le","Jian Yiee"]

print("Product Owner: " + team1[randomPO])
print("Scrum Master: " + team1[randomSM])

