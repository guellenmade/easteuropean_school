# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True

define _scene_show_hide_transition = Dissolve(0.25)


define d = Character("David") # Is the Main character, will be changed to Whatever the user says
define c = Character("Girl") # Will be changed to luna
define a = Character("Lukaš") #change
define b = Character("Aishah") #change
define e = Character("Camila") #change



define a_like = int(0)
define b_like = int(0)
define c_like = int(0)
define e_like = int(0)
define is_homophobe = False
define homeland = False

# The game starts here.



#{i}text{/i} macht text kursiv
# wenn d = "sigma"
# "Hallo [d]" == Hallo sigma
label start:
    scene bg start
    python:
        d = Character(renpy.input(prompt="Whats your name?", length=41, copypaste=True, default="Давид").lower().title()) 

    scene bg home room

    "Alarm clock" "{i}Beep, Beep, Beep{/i}"
    d "Shut up"
    "I turn of the alarm and get ready for School"
    "Today is my first day."
    "I dress up and go down to the kitchen."
    scene bg home kitchen
    d "{i}Why are my Parents always working?{/i}"
    "I make myself a nice piece of bread with some strawberry jam."
    d "This shit is so delicious."
    "I take my backpack and get out the House."

label school_place:
    scene bg street
    "I start walking to my new School."
    pause 1.5
    scene bg school front
    pause 0.5
    "I see a Girl running in front of me."
    "But why is she running?"

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
            c "Fuck you, i just fell and the only thing you think about is: \"Oh she looks fucking hot, im gonna say that now\""
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
    "I think she likes me... Will i get my first Girlfriend... In this school?"
    "Okay maybe she is just a kind Person"
    jump clubjoin


label noluna_school_ending:
    "The bell rings."
    d "Wow finally over." 
    "I need to join a Club now."
    "But which one?"
    "Wait i have a list."
    "i get out a list from my backpack."
    "Poem-Writing, Gaming, IT, Dancing, Tiktok???\nWhat the fuck does Tiktok even mean? Are they Dancing or what?\nAnyways... Gym, Backing, Cooking..."
    d "{b}Backing?{/b}"
    "I Love baking... so i should really join this club."
    # later
    d "{i}Backing Club.{/i}"
    "I knock the door and enter in."
    c "Oh Hi [d]"
    d "Oh you are here too?"

label clubjoin:
    c "Anyways, i go and get the others.\n{b}HEEEEY [a] [b] [e] We may have a new Member!{/b}"
    
    "I gasp as i see 3 Beautiful Girls coming and stop next to [c]"
    d "Hi... Hi i am [d]"
    a "Oh nice to meet you [d].\nI am [a].\nWhy did you wanna join the Backing Club?"
    b "I'm sure he's just a Socially akward Reddit Mod that wants some Female contact."
    e "Shut up [b] we don't even know him yet."
    b "True but i still wanna keep an eye on him."
    "It seems like [b] is a little bit aggressive towards me."
    menu:
        "Do you have a bad past with Reddit mods?":
            d "Do you have a bad past with Reddit mods?"
            #block of code to run
            b "Yes... I mean no...\nFuck it. I just {b}know{/b} it."
            d "Yes sure..."
            "I'm smiling because she has no arguments."
            b "I swear i beat you up if you laugh one more time like that!"
            $ b_like -= 2
        "Shut up not every man is like that.":
            d "Shut up not every man is like that."
            b "In my opinion they are"
            d "And how do you know that?"
            b "Aehm... \nI have my sources"
            $ b_like -= 3

        "Say nothing":
            #block of code to run
            d "..."
            b "Oh so i am right???"
            d "No,  i just don't want to start an argument with you."
            c "Sorry [d].\n[e] is always a bit aggressive towards new people."
            b "Shut up"
            d "I'ts allright. Im gonna show her that i am a cool guy."
            "i Smile"

    b "Okay you can stay... for now.\nAnd before i forget: I am [b], {b}not{/b} nice to meet you."
    e "And i am [e], {b}nice{/b} to meet you."
    a "Like i said: I am [a], and {b}very very nice{/b} to meet you~"
    b "Why are you guys always that kind?"
    d "I think your just a bit overreacting."
    a "Me too.\nYou are always sooooo Agressive towards men."
    b "Shut up you small ass Femboy."

    "Suddenly [a] blushes very hard. And runs to the Kitchen."
    d "What just happened?"
    "[c] and [d] went silent and are now staring at [b]"
    menu:
        "Look for [a]":
            jump lookforLukas
        "Do Nothing":
            jump nothingdoer

        "Talk with [c]" if c_like > 10:
            #block of code to run
            jump talkwithluna



