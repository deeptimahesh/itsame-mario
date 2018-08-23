#Python terminal Super Mario Bros
## itsame-mario

### Introduction
This game has been written using common Python libraries and also, __Numpy__ library for 
board rendering and __Colorama__ lib for adding background, foreground and/or style.

###Structure
This game's code demonstrates inheritance, encapsulation, polymorphism and overloading.
* __Board__ has its own class and captures all objects to be rendered. Made using Numpy.
* Each player/enemy is derived of __Person__ class
* Many objects such as bricks, pipes, etc are of __Object__ class

###Running the program

1) Install all the requirements:

   ```pip install -r requirements.txt```  
2) Now, replace first line of main.py with your location of python installation

   ```#!/usr/bin/env python```
3) Run program
   
   ```python3 main.py```

###Controls
* ```A```: Left, ```D```: Right, ```W```: Jump
* Additionally you can move right/left/up while jumping again
* To quit, press ```q```
* To restart game after losing/winning, press ```r```

###File Structure
* init.py
* person.py
* objects.py
* board.py
* config.py
* requirements.txt
* README.md