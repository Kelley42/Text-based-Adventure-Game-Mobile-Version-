import textwrap

death_count = 0
breakpoint = 0
weapon = False
wrapper = textwrap.TextWrapper(width=38, break_long_words=False, replace_whitespace=False, subsequent_indent='   ')

# Defs
def intro():
    global death_count, wrapper
    death_count = 0

    print(wrapper.fill(text = "\n--->\tA storm has shipwrecked you and your crew on a tropical island. There are rumors that the island had a terrible curse put upon it long ago. Numerous treasure ships have mysteriously sunk along its coast, and the few who survived insisted that anyone who stepped foot on land was never seen again.\n\tNight has fallen and you have woken up on the beach alone in the cold rain. You can't see or hear any of your crew members. Cold and wet, you can't stop shivering. Suddenly you hear rustling in the bushes behind you.\n"))

    beach()


def beach():
    global death_count, breakpoint, wrapper
    breakpoint = 1

    beach_response = input(wrapper.fill(text = "\nWhat do you do? Run into the water, check out the bushes, or stay put? ")).lower()
  
    beach_answer1 = ["run", "into", "water"]
    beach_answer2 = ["check", "out", "bushes"]
    beach_answer3 = ["stay", "put"]

    if any(match in beach_response for match in beach_answer1):
        print(wrapper.fill(text = "\n--->\tOh, no! A very large sea monster has eaten you. That's too bad.\n"))
        game_over()
    elif any(match in beach_response for match in beach_answer2):
        see_shape()
    elif any(match in beach_response for match in beach_answer3):
        hungry()
    else:
        error()
        beach()


def see_shape():
    global death_count, breakpoint, wrapper
    breakpoint = 2

    print(wrapper.fill(text = "\n--->\tYou bravely check the bushes for the source of the noise. It's so dark you can barely see your hand in front of your face. You hear rustling again. A huge shadow appears in front of you. You can feel its presence more than you can see it. In the darkness it appears blacker than night... and has the outline of a person.\n"))

    see_shape_response = input(wrapper.fill(text = "\nDo you run away, attack, or talk to the person? ")).lower()
  
    see_shape_answer1 = ["run", "away"]
    see_shape_answer2 = ["attack"]
    see_shape_answer3 = ["talk", "person"]

    if any(match in see_shape_response for match in see_shape_answer1):
        print(wrapper.fill(text = "\n--->\tYou run away. Unfortunately, you run into a tree, shaking a coconut loose. Your hard head is no match for a falling coconut.\n"))
        game_over()
    elif any(match in see_shape_response for match in see_shape_answer2):
        print(wrapper.fill(text = "\n--->\tYou jump at the shape, attacking it with all your strength and tackling it to the ground. Unfortunately, the thing you attacked has a weapon and you don't. You lose.\n"))
        game_over()
    elif any(match in see_shape_response for match in see_shape_answer3):
        talk_crew()
    else:
        error()
        see_shape()


def talk_crew():
    global death_count, breakpoint, wrapper
    breakpoint = 3

    print(wrapper.fill(text = '\n--->\tIn a shaky voice, you whisper, "Hello?" The shape answers back, "It\'s you! I\'m so glad I found you."\n\tYou recognize the voice. It belongs to Stefansson, your friend and favorite crew member. You\'re so relieved!\n\tThen he grabs your arm. "I haven\'t been able to find anyone else. But I hear them. I hear the whispers. Have you heard them? They\'re all around us. Shhh... do you hear them? Come, let\'s get out of this rain. I found some shelter higher up. Come with me!"\n'))

    talk_crew_response = input(wrapper.fill(text = "\nDo you go with him or run away? ")).lower()

    talk_crew_answer1 = ["go", "with", "him"]
    talk_crew_answer2 = ["run", "away"]

    if any(match in talk_crew_response for match in talk_crew_answer1):
        crew_center()
    elif any(match in talk_crew_response for match in talk_crew_answer2):
        print(wrapper.fill(text = "\n--->\tYou run away. Unfortunately, you run into a tree, shaking a coconut loose. Your hard head is no match for a falling coconut.\n"))
        game_over()
    else:
        error()
        talk_crew()
    

