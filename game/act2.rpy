
image bg_zoomvideo = Movie(play="images/bg_sunrotatingfullhd.webm")
image bg_windowvideo = Movie(play="images/bg_sunRotatingFromwindow.webm")

label act2:

    scene bg_spaceship2 with fade
    "You are in the hangar with the simulator spaceship. The ship is ready for take-off."

    play music "bgm_rocketloop.wav" volume 1.0 loop

    scene bg_spaceship with vpunch
    "You feel almost like you're in a real spaceship."
    stop music

    play music "bgm_alarm.flac" loop
    scene bg_blackscreen with fade
    "..."


    scene bg_insidesimulationalert with fade

    show stella pointing at center with dissolve
    dstella "Do you hear that alarm again? It indicates that a solar storm is happening!"
    play music "bgm_simulation.mp3" volume 0.25 loop
    show stella excited medio at center with dissolve
    dstella "It's simulating the storms between May 7th and May 11th, 2024."
    show stella thinking at center with dissolve
    dstella "On that day, we experienced a very intense storm, much stronger than in many other years."
    hide stella

    scene bg_windowvideo with fade
    "You are witnessing the intense activity on the surface of the Sun."
    "You see surprised faces around you."


    show stella excited medio at right with dissolve
    dstella " Look, kids. That’s a solar flare."
    hide stella


    show stella thinking at right with dissolve
    dstella "It's like the Sun is releasing a big burst of light, which can affect Earth!"
    hide stella

    show kai surprised at right with dissolve
    kai "What happens if a storm hits Earth?"
    hide kai

    show stella portrait medio at right with dissolve
    dstella "Depending on how strong the storm is, the impacts will be different."
    show stella action at right with dissolve
    dstella "We can discover more together!"
    hide stella

    scene bg_zoomvideo with fade

    stop music
    "Everyone takes a good look at the bursts of light from the sun, marveling at the vibrant display of solar energy illuminating the sky."
    "..."
    window hide  
    pause(10.0)

    show luna excited at left with dissolve
    luna "Wow! It's huge!"
    hide luna

    show kai thinking at right with dissolve
    kai "What are those giant bubbles?"
    hide kai

    show stella thinking at right with dissolve
    dstella "They are like fireballs that the Sun throws into space."    
    show stella excited medio at right with dissolve
    dstella "They travel through the solar system and take a few days to reach Earth because they are full of little pieces of material from the Sun."
    show stella excited close at right with dissolve
    dstella "When these fireballs reach Earth, that's when our magnetic field kicks in!"
    hide stella

    # Interação com o jogador
    menu:
        "Magnetic field?":
            $ player_points += 10

            show stella excited close at center with dissolve
            dstella "Yess! The magnetic field!!"

            show stella portrait medio at center with dissolve
            dstella "Well, Earth’s magnetic field is like an invisible shield that surrounds the whole planet."
            hide stella

            scene bg_magneticfield with fade
            
            dstella "It helps protect us from those little pieces from the Sun."
            window hide
            pause(4.0)

            scene bg_magneticfieldumbrella with fade
            dstella "It’s almost like a magic umbrella that keeps Earth safe!"

            scene bg_aurora with fade
        
            dstella "And this interaction between the Sun’s particles and Earth's shield can create the Northern Lights, colorful lights that appear in the sky, especially near the poles."

        "...":
            show stella thinking at center with dissolve
            dstella "I bet you'd love to know more about that."
            hide stella
            jump storm_effects  # Pular diretamente para a tela de alerta

label storm_effects:
    scene bg_nointernetwithkai with fade
    dstella "Storms of this level can affect satellites, cause power outages, and disrupt TV and internet transmissions."

    scene bg_insidesimulation with fade

    show kai surprised at right with dissolve
    kai "Wow! This is serious!"
    hide kai

    show luna excited at left with dissolve
    luna "Now we understand how solar storms can affect Earth. That’s so cool!"
    hide luna

    jump act3
