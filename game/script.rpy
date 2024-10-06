# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define luna = Character("Luna", color="#ffcc00")
define kai = Character("Kai", color="#99ff99")
define dstella = Character("Dra. Stella", color="#66ccff")
define you = Character("You")
define everyone = Character("Everyone")


# oi
# The game starts here.

# labeluna start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This endstellathe game.

#     return

# Roteiro de cena
label start:

    scene bg_busonroad with vpunch
    play music "bus_ride.ogg"
    
    # $ tremor_active = True

    # while tremor_active:
    #     # Aplica o tremor
    #     scene bg_busonroad with vpunch
    #     pause(0.1)  # Ajuste o tempo de pausa conforme necessário
    #     scene bg_busonroad
    #     pause(0.1)

    "Your friends Luna, Kai, and you are on the school bus heading to the Space Observatory. Excited, you are all looking out the window."

    jump act1