def crew_center():
    global death_count, breakpoint, wrapper
    breakpoint = 4

    print(wrapper.fill(text = '\n--->\tStefansson\'s words frighten you, but you decide to follow him anyway. Anything to get out of this rain. You follow him, slowly and carefully, on a sandy path that cuts into the island. The trees close in on you more and more, wet leaves slapping your face and arms, and the path narrows until it\'s almost impossible to travel further.\n\tFinally you reach a rocky wall with a winding path to the top. The two of you climb together, hands and knees trying to find anything to grip in the slippery surface, until you reach the top of a ledge. There he shows you his makeshift shelter of broken tree branches and leaves. It\'s not much, but it\'s better than the beach.\n\t"We\'ll stay here tonight," he says. "Sleep. Tomorrow we go to the interior of the island. There is treasure there."\n\tTreasure! Has he really seen treasure? Before you can ask, he adds, "And also that\'s where the voices come from. We will go and stop the voices. The voices. Shhh... Do you hear them?"\n'))

    crew_center_response = input(wrapper.fill(text = "\nDo you go to sleep, make a weapon, or run away? ")).lower()

    crew_center_answer1 = ["go", "sleep"]
    crew_center_answer2 = ["make", "weapon"]
    crew_center_answer3 = ["run", "away"]

    if any(match in crew_center_response for match in crew_center_answer1):
        hear_whispers()
    elif any(match in crew_center_response for match in crew_center_answer2):
        make_weapon()
    elif any(match in crew_center_response for match in crew_center_answer3):
        print(wrapper.fill(text = "\n--->\tYou run away. Unfortunately, you slip off the rocky ledge and fall to your untimely death.\n"))
        game_over()
    else:
        error()
        crew_center()
  

def hear_whispers():
    global death_count, breakpoint, wrapper
    breakpoint = 5

    print(wrapper.fill(text = "\n--->\tYou decide to trust your dear friend Stefansson. You lay down and try to fall asleep. Through the wind and rain, you swear you hear something else. Are those whispers?\n"))

    hear_whispers_response = input(wrapper.fill(text = "\nDo you go back to sleep or make a weapon? ")).lower()

    hear_whispers_answer1 = ["go", "sleep"]
    hear_whispers_answer2 = ["make", "weapon"]

    if any(match in hear_whispers_response for match in hear_whispers_answer1):
        cave_tunnel()
    elif any(match in hear_whispers_response for match in hear_whispers_answer2):
        make_weapon()
    else:
        error()
        hear_whispers()


def make_weapon():
    global death_count, breakpoint, wrapper, weapon
    breakpoint = 6

    print(wrapper.fill(text = "\n--->\tYou decide to make a weapon. Surely the voices aren't real, but still a weapon would be nice to have. Especially with Stefansson's delusional ramblings. What if he becomes dangerous?\n\tOnce he falls asleep and the rain has nearly stopped, you get up and sneak outside the makeshift shelter in search of a weapon. You look around but all you see are rocks and branches. You could try to use branches to make a bow and arrow or a sharpened stick. Or you could just grab a big rock.\n"))

    make_weapon_response = input(wrapper.fill(text = "\nWhich weapon will you get? Bow and arrow, sharpened stick, or big rock? ")).lower()

    make_weapon_answer1 = ["bow", "arrow"]
    make_weapon_answer2 = ["sharpened", "stick"]
    make_weapon_answer3 = ["big", "rock"]

    if any(match in make_weapon_response for match in make_weapon_answer1):
        print(wrapper.fill(text = "\n--->\tYou try to make a bow and arrow out of tree branches. Unfortunately, the wood is too wet. In frustration, you throw the branches down and stomp your feet. In your tantrum, you slip and you fall... off the rocky ledge and to your death.\n"))
        game_over()
    elif any(match in make_weapon_response for match in make_weapon_answer2):
        print(wrapper.fill(text = "\n--->\tYou decide to fashion a sharpened stick out of a thick branch. Now that you have a weapon, you feel safer.\n"))
        weapon = True
        cave_tunnel()
    elif any(match in make_weapon_response for match in make_weapon_answer3):
        print(wrapper.fill(text = "\n--->\tJust as you're grabbing the largest rock you can find, Stefansson walks up behind you. Seeing you with the rock in your hand, he grows suspicious of your intentions. He finds an equally large rock and hits you on the head with it.\n"))
        game_over()
    else:
        error()
        make_weapon()


