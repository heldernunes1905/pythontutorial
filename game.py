# game.py
# import the draw module

#works the same as if a normal class in a file, to use it I gotta call it and after that I can reference any functions in that file, send values and the same as if it was a normal function in the same file
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()



#can also just call a specific object from a module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)


# game.py
# import the draw module
#will import all objects from a module
from draw import *

def main():
    result = play_game()
    draw_game(result)


# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)




#get re module and print all functions with the word find
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))