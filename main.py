''' 
improved game by bill and rice
new theme: Lord of the rings
Goal: progress through the game without dying
game status: basically done, could always add more content but it works for now
'''
from room import Room
from character import Enemy, Character, Friend, Neutral
from item import Item

HobbitHole = Room("Hobbit Hole")
HobbitHole.set_description("Humble little house, full of character")

HobbitKitchen = Room("Hobbit Kitchen")
HobbitKitchen.set_description("Surprisingly well equipped for a kitchen of its size")

Cupboard = Room("Cupboard")
Cupboard.set_description("A small, easily missed, room. smells good")

Farmland = Room("Farmland")
Farmland.set_description("An honest farming patch, enough for the village at least")

Forrest = Room("Forrest")
Forrest.set_description("A massive forrest, dense with tree's and foliage")

DustyGrove = Room("DustyGrove")
DustyGrove.set_description("a dusty grove saturated with bushes. there are great big elephants in the distance.")

DeadMarshes = Room("DeadMarshes")
DeadMarshes.set_description("a winding pathway through deadly graveyards")

Mirkwood = Room("Mirkwood")
Mirkwood.set_description("A dingey, dank area saturated with dangerous things")

BossArea = Room("Mordor")
BossArea.set_description("A dangerous place, with volcanoes scattered everywhere")

Hobbiton = Room("Hobbiton")
Hobbiton.set_description("A respectable rural village filled with polite people, and you")

Storage = Room("Storage")
Storage.set_description("a crampt room full of random stuff, and an inhailer")


HobbitHole.link_room(HobbitKitchen, "east", True)
HobbitKitchen.link_room(HobbitHole, "west", True)
HobbitHole.link_room(Farmland, "north", False)
Farmland.link_room(HobbitHole, "south", True)
Farmland.link_room(Forrest, "north", False)
Forrest.link_room(Farmland, "south", True)
Farmland.link_room(Hobbiton, "east", True)
Hobbiton.link_room(Farmland, "west", True)
Hobbiton.link_room(Storage, "east", False)
Storage.link_room(Hobbiton, "west", True)
Forrest.link_room(DeadMarshes, "north", False)
DeadMarshes.link_room(Forrest, "south", True)
Forrest.link_room(DustyGrove, "east", True)
DustyGrove.link_room(Forrest, "west", True)
DeadMarshes.link_room(Mirkwood, "north", False)
Mirkwood.link_room(DeadMarshes, "south", True)
Mirkwood.link_room(BossArea, "north", False)
BossArea.link_room(Mirkwood, "south", True)
HobbitKitchen.link_room(Cupboard, "south", False)
Cupboard.link_room(HobbitKitchen, "north", True)


Gandalf = Friend("Gandalf", "A tall, polite grey wizard")
Gandalf.set_conversation("Good day master Baggins\nThe door is jammed but i can open it for you, so long as i get a drink to recharge my magic")
Gandalf.set_want("tea", "north")
HobbitHole.set_character(Gandalf)

