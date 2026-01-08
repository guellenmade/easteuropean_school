# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("David") # Is the Main character, will be changed to [d]
define c = Character("Cat-Therian") # Will be changed to luna
define a = Character("Placeholdergirl1") #change
define b = Character("Placeholdergirl2") #change
define e = Character("Placeholdergirl3") #change



define a_like = int(0)
define b_like = int(0)
define c_like = int(0)
define e_like = int(0)
# The game starts here.
define homeland = False



#{i}text{/i} macht text kursiv
# wenn d = "sigma"
# "Hallo [d]" == Hallo sigma
label start:
    python:
        d = Character(renpy.input(prompt="Whats your name?", length=41, copypaste=True).lower().title()) 
    
    
    
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
                d "{i}Why should i even Apologize? She is so arrogant.{/i}"
    jump classroom

label classroom:
    
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
                python:
                    c_like -= 2
                c "aww come on."
                menu:
                    "Ok, because it's you.":
                        d "Ok, because it's you."
                        c "Yay thank you"
                        jump classroom_luna
                    "I said no.":
                        d "I said no."
                        c "Okay sorry"
                        #block of code to run
                    
    "I sit at that one empty Table."
    d "I really need to find some friends. Im gonna join a club later that day."
    jump noluna_school_ending
            

label classroom_luna:
    "So i sit next to her."
    python:
        c_like += 5 # A maximum of 13 "LunaPoints" are possible rn
    c "And? From where do you come?"
    d "I come from:"
    menu:
        "I come from...":
            python:
                c_like += 3 # A maximum of 16 "LunaPoints" are possible rn
                #block of code to run
                homeland = Character(renpy.input(prompt="Whats your Homeland??", length=41, copypaste=True).lower().title())
            d "I come from [homeland]"

            c "Yooo cool. I was in [homeland] for a week and it's pretty cool."
            d "For Real?"
            c "Yes. I really liked it there."
        "I don't wanna answer that.":
            d "I don't wanna answer that."
            c "Aww come on."
            python:
                c_like -= 1
            #block of code to run
    
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
    c "I know you will."

    #later
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
    d "I need to join a Club now. \nBut which one?\nWait i have a list."
    "i get out a list from my backpack."
    d "{i}Poem-Writing, Gaming, IT, Dancing, Tiktok???\n What the fuck does Tiktok even mean? Are they Dancing or what?\nAnyways... Gym, Backing, Cooking...{/i}"
    d "{b}Backing?{/b}"
    "I Love baking I should really join this club."
    # later
    d "{i}Backing Club.{/i}"
    "I knock the door and enter in."
    c "Oh Hi [d]"
    d "Oh you are here too?"

label clubjoin:
    c "Anyways, i go and get the others.\n{b}HEEEEY [a] [b] [e] We may have a new Member!{/b}"
    
    "I gasp as i see 3 Beautiful Girls coming and stop next to [c]"
    d "Hi... Hi i am [d]"
    a "Oh nice to meet you [d].\nWhy did you wanna join the Backing Club?"
    b "I'm sure he's just a Socially akward Reddit Mod that wants some Female contact."
    e "Shut up [b] we don't even know him yet."
    b "True but i still wanna keep an eye on him."
    "It seems like [b] is a little bit aggressive towards me."
    menu:
        "Do you have a bad past with Reddit mods?":
            #block of code to run
        "Shut up nobody cares":
            $e_like -= 1
            $a_like -= 1
            $b_like -= 3
            $c_like -= 1


        "Say nothing":
            #block of code to run
            d "..."
        






return