image alert = Movie(play="images/bg_animatedalertconverted.webm")

label act1:
    play music "bgm_busloop.flac" volume 0.1 loop 

    scene bg_innerbuszoom with fade

    show luna excited at left with dissolve
        # yalign 4.5 #medium cut
        # zoom 1.5
        # yalign 2
        # xalign 0.5
        # yalign 8.5 #medium cut

        
    luna "I can't wait to see the stars up close!"

    hide luna
    show luna portrait at left with dissolve:
        xzoom -1.0
    
    "Luna is 9 years old and very curious. She loves space and has always wanted to be an astronaut."
    hide luna
    show kai excited at right with dissolve:
        xzoom -1.0
    kai "And I want to see the giant telescopes! Maybe we can even build a model later."

    hide kai
    show kai portrait at right with dissolve
    
    "Kai is 8 years old and passionate about technology. He loves building robots and inventing things. His dream is to create a spaceship one day."
    hide kai

    show kai thinking at right with dissolve

    kai "What about you? What do you want to learn today?"
    hide kai

    # Interação com o jogador
    menu:
        "I want to see the Sun up close!":
            show luna happy at left with dissolve
            luna "Me too! I wonder what the Sun looks like up close"
            hide luna
        "I really want to observe the solar system!":
            show kai happy at right with dissolve:
                xzoom -1.0
            kai "You're right! Planets are so interesting!"
            hide kai

    stop music
    # Chegada ao Observatório
    scene bg_newauroraclean with fade

    "The bus arrives at the Observatory. You and your friends get off and are greeted by Dr. Stella"
    

    scene bg_observatoryinterior with fade

    show stella greeting at center with dissolve
    dstella "Welcome to the Space Observatory!"
    show stella excited medio at center with dissolve
    dstella "Today, we’re going to explore the mysteries of the Sun."
    hide stella

    show stella portrait at center with dissolve
    "Stella is an astrophysicist passionate about the Sun. She has a gift for explaining complex topics in a simple and fun way, always with a smile on her face."
    hide stella

    scene bg_observatoryscreens with dissolve
    "Large screens around the observatory display cool pictures of space and special tools that watch how the Sun and planets move."

    show stella happy at center with dissolve
    dstella "The Sun is the closest star to us, providing light and heat, and it’s very important for life on Earth."

    # Interação com o jogador
    menu:
        "What is a star?":
            $ player_points += 10
            show stella pointing at center with dissolve
            dstella "A star is a giant ball made of gas that shines and releases heat because it has a little 'fire' inside that releases energy."
            hide stella
        "I don't want to learn about stars.":
            show stella thinking at center with dissolve
            dstella "Oh, that's too bad! I bet you'd love to know more about that."
            hide stella
            jump alert_screen  # Pular diretamente para a tela de alerta

    show luna surprised at left with dissolve
    luna "Wow, incredible!"
    hide luna excited
    
label alert_screen:  # Etiqueta para a parte do alerta

    play music "bgm_alarm.flac" loop

    scene alert with dissolve
    "Suddenly, an alert appears on one of the screens. Lights begin to flash."

    show kai surprised at right with dissolve
    kai "What's happening?"
    hide kai

    stop music
    scene bg_observatoryscreens with dissolve
    show stella thinking at center with dissolve
    dstella "Hmm."
    show stella action at center with dissolve
    dstella "It seems the Sun is very active today."
    hide stella

    show luna thinking at left with dissolve
    luna "What does that mean?"
    hide luna

    show stella excited medio at center with dissolve
    dstella "It means we might be about to witness a solar storm!"

    # Interação com o jogador
    menu:
        "What is a solar storm?":
            $ player_points += 10

            show stella excited close at center with dissolve
            dstella "I'm glad you asked!!"

            show stella portrait medio at center with dissolve
            dstella "They are events that happen on the Sun and can affect the entire solar system."
            hide stella
        "...":
            show stella thinking at center with dissolve
            dstella "I bet you'd love to know more about that."
            hide stella
            jump simulation_call  # Pular diretamente para a tela de alerta


    show kai excited at right with dissolve:
        xzoom -1.0
    kai "Wow, that's cool!"
    hide kai

label simulation_call:
    show luna happy at left with dissolve
    luna "Can you show us??"
    hide luna

    show stella portrait medio at center with dissolve
    dstella "Of course, we can see it on the Observatory's screens. How about an adventure?"

    show stella excited medio at center with dissolve
    dstella "We have a spaceship simulator here. Want to see the Sun up close?"
    hide stella

    show kai excited at right with dissolve
    show luna excited at left with dissolve
    Everyone "Yes!"

    


    jump act2