flyGarry = Enemy("Garry the fly", "A tiny fly making an annoying buzzing noise")
flyGarry.set_conversation("Buzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
flyGarry.set_weakness("book", "south")
HobbitKitchen.set_character(flyGarry)

farmerSteve = Neutral("Steve the farmer", "An honest man earning an honest living")
farmerSteve.set_conversation("aye there Bilbo, how are ya?\nDo you by any chance know how to farm?")
farmerSteve.set_weakness("book", "north")
Farmland.set_character(farmerSteve)

rabbitHarry = Neutral("harry the rabbit", "The biggest rabbit you\'ve ever seen")
rabbitHarry.set_conversation("im famished, cant risk farmer Steve hitting me with a pitchfork again :(")
rabbitHarry.set_weakness("carrot", "north")
Forrest.set_character(rabbitHarry)

path = Neutral("a signpost is here ", "\'do not to follow the lights.\'")
path.set_conversation("you need to find a safe path through the marshes")
path.set_weakness("map", "north")
DeadMarshes.set_character(path)

bigBoiDan = Neutral("Dan the dragon", "A massive dragon with asthma, dont let that fool u tho, he can still mess u up")
bigBoiDan.set_conversation("your in my teritory **weeze** now boi **asthma attack - gets out inhaler and takes a breath** drat its ran out, get me a new one and ill spare your life")
bigBoiDan.set_weakness("inhailer", "north")
Mirkwood.set_character(bigBoiDan)

shopKeeper = Neutral("shop keeper", "I have many goods dear boy")
shopKeeper.set_conversation("what i have to offer:\n -farming sythe\n -broadswoard\n -inhailer\n -dead fish\n -book entitled \'how grow melons\'")
shopKeeper.set_weakness("gold", "east")
Hobbiton.set_character(shopKeeper)

boss = Enemy("Morgoth, the First Dark Lord", "edgelord no.1")
boss.set_conversation("And he descended upon Arda in power and majesty greater than any other of the Valar, as a mountain that wades in the sea and has its head above the clouds and is clad in ice and crowned with smoke and fire; and the light of the eyes of Melkor was like a flame that withers with heat and pierces with a deadly cold")
boss.set_weakness("sword")
BossArea.set_character(boss)


tea = Item("tea")
tea.set_description("freshly poured")
HobbitKitchen.set_item(tea)

book = Item("book")
book.set_description("a big book entitled \'farming 101\'")
HobbitHole.set_item(book)

carrot = Item("carrot")
carrot.set_description("very orange, half dug out carrot")
Farmland.set_item(carrot)

gold = Item("gold")
gold.set_description("vary shiny, looks pretty expensive")
Forrest.set_item(gold)

map = Item("map")
map.set_description("dusty, has a lot of blue")
DustyGrove.set_item(map)

inhailer = Item("inhailer")
inhailer.set_description("medical grade goodness")
Storage.set_item(inhailer)

sword = Item("sword")
sword.set_description("An Encharnted Elven Sword: sharper than diamond, glowing in the darkness")
Cupboard.set_item(sword)

current_room = HobbitHole
backpack = []

dead = False
print('hello punie traveler,\neach room has a challenge, to progess to the next section you must complete the problem in each room, either by killing the enemy or assisting a friend to help you on your way\n\nList of commands:\n-talk: talks to character in area\n-north, east, south, west: moves in given direction\n-take: takes current item\n-give: attempts to give character an item\n-fight: attacks the enemy character\n-sing: sing a christmas song\n')
while dead == False:
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()
  
  command = input("> ")
  if command == 'sing':
    lyrics = open('lyrics.txt', 'r')
    print('\n%s' %(''.join(lyrics.readlines())))
    lyrics.close()
  elif command == 'hug':
    inhabitant.hug()
  elif command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
  elif command == "talk":
    if inhabitant is not None:
      inhabitant.talk()
    else:
      print('There is no one to talk to')
  elif command == "give":
    if inhabitant is not None:
      print("What will you give?")
      give_with = input()
      if give_with in backpack:
        if inhabitant.give(give_with) == True:
          print("They let u pass!\nyou can now go " + inhabitant.direction)
          current_room.enableDirection(inhabitant.direction)
          current_room.character = None
      else:
        print("You don't have a " + give_with)
    else:
      print("There is no one here to give")
  elif command == "fight":
    if inhabitant is not None:
      print("What will you fight with?")
      fight_with = input()
      if fight_with in backpack:
        fight = inhabitant.fight(fight_with)
        if fight == True:
          print("Hooray, you won the fight!")
          if inhabitant.direction != '':
            print("you can now go " + inhabitant.direction)
          current_room.enableDirection(inhabitant.direction)
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Congratulations, you have brought peace to the shire!")
            dead = True
        elif fight != 3:
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
        print("You don't have a " + fight_with)
    else:
      print("There is no one here to fight with")
  elif command == "take":
    if item is not None:
      print("You put the " + item.get_name() + " in your backpack")
      backpack.append(item.get_name())
      current_room.set_item(None)
    else:
      print("There's nothing here to take!")
  else:
    print("I don't know how to " + command)
    
  