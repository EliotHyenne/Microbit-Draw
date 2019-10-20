import microbit

posX = 2
posY = 2
points = []
editing = True

def newPoint(x, y):
    points.append([x, y])
    
def removePoint(x, y, array):
    for i in range(len(array)):
        if array[i][0] == x and array[i][1] == y:
            array.remove(array[i])
            break
    
def setPoints(array):
    if array:
        for i in range(len(array)):
            microbit.display.set_pixel(array[i][0], array[i][1], 9)

def freeze(array):
    editing = False
    microbit.display.clear()
    
    while not editing:
        setPoints(array)
        if (microbit.button_a.was_pressed()):
            editing = True
    
def updatePos(x, y):
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
        
    microbit.display.clear()
    microbit.display.set_pixel(x, y, 9)
        
    if microbit.button_b.was_pressed():
        newPoint(x, y)
    elif microbit.button_a.was_pressed():
        if points:
            for i in range(len(points)):
                if points[i][0] == x and points[i][1] == y:
                    removePoint(x, y, points)
                    break

while editing:
    updatePos(posX, posY)
    setPoints(points)
    
    if (microbit.accelerometer.is_gesture("shake")):
         points.clear()
    
    if (microbit.button_a.is_pressed() and microbit.button_b.is_pressed()):
        freeze(points)
    