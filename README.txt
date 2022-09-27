When running this program a console and a pygame window will appear on screen.

In the console you will need to choose what type of shape you will want to create:

1: Circle
2: Triangle
3: Rectangle
4: Line
5: Ellipse

In order to create each shape you will be required to select points with your mouse in the pygame window, you will also need to choose which point you are placing.  You do this by using the number keys located at the top of the keyboard using the 1, 2, or 3 keys.  You must press the number and left-click with your mouse at the same time for the variable to save in the program.  Each shape will let you know how many points are needed once you select it in the console output.

After the first shape is drawn you will be given another option in the menu.

6: Screen Shot

This option will allow you to save the pygame window as a .jpeg in the root folder of the program. Each screenshot will be saved as screenshot#.jpeg where the # is a number ranging from 0 to a MAX_VALUE int.

There is the possibility that the shapes created can be larger than the pygame window.  A circle uses two selected points.  These are used to obtain the center and the radius.  If the center of the circle is close to the edge of the screen and the radius is quite far from the center-point, then it is possible that part of the circle will be outside of the window.