def cave_tunnel():
    global death_count, breakpoint, wrapper
    breakpoint = 7

    print(wrapper.fill(text = "\n--->\tYou go to sleep and in the morning Stefansson is waiting for you to follow him further into the interior of the island. He promises you there is treasure on this island. He saw it last night.\n\tYou agree to follow him along a path through dense underbrush. Sometimes the forest is so thick that you lose him for a few minutes, only finding him again through glimpses of frazzled blond hair bobbing ahead of you.\n\tHours later you come upon an opening in a rock face. It's the opening to some sort of cave or tunnel.\n\tStefansson fashions a torch out of a tree branch and you both walk into the winding dark tunnel. You hear scrabbling sounds on the walls around you, but see nothing in the torchlight. After what seems like miles of endless tunnel and echoing footsteps, you see three paths open up in front of you.\n"))

    cave_tunnel_response = input(wrapper.fill(text = "\nDo you take the left, the middle, or the right path? ")).lower()
  
    cave_tunnel_answer1 = ["left"]
    cave_tunnel_answer2 = ["middle"]
    cave_tunnel_answer3 = ["right"]

    if any(match in cave_tunnel_response for match in cave_tunnel_answer1):
        print(wrapper.fill(text = "\n--->\tYou choose the left path. As you walk a little farther on, you notice the ground sloping steeply downward. You both slip and fall, the ground becoming as slippery as a slide.\n\tYou fall for what feels like ages as the slide weaves this way and that, eventually dumping you into a crystal clear lake surrounded by an open clearing in the forest.\n\tSwimming up to the surface, you see the most beautiful waterfall pouring into the lake. Feeling the silky water on your skin, you suddenly have no memory of how you came to be here. All you know is this place is your home and you are ruler over it all.\n\tYou decide to climb to the top of the island's highest peak to make a throne for yourself there and declare yourself ruler of the island. Unfortunately, the highest peak is a volcano and you are not careful. You fall into lava and die.\n"))
        game_over()
    elif any(match in cave_tunnel_response for match in cave_tunnel_answer2):
        print(wrapper.fill(text = "\n--->\tYou choose the middle path. As you walk a little farther on, you notice you are in a small chamber. As Stefansson shines the torchlight around, the doorway starts to seal itself. You notice smoke filling the room. Through your last coughing gasps for air, you realize you are breathing poisonous gas.\n"))
        game_over()
    elif any(match in cave_tunnel_response for match in cave_tunnel_answer3):
        rat()
    else:
        error()
        cave_tunnel()


def rat():
    global death_count, breakpoint, wrapper, weapon
    breakpoint = 8

    print(wrapper.fill(text = "\n--->\tYou choose the right path. As you walk a little farther on, you notice you are in a hallway with ropes hanging here and there from the ceiling and walls. There is a weird smell all around you.\n\tYou see a rat on the wall beside you, gnawing on one of the ropes.\n"))

    if weapon == False:
        print(wrapper.fill(text = "\n\tUnfortunately, the rope the rat is chewing was an important rope. It was holding up an array of sharp spears hanging from the ceiling. With the rope now chewed through, the spears come crashing down into you... and through you.\n"))
        game_over()
    else:    
        print(wrapper.fill(text = "\tWith your sharpened knife, you kill it. You are so hungry. Finally you have something to eat.\n"))

        rat_response = input(wrapper.fill(text = "\nDo you eat the rat or leave it? ")).lower()

        rat_answer1 = ["eat", "rat"]
        rat_answer2 = ["leave"]

        if any(match in rat_response for match in rat_answer1):
            print(wrapper.fill(text = "\n--->\tFinally! You get to eat something. You use Stefansson's torch to cook the rat, and you both sit down to enjoy the small meal.\n\tUnfortunately, whatever you sat on just shifted under your weight. Seems it was a lever of some kind to spring a trap. The room floods with water and you both drown.\n"))
            game_over()
        elif any(match in rat_response for match in rat_answer2):
            center_island()
        else:
            error()
            rat()


