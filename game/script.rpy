

define luna = Character("Luna", color="#ffcc00")
define kai = Character("Kai", color="#99ff99")
define dstella = Character("Dra. Stella", color="#66ccff")
define you = Character("You")
define Everyone = Character("Everyone")



label start:
    $ quick_menu = False
    default player_points = 0

    scene bg_busonroad with vpunch

    play music "bgm_busloop.flac" volume 0.3 loop
    
    "Your friends Luna, Kai, and you are on the school bus heading to the Space Observatory. Excited, you are all looking out the window."
    
    stop music

    jump act1

