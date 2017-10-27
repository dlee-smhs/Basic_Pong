import time
import random
import sys


def type(text):
    for c in text:
        sys.stdout.write(c)
        time.sleep(random.randrange(5, 10)/100.0)


def main():
    type("The Tale of Gladion Knit3blad3: A Choose Your Own Adventure!\n"
          "(You'll never beat this game. It makes no sense.)\n")
    type("\nIt is a dark and stormy night. Thunder clashes in the distance, awakening you.\n"
          "You clamber to you feet, noticing that you are drenched in rain.\n"
          "Around you, a supernatural storm is destroying the city. What could be causing it?\n"
          "Across the street, you can see a burning streetlamp, despite the rain.\n"
          "The building next to you creaks with uncertainty as it is buffered by the wind.\n")
    type("1. Cross the street and investigate.")
    type("2. Wait and regain you senses.")
    type("3. Back away slowly.")
    choice = input("Make your choice: ")
    if choice == 1:
        lamp()
    elif choice == 2:
        wait()
    else:
        back_away()


def fight():
    type("\nYou draw you blade and leap backwards, just in time to dodge the demon's blade.\n"
          "You can hear the blade slice through the air in the place you were standing moments ago.\n"
          "You regain your bearings and look up.\n"
          "Enraged, the demon charges at you.\n")
    type("1. Dodge to the side.")
    type("2. Roll behind it.")
    type("3. PANIC")
    choice = input("What will you do?")
    if choice == 3:
        charge()
    else:
        backslash()


def backslash():
    type("\nYou dodge just in time.\n"
          "The demon barrels past you, and you have time to counter attack.\n"
          "You leap through the air with your runeblade raised above your head. \n"
          "You exclaim 'BACK SLASH!!!' as you slice the demon's back open.\n"
          "Screaming in agony, the demon collapses to the ground. \n"
          "It roars 'KnIT3blAD3! I WiLL RETurN!'\n"
          "The demon opens a portal to the nether.\n"
          "Before it leaves, it shouts 'MaSTEr WarLOck GRaY WIlL HaVE HiS ReVEngE!\n"
          "It dissolves into the nether."
          "'That was close.' You think.\n"
          "'Master Warlock Gray', you think,'Who could that be? It seems that he is behind the city's destruction.'\n"
          "It doesn't matter right now. You have limited time before the portal closes.\n")
    type("1. Go to the weapon shop.")
    type("2. Dig up information on Master Warlock Gray.")
    type("3. Go home and sleep.")
    type("4. Brave the nether.")
    choice = input("What should I do now? I only have enough time for one action.")
    if choice == 1:
        weapon()
    elif choice == 2:
        information()
    elif choice == 3:
        sleep()
    else:
        deathportal1()


def deathportal1():
    type("\nYou step into the portal, transporting you to the nether. Darkness surrounds you. \n"
          "You hear a screeching behind you. You turn around to see an army of imps.\n"
          "You try to fight them off, but your sword breaks.\n"
          "YOU DIED. GAME OVER.\n"
          "If only you had a better weapon...")


def weapon():
    type("\n'I need a better weapon' you think as you get into your car. \n"
          "Luckily, I know a guy.\n"
          "You pull into the parking lot of Gary's Weapon Shop: 'Monstah Huntering Suppliez and Geer'.\n"
          "As you get out of the car, the shop explodes into an ethereal flame.\n"
          "You hear a maniacal laughter coming from the flames. Spooky.\n"
          "Nobody could have survived that. But what if he did...\n")
    type("1. Try to save Gary from the ethereal flames")
    type("2. Back to the portal.")
    choice = input("Should I go in after him?...")
    if choice == 1:
        flames()
    else:
        deathportal1()


def flames():
    type("\nIn an attempt to save Gary the shopkeeper, you charge into the blaze.\n"
          "As you approach, you are consumed by flames.\n"
          "You burn to death.\n"
          "YOU DIED. GAME OVER.\n"
          "'Some people just want to watch the world burn...'")


def information():
    type("\nYou decide to dig up some information on Master Warlock Gray.\n"
          "You head to a dark alley and meet with the crime boss known as 'TYPH00N'.\n"
          "He is notorious as a legendary gambler and a card shark. Despite his reputation, he is only 16 years old.\n"
          "'TYPH00N - I've come to bargain' you proclaim.\n"
          "'What is your name?' He replies.\n"
          "'It's Gladion Knit3blad3.'\n"
          "'What a wacky name. Is it spelled 'N-I-G-H-T-B-L-A-D-E?' He inquires.\n"
          "'It's spelled 'K-N-I-T-3-B-L-A-D-3', and it's way better than yours. Why does it have zeroes in it?'\n"
          "'I'm an edgy teen, so I get to be different.' He retorts 'You don't have a reason.'\n"
          "Dismissing his rudeness, you get down to business.\n"
          "After hearing what happened, he agrees to help, but under one condition.\n"
          "'I'll help you out, but only if you can beat me in a children's card game.'\n"
          "'WHAT?!?', you exclaim, 'That's the most ridiculous thing I've ever heard.'\n"
          "He replies:'It can't be more ridiculous than this game. It makes no sense...'\n"
          "'Did you just break the fourth wall? You can't do that!'\n"
          "'I believe I just did', he replies, 'Now do we have a deal or not?'\n"
          "'Fine' you reply."
          "You agree, and he gives you the choice between two decks.\n")
    type("1. Take 'DINOPOWER'-the dinosaur themed deck.")
    type("2. Take 'VERSUS ZOMBIES'- the plant themes deck.")
    choice = input("Which deck do you want?")
    if choice == 1:
        dinopower()
    else:
        pvz()


