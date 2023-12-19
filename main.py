#Name:M. Dusome
#Date: Dec 11
#Break down of PyGame to many files
#File to store all the global settings for your program
import settings
#Import the different Screens
import page1
import runaround_game
import page_exit

# The order of the screens to Run
#page1.display(settings.window)
runaround_game.display(settings.window)
#page_exit.display(settings.window)
