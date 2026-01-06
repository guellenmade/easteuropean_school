# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("David")
define c = Character("Cat-Therian") # Will be changed to luna
define c_like = int(0)
# The game starts here.


# wenn d = "sigma"
# "Hallo [d]" == Hallo sigma
label start:
    python:
        d = Character(renpy.input(prompt="Whats your name?", length=41, copypaste=True).lower().title())

    "Alarm clock" "Beep, Beep, Beep"
    d "Shut up"
    "I turn of the alarm and get ready for School"
    "Todays my first day."
    "I dress up and go down to the kitchen"
    d "Why are my Parents always working?"
    "I take my backpack and get out the House."

label school_place:
    "I walked to my new School."
    "I see a Girl walking in front of me. But..."
    d "SHE HAS CAT EARS???"
    "Okay maybe she is a Therian or so?"

    "The girl trips over a stone."
    c "Ouch, Fuck this shit. FUCK!"

    menu whattosay:
        "What should i say?"
        "Hey are you alright?":
            d "Hey are you alright?"
            c "Yea it's all good. Thanks."
            python:
                c_like += 5
        "Are you alright? Can i help you?":
            d "Are you alright? Can i help you?"
            c "No i am fine but thanks for asking."
            python:
                c_like += 8
        "You look good.":
            d "You look good."
            c "Fuck you, i fall and the only thing you think about is: \"Oh she looks fucking hot, im gonna say that now\""
            d "No i Just wanted to say something nice."
            c "Just stop flirting okay?"
            python:
                c_like -= 5
    c "Whats your name tho?"
    d "My name is [d] and yours?"
    
    if c_like < 0:
        c "Ah you are in my class... cool i guess"
        d "Okay, but where is our classroom?"
        c "I will show it to you, i guess."
        d "Thanks"

    if c_like > 7:
        c "Wait you are [d]??? Your in my class! We can sit together if you want."
        d "Yea we can... But where is our classroom?"
        c "I will lead you."
        d "Yes please"
    if c_like > 0 and c_like < 6:
        c "Wait you are [d]?"
        d "Yes"
        c "We are in the same class."
        c "i can lead you to our classroom if you want."
        d "Yes that would be nice."
    c "Okay, then follow me"
    d "What is your name now?"
    c "My name is Luna"
    python:
        c = Character("Luna")
    d "Nice to meet you, [c]."
    if c_like < 0:
        menu:
            "Apologize":
                d "Hey, i wanna say... I am really Sorry what happened before. Can you forgive me?"
                c "Yea it is alright. I overreacted a lot to be honest."
                python:
                    c_like = 2

            "Don't Apologize":
                pass
    jump classroom

label classroom:
