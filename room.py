class Room():
  
  def __init__(self, room_name):
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.possible = {}
    self.character = None
    self.item = None
    self.completed = False
    
  def set_character(self, new_character):
    self.character = new_character
    
  def get_character(self):
    return self.character 
  
  def set_description(self, room_description):
    self.description = room_description
    
  def get_description(self):
    return self.description
    
  def get_name(self):
    return self.name
    
  def set_name(self, room_name):
    self.name = room_name 
  
  def get_item(self):
    return self.item
    
  def set_item(self, item_name):
    self.item = item_name
  
  def describe(self):
    print(self.description)
    
  def link_room(self, room_to_link, direction, possible):
    self.linked_rooms[direction] = room_to_link
    self.possible[direction] = possible
    #print( self.name + " linked rooms: " + repr(self.linked_rooms))
  
  def enableDirection(self, direction):
    self.possible[direction] = True
  
  def get_details(self):
    print(self.name)
    print("--------------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      poss = self.possible[direction]
      if not poss:
        go = ' but you cant go that way yet'
      else:
        go = ''
      print("The " + room.get_name() + " is " + direction + go)
  
  def move(self, direction):
    if direction in self.linked_rooms and self.possible[direction] == True:
      return self.linked_rooms[direction]
    elif direction in self.linked_rooms:
      print('you need to complete the room to go ' + direction)
      return self
    else:
      print("You can't go that way")
      return self