label lookforLukas:
    "I run into the kitchen."
    d "[a]? LUKAAAŠ!!!"
    a "Wha... What?"
    "I walk next to the kitchen and see [a] crying in the corner."
    d "Are... you okay?"
    a "Yes... i am alright."
    "Seeing [a] cry kinda makes me sad too.\nSo i decide to sit next to to her."
    a "Aaah... Hi~"
    d "I clearly see that you are {b}NOT{/b} okay."
    a "Okay... can i trust you?"
    "I nod"
    d "I... You can trust me."
    "I see a smile in her face."
    a "Do you see something... thats different about me?\nLike... my voice?"
    d "No"
    a "My look?"
    d "No\nWhat do you wanna say?"
    a "I am... Nnngh...\nI am a femboy."
    d "Wha WHAT?"
    "Thats why {b}she{/b} is named [a]"
    a "Oh... You hate me now right?"
    menu:
        "I don't really like LGBTQ+ but i don't hate you because of that.":
            $a_like += 5
            #block usw
            d "I have to say, that i don't really like the LGBTQ+ Community but i don't hate you because of that."
            a "Thanks.\nThat sounds really nice from you."
            d "It's just... i don't like the idea of being Trans or Gay.\nBut you do you.\nAnd i don't hate you because you're gay or so."
            a "That... Sounds like a valid compromise."
            d "Yeah."
            "[a] is clearly relieved."
            $ a = Character("Luki")
            a "You can call me [a]"
            d "Okay.\nLets go back to the others."
            a "Okay~"
            jump lukigood

        "I don't care":
            $a_like += 12
            d "I don't care what you are, as long as you are a cool person."
            a "Ohm... Thanks i guess?"
            a "Let's go back to the others... right?"
            d "Okay"
            jump lukigood



        "You are too cute to hate":
            d "You are too cute to hate."
            $a_like += 67 # Maximum of 67 points 
            a "Wha... What?"
            "[a] is really red right now"
            d "Yes i am real right now."
            a "Sto...Stop it."
            d "Your red cheeks make you even cuter."
            a "..."
            d "And i can't hate you, as long as you keep looking at me like that.\nNo matter what you are or what you will do..."
            a "Nnngh..."
            d "And you did a very good Job.\nYou are the cutest \"Woman\" that ever existed."
            a "Ahhh..."
            "I've never seen such a cute guy... \nI really wanna kiss him right now..."
            d "Is everything okay?"
            a "I... We..."
            "He is so cute."
            a "Thanks for the compliments."
            "[a] Runs out of the Kitchen"
            pause 2.5
            c "[d]!!!"
            d "Wha...What?"
            "I also run towards the main room."
            d "What happened?"
            c "[a] ran out of the kitchen and i wanna ask you why.\nWhat have you done???"
            d "I... I just complimented him."
            c "You know... It doesn't look like this."
            "She's right.\nIt really doesn't look like that."
            d "Yes but...\nPlease believe me."
            "[c] looks like she's thinking about executing me."
            d "I did nothing wrong... Believe me."
            c "Okay. I will ask him tomorrow, and if he doesn't defend you... \nYou are in big trouble."
            d "Oh... Okay"
            "I really hope [a] won't be mad on me."
            jump firstday

            #block of code to run





        "Oh my fucking god.\nYou are a such an ugly faggot.":
            $a_like = -10000000
            $is_homophobe = True
            d "Oh my fucking god.\nYou are a such an ugly faggot."
            a "Wha... What?"
            "[a] Starts to cry again."
            d "Yeah go fucking crying you little faggot.\nGo Kill yourself."
            "[a] Is still crying.\nBut that little bitch deserved it."
            "I walk back to the others."
            d "I \"Talked\" to {b}him{/b}."
            jump nothingdoer

        




label talkwithluna:
    d "Hey [c] we need to talk."
    c "N...Now?"
    "[c] is clearly blushing right now."
    d "Yes"
    c "Oh...Okay."
    "We walk outside the room."
    d "Okay... please explain me..."
    c "Oh... okay...\nAs you may have noticed i have cat ears..."
    "I look at her head and..."
    d "HOLY SHIT??? WHY DO YOU HAVE CAT-EARS???"
    c "You didn't notice yet???"
    "I am shoked."
    d "Yes..."
    c "Okay... You're pretty slow."
    d "But why? Aren't cat-girls just a invention of Gooners?"
    c "Oh my god.\nThese aren't real of course."
    c "I am a therian...\nI hope you don't hate me because of that."
    menu:
        "What's that?":
            c "Okay, i try to explain.\nA therian is basically a person that feels connected to an animal.\nFor example i kinda feel like i am a cat."
            c "It's not about acting like a cat, it's about my inner identity.\nAnd i sometimes wanna make cat sounds, even tho i am a \"Girl\"."
            
            d "Oh... a therian?"

        "Oh a therian...":
            d "Oh... a therian."
    
    
    c "Does this mean something bad?"       
    d "No no no... it's all okay."
    c "Thank you.\nYou are one of the calmest person i have ever met."
    c "Anyways... [a] is a femboy.\nHe is gay too."
    d "Okay... i also don't really mind that."
    c "Okay, that's good.\nLet's get back to the others, before they think we are dating or so."
    "Why do i feel like that would unironically be the best thing to happen?"
    d "Sure"
    
    $ c_like += 10 #maximum of 26 "lunapoints"
    jump nothingdoer






