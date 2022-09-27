import math
import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
dark_green = (21, 71, 52)

WIDTH = 1200
HEIGHT = 800
FPS = 60

display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

clock = pygame.time.Clock()

def drawCircle():
    print("2 points are needed to draw a circle")
    firstClick = False
    secondClick = False
    key1 = False
    key2 = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key1 = True

                if event.key == pygame.K_2:
                    key2 = True

                if key1 and pygame.mouse.get_pressed()[0]:
                    x1, y1 = pygame.mouse.get_pos()
                    print("first click")
                    firstClick = True

                if key2 and pygame.mouse.get_pressed()[0]:
                    x2, y2 = pygame.mouse.get_pos()
                    print("second click")
                    secondClick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    key1 = False
                    key2 = False

        pygame.display.update()
        clock.tick(FPS)

        if firstClick and secondClick:
            break

        pygame.display.update()
        clock.tick(FPS)

    pygame.draw.circle(display, black, (x1, y1), math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2))), 5)

def drawTriangle():
    print("3 points are needed to draw a triangle")
    firstClick = False
    secondClick = False
    thirdClick = False
    key1 = False
    key2 = False
    key3 = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key1 = True

                if event.key == pygame.K_2:
                    key2 = True

                if event.key == pygame.K_3:
                    key3 = True

                if key1 and pygame.mouse.get_pressed()[0]:
                    x1, y1 = pygame.mouse.get_pos()
                    print("first click")
                    firstClick = True

                if key2 and pygame.mouse.get_pressed()[0]:
                    x2, y2 = pygame.mouse.get_pos()
                    print("second click")
                    secondClick = True

                if key3 and pygame.mouse.get_pressed()[0]:
                    x3, y3 = pygame.mouse.get_pos()
                    print("third click")
                    thirdClick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                    key1 = False
                    key2 = False
                    key3 = False

        pygame.display.update()
        clock.tick(FPS)

        if firstClick and secondClick and thirdClick:
            break

        pygame.display.update()
        clock.tick(FPS)

    pygame.draw.polygon(display, blue ,[(x1,y1),(x2,y2),(x3,y3)],5)

def drawRectangle():
    print("2 points are needed to draw a rectangle")
    firstClick = False
    secondClick = False
    key1 = False
    key2 = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key1 = True

                if event.key == pygame.K_2:
                    key2 = True

                if key1 and pygame.mouse.get_pressed()[0]:
                    x1, y1 = pygame.mouse.get_pos()
                    print("first click")
                    firstClick = True

                if key2 and pygame.mouse.get_pressed()[0]:
                    x2, y2 = pygame.mouse.get_pos()
                    print("second click")
                    secondClick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    key1 = False
                    key2 = False

        pygame.display.update()
        clock.tick(FPS)

        if firstClick and secondClick:
            break

        pygame.display.update()
        clock.tick(FPS)

    pygame.draw.polygon(display,red,[(x1,y1),(x2,y1),(x2,y2),(x1,y2)],5)

def drawLine():
    print("2 points are needed to draw a line")
    firstClick = False
    secondClick = False
    key1 = False
    key2 = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key1 = True

                if event.key == pygame.K_2:
                    key2 = True

                if key1 and pygame.mouse.get_pressed()[0]:
                    x1, y1 = pygame.mouse.get_pos()
                    print("first click")
                    firstClick = True

                if key2 and pygame.mouse.get_pressed()[0]:
                    x2, y2 = pygame.mouse.get_pos()
                    print("second click")
                    secondClick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    key1 = False
                    key2 = False

        pygame.display.update()
        clock.tick(FPS)

        if firstClick and secondClick:
            break

        pygame.display.update()
        clock.tick(FPS)

    pygame.draw.line(display, green, (x1, y1), (x2, y2), 5)

def drawEllipse():
    print("2 points are needed to draw an ellipse")
    firstClick = False
    secondClick = False
    key1 = False
    key2 = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key1 = True

                if event.key == pygame.K_2:
                    key2 = True

                if key1 and pygame.mouse.get_pressed()[0]:
                    x1, y1 = pygame.mouse.get_pos()
                    print("first click")
                    firstClick = True

                if key2 and pygame.mouse.get_pressed()[0]:
                    x2, y2 = pygame.mouse.get_pos()
                    print("second click")
                    secondClick = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    key1 = False
                    key2 = False

        pygame.display.update()
        clock.tick(FPS)

        if firstClick and secondClick:
            break

        pygame.display.update()
        clock.tick(FPS)

    if x1 < x2:
        l = x1
        w = x2 - x1
    else:
        l = x2
        w = x1 - x2

    if y1 < y2:
        t = y1
        h = y2 - y1
    else:
        t = y2
        h = y1 - y2

    pygame.draw.ellipse(display,purple,(l,t,w,h),5)

def main():
    display.fill(white)
    captureCount = 0
    loopCount = 0
    scale = 1.2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if loopCount == 0:
            chosenShape = input("Which shape would you like to draw?"
                                "\n1: Circle"
                                "\n2: Triangle"
                                "\n3: Rectangle"
                                "\n4: Line"
                                "\n5: Ellipse"
                                "\nChoice: ")

            if chosenShape == "1":
                drawCircle()

            if chosenShape == "2":
                drawTriangle()

            if chosenShape == "3":
                drawRectangle()

            if chosenShape == "4":
                drawLine()

            if chosenShape == "5":
                drawEllipse()

            loopCount = 1

        else:
            chosenShape = input("Which shape would you like to draw?"
                                "\n1: Circle"
                                "\n2: Triangle"
                                "\n3: Rectangle"
                                "\n4: Line"
                                "\n5: Ellipse"
                                "\n6: Screen Shot"
                                "\nChoice: ")

            if chosenShape == "1":
                drawCircle()

            if chosenShape == "2":
                drawTriangle()

            if chosenShape == "3":
                drawRectangle()

            if chosenShape == "4":
                drawLine()

            if chosenShape == "5":
                drawEllipse()

            if chosenShape == "6":
                print("Screen Grabbed")
                pygame.image.save(display, "screenshot" + str(captureCount) + ".jpeg")
                captureCount = captureCount + 1

        pygame.display.update()
        clock.tick(FPS)

main()
