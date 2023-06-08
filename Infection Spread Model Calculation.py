import random

WIDTH = 1920
HEIGHT = 1080

population = 1000
rep = 5
distanceSquare = (200 / 3.5) ** 2
inflectionProb = 3 / 1000
carrier = 1
data = []
carriers = set()
while len(carriers) < 5:
    carriers.add(random.randint(0, population - 1))
    
i = 0
while i < population:
    data.append((random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, WIDTH), random.randint(0, HEIGHT), 0))
    i += 1
    
complete = 0
result = []

def move(x, y, gX, gY, goal, index):
    if (x, y) != (gX, gY):
        if x == gX:
            if y < gY:
                y += 1
            else:
                y -= 1
        elif y == gY:
            if x < gX:
                x += 1
            else:
                x -= 1
        else:
            d = random.random()
            if d < 0.5:
                if x < gX:
                    x += 1
                else:
                    x -= 1
            else:
                if y < gY:
                    y += 1
                else:
                    y -= 1
    else:
        if rep != goal:
            goal += 1
            gX = random.randint(0, WIDTH)
            gY = random.randint(0, HEIGHT)
        else:
            x = -1
            y = -1
            gX = -1
            gY = -1
            global complete
            complete += 1
    data[index] = (x, y, gX, gY, goal)
    
def spreadDisease():
    for (x1, y1, _, _, goal1) in [data[i] for i in carriers]:
        if not goal1 is rep:
            j = 0 
            while j < population:
                if not j in carriers:
                    (x2, y2, _, _, goal2) = data[j]
                    if not goal2 is rep and (x1 - x2) ** 2 + (y1 - y2) ** 2 < distanceSquare and random.random() < inflectionProb:
                        carriers.add(j)
                j += 1
        
    

while True:
    i = 0
    while i < population:
        (x, y, gX, gY, goal) = data[i]
        move(x, y, gX, gY, goal, i)
        i += 1
    spreadDisease()
    result.append(len(carriers))
    if population is len(carriers) or complete - 1 is population:
        break

print(result)