label nothingdoer:
    d "It's probably nothing."
    b "Yes, [a] is a typical man."
    c "Please stop it [b]"
    d "I think [a] is overreacting a bit."
    b "Wait your not that big of an asshole. [d]"
    d "Thanks i guess?"

    
    $ b_like += 4 #maximum 4 points for b
    if is_homophobe == True:
        pause 3.2
        "[b] walks towards me"
        b "{i}You...harassed him... right?{/i}"
        d "{i}Yes.{/i}"
        "[b] smiles"
        b "Good Job. You are getting more symphatic every second.~"
        "I kinda have a crush on [b] now."
        d "I loved doing it."
        $ b_like += 12 #maximum of 16 Points for B
    e "Anyways it's already late...\nLet's go home."
    c "You're right."
    b "Bye guys."
    d "Bye"
    jump firstday




label lukigood:
    "So we go back to the others."
    a "Hi guys...\nI am fine"
    c "You didn't seem like it tho."
    d "It's all good.\nI talked with him."
    e "So it is all okay now?"
    a "Yes."
    b "Can we go home now?"
    c "Good idea...\nIt's already 6 o'clock"
    d "Okay...\nBye guys."
    a "Bye~"
    b "Until tomorrow guys."
    jump firstday



label firstday:
    "As i walk home, i try to remember what happened today.\nAnd how i will \"survive\" this club."
    "Those beautiful girls are way too much for me..."
    "[c]"
    "[a]"
    "[b]"
    "[e]"
    "This is so unfair."
    "{b}WHY AM I THAT UGLY?!?{/b}"
    d "I hate my life"
    scene black
    with dissolve
    pause 1.0
    scene bg room
    "I wake up again."
    "I dress up and go down to the kitchen."
    scene bg home kitchen
    "I make myself a nice piece of bread with some strawberry jam."
    d "This shit is so delicious."
    "I take my backpack and get out the House."
    "Wait... Why does this feel like a Déjà-vu?"
    scene bg street
    "I start walking to School."
    pause 1.5
    scene bg school front
    pause 0.5
    "Another morning passes"

    #the scene switches to the club room
    if c_like > 4:
        c "Oh hiii [d]"
        d "Good morning [c]"
        c "What?\nIt's already 13 o'clock..."
        d "Haha i always say good morning"
        # C is smiling.
        c "Typical [d]"
        menu:
            "Ask her out":
                d "Do you have time this afternoon?"
                c "Yes.\nWhy do you ask?"
                menu:
                    "Ask her for a date":
                        d "Do you wanna come on a...\nDate with me?"
                        "[c] stops smiling and looks directly into my eyes."
                        if c_like > 15:
                            c "Are... Are you sure?"
                            d "Yes.\nYou seem very nice and i kinda have a crush on you."
                            c "I would love to go on a date with you... [d]"
                            d "Really?"
                            "[c] runs to me and wraps her arms around my waist."
                            c "I love you... everytime i think about you..."
                            c "I... I... I..."
                            # here c starts getting weird.
                            c "I always cut myself until i pass out."
                            d "Wha...What?"
                            c "And i will cut myself before we go on this date too...\nHihi"
                            # c gets normal again.
                            c "That will be a lot of fun."
                            d "Okay..."
                            "I kinda don't believe this.\nShe clearly makes a joke... Right?"
                            c "See you later."
                            "[c] walks back into the clubroom."
                            jump firstdaynoon
                        if c_like < 15:
                            # c turns weird
                            c "NO NEVER!"
                            d "Sorry..."
                            c "FUCK YOU!"
                            "[c] walks back into the clubroom."
                            "Holy fuck... she is really pissed..."
                            jump firstdaynoon




                    "Go to the Ice Truck with her":
                        d "Do you want to go to the Ice Truck with me?"
                        c "After school?"
                        d "Yes"
                        c "Nice idea... i pay for myself tho."
                        d "No, I would pay for you."
                        c "No it's alright.\nI am not broke."
                        d "Haha fine... let's meet at 16 o'clock in front of the main entrance."
                        c "Good idea"
                        "[c] walks back into the clubroom."
                        jump firstdaynoon

                        #block of code to run
                    

                #block of code to run
            "Say nothing.":
                jump firstdaynoon
    jump firstdaynoon
            
    
label firstdaynoon:
    "I walk into the clubroom."






return
