from components import vars
from PIL import Image

def total(value):
    # do some logic to see which character you selected

    if value == 40:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
       
        myImage = Image.open("bruce.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 130:
        vars.character = vars.characters[1]

        print("It's " + vars.character)

        myImage = Image.open("thor.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 260:
        vars.character = vars.characters[2]

        print("It's " + vars.character)
        myImage = Image.open("natasha.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 80:
        vars.character = vars.characters[3]

        print("It's " + vars.character)
        myImage = Image.open("steve.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 60:
        vars.character = vars.characters[4]

        print("It's " + vars.character)
        myImage = Image.open("tony.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    elif value == 100:
        vars.character = vars.characters[5]

        print("It's " + vars.character)
        myImage = Image.open("clint.jpg")
        myImage.show()
        # add some emoji icons, or show the character image using the Pillow package

    else:
        print("You are not an avenger from the 2012 Avengers movie")