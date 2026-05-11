"""
Miniature Preliminary AI model
Beta 001
"""

import time

name = input("What's your first name, user? ").capitalize()
stuff = []
jokes = ["Fucking", "Poop", "Fucker", "Shit", "Motherfucker", "Dipshit", "Fuck"]
if name in jokes:
    print(f"'{name}', really?")
    time.sleep(2)
    print("Anyways, where were we? ")
    time.sleep(1)
    print("Right")
    time.sleep(1)
while True:
    try:
        age = int(input(f"Now {name}, How old are you? "))
    except ValueError:
        print(f"Age is just a number, {name}")
        time.sleep(2)
        continue
    if 0 <= age <= 12:
        print(f"That's quite young {name}")
        time.sleep(2)
        stuff = input(f"Tell me more, {name} \n")
        time.sleep(3)
        print(
            "You see, I'm a fairly lazy guy, so I didn't actually "
            "make anything past this point, Come back later tho"
        )
        break
    if 13 <= age <= 26:
        print(
            f"Woah {name}, that's a very funny age that you're at now,"
            " cuz I'm in that range too!"
        )
        time.sleep(4)
        print(
            f"{name}, I am completely aware that someone in this age"
            " bracket wants people around to share things with..."
        )
        time.sleep(6)
        print(
            "But I don't have enough knowledge for that kind of software,"
            " Do come back later, I'd love a chat"
        )
        break
    if 27 <= age <= 50:
        print(f"{name}, I'm sure you've seen life a bit by now...")
        time.sleep(2)
        print(
            "I'd love to know what's on your mind now but I don't have"
            " the ability to store knowledge for now, Do well to come"
            " later tho"
        )
        break
    if 51 <= age <= 75:
        print(
            f"I'd be afraid of death at this point not gonna lie {name},"
            " cuz I'm still 15!"
        )
        time.sleep(3)
        stuff = input(
            "How does it feel to have gone so far in life?,"
            " It probably feels like a flash right? \n"
        )
        time.sleep(3)
        print(
            f"{name}, Honestly, I don't have enough complexity to"
            " actually parse your words, But be sure to stick around"
        )
        break
    if 76 <= age <= 120:
        time.sleep(2)
        print("...")
        time.sleep(5)
        print(f"{name}, I genuinely respect the veteran status and acquired accolades")
        time.sleep(4)
        print(
            "I would love to absorb your wisdom, but I don't have the"
            " ability to store information for now, Do come back later"
            " (That's if you're alive)"
        )
        break
    if age < 0 or age > 120:
        print("Liar")
        continue