def dinopower():
    type("\nYou pick the deck 'DINOPOWER'.\n"
          "You play his game, and easily win. \n"
          "Your deck had some of the most powerful cards in the game.\n"
          "You exclaim 'GET TYRANNOSAURUS REKT!'. He replies 'You only won because I got terrible RNG...'\n"
          "'Fine', he says, 'I'll uphold my end of the bargain...'\n"
          "This land is dangerous. It's full of spelling errors and plot holes.\n"
          "To get through it, you'll need this spell.\n"
          "'Master Warlock Gray's minions can't stand water. \n"
          "TYPH00N gives you a water incantation to flood the nether.\n"
          "Gray himself is immune to water based attacks: he's a master of scuba diving as well...\n"
          "You think that you can hit the weapons shop on the way back.\n")
    type("1. Head to Gary's Weapon Shop: 'Monstah Huntering Suppliez and Geer'.")
    type("2. Head back to the portal.")
    choice = input("What should I do now?")
    if choice == 1:
        weapon2()
    else:
        safeportal()


def safeportal():
    type("\nYou decide to hurry back to the portal before it closes.\n"
          "On the way, you drive by Gary's Weapon Shop: 'Monstah Huntering Suppliez and Geer'.\n"
          "Out of the corner of your eye, you see the shop combust into an ethereal flame.\n"
          "You hear a maniacal laughter coming from the flames. Spooky.\n"
          "You decide to leave it, but call 911 on the way.\n\n"
          "You arrive at the portal.\n"
          "Before entering, you recite the water incantation TYPH00N gave you.\n"
          "The portal floods. You can hear souls howling in agony from inside.\n"
          "After a few minutes, you step into the inky void.\n"
          "Afer your eyes adjust, you can look round you."
          "You can see the bodies of hundreds, maybe thousands of imps, dissolving in water.\n"
          "You walk for a bit, until you see a creepy man next to a rowboat. He seems really shady...\n"
          "He offers to take you across this river.\n")
    type("1. Accept his guidance.")
    type("2. Steal his boat.")
    type("3. Decline his offer.")
    choice = input("What should I do now?")
    if choice == 1:
        guidance()
    elif choice == 2:
        steal()
    else:
        decline()


def guidance():
    type("\nYou choose to accept the creepy man's guidance.\n"
          "He takes you across the rapids. When you get off of the boat, \n"
          "it vaporizes into thin air along with the man.\n"
          "Was he a ghost? A spirit?\n"
          "You ignore it and move on.\n"
          "You walk for a while, until you see an ominous castle in the distance.\n"
          "On the gates, there is large golden lettering spelling out'MWG'."
          "The castle probably belongs to Master Warlock Gray.\n"
          "It seems to be guarded by a giant anaconda.\n"
          "It looks like it's as large as three train cars linked together.\n")
    type("1. Approach the castle head on.")
    type("2. Sneak into the castle.")
    type("3. Go around back")
    choice = input("What is the smartest approach?")
    if choice == 1:
        entercastle()
    elif choice == 2:
        sneak()
    else:
        back()


def entercastle():
    type("\nYou decide to approach the castle head on.\n"
          "You wait until the snake slithers behind the castle before approaching.\n"
          "You enter the castle. The walls are lined with ancient artifacts on display.\n"
          "Everything is coated with a thick layer of dust.\n"
          "You notice that there is no dust on the carpets stretching through the castle.\n"
          "You reach two staircases.\n"
          "One leads up to the spire, another to the basement.\n")
    type("1. Head up to the spire.")
    type("2. Head down to the basement.")
    type("3. Ignore the stairs and continue onward")
    choice = input("What should I do now?")
    if choice == 1:
        spire()
    elif choice == 2:
        basement()
    else:
        onward()


def actualonward():
    type("You make your way back to the middle room.\n"
          "On the door, there are two glowing symbols.\n"
          "The door slides open.\n"
          "You walk through the doorway.\n"
          "You find a light shield in the next room.\n"
          "You enter the next room.\n")
    icedemon()


def icedemon():
    type("The room is dark.\n"
          "Suddenly, torches light up the room.\n"
          "In front of you stands a hooded figure.\n"
          "He mutters 'Heh, Nothing personnel kid' and teleports away.\n"
          "The door slams closed behind you.\n"
          "In the center of the room, a portal opens on the ceiling.\n"
          "A demon drops out of it. The portal closes.\n"
          "The demon glows blue, and becomes enclosed in ice.\n"
          "The temperature of the room drops to freezing. Puddles of water freeze and become ice.\n"
          "For some reason, it starts snowing inside.\n"
          "Some metal chunks of the ceiling collapse to the ground.\n"
          "The demon forms a sword and shield out of ice.\n"
          "It charges toward you at lightning speed...\n")
    type("1. Raise your shield.")
    type("2. Attack with your sword.")
    type("3. Use water magic.")
    type("4. Use your bow.")
    type("5. Use your ice rod.")
    type("6. Take time to survey the room.")
    choice = input("What should I do?")
    if choice == 1:
        shield()
    elif choice == 2:
        sword()
    elif choice == 3:
        magic()
    elif choice == 4:
        bow()
    elif choice == 5:
        shieldrod()
    else:
        survey()


def survey():
    type("\nBefore charging into battle, you look around the room.\n"
          "You see a chain partially hidden under a pile of snow.\n"
          "There are torches in the corners of the room, but they are out of reach.\n"
          "The floor is slippery and covered with ice. It would not be safe to run in here.\n"
          "There are mounds of snow on either side of you.\n"
          "You need to act before the demon reaches you...\n")
    type("1. Raise your shield.")
    type("2. Attack with your sword.")
    type("3. Use water magic.")
    type("4. Use your bow.")
    type("5. Use your ice rod.")
    type("6. Roll forward.")
    type("7. Roll backwards.")
    type("8. Dodge to the side.")
    choice = input("What should I do?")
    if choice == 1:
        shield()
    elif choice == 2:
        sword()
    elif choice == 3:
        magic()
    elif choice == 4:
        bow()
    elif choice == 5:
        shieldrod()
    elif choice == 6:
        rf()
    elif choice == 7:
        rb()
    else:
        ds()


