# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define luna = Character("Luna", color="#ffcc00")
# define kai = Character("Kai", color="#99ff99")
# define dstella = Character("Dra. Stella", color="#66ccff")
# define you = Character("You")
# define everyone = Character("Everyone")


# # oi
# # The game starts here.

# # labeluna start:

# #     # Show a background. This uses a placeholder by default, but you can
# #     # add a file (named either "bg room.png" or "bg room.jpg") to the
# #     # images directory to show it.

# #     scene bg room

# #     # This shows a character sprite. A placeholder is used, but you can
# #     # replace it by adding a file named "eileen happy.png" to the images
# #     # directory.

# #     show eileen happy

# #     # These display lines of dialogue.

# #     e "You've created a new Ren'Py game."

# #     e "Once you add a story, pictures, and music, you can release it to the world!"

# #     # This endstellathe game.

# #     return

# # Roteiro de cena
# label start:

#     scene bg_busonroad with vpunch
#     play music "bus_ride.ogg"
    
#     # $ tremor_active = True

#     # while tremor_active:
#     #     # Aplica o tremor
#     #     scene bg_busonroad with vpunch
#     #     pause(0.1)  # Ajuste o tempo de pausa conforme necessário
#     #     scene bg_busonroad
#     #     pause(0.1)

#     "Your friends Luna, Kai, and you are on the school bus heading to the Space Observatory. Excited, you are all looking out the window."

#     scene bg_innerbuszoom with fade

#     show luna excited at left with dissolve
#         # yalign 4.5 #medium cut
#         # zoom 1.5
#         # yalign 2
#         # xalign 0.5
#         # yalign 8.5 #medium cut

        
#     luna "I can't wait to see the stars up close!"

#     hide luna
#     show luna portrait at left with dissolve
    
#     "Luna is 9 years old and very curious. She loves space and has always wanted to be an astronaut."
#     hide luna
#     show kai excited at right with dissolve
#     kai "And I want to see the giant telescopes! Maybe we can even build a model later."

#     hide kai
#     show kai portrait at right with dissolve
    
#     "Kai is 8 years old and passionate about technology. He loves building robots and inventing things. His dream is to create a spaceship one day."
#     hide kai

#     show kai thinking at right with dissolve

#     kai "What about you? What do you want to learn today?"
#     hide kai
    
#     # Interação com o jogador
#     menu:
#         "I want to see the Sun up close!":
#             show luna happy at left with dissolve
#             luna "Me too! I wonder what the Sun looks like up close"
#             hide luna
#         "I really want to observe the solar system!":
#             show kai happy at right with dissolve
#             kai "You're right! Planets are so interesting!"
#             hide kai

#     # Chegada ao Observatório
#     scene bg_observatorylongview with fade
#     play sound "bus_stop.ogg"

#     "The bus arrives at the Observatory. The children get off and are greeted by Dr. Stella."

#     scene bg_observatoryinterior with fade

#     show stella greeting at center with dissolve
#     dstella "Welcome to the Space Observatory!"
#     dstella "Today, we’re going to explore the mysteries of the Sun."
#     hide stella

#     "Stella is an astrophysicist passionate about the Sun. She has a gift for explaining complex topics in a simple and fun way, always with a smile on her face."

#     scene bg_observatoryscreens with dissolve

#     "Large screens around the observatory display images of space and magnetic monitoring."

#     show stella happy at center with dissolve
#     dstella "The Sun is the closest star to us, providing light and heat, and it’s very important for life on Earth."

#     # Interação com o jogador
#     menu:
#         "What is a star?":
#             dstella "A star is a giant ball made of gas that shines and releases heat because it has a little 'fire' inside that releases energy."
#             hide stella
    
#     you "Wow, incredible!"

#     "Suddenly, an alert appears on one of the screens. Lights begin to flash."

#     show kai surprised at right with dissolve
#     kai "What's happening?"
#     hide kai

#     show stella thinking at center with dissolve
#     dstella "Hmm."
#     dstella "It seems the Sun is very active today."
#     hide stella

#     show luna thinking at left with dissolve
#     luna "What does that mean?"
#     hide luna

#     show stella happy at center with dissolve
#     dstella "It means we might be about to witness a solar storm!"

#     # Interação com o jogador
#     menu:
#         "What is a solar storm?":
#             dstella "I'm glad you asked!!"
#             show stella excited at center with dissolve
#             dstella "They are events that happen on the Sun and can affect the entire solar system."
#             hide stella

#     you "Wow, that's cool!"

#     show luna happy at left with dissolve
#     luna "Can you show us??"
#     hide luna

#     show stella happy at center with dissolve
#     dstella "Of course, we can see it on the Observatory's screens. How about an adventure?"
#     dstella "We have a spaceship simulator here. Want to see the Sun up close?"
#     hide stella

#     everyone "Yes!"

#     # Fim da cena
#     return