def center_island():
    global death_count, breakpoint, wrapper
    breakpoint = 9

    print(wrapper.fill(text = '\n--->\tYou keep traveling further into the depths of the island. The tunnel seems to go on forever.\n\tFinally it opens into a huge chamber. The light from Stafansson\'s torch doesn\'t reach to the edges of the room, but you can hear scratching noises there.\n\tIn fact, you can hear noises everywhere. And whispers.And shrieks. And the scratching sound of claws....\n\tYou are at last at the heart of the island, in what seems like the depths of Hell, and all you see are monstrous spirits encircling you both.\n\tAs the wispy shades of blackness fly past you, they screech in your ear, pull at your hair and clothes, and pour ice into your veins.\n\tSome of these faces you can almost make out, they look so familiar... as if they had once been your old crew members. One of them even has the same hair as Stefansson. And the voice sounds so similar to his as it flashes past.\n\tYou realize the Stefansson beside you is not the real Stefansson\n\tAs his eyes turn toward yours, you feel a shift in the air around you, a heaviness, an electricity. And suddenly his eyes become sunken holes, his mouth twisting into something that no longer looks like a mouth.\n\tAnd then you realize this whole thing was a trap. That he lured everyone else here just like you.\n\tYou notice movement in the darkness. Enormous figures crouch in the corners, rising up as you watch in horror. More claws scraping against the ground.\n\tUp above, on a ledge jutting out from the rocky wall, something glistens in the torchlight. A sea of glittering objects blankets the ledge.\n'))

    center_island_response = input(wrapper.fill(text = "\nDo you run away, stab a creature, attack Stefansson, or try to reach the ledge? ")).lower()

    center_island_answer1 = ["run", "away"]
    center_island_answer2 = ["stab", "creature"]
    center_island_answer3 = ["attack", "Stefansson"]
    center_island_answer4 = ["try", "reach", "ledge"]

    if any(match in center_island_response for match in center_island_answer1):
        print(wrapper.fill(text = "\n--->\tYou run as fast as you can out of the chamber. No treasure is worth that. In your haste, you fall through a trap door in the floor and into a pit of sharp spears.\n"))
        game_over()
    elif any(match in center_island_response for match in center_island_answer2):
        print(wrapper.fill(text = "\n--->\tYou pull the sharpened stick out of your pocket and run at the nearest hulking shape. You try to stab it, but it's too fast for you. It takes less than two seconds for it to slash you with it's powerful claws.\n"))
        game_over()
    elif any(match in center_island_response for match in center_island_answer3):
        print(wrapper.fill(text = "\n--->\tYou pull out your sharpened stick and lunge at the fake Stefansson. But you slowly realize, with his face that no longer looks like a face, ancient evil like this cannot be killed. You feel coldness in your veins, creeping toward your heart, and you understand that you will now join the rest of your crew....\n"))
        game_over()
    elif any(match in center_island_response for match in center_island_answer4):
        treasure()
    else:
        error()
        center_island()


def treasure():
    global death_count, breakpoint, wrapper
    breakpoint = 10

    print(wrapper.fill(text = "\n--->\tYou run to the far side of the room, your eyes on the treasure. You narrowly avoid a mass of sharp claws swiping toward your face. You skid to a stop under the ledge. There are strings of vines hanging all over the walls and ceiling. You also notice the walls aren't smooth but have grooves cut into them.\n"))
  
    treasure_response = input(wrapper.fill(text = "\nDo you swing on a vine or climb the wall? ")).lower()

    treasure_answer1 = ["swing", "vine"]
    treasure_answer2 = ["climb", "wall"]

    if any(match in treasure_response for match in treasure_answer1):
        print(wrapper.fill(text = "\n--->\tYou grab a vine and attempt to swing toward the ledge. Unfortunately, you've watched too many action movies because this rarely works in real life. You crash to the ground, and the monstrous creatures devour you. At least now you are reunited with your crew in the afterlife.\n"))
        game_over()
    elif any(match in treasure_response for match in treasure_answer2):
        ending()
    else:
        error()
        treasure()


