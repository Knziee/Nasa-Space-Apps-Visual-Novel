image bg_creditsvideo = Movie(play="images/credits.webm")

label act3:

    scene bg_newaurora with fade
    "Outside the observatory, everyone watches a solar storm hitting Earth. Bright auroras light up the sky."

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
    menu:

        "The Sun is important to our solar system, but sometimes it can cause problems.":
            show stella excited medio at center with dissolve
            dstella "That's right!"
            hide stella

        "We all need to know a bit about the Sun, how it works, its interactions with our planet, how it affects us, and how important it is to our solar system.":
            show stella excited medio at center with dissolve
            dstella "Wow! You’ve really thought about this!"
            hide stella

        "I'm not sure.":
            show stella portrait medio at center with dissolve
            dstella "What would you like to explore again?"

            menu:
                "The first explanation about solar storms":
                    jump alert_screen

                "The simulation":
                    jump act2

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


    scene bg_blackscreen with fade

    "..."

    scene bg_newaurora with vpunch
    
    show stella excited medio at center with vpunch
    dstella "Oh, I almost forgot! "
    show stella excited close at center with dissolve
    dstella "Would you like to know how much you learned today?"

    menu:

        "Yes!":
            jump points_reveal
            hide stella
        "No!":
            jump credits
            hide stella

label points_reveal:

    show stella portrait at center with dissolve
    dstella "I'd say ..."
    hide stella

    if player_points >= 30:
        show stella excited close at center with vpunch
        play sound "bgm_congratulations.wav"

        dstella "A lot! Amazing job! You really understood everything about the Sun and its storms!"
    elif player_points >= 10:
        show stella pointing at center with dissolve
        dstella "Most of it! Great work! You learned a lot, but there's still more to explore next time!"
    else:
        show stella thinking at center with dissolve
        dstella "Hmm, it seems you missed some information. Don't hesitate to ask more next time!"


    hide stella

label credits:
    play movie "images/credits.webm"
    pause(30.0)
    # show stella excited close at center with vpunch
    # dstella "Bye!"


    return