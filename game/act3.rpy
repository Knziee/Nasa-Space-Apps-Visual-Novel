# Definição dos personagens
# define luna = Character("Luna", color="#ffcc00")
# define kai = Character("Kai", color="#99ff99")
# define dstella = Character("Dra. Stella", color="#66ccff")
# define you = Character("You")
# define everyone = Character("Everyone")

# Ato 3: Back to Earth

label act3:

    scene bg_telescope with fade
    "At the top of the observatory, everyone watches a solar storm hitting Earth. Bright auroras light up the sky."

    # Interação do jogador
    "Choose a location on the map to see the auroras."
    #menu:
        #"North America":

        #"Europe":

        #"South America":

        #"Asia":

        #"Oceania":

    show luna happy at left with dissolve
    luna "Look at the lights in the sky! They're the auroras!!"
    hide luna

    show kai happy at right with dissolve
    kai "They're so beautiful!"
    hide kai

    show stella happy at center with dissolve
    dstella "So, what did you learn today?"
    hide stella

    # Interação do jogador
    # menu:
    #     "The Sun is important to our solar system, but sometimes it can cause problems."

    #     "We all need to know a bit about the Sun, how it works, its interactions with our planet, how it affects us, and how important it is to our solar system."

    show luna portrait medio at left with dissolve
    luna "I really enjoyed learning about the Sun and seeing the auroras today!"
    hide luna

    show kai portrait medio at right with dissolve
    kai "The Sun is very powerful, and we need to understand how it works to protect ourselves."
    hide kai

    show stella excited medio at center with dissolve
    dstella "Exactly! With knowledge and cooperation, we can face any challenge."
    show stella portrait medio at center with dissolve
    dstella "Congratulations, kids!"
    hide stella

    # Uma cena de encerramento???
    # Creditos com cenas dos personagens, incluir o lance do yt la, a doc fazendo algo aleatorio, inventar um encerramento inspirador pra cada um?

    return