def rf():
    type("You roll forward, past the demon.\n"
          "It roars past you, and crashes into the door.\n"
          "The demon is stunned.\n"
          "Now's your chance!\n")
    type("1. Attack while it is stunned.")
    type("2. Investigate the chain.")
    type("3. Find another way.")
    choice = input("What do I do?")
    if choice == 1:
        stunnedsword()
    elif choice == 2:
        ballandchain()
    else:
        way()


def way():
    type("'There must be some other way...' you think.\n"
          "You don't come up with any ideas.\n"
          "The demon reaches you and freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def ballandchain():
    type("\nYou dig through the pile of snow.\n"
          "On the other end of the chain, there is a metal ball attached.\n"
          "You swing the ball around you to build up momentum.\n"
          "You release it, and it flies at the demon.\n"
          "The impact shatters its icy weapons and armor.\n"
          "The demon turns from blue to pale.\n"
          "You run up and stab it with your sword.\n"
          "The demon cries in anguish.\n"
          "It explodes into a puff of purple smoke.\n"
          "The doors open.")
    finalhallway()


def finalhallway():
    type("\nThe next room is a hallway.\n"
          "You take your time walking through it, preparing for what could be the final battle.\n"
          "At the end of the hall, there is a grand door.\n"
          "You push it open.")
    masterwarlockgray()


def masterwarlockgray():
    type("\nThe hooded figure from before is sitting alone, staring into a fireplace.\n"
          "'Gladion Knit3blad3' he says, 'I've been expecting you.'\n"
          "'You've been waiting here in this room for me?!? What if I never came here?!?\n"
          "What if I died in the castle?!? That's the worst plan I've ever heard!' you exclaim.\n"
          "'Ignore that obvious plot hole' he replies.\n"
          "He continues:\n"
          "'I will now tell you my overly complicated and irrelevant back story \n"
          "that will not affect the plot in any way...\n\n"
          "It all started when I was a child. My family always took me scuba diving during the summer.\n"
          "I became an expert at scuba diving. I even started to go spear fishing with a harpoon gun.\n"
          "One day, I was out scuba diving, and my parents died.'\n"
          "You interrupt: 'Well how did they die-'\n"
          "'NO INTERRUPTING!' he screams\n"
          "Anyways, a mysterious voice contacted me and told me that my parents could be revived.\n"
          "In return, I would have to sacrifice my soul.\n"
          "To perform the ritual of soul sacrificing, I would have to become stronger.\n"
          "I went on a soul searching journey after that, travelled the world.\n"
          "I learned karakungjutotejitsu from some monks living in the mountains of Tibet.\n"
          "I went on a quest to slay a rainbow yeti with wings that was terrorizing the people of my imagination.\n"
          "I braved the rivers of the Amazon, discovered Atlantis, and travelled to other galaxies... \n"
          "all in order to exact my revenge.'\n"
          "He pauses to take a sip of tea.\n"
          "'Atlantis doesn't exist, and travel between galaxies isn't possible yet.' You interject.\n"
          "'Also, who is your revenge toward?'\n"
          "Gray spits out his tea. 'I SAID NO INTERRUPTING!'\n"
          "He stands up from his chair, still facing the fire.\n"
          "He whirls around and pulls down his hood.\n"
          "In front of you stands a shadowy effigy of Gary, the shopkeeper.\n"
          "You reel in surprise.\n"
          "'Gary?!? You died in an explosion!'\n"
          "'That's what you thought...\n"
          "You see, after my journey around the world, I settled down to become a shopkeeper.\n"
          "But that was just a part of my plan...\n"
          "In order to perform the ritual, I had to collect large amounts of cash.\n"
          "I profited from the shop, and gained the necessary funds.\n"
          "The voice told me to leave the money in a dumpster in a shady alleyway.\n"
          "In return, my parents would be revived.\n"
          "He took my soul as promised and gave me this castle. I also got magical powers.\n"
          "That was what happened when my shop exploded.\n"
          "From that point on, I fully adopted my ego known as Gray."
          "He never revived my parents. \n"
          "All I know is that he is somewhere in the city, and that's why I have to destroy it!\n"
          "You summarize 'So you got conned by a magical scammer and now want to destroy the city?'\n"
          "'Yes. Why?'\n"
          "'This still makes no sense. The shop exploded after you sent a demon after me.\n"
          "Also, why were you expecting me? Also, that's the most ridiculous story I've ever heard.\n"
          "'You're the main character, so I blamed you. That's why the demon attacked you.\n"
          "It was all in order to get my vaguely defined revenge. MWAHAHAHAHAHA!'\n"
          "'Wait. If you suspected me, why did you attack the city?\n"
          "It seems like you made this story up five minutes ago...'\n"
          "'I told you to ignore all these plot holes.\n"
          "Enough talk... Let us do battle!'\n")
    garybattle()


def garybattle():
    type("You draw you sword.\n"
          "As long as you believe in the power of friendship, \n"
          "your main character powers will prevail.\n"
          "Gary holds one hand behind his back.\n"
          "He holds the other in front of him.\n"
          "'I'M GoNNa BlOCk YouR AttaCKS' he says.\n"
          "His voice seems different than before.\n"
          "He talks in a strange, almost demonic tone.\n")
    type("1. Stab him.")
    type("2. Slash at him.")
    type("3. Have mercy.")
    choice = input("What should I do?")
    if choice == 1:
        stab()
    elif choice == 2:
        slash()
    else:
        mercy()


def stab():
    type("You thrust your sword at him.\n"
          "He tries to catch it, but is too slow.\n"
          "The sword is stuck in his chest.\n"
          "ThAT WaS A CheaP MoVE!!!\n"
          "YoU'Ll PAy fOR ThAt!!!\n"
          "He leaps backwards, onto the mantle.\n"
          "He pulls out a harpoon gun and aims it at you.\n"
          "'HeYYY hEyyyYY, TiEmE ToO DIEIEE' He shrieks.\n")
    type("1. Prepare to die.")
    type("2. Get to cover.")
    type("3. Prepare to dodge.")
    choice = input("Is this the end?")
    if choice == 1:
        panic2()
    elif choice == 2:
        cover()
    else:
        nicedodge()


def panic2():
    type("You panic, seeing your life flash before your eyes.\n"
          "You hear the gun go off.\n"
          "Nothing happens.\n"
          "You look up to see Gary with the harpoon through him.\n"
          "'CURse YoU...\n"
          "ThE Gun WAs BaCKwARdS...'\n"
          "It seems that Gary has accidentally shot himself with the gun.\n"
          "He apparently was holding it backwards.\n"
          "As Gary dies, he whispers his last words to you:\n"
          "'THe OnlY THIng DarKEr ThaN BlacK iS GRAY...'\n\n"
          "Master Warlock Gray was defeated.\n"
          "The city had been saved from his vague and generic plan.\n"
          "You didn't really do anything because he shot himself.\n"
          "All of your efforts were for nothing.\n"
          "\nYOU WIN.\n"
          "Congratulations!")


def cover():
    type("You dash behind the chair, hoping to get to cover.\n"
          "You hear the gun go off.\n"
          "Nothing happens.\n"
          "You look up to see Gary with the harpoon through him.\n"
          "'CURse YoU...\n"
          "ThE Gun WAs BaCKwARdS...'\n"
          "It seems that Gary has accidentally shot himself with the gun.\n"
          "He apparently was holding it backwards.\n"
          "As Gary dies, he whispers his last words to you:\n"
          "'THe OnlY THIng DarKEr ThaN BlacK iS GRAY...'\n\n"
          "Master Warlock Gray was defeated.\n"
          "The city had been saved from his vague and generic plan.\n"
          "You didn't really do anything because he shot himself.\n"
          "All of your efforts were for nothing.\n"
          "\nYOU WIN.\n"
          "Congratulations!")


def nicedodge():
    type("You prepare yourself to dodge the harpoon.\n"
          "It's a gutsy move, but you don't have many options...\n"
          "You hear the gun go off.\n"
          "Nothing happens.\n"
          "You look up to see Gary with the harpoon through him.\n"
          "'CURse YoU...\n"
          "ThE Gun WAs BaCKwARdS...'\n"
          "It seems that Gary has accidentally shot himself with the gun.\n"
          "He apparently was holding it backwards.\n"
          "As Gary dies, he whispers his last words to you:\n"
          "'THe OnlY THIng DarKEr ThaN BlacK iS GRAY...'\n\n"
          "Master Warlock Gray was defeated.\n"
          "The city had been saved from his vague and generic plan.\n"
          "You didn't really do anything because he shot himself.\n"
          "All of your efforts were for nothing.\n"
          "\nYOU WIN.\n"
          "Congratulations!")


def slash():
    type("You slash at him.\n"
          "To your surprise, he catches the blade.\n"
          "You wonder how he caught the sword without slicing his hand.\n"
          "He wrestles the sword from your hand and stabs you with it.\n"
          "YOU DIED. GAME OVER.\n"
          "'Nothing personnel kid.'")


def mercy():
    type("You sheath your sword.\n"
          "'We can find another way.' you say.\n"
          "'ThE OnlY wAY iS My Way!!!' he screeches.\n"
          "Gary teleports away.\n"
          "You look around you but don't see where he went.\n"
          "He appears behind you and stabs you with a katana.\n"
          "As you fall to the ground, you hear him whisper\n"
          "'NoTHiNG PErSoNNEl KiD.'\n"
          "YOU DIED. GAME OVER.\n"
          "You came so far...")


def stunnedsword():
    type("You run up behind it and slash with your sword.\n"
          "Your arm becomes frozen from the subzero temperatures.\n"
          "The demon attacks you and freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def rb():
    type("You roll backwards.\n"
          "You forgot about the door behind you and roll into it.\n"
          "The demon catches you and freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def ds():
    type("In the nick of time, you dodge to the side.\n"
          "If you read the paragraph before, you would have known about the piles of snow near you.\n"
          "You get stuck in the mound of snow.\n"
          "The demon catches you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


# bow
def bow():
    type("\nYou pull out your bow.\n"
          "While strafing around the demon, you fire an arrow.\n"
          "It bounces off of the demon's ice shield.\n"
          "While you recover, it runs over and slashes at you with its ice sword.\n"
          "You dodge, and pull out:\n")
    type("1. Your sword.")
    type("2. Your shield.")
    type("3. Your ice rod.")
    type("4. Your water spell.")
    choice = input("What item do I use?")
    if choice == 1:
        sword()
    elif choice == 2:
        shield()
    elif choice == 3:
        shieldrod()
    elif choice == 4:
        magic()


# swordseries
def sword():
    type("\nYou swing your sword at the demon, but miss.\n"
          "You raise your sword to block an attack.\n"
          "The sword along with your arm becomes frozen.\n"
          "The freeze stops you from using some weapons.\n")
    type("1. Raise your shield.")
    type("2. Use water magic.")
    type("3. Use ice rod.")
    choice = input("What do I do?")
    if choice == 1:
        swordshield()
    elif choice == 2:
        magic()
    else:
        shieldrod()


def swordshield():
    type("\nYou raise your shield to block the demon's attack.\n"
          "It slashes at you with its sword, but is blocked by your shield.\n"
          "Your other arm and shield become frozen from the contact.\n"
          "You are defenseless. The demon freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


# shieldseries
def shield():
    type("\nYou raise your shield to block the demon's attack.\n"
          "It slashes at you with its sword, but is blocked by your shield.\n"
          "Your arm becomes frozen from contact.\n"
          "The freeze stops you from using some weapons.\n"
          "The shield is frozen as well.\n")
    type("1. Use sword.")
    type("2. Use ice rod.")
    type("3. Use water magic")
    choice = input("What now?")
    if choice == 1:
        shieldsword()
    elif choice == 2:
        shieldrod()
    else:
        magic()


def shieldsword():
    type("\nYou swing your sword at the demon, but miss.\n"
          "You raise your sword to block an attack.\n"
          "The sword along with your other arm becomes frozen.\n"
          "You are defenseless. The demon freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def shieldrod():
    type("\nYou use the ice rod on the demon.\n"
          "Your ice based attack did nothing against the ice elemental.\n"
          "You jump out of the way to dodge one of its attacks, but drop your sword, shield, and bow.\n"
          "It approaches.")
    type("1. Go for your lost items.")
    type("2. Use water magic.")
    choice = input("What now?")
    if choice == 1:
        gonow()
    else:
        magic()


def gonow():
    type("\nYou decide to try to get your items back.\n"
          "You start running across the room, but slip and fall.\n"
          "The demon catches you and freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def magic():
    type("\nYou use the water spell.\n"
          "It sends a geyser of water spiraling towards the demon.\n"
          "The water freezes before it reaches the demon.\n"
          "It catches you and freezes you.\n"
          "YOU DIED. GAME OVER.\n"
          "What a COOL boss.")


def onward():
    type("\nYou keep going until you reach a locked door.\n"
          "Next to the door, there is a plaque.\n"
          "It says 'Conquer the beasts above and below;\n"
          "only then with the true path show'.\n"
          "You decide to come back later.\n")
    type("1. Go up to the spire.")
    type("2. Go down to the basement.")
    choice = input("Now what?")
    if choice == 1:
        spire()
    else:
        basement()


# spire series
def spire():
    type("\nYou climb the spire until you reach the top.\n"
          "You reach the roof.\n"
          "As you climb up, the door slams closed behind you.\n"
          "There is a harsh downpour. Lightning strikes in the distance.\n"
          "Suddenly, a strong wind starts blowing against the tower.\n"
          "You turn around to where the wind is coming from.\n"
          "A giant dragon flaps it's wings, hovering in place.\n"
          "'This is the obligatory dragon boss' you think.\n"
          "You find an old bow on the ground. There are no arrows around.\n"
          "It is also too windy to aim properly.\n"
          "The dragon draws near.\n")
    type("1. Use the water spell to fight it.")
    type("2. Use your sword.")
    type("3. Jump off of the spire.")
    choice = input("What should I do?")
    if choice == 3:
        jump()
    else:
        dragonkills()


def jump():
    type("\nYou jump off of the roof, narrowly avoiding the dragons flames.\n"
          "You cast the water spell in a downward direction, slowing your fall.\n"
          "You smash through the roof of a lower level.\n"
          "After a while, you recover.\n"
          "It was a risky gamble, but it payed off.\n"
          "You keep going until you reach a locked door.\n"
          "Next to the door, there is a plaque.\n"
          "It says 'Conquer the beasts above and below;\n"
          "only then with the true path show'.\n"
          "You find some arrows in the room.\n"
          "You decide to come back later.\n"
          "You decide to go to the last unexplored room, the basement.")
    basement2()


def basement2():
    type("\nYou decide to head down to the basement.\n"
          "It's less of a basement and more of a dungeon.\n"
          "The floors are grates that are suspended over lava.\n"
          "You walk into a room.\n"
          "Suddenly, the door closes behind you!\n"
          "In the room, you find a magical ice rod.\n"
          "It won't work in here, the lava is too hot.\n"
          "The room begins to shake, bits of stone fall from the ceiling.\n"
          "The lava under you is bubbling.\n"
          "A giant hand smashes up through the grate from the lava.\n"
          "The hand is made entirely of bone.\n"
          "Another hand does the same.\n"
          "The skeletal beast pulls itself out of the lava.\n"
          "The colossus peers down at you with a single giant eye.\n"
          "It roars with rage.\n"
          "It raises a single hand above its head, then starts to bring it down towards you.\n")
    type("1. Hit it with water magic.")
    type("2. Dodge to the side.")
    type("3. Attack with your sword.")
    type("4. Shoot its eye with your bow.")
    choice = input("What should I do?")
    if choice == 2:
        skeleescape()
    elif choice == 4:
        skelekilled()
    else:
        skelekills()


def skelekilled():
    type("\nYou fire an arrow into its eye.\n"
          "The colossus roars in pain and collapses to the ground.\n"
          "You run over to it and begin to stab its eye with your sword.\n"
          "The eye explodes in a puff of dark smoke.\n"
          "The remains of the skeleton slide back into the lava.\n"
          "The door behind you opens.\n")
    type("1. Head back to the middle room.")
    type("2. Head up to the spire.")
    choice = input("What now?")
    if choice == 1:
        onwardskele()
    else:
        spire2()


def onwardskele():
    type("\nYou head back to the corridor from before.\n"
          "On the door, a symbol resembling a skull is glowing.\n"
          "The plaque still reads the same thing.\n"
          "You decide to head up to the spire.\n")
    spire2()


def spire2():
    type("You climb the spire until you reach the top.\n"
          "You reach the roof.\n"
          "As you climb up, the door slams closed behind you.\n"
          "There is a harsh downpour. Lightning strikes in the distance.\n"
          "Suddenly, a strong wind starts blowing against the tower.\n"
          "You turn around to where the wind is coming from.\n"
          "A giant dragon flaps it's wings, hovering in place.\n"
          "'This is the obligatory dragon boss' you think.\n")
    type("1. Use the water spell to fight it.")
    type("2. Use your sword.")
    type("3. Jump off of the spire.")
    type("4. Use the freezing rod.")
    choice = input("What should I do?")
    if choice == 3:
        jump2()
    elif choice == 4:
        freeze()
    else:
        dragonkills()


def freeze():
    type("\nYou point your freezing rod toward the skies.\n"
          "It shoots a beam of magic into the clouds above.\n"
          "The clouds freeze and fall out of the sky.\n"
          "The dragon is pinned to the tower under their weight.\n"
          "While it is trapped, you run over and slash it with your sword.\n"
          "The beast lets out a final anguished wail and collapses to the floor.\n"
          "It explodes in a puff of dark smoke.\n"
          "The door opens behind you.\n"
          "You decide to head back to the center room.\n")
    actualonward()


def jump2():
    type("\nYou decide to jump off of the roof again.\n"
          "This time, you weren't so lucky.\n"
          "You slip as you run to the edge, and drop the water spell.\n"
          "With nothing to slow your fall, you fall to your death.\n"
          "YOU DIED. GAME OVER.\n"
          "What a stupid plan.")


def dragonkills():
    type("\nYou raise your weapon to attack.\n"
          "The dragon is faster. It melts you with it's fire breath.\n"
          "YOU DIED. GAME OVER.\n"
          "Heh, this guys toast.")


# basement series
def basement():
    type("\nYou decide to head down to the basement.\n"
          "It's less of a basement and more of a dungeon.\n"
          "The floors are grates that are suspended over lava.\n"
          "You walk into a room.\n"
          "Suddenly, the door closes behind you!\n"
          "In the room, you find a magical ice rod.\n"
          "It won't work in here, the lava is too hot.\n"
          "The room begins to shake, bits of stone fall from the ceiling.\n"
          "The lava under you is bubbling.\n"
          "A giant hand smashes through the grate from the lava.\n"
          "The hand is made entirely of bone.\n"
          "Another hand does the same.\n"
          "The skeletal beast pulls itself out of the lava.\n"
          "The colossus peers down at you with a single giant eye.\n"
          "It roars with rage.\n"
          "It raises a single hand above its head, then starts to bring it down towards you.\n")
    type("1. Hit it with water magic.")
    type("2. Dodge to the side.")
    type("3. Attack with your sword.")
    choice = input("What should I do?")
    if choice == 2:
        skeleescape()
    else:
        skelekills()


def skeleescape():
    type("\nThe skeleton launches its fist at you.\n"
          "You tumble to the side, evading the attack.\n"
          "The fist breaks through the wall.\n"
          "You run through the hole in the wall and escape the beast.\n"
          "You keep going until you reach a locked door.\n"
          "Next to the door, there is a plaque.\n"
          "It says 'Conquer the beasts above and below;\n"
          "only then with the true path show'.\n"
          "You find some arrows in the room.\n"
          "You decide to come back later.\n")
    type("1. Go up to the spire.")
    type("2. Go down to the basement.")
    choice = input("Where should I go?")
    if choice == 1:
        spire3()
    else:
        nobasement()


def nobasement():
    type("\nYou were just at the basement.\n"
          "You climb the spire until you reach the top.\n"
          "You reach the roof.\n"
          "As you climb up, the door slams closed behind you.\n"
          "There is a harsh downpour. Lightning strikes in the distance.\n"
          "Suddenly, a strong wind starts blowing against the tower.\n"
          "You turn around to where the wind is coming from.\n"
          "A giant dragon flaps it's wings, hovering in place.\n"
          "'This is the obligatory dragon boss' you think.\n"
          "You find an old bow on the ground. There are no arrows around.\n"
          "It is also too windy to aim properly.\n"
          "The dragon draws near.\n")
    type("1. Use the water spell to fight it.")
    type("2. Use your sword.")
    type("3. Jump off of the spire.")
    type("4. Use the freezing rod.")
    choice = input("What should I do?")
    if choice == 3:
        jump2()
    elif choice == 4:
        freeze2()
    else:
        dragonkills()


def spire3():
    type("\nYou climb the spire until you reach the top.\n"
          "You reach the roof.\n"
          "As you climb up, the door slams closed behind you.\n"
          "There is a harsh downpour. Lightning strikes in the distance.\n"
          "Suddenly, a strong wind starts blowing against the tower.\n"
          "You turn around to where the wind is coming from.\n"
          "A giant dragon flaps it's wings, hovering in place.\n"
          "'This is the obligatory dragon boss' you think.\n"
          "You find an old bow on the ground. There are no arrows around.\n"
          "It is also too windy to aim properly.\n"
          "The dragon draws near.\n")
    type("1. Use the water spell to fight it.")
    type("2. Use your sword.")
    type("3. Jump off of the spire.")
    type("4. Use the freezing rod.")
    choice = input("What should I do?")
    if choice == 3:
        jump3()
    elif choice == 4:
        freeze2()
    else:
        dragonkills()


def jump3():
    type("\nYou decide to jump off of the roof.\n"
          "You weren't so lucky.\n"
          "You slip as you run to the edge, and drop your gear.\n"
          "With nothing to slow your fall, you fall to your death.\n"
          "YOU DIED. GAME OVER.\n"
          "What a stupid plan.")


def freeze2():
    type("\nYou point your freezing rod toward the skies.\n"
          "It shoots a beam of magic into the clouds above.\n"
          "The clouds freeze and fall out of the sky.\n"
          "The dragon is pinned to the tower under their weight.\n"
          "While it is trapped, you run over and slash it with your sword.\n"
          "The beast lets out a final anguished wail and collapses to the floor.\n"
          "It explodes in a puff of dark smoke.\n"
          "The door opens behind you.\n")
    type("1. Go back to the middle room.")
    type("2. Down to the basement.")
    choice = input("Where should I go?")
    if choice == 1:
        onwarddragon()
    else:
        basement3()


def onwarddragon():
    type("\nYou head back to the corridor from before.\n"
          "On the door, a symbol resembling a skull is glowing.\n"
          "The plaque still reads the same thing.\n"
          "You decide to head up to the spire.")
    basement3()


def basement3():
    type("\nYou decide to head down to the basement.\n"
          "It's less of a basement and more of a dungeon.\n"
          "The floors are grates that are suspended over lava.\n"
          "You walk into a room.\n"
          "Suddenly, the door closes behind you!\n"
          "The room begins to shake, bits of stone fall from the ceiling.\n"
          "The lava under you is bubbling.\n"
          "A giant hand smashes up through the grate from the lava.\n"
          "The hand is made entirely of bone.\n"
          "Another hand does the same.\n"
          "The skeletal beast pulls itself out of the lava.\n"
          "The colossus peers down at you with a single giant eye.\n"
          "It roars with rage.\n"
          "It raises a single hand above its head, then starts to bring it down towards you.\n")
    type("1. Hit it with water magic.")
    type("2. Dodge to the side.")
    type("3. Attack with your sword.")
    type("4. Shoot its eye with your bow.")
    choice = input("What should I do?")
    if choice == 2:
        skeleescape2()
    elif choice == 4:
        skelekilled2()
    else:
        skelekills()


def skeleescape2():
    type("\nThe skeleton launches its fist at you.\n"
          "You try tumble to the side to evade the attack.\n"
          "You are too slow, the skeleton smashes you with its fist.\n"
          "YOU DIED. GAME OVER.\n"
          "'Spooky scary skeletons send shivers down your spine...'")


def skelekilled2():
    type("\nYou fire an arrow into its eye.\n"
          "The colossus roars in pain and collapses to the ground.\n"
          "You run over to it and begin to stab its eye with your sword.\n"
          "The eye explodes in a puff of dark smoke.\n"
          "The remains of the skeleton slide back into the lava.\n"
          "The door behind you opens.\n"
          "You decide to head back up to the middle room.\n")
    actualonward()


def skelekills():
    type("\nYou raise your weapon to attack.\n"
          "The skeleton is faster.\n"
          "It brings its fist down, smashing the grate below you.\n"
          "You fall into the lava.\n"
          "YOU DIED. GAME OVER.\n"
          "Well that's just grate...")


def sneak():
    type("\nYou decide to sneak into the castle.\n"
          "You see an open window that is within reach.\n"
          "You start to climb up to the window, but slip and fall. \n"
          "The guard snake is alerted, and attacks you.")
    snake()


def back():
    type("\nYou go around to the backside of the castle.\n"
          "There is a murky moat with what seems to be alligators in it.\n"
          "A drawbridge sits over the moat.\n"
          "Suddenly, the giant anaconda slithers behind the castle.\n"
          "You aren't able to avoid detection, and it attacks you.")
    snake()


def snake():
    type("\nThe snake is coming towards you. You need to act.\n"
          "You have TYPH00N's water spell and your runeblade.\n"
          "You don't have much time...\n")
    type("1. Fight it.")
    type("2. Run across the drawbridge into the castle.")
    type("3. Get to the moat.")
    choice = input("What should I do about the snake?")
    if choice == 1:
        snakefight()
    elif choice == 2:
        drawbridge()
    else:
        moat()


def snakefight():
    type("\nYou cast the water spell. It sends a torrent of water toward the beast.\n"
          "Nothing happens. You draw your sword, but the snake kills you with a single bite.\n"
          "YOU DIED. GAME OVER\n"
          "'Why did it have to be snakes?'")


def drawbridge():
    type("\nYou turn to the castle and start running.\n"
          "You start across the drawbridge, but the snake smashes it with it's tail.\n"
          "You fall into the water. The alligators eat you.\n"
          "YOU DIED. GAME OVER.\n"
          "What did you expect?")


def moat():
    type("\nYou head to the moat, with the snake following you.\n"
          "It lunges for you, but you sidestep.\n"
          "The snake barrels past you, into the moat.\n"
          "The alligators attack it, buying you some time.\n"
          "You enter the castle.")
    entercastle2()


def entercastle2():
    type("\nYou enter the castle. The walls are lined with ancient artifacts on display.\n"
          "Everything is coated with a thick layer of dust.\n"
          "You notice that there is no dust on the carpets stretching through the castle.\n"
          "You reach two staircases.\n"
          "One leads up to the spire, another to the basement.\n")
    type("1. Head up to the spire.")
    type("2. Head down to the basement.")
    type("3. Ignore the stairs and continue onward.")
    choice = input("What should I do now?")
    if choice == 1:
        spire()
    elif choice == 2:
        basement()
    else:
        onward()


def steal():
    type("\nWhen the man isn't looking you steal his boat.\n"
          "You start to cross the river. Around halfway across, your boat gets caught in a fierce current.\n"
          "You lose control and capsize in the river. You drown.\n"
          "YOU DIED. GAME OVER.\n"
          "'We're gonna need a bigger boat.'")


def decline():
    type("\nYou decline his offer. To your surprise, the man vanishes along with his boat.\n"
          "'Great' you think, 'Now I have to find another way across the river.\n"
          "You wander around, but get lost within the nether.\n"
          "You continue to wander around, until you starve to death.\n"
          "YOU DIED. GAME OVER.\n"
          "Not all who wander are lost...")


def weapon2():
    type("\n'I need a better weapon' you think as you get into your car. \n"
          "Luckily, I know a guy.\n"
          "You pull into the parking lot of Gary's Weapon Shop: 'Monstah Huntering Suppliez and Geer'.\n"
          "The name is stupid, but the goods are quality.\n"
          "As you get out of the car, the shop explodes into an ethereal flame.\n"
          "You hear a maniacal laughter coming from the flames. Spooky.\n"
          "Nobody could have survived that. But what if he did...\n")
    type("1. Try to save Gary from the flames")
    type("2. Back to the portal.")
    choice = input("What should I do???")
    if choice == 1:
        flames()
    else:
        deathportal2()


def deathportal2():
    type("\nYou hurry back to the portal, slightly traumatized over your decision...\n"
          "As you rush forward, you forget about your water incantation.\n"
          "You step into the portal, transporting you to the nether. Darkness surrounds you. \n"
          "You hear a screeching behind you. You turn around to see an army of imps.\n"
          "You try to fight them off, but your sword breaks.\n"
          "YOU DIED. GAME OVER.\n"
          "If only you had a better weapon...")


def pvz():
    type("\nYou pick the deck 'VERSUS ZOMBIES'. \n"
          "You play his game, and loose terribly. \n"
          "His deck had some of the most powerful cards in the game...\n"
          "He exclaims 'GET TYRANNOSAURUS REKT!'. You reply: 'You only won because I got terrible RNG...'\n"
          "He kicks you out of his territory and tells you to stay out.\n")
    type("1. Demand a rematch.")
    type("2. Back to the portal.")
    choice = input("What should I do?")
    if choice == 2:
        deathportal1()
    else:
        rematch()


def rematch():
    type("\nYou intrude back into TYPH00N's territory.\n"
          "When he sees you, he cries 'Interloper! I told you not to return!'\n"
          "He orders his guards to kill you. You are shot to death.\n"
          "YOU DIED. GAME OVER.\n"
          "Don't jump the gun now...")


def sleep():
    type("\nYou head home to take a quick nap. You set an alarm to ring in fifty minutes.\n"
          "You oversleep your alarm.\n"
          "The portal closes.\n"
          "\nYOU SURVIVED:\n"
          "This is really more of a loss than a win...\n"
          "You are safe for now, but Master Warlock Gray is still at large, destroying the city.\n"
          "Try again for the actual ending.")


def charge():
    type("\nThe demon charges at you, filled with rage. \n"
          "Panicked, you take a step backwards, only to slip in a puddle behind you. \n"
          "While you are getting up, the demon reaches you and kills you with a savage blow.\n"
          "YOU DIED. GAME OVER.\n"
          "If only you had payed better attention to your surroundings...")


def back_away():
    type("\nYou begin to back away slowly. You reach the entrance to the building.\n"
          "The sign reads 'SKYSCRAPERS R US'. The building shudders in the wind.\n")
    type("1. Enter the building.")
    type("2. Back away some more.")
    choice = input("Make your choice\n")
    if choice == 1:
        building()
    else:
        back_away_again()


def back_away_again():
    type("\nThe streetlamp continues to smoke.\n"
          "You continue to back away from it. \n"
          "Not looking where you are going, you back into a street. \n"
          "A car runs you over.\n"
          "YOU DIED. GAME OVER.\n"
          "Look both ways before you cross the street!")


def five():
    type("\nYou reach the fifth floor. The building begins to sway in the wind. \n"
          "Suddenly, it falls to the ground. \n"
          "Luckily, you were unharmed by the fall because of your main character powers.\n"
          "Also, you weren't that high up...\n")
    type("1. Investigate the lamp.")
    type("2. Back away from the rubble.")
    choice = input("What now?")
    if choice == 1:
        lamp()
    else:
        back_away_again()


def building():
    type("\nThere is a working elevator inside. \n"
          "You enter the elevator.\n"
          "The doors close. \n"
          "A relaxing song plays in the background while you choose your floor.\n")
    type("1. Floor five.")
    type("2. Floor ten.")
    type("3. Roof.")
    choice = input("What floor do you want to go to?")

    if choice == 1:
        five()
    else:
        collapse()


def collapse():
    type("\nThe elevator accelerates upward. You feel the building sway.\n"
          "The building collapses while you are riding the elevator upwards. \n"
          "The elevator falls with you inside it, causing an instant death. \n"
          "YOU DIED. GAME OVER.\n"
          "'SKYSCRAPERS R US is experiencing technical difficulties. Please stand by...'")


def wait():
    type("\nYou decide to wait around to regain your senses. The wind howls fiercely.\n"
          "You turn around to see the building swaying violently.\n"
          "The building you are standing next to collapses, crushing you.\n"
          "YOU DIED. GAME OVER.\n"
          "A hero is never idle...")


def lamp():
    type("\nYou cross the street to investigate the lamp. \n"
          "Suddenly, lightning strikes it! Luckily, you were unharmed. \n"
          "The building you awoke next to collapses suddenly. \n"
          "Out of the smoke appears a giant, humanoid in appearance. \n"
          "It is a fel demon from the netherworld.\n"
          "It calls to you 'GlAdioN, I haVE coME For YoUR SoUl! VenGEncE Will BE MiNE!' \n"
          "You don't know what it's talking about, but it seems angry.\n"
          "You have a sword.\n")
    type("1. RUN FOR IT!.")
    type("2. Try to bargain.")
    type("3. Fight the demon.")
    choice = input("Make your choice: ")

    if choice == 1:
        run()
    elif choice == 2:
        bargain()
    else:
        fight()


def run():
    type("\nYou turn to run away.\n"
          "As you do, the demon pulls out a sword.\n"
          "You are not fast enough. \n"
          "The demon cries 'EldRitCH SmACKdOwN!!!' and cuts you down.\n"
          "YOU DIED. GAME OVER.\n"
          "Stay and face the darkness.")


def bargain():
    type("\nYou call out to the demon,'WHAT DO YOU WANT FOUL BEAST?'\n"
          "It screams back a reply: 'KnIT3bLAD3, i WIll Not BARGaiN WitH THe LikES Of YoU!!!!!!!!!!!!'\n"
          "The demon draws its sword. \n"
          "You pull out your sword, an elegant blade shining with the power of the holy light. \n"
          "You can feel the power of the runeblade flowing through you as you grasp its hilt. \n"
          "The light of the moon reflects off of the surface, revealing a dazzling shine.\n"
          "The demon slashes at you. You block with your sword. The force of the impact shatters the blade. \n"
          "You have time to mutter a sarcastic 'WOW...' before the demon beheads you. \n"
          "YOU DIED. GAME OVER.\n"
          "'Dormammu, I've come to bargain...'")
main()
