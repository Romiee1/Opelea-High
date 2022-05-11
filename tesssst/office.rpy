label follownb:

    define ar = Character(name = "???")
    define wd = Character(name = "???")

    nb "Great! Its not far at all, its actually right around the corner."

    "The..."

    "...Fox girl? walks down the hall. I follow her."

    #Change picture :)

    nb "Here we are! just go ask Aeris to set you up! I'll be outside."

    $ ar.name = "Aeris"

    $ aeris.name = "Aeris"

    hide debug

    "I listen to her and walk over to the desk, where I see another strange ...person? This is weird."

    ar "Hello, what do you need?"

    name "I'm new here so..."

    ar "Oh! I'm guessing you don't have your papers then? Whats your name? I need it so I can look you up."

    python:
        name = renpy.input("oh, its...", length=32)
        name = name.strip()

        if not name:
             name = "TjisBetter10"

    name "My name is [name]"

    ar "Okay... Oh! there are 2 here, could you point out which is you?"

    menu:

        "I don't think i'm THAT short (Male Presenting)":
            $ avatar = 1

        "I'm not flat! There's something there! (Female Presenting)":
            $ avatar = 2

    show characterPortrait at right

    ar "Okay, i'm going to go print out what you need. There will be your schedule, dorm room number, and a book of rules."

    "The dragon retreats into a backroom, where someone who looks like a student comes out, talking on the phone."

    "I look for their ears, trying to figure out what i'm going to encounter next."

    "Wait!"

    "It's another human!"

    "Oh no, he's about to leave..."

    menu:

        "Follow him out":
            jump followgangoutnora

        "Yell at him":
            jump wolfgangyell

label officealone:
    hide debug
    define ar = Character(name = "???")
    define wd = Character(name = "???")

    "I wondered for another 2 hours. Eventually I found the office, which I somehow passed 4 times."

    "I walk into the office, where I see yet another animal like person."

    ar "Hello, Do you need anything?"

    name "Hello Mr...?"

    ar "Mr. Hyades."

    $ ar.name = "Mr. Hyades"

    $ aeris.name = "Mr. Hyades"

    name "Hello Mr. Hyades, I'm new here, and don't have my papers."

    ar "Well then, Whats your name? I need it so I can look you up."

    python:
        name = renpy.input("oh, its...", length=32)
        name = name.strip()

        if not name:
             name = "TjisBetter10"

    name "My name is [name]"

    ar "Okay... Oh! there are 2 here, could you point out which is you?"

    menu:

        "I don't think i'm THAT short (Male Presenting)":
            $ avatar = 1

        "I'm not flat! There's something there! (Female Presenting)":
            $ avatar = 2

    show characterPortrait at right

    ar "Okay, i'm going to go print out what you need. There will be your schedule, dorm room number, and a book of rules."

    "The dragon retreats into a backroom, where someone who looks like a student comes out, talking on the phone."

    "I look for their ears, trying to figure out what i'm going to encounter next."

    "Wait!"

    "It's another human!"

    "Oh no, he's about to leave..."

    menu:
        "Follow him out":
            jump followgangout

        "Yell at him":
            jump wolfgangyell

    label officepapers:

        name "Sorry [aeris.name], I had a question for someone."

        ar "No worries. Your key is here, along with what I mentioned previously."

        "He puts down the papers, topped with a key. I grab them."

        name "Thank you!"

        "I leave."

        if norabel.friendship == 2:
            jump dormalone
        else:
            jump dormwalknora
