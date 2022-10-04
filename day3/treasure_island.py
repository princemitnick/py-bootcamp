print('''
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
miK     `':::_:' -- '' -'-' `':_::::'`
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

direction = input('You\'re at the cross road. Where do you want to go? Type "left" or  "right" :').lower()

if direction == "left":
    action = input('You come to a lake. There is an island in the middle of the lake. Type '
                   '"wait" to wait for a boat. Type "swim" to swim across. : ').lower()
    if action == "wait":
        door_color = input('You arrive at the island unharmed. There is a house with 3 doors. '
                           'One red, one yellow and one blue. Which colour do you chose? : ').lower()
        if door_color == "red":
            print("Game over.")
        elif door_color == "blue":
            print("Game over.")
        else:
            print("You win.")
    else:
        print("Game over.")
else:
    print("Game over.")
