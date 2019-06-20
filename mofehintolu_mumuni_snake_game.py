
def showinstructions():
    #print a main menu and the commands
    print('''
    RPG GAME
    ==========
    'Get to the garden with a key and a  coin'
    'Avoid the monkeys!'

    Commands:
        go [direction]
        get [item]
        ''')
def showstatus():
    #print the player's current status
    print('---------------')
    print('You are in the ' + currentroom)
    #print the current inventory
    print('Inventory: '+ str(inventory))
    #print an item if there is one
    if 'item' in rooms[currentroom]:
        print('You see a '+ rooms[currentroom]['item'])
    print('------------------')


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms ={
    'Parlor' : {
        'south' : 'kitchen',
        'east'  : 'Dining room',
        'west'  : 'Master bedroom',
        'north' : 'Balcony',
        'item'  : 'key'
    },
    'kitchen'  : {
        'west'  : 'Dining room',
        'east'  : 'Garage',
        'north' :  'Bathroom',
        'item'  : 'malt'
    },
    'Dining room' : {
        'west'  : 'Master bedroom',
        'south' :  'Bathroom',
        'item'   : 'coin'
    },
    'Bathroom'  : {
        'east'  : 'Master bedroom',
        'west'  : 'Laundry',
    },
    'Balcony' : {
        'south' : 'Parlor',
        'item'  : 'carton'
    },
'Master bedroom' : {
        'east'  : 'Garage',
        'south' : 'Visitors bedroom',
        'item'  : 'box'
    },
'Visitors bedroom' : {
        'south' : 'Laundry',
        'north' : 'Master bedroom',
        'item'  : 'snake'
    },""
'Laundry' : {
        'north' : 'Visitors bedroom',
        'item'  : 'monkey'
    },
'Garage' : {
        'north' : 'Garden',
        'item'  : 'car_brush'
    }

}
#start the player in the parlor
currentroom = 'Parlor'
showinstructions()

#loop forever
while True:
    showstatus()
            #player looses if they enter a room with a monkey
    if 'item' in rooms[currentroom] and 'monkey' in rooms[currentroom]['item']:
        print('A monkey has got you ..... GAME OVER!')
        break
             #player looses if they enter a room with a snake
    if 'item' in rooms[currentroom] and 'snake' in rooms[currentroom]['item']:
        print('A Snake has got you ..... GAME OVER!')
        break

    #get the players next 'move'
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()
    #if the player types 'go' first
    if move[0] == 'go':
        #check that they are allowed to move wherever they want to go
        if move[1] in rooms[currentroom]:
            #set the current room to the new room
            currentroom = rooms[currentroom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        if len(inventory) == 0 and move [1] == 'carton':

            #if the room contains an item, and the item is the only one they want to get
            if 'item' in rooms[currentroom] and move[1] in rooms[currentroom]['item']:

                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + 'got!')
                #delete the item from the room
                del rooms[currentroom]['item']

             #otherwise, if the item isn't there to get
            else:
                #tell them they cant get it
                print('Can\'t get ' + move[1] + '!')
        else:
            if len(inventory) == 0 and move [1] != 'carton':
                #tell them they cant get it
                print('You need to get the Carton first from the Balcony!')

        if len(inventory) > 0 and move [1] != 'carton':

        #if the room contains an item, and the item is the only one they want to get
            if 'item' in rooms[currentroom] and move[1] in rooms[currentroom]['item']:

                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + 'got!')
                #delete the item from the room
                del rooms[currentroom]['item']

            #otherwise, if the item isn't there to get
            else:
                #tell them they cant get it
                print('Can\'t get ' + move[1] + '!')
        else:
            if len(inventory) > 0 and move [1] != 'carton':
                #tell them they cant get it
                print('You need to get the Carton first from the Balcony!')

    #player looses if they enter a room with a monkey
        if 'item' in rooms[currentroom] and 'monkey' in rooms[currentroom]['item']:
            print('A monkey has got you ..... GAME OVER!')
             #player looses if they enter a room with a snake
        if 'item' in rooms[currentroom] and 'snake' in rooms[currentroom]['item']:
            print('A Snake has got you ..... GAME OVER!')
    #player wins if they get to the Garden with a key,a coin, a carton, a malt, a box, and a car_brush
    if currentroom == 'Garden' and 'carton' in inventory and 'coin' in inventory and 'key' in inventory and 'malt' in inventory and 'car_brush' in inventory and 'box' in inventory:
        print('You escaped the house to the Garden....... HURRAY YOU WIN!')
        break