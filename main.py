''' 
improved game by bill and rice
new theme: Lord of the rings
Goal: surive
'''
from room import Room
from character import Enemy, Character, Friend, Neutral
from item import Item

HobbitHole = Room("Hobbit Hole")
HobbitHole.set_description("pleasant little hole, small but cosy")

HobbitKitchen = Room("Hobbit Kitchen")
HobbitKitchen.set_description("definitely not the biggest kitchen, but a kitchen none the less")

Farmland = Room("Farmland")
Farmland.set_description("A large expanse of grass, fields and meadows")

Forrest = Room("Forrest")
Forrest.set_description("A massive forrest, dense with tree's and foliage")

Mirkwood = Room("Mirkwood")
Mirkwood.set_description("A dingey, dank area saturated with dangerous things")

Hobbiton = Room("Hobbiton")
Hobbiton.set_description("A respectable rural village filled with polite people, and you")


HobbitHole.link_room(HobbitKitchen, "east", True)
HobbitKitchen.link_room(HobbitHole, "west", True)
HobbitHole.link_room(Farmland, "north", False)
Farmland.link_room(HobbitHole, "south", True)
Farmland.link_room(Forrest, "north", False)
Forrest.link_room(Farmland, "south", True)
Farmland.link_room(Hobbiton, "east", False)
Hobbiton.link_room(Farmland, "west", True)
Forrest.link_room(Mirkwood, "north", False)
Mirkwood.link_room(Farmland, "south", True)


Gandalf = Friend("Gandalf", "A tall grey wizard with a long ass stick")
Gandalf.set_conversation("Good day master Baggins")
Gandalf.set_want("tea n biscuits", "north")
HobbitHole.set_character(Gandalf)

flyGarry = Enemy("Garry the fly", "A tiny fly making an annoying buzzing noise")
flyGarry.set_conversation("Buzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
flyGarry.set_weakness("book")
HobbitKitchen.set_character(flyGarry)

farmerSteve = Neutral("Steve the farmer", "An honest man earning an honest living")
farmerSteve.set_conversation("aye there Bilbo, how are ya?\nDo you by any chance know how to farm?")
farmerSteve.set_weakness("book", "east")
Farmland.set_character(farmerSteve)

rabbitHarry = Neutral("harry the rabbit", "The biggest rabbit you\'ve ever seen")
rabbitHarry.set_conversation("im famished, cant risk farmer Steve hitting me with a pitchfork again :(")
rabbitHarry.set_weakness("carrot", "north")
Forrest.set_character(rabbitHarry)

bigBoiDan = Neutral("Dan the dragon", "A big-ass dragon with asthma, dont let that fool u tho, he can still mess u up")
bigBoiDan.set_conversation("your in my teritory **weeze** now boi **asthma attack - gets out inhaler and takes a breath** drat its ran out, get me a new one and ill spare your life")
bigBoiDan.set_weakness("inhailer", "north")
Mirkwood.set_character(bigBoiDan)

shopKeeper = Neutral("shop keeper", "I have many goods dear boy")
shopKeeper.set_conversation("what i have to offer:\n -farming sythe\n -broadswoard\n -inhailer\n -dead fish\n -book entitled \'how grow melons\'")
shopKeeper.set_weakness("gold", "west")
Hobbiton.set_character(shopKeeper)


tea_n_biscuits = Item("tea n biscuits")
tea_n_biscuits.set_description("freshly poured")
HobbitKitchen.set_item(tea_n_biscuits)

book = Item("book")
book.set_description("a big book entitled \'farming 101\'")
HobbitHole.set_item(book)

carrot = Item("carrot")
carrot.set_description("very orange, half dug out carrot")
Farmland.set_item(carrot)

gold = Item("gold")
gold.set_description("shiny af, looks pretty expensive")
Forrest.set_item(gold)

inhailer = Item("inhailer")
inhailer.set_description("medical grade goodness")
Hobbiton.set_item(inhailer)

current_room = HobbitHole
backpack = []

dead = False
print('''hello punie traveler,\neach room has a challenge, to progess to the next section you must complete the problem in each room, either by killing the enemy or assisting a friend to help you on your way in return\nhave fun :)''')
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
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "give":
    if inhabitant is not None:
      # Fight with the inhabitant, if there is one
      print("What will you give?")
      give_with = input()
      # Do I have this item?
      if give_with in backpack:
        if inhabitant.give(give_with) == True:
          # What happens if you win?
          print("They let u pass!\nyou can now go " + inhabitant.direction)
          current_room.enableDirection(inhabitant.direction)
          current_room.character = None
      else:
        print("You don't have a " + fight_with)
    else:
      print("There is no one here to fight with")
  elif command == "fight":
    if inhabitant is not None:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      # Do I have this item?
      if fight_with in backpack:
        if inhabitant.fight(fight_with) == True:
          # What happens if you win?
          print("Hooray, you won the fight!")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Congratulations, you have vanquished the enemy horde!")
            dead = True
        else:
          # What happens if you lose?
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
    
  