def ending():
    global death_count, breakpoint, wrapper
    breakpoint = 11

    print(wrapper.fill(text = "\n--->\tYou have always been a fan of parkour, and now you finally get to put the skills you've only watched but never actually practiced to good use. Your fingers and feet find every groove, and your legs launch you to the platform holding the treasure. You kneel, sifting the gold coins and colored jewels between your fingers. So many trinkets and baubles and - a chest! Larger than you ever imagined.You reach out to it...and stop. Should you open the chest?\n"))

    ending_response = input("\nYes or no? ").lower()

    ending_answer1 = ["yes", "y"]
    ending_answer2 = ["no", "n"]

    if any(match in ending_response for match in ending_answer1):
        print(wrapper.fill(text = '\n--->\tYou open the treasure chest! Hooray!\n\tUnfortunately, this was the trap set for all who land on the island who manage to make it this far.\n\tYou have fallen victim to the curse of Treasure Island. All who open the chest of Captain Roberto "Bones" Luis\'s treasure become trapped souls on the island forever. But at least you are reunited with your beloved crew.\n'))
        game_over()
    elif any(match in ending_response for match in ending_answer2):
        print(wrapper.fill(text = "\n--->\tYou decide not to open the chest. There's enough treasure laying by your feet, and you won't even be able to carry much of that out of here. Maybe you'll just leave it all here. If you ever make it out alive, you don't want to have any piece of this dreadful place with you.\n\tNow you just need a plan to escpae. You see a tiny space in the wall ahead and squeeze through. It's a secret tunnel out of the chamber. Hunching over, you run as fast as you can through the narrow tunnel. Through zigs and zags, miles upon miles, you finally make it back to the forest, and then to the beach.\n\tJust as the sun begins to set, you see a small brown dot upon the horizon growing larger. As it comes nearer, you can make out a mast and a sail, and you smile.\n\nTHE END!\n"))
        restart()
    else:
        error()
        ending()


def hungry():
    global death_count, breakpoint, wrapper
    breakpoint = 12

    print(wrapper.fill(text = "\n--->\tYou decide to stay put until daylight. No need to go running around in the dark in a strange place. When you wake up, it is finally daylight. You are so hungry.\n"))

    hungry_response = input(wrapper.fill(text = "Do you explore the island for food, climb a coconut tree, or stay put? ")).lower()

    hungry_answer1 = ["explore", "island", "food"]
    hungry_answer2 = ["climb", "coconut", "tree"]
    hungry_answer3 = ["stay", "put"]

    if any(match in hungry_response for match in hungry_answer1):
        waterfall()
    elif any(match in hungry_response for match in hungry_answer2):
        print(wrapper.fill(text = "\n--->\tYou decide to climb a nearby coconut tree and see if you can knock a coconut off. You saw someone do it in a movie once, and it didn't look too hard.\n\tUnfortunately, today is not your day. You get all the way up to the tree, slip and fall, and a coconut smashes onto your head.\n"))
        game_over()
    elif any(match in hungry_response for match in hungry_answer3):
        print(wrapper.fill(text = "\n--->\tYou decide to stay put a little longer. It just really doesn't seem very safe here. Maybe a rescue ship will come by soon? You fall asleep on the beach. Unfortunately this is feeding time for the giant sand crabs on this island. Guess you weren't the only one who was hungry.\n"))
        game_over()
    else:
        error()
        hungry()


def waterfall():
    global death_count, breakpoint, wrapper
    breakpoint = 13

    print(wrapper.fill(text = "\n--->\tWhile scouring the island for food, searching high and low in the jungle for anything edible, you come across a magnificient waterfall and crystal clear lake.\n"))

    waterfall_response = input(wrapper.fill(text = "Do you drink from the lake, bathe in it, or go behind the waterfall? ")).lower()

    waterfall_answer1 = ["drink", "lake"]
    waterfall_answer2 = ["bathe"]
    waterfall_answer3 = ["go", "behind", "waterfall"]

    if any(match in waterfall_response for match in waterfall_answer1):
        print(wrapper.fill(text = "\n\--->tYou are so thirsty that you decide to drink from the luscious cool water. Unfortunately, something is wrong with this water. Immediately after drinking it, you fall into an everlasting sleep.\n"))
        game_over()
    elif any(match in waterfall_response for match in waterfall_answer2):
        print(wrapper.fill(text = "\n--->\tYou are so hot and dirty from trudging through the jungle all day. You really just want to get clean.\n\tUnfortunately, there's something not quite right about this lake.\n\tAfter a few moments in the silky water, you suddenly have no idea why you're here or how you got here. All you know is this place is your home and you are ruler over it all. You decide to climb to the top of the island's highest peak to make a throne for yourself there and declare yourself ruler of the island. Unfortunately, the highest peak is a volcano and you are not careful. You fall into lava and die.\n"))
        game_over()
    elif any(match in waterfall_response for match in waterfall_answer3):
        behind_waterfall()
    else:
        error()
        waterfall()


def behind_waterfall():
    global death_count, breakpoint, wrapper
    breakpoint = 14

    print(wrapper.fill(text = "\n--->\tYou decide to go behind the waterfall. Maybe there will be a secret cave. Yes! You manage to make it safely behind the waterfall and find an entrance to a tunnel. You find that a little light is able to make it into the entrance and you can see something on the walls. It looks like drawings. Suddenly you hear noises.\n"))

    behind_waterfall_response = input(wrapper.fill(text = 'Do you look at the drawings, call out, or run away? ')).lower()

    behind_waterfall_answer1 = ["look", "drawings", "drawing"]
    behind_waterfall_answer2 = ["call", "out"]
    behind_waterfall_answer3 = ["run", "away"]

    if any(match in behind_waterfall_response for match in behind_waterfall_answer1):
        drawing()
    elif any(match in behind_waterfall_response for match in behind_waterfall_answer2):
        print(wrapper.fill(text = '\n--->\tYou call out, "Hello?" You\'re hoping to hear the voice of one of your crew.\n\tUnfortunately, it\'s not a person who answers. You see a massive creature that nature has no name for charging headlong at you. You barely get out the beginnings of a scream before it crashes into you and eats you for lunch.\n'))
        game_over()
    elif any(match in behind_waterfall_response for match in behind_waterfall_answer3):
        print(wrapper.fill(text = "\n--->\tYou run away, back toward the waterfall. But it's very slippery, and you fall over the edge into the lake.\n\tAfter a few moments in the silky water, you suddenly have no idea why you're here or how you got here. All you know is this place is your home and you are ruler over it all. You decide to climb to the top of the island's highest peak to make a throne for yourself there as ruler of the island. Unfortunately, the highest peak is a volcano and you are not careful. You fall into lava and die.\n"))
        game_over()
    else:
        error()
        behind_waterfall()


def drawing():
    global death_count, breakpoint, wrapper
    breakpoint = 15

    print(wrapper.fill(text = '\n--->\tYou decide to look more carefully at the drawings on the cave wall. Maybe it will give you a clue to what lies in the cave.\n\tThrough the little bit of light streaming through the waterfall nearby, you can see outlines of animals on the walls. Except you can\'t tell what kind of animals these are. They look unfamiliar somehow. You swear the red paint smeared in places across the drawings looks an awful lot like blood.\n\tAnd underneath one of the drawings, it looks like someone carved "Aaaaaahhhhh" into the wall.\n'))

    drawing_response = input(wrapper.fill(text = "Do you go further into the cave or run away? ")).lower()

    drawing_answer1 = ["go", "further", "cave"]
    drawing_answer2 = ["run", "away"]

    if any(match in drawing_response for match in drawing_answer1):
        center_island2()
    elif any(match in drawing_response for match in drawing_answer2):
        print(wrapper.fill(text = "\n--->\tYou run away, back toward the waterfall. But it's very slippery, and you fall over the edge into the lake.\n\tAfter a few moments in the silky water, you suddenly have no idea why you're here or how you got here. All you know is this place is your home and you are ruler over it all. You decide to climb to the top of the island's highest peak to make a throne for yourself there as ruler of the island. Unfortunately, the highest peak is a volcano and you are not careful. You fall into lava and die.\n"))
        game_over()
    else:
        error()
        drawing()


def center_island2():
    global death_count, breakpoint, wrapper
    breakpoint = 16

    print(wrapper.fill(text = '\n--->\tYou keep traveling further into the depths of the island. The tunnel seems to go on forever, an endless walk into darkness.\n\tFinally it splits into two paths, one that slopes gently down and another that rises sharply upward.\n'))

    center_island2_response = input(wrapper.fill(text = "Do you take the path that goes down or up? ")).lower()

    center_island2_answer1 = ["down"]
    center_island2_answer2 = ["up"]

    if any(match in center_island2_response for match in center_island2_answer1):
        print(wrapper.fill(text = "\n--->\tYou take the path that leads down. Unfortunately, this tunnel is flooded with something that doesn't look or smell like water. You decide not to risk wading through it and turn back.\n"))
        center_island2()
    elif any(match in center_island2_response for match in center_island2_answer2):
        print(wrapper.fill(text = "\n--->\tYou take the path that leads up. This path is at such a steep incline that you have to climb on your hands and knees at some points. Finally it levels out, and you stand up in relief. Just then, a pair of bats emerge from the ceiling and fly toward your face. You scream, flail your arms about, and lose your balance. You fall back down the steep tunnel, break several bones, and smash your head against the wall.\n"))
        game_over()
    else:
        error()
        center_island2() 


def error():
    print("!!!Incorrect response - try again!!!")


def restart():
    restart_response = input("\nPlay again? Yes or no? ").lower()

    restart_answer1 = ["yes", "y"]
    restart_answer2 = ["no", "n"]

    if any(match in restart_response for match in restart_answer1):
        intro()
    if any(match in restart_response for match in restart_answer2):
        exit()


def quit():
    quit_response = input("Quit game? Yes or no? ").lower()

    quit_answer1 = ["no", "n"]
    quit_answer2 = ["yes", "y"]

    if any(match in quit_response for match in quit_answer1):
        intro()
    elif any(match in quit_response for match in quit_answer2):
        exit()
    else:
        error()
        quit()


def game_over():
    global death_count, breakpoint
    death_count += 1
    lives = 3 - death_count
    print("You lost a life!\n")
    print(f"Lives Remaining: {lives}")

    # If this is their 3rd GAME OVER, they must start over at the beginning.
    if death_count == 3:
        print("GAME OVER!\n")
        restart()

    # Otherwise they get to choose to start over or just go back one step and redo last action. 
    else:
        start_over_response = input("Try again? Yes or No? ").lower()

        start_over_answer1 = ["no", "n"]
        start_over_answer2 = ["yes", "y"]
  
        if any(match in start_over_response for match in start_over_answer1):
            quit()

        elif any(match in start_over_response for match in start_over_answer2):

            # Breakpoints to revert to different parts of the story:
            if breakpoint == 1:
                beach()
            if breakpoint == 2:
                see_shape()
            if breakpoint == 3:
                talk_crew()
            if breakpoint == 4:
                crew_center()
            if breakpoint == 5:
                hear_whispers()
            if breakpoint == 6:
                make_weapon()
            if breakpoint == 7:
                cave_tunnel()
            if breakpoint == 8:
                rat()
            if breakpoint == 9:
                center_island()
            if breakpoint == 10:
                treasure()
            if breakpoint == 11:
                ending()
            if breakpoint == 12:
                hungry()
            if breakpoint == 13:
                waterfall()
            if breakpoint == 14:
                behind_waterfall()
            if breakpoint == 15:
                drawing()
            if breakpoint == 16:
                center_island2()
        else:
            error()
            game_over()
    

# Beginning of story
print("\n\tWelcome to Treasure Island.\n")
print(wrapper.fill(text = "\tYour mission is to find the treasure.\n"))    

intro()