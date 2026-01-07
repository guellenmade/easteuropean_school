# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True

define _scene_show_hide_transition = Dissolve(0.25)


define d = Character("David") # Is the Main character, will be changed to [d]
define c = Character("Cat-Therian", color="#ff1493") # Will be changed to luna
define a = Character("") #change
define b = Character("") #change
define e = Character("") #change
define c_like = int(0)
# The game starts here.
define homeland = False



#{i}text{/i} macht text kursiv
# wenn d = "sigma"
# "Hallo [d]" == Hallo sigma
label start:
    python:
        d = Character(renpy.input(prompt="Whats your name?", length=41, copypaste=True).lower().title(), color="#ffffff")
    
    
    
    "Alarm clock" "{i}Beep, Beep, Beep{/i}"
    d "Shut up"
    "I turn of the alarm and get ready for School"
    "Today is my first day."
    "I dress up and go down to the kitchen"
    d "{i}Why are my Parents always working?{/i}"
    "I take my backpack and get out the House."

label school_place:
    "I walked to my new School."
    "I see a Girl walking in front of me. But..."
    d "{i}SHE HAS CAT EARS???{/i}"
    d "{i}Okay maybe she is a Therian or so?{/i}"

    "The girl trips over a stone."
    c "Ouch, Fuck this shit. FUCK!"

    menu whattosay:
        "What should i say?"
        "Hey are you alright?":
            d "Hey are you alright?"
            c "Yea it's all good. Thanks."
            $c_like += 5
        "Are you alright? Can i help you?":
            d "Are you alright? Can i help you?"
            c "No i am fine but thanks for asking."
            $c_like += 8
        "You look good.":
            d "You look good."
            c "Fuck you, i fall and the only thing you think about is: \"Oh she looks fucking hot, im gonna say that now\""
            d "No i Just wanted to say something nice."
            c "Just stop flirting okay?"

            $c_like -= 5
    c "Whats your name tho?"
    d "My name is [d] and yours?"
    
    if c_like < 0:
        c "Ah you are in my class... {i}fuck{/i} i mean cool i guess"
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
        c = Character("Luna", color="#ff1493")
    d "Nice to meet you, [c]."
    if c_like < 0:
        menu:
            "Apologize":
                d "Hey, i wanna say... I am really Sorry what happened before. Can you forgive me?"
                c "Yea it is alright. I overreacted a lot to be honest."
                $c_like = 2

            "Don't Apologize":
                d "{i}Why should i even Apologize? She is so arrogant.{/i}"
    jump classroom

label classroom:
    pause 3
    "We stand in front of a room"
    c "This is our classroom [d]"
    d "Oh, thank you [c]."
    c "No problem"
    "I go into the classroom and greet the teacher."
    if c_like > 7:
        c "Here please sit next to me."
        menu:
            "Yes, Sure":
                d "Yes, Sure"
                jump classroom_luna
                
            "No":
                d "No thanks."

                $c_like -= 2
                c "aww come on."
                menu:
                    "Ok, because it's you.":
                        d "Ok, because it's you."
                        c "Yay thank you"
                        jump classroom_luna
                        $c_like += 1
                    "I said no.":
                        d "I said no."
                        c "Okay sorry"
                        #block of code to run
    pause 2.0                
    "I sit at that one empty Table."
    d "I really need to find some friends. Im gonna join a club later that day."
    jump noluna_school_ending
            

label classroom_luna:
    "So i sit next to her."
    $c_like += 5 # A maximum of 13 "LunaPoints" are possible rn
    c "And? From where do you come?"
    menu:
        "I come from...":
            $c_like += 3 # A maximum of 16 "LunaPoints" are possible rn
            
            #block of code to run
            
            $homeland = Character(renpy.input(prompt="Whats your Homeland??", length=41, copypaste=True).lower().title())
            d "I come from [homeland]"

            c "Yooo cool. I was in [homeland] for a week and it's pretty cool."
            d "For Real?"
            c "Yes. I really liked it there."
        "I don't wanna answer that.":
            d "I don't wanna answer that."
            c "Aww come on."
            $c_like -= 1
            #block of code to run


    pause 4.0
    c "Hey i have a nice idea"
    c "Aehm"
    d "What is it [c]?"
    c "You could... Join a Club."
    d "A club?"
    c "Yea there are a lot of Clubs in this School. There is an Anime-Club, an IT-club full of Nerds and a lot more"
    d "IT sounds nice..."
    c "Or there is a \"Backing\" Club. I am there too. So i wanted to ask you, if you could join it."
    d "Backing Club?"
    c "Yes... Aehm... Please join."
    d "Okay i will look into it..."
    c "Okay.. I will See you then."
    d "HEY! I never said i'll join."
    "[c] Smiles"
    pause 1.0
    c "I know you will."

    #later
    pause 3.0
    "I am standing in front of the Backing Club."
    d "{i}So this is the Backing Club that Luna told me about...{/i}"
    "I open the door and Step in."
    c "HIII [d]!!! I knew you wouldn't leave me alone."
    d "How would you know that? We only know each other for two hours or so."
    c "You know... You give me that \"Chill nice guy\" Vibe."
    "I smile"
    d "{i}I think she likes me... Will i get my first Girlfriend... In this school?{/i}"
    jump clubjoin


label noluna_school_ending:
    "The bell rings."
    d "Wow finally over." 
    d "{i}I need to join a Club now. \nBut which one?\nWait i have a list.{/i}"
    "i get out a list from my backpack."
    d "{i}Poem-Writing, Gaming, IT, Dancing, Tiktok???\n What the fuck does Tiktok even mean? Are they Dancing or what?\nAnyways... Gym, Backing, Cooking...{/i}"
    d "{b}Backing?{/b}"
    d "{i}I Love baking I should really join this club.{/i}"
    # later
    d "{i}Backing Club.{/i}"
    "I knock the door and enter in."
    c "Oh Hi [d]"
    d "Oh you are here too?"

label clubjoin:
    c "Anyways, i go and get the others.\n{b}HEEEEY [a] [b] [e] We may have a new Member!{/b}"






return