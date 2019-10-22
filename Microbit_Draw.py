import microbit

points = []
grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
editing = True

def displayGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            microbit.display.set_pixel(j, i, grid[i][j])

def clearGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0;

def displayCursor(x, y):
    grid[y][x] = 5
    displayGrid()
    grid[y][x] = 0

def displayPoint(x, y):
    grid[y][x] = 9

def displayPoints(e):
    if e and points:
        for i in range(len(points)):
            displayPoint(points[i][0], points[i][1])
    elif not e and points:
        for i in range(len(points)):
            displayPoint(points[i][0], points[i][1])
            displayGrid()

def newPoint(x, y):
    points.append([x, y])

def removePoint(x, y):
    points.remove([x, y])

def freeze():
    editing = False
    clearGrid()

    while not editing:
        displayPoints(editing)
        if (microbit.button_a.was_pressed()):
            editing = True

def updatePos():
    x = 2
    y = 2

    if (microbit.accelerometer.get_x() <= -550):
        x = 0
    elif (-550 < microbit.accelerometer.get_x() <= -250):
        x = 1
    elif (-250 < microbit.accelerometer.get_x() <= 250):
        x = 2
    elif (250 < microbit.accelerometer.get_x() <= 550):
        x = 3
    elif (microbit.accelerometer.get_x() > 550):
        x = 4

    if (microbit.accelerometer.get_y() <= -550):
        y = 0
    elif (-550 < microbit.accelerometer.get_y() <= -250):
        y = 1
    elif (-250 < microbit.accelerometer.get_y() <= 250):
        y = 2
    elif (250 < microbit.accelerometer.get_y() <= 550):
        y = 3
    elif (microbit.accelerometer.get_y() > 550):
        y = 4

    displayCursor(x, y)

    if microbit.button_b.was_pressed():
        newPoint(x, y)
    elif microbit.button_a.was_pressed():
        if points:
            for i in range(len(points)):
                if points[i][0] == x and points[i][1] == y:
                    removePoint(x, y)
                    break

while editing:
    updatePos()
    displayPoints(editing)

    if (microbit.accelerometer.is_gesture("shake")):
        points.clear()
        clearGrid()
        displayGrid()
    elif (microbit.button_a.is_pressed() and microbit.button_b.is_pressed()):
        freeze()
