from components import vars
from PIL import Image
from emoji import emojize

def total(value):
    # do some logic to see which character you selected

    if value == 40:
        vars.character = vars.characters[0]

        print("You are " + vars.character + emojize(":green_heart:"))
       
        myImage = Image.open("bruce.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 130:
        vars.character = vars.characters[1]

        print("You are " + vars.character + emojize(":hammer:")) 

        myImage = Image.open("thor.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 260:
        vars.character = vars.characters[2]

        print("You are " + vars.character + emojize(":fist:"))
        myImage = Image.open("natasha.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 80:
        vars.character = vars.characters[3]

        print("You are " + vars.character + emojize(":muscle:"))
        myImage = Image.open("steve.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 60:
        vars.character = vars.characters[4]

        print("You are " + vars.character + emojize(":battery:"))
        myImage = Image.open("tony.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 100:
        vars.character = vars.characters[5]

        print("You are " + vars.character + emojize(":eyes:"))
        myImage = Image.open("clint.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    else:
        print("You are not an avenger from the 2012 Avengers movie")