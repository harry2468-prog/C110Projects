print(f'You are a Mining Engineer specializing in abandoned mine exploration.'\
        'You have been hired to assess the feasibility of reopening the century-old Oakwood Mine.'\
        'You are standing at the entrance of the Oakwood Mine,and you see:'\
        'A narrow path leading deeper into the mine.'\
        'A sign that reads "Danger: Keep Out! leading to a room with old used substation".'\
        'A room filled with old mining equipment.')
Response = input('What do you want to do? (explore narrow tunnel/enter the room with mining equipment/enter room with old substation/leave): ').strip().lower()
if Response == 'explore narrow tunnel':
    print(f'You decide to explore the mine further.'\
            'As you walk deeper into the mine,you hear a faint dripping sound.'\
            'You find a small pool of water with strange glowing crystals around it.'\
            'You can either collect the crystals or continue deeper into the mine.')
    Action = input('What do you want to do? (collect/continue): ').strip().lower()
    if Action == 'collect':
        print(f'You carefully collect some of the glowing crystals,noticing their unique properties.'\
                'These could be valuable for research or sale!')
    elif Action == 'continue':
        print(f'You decide to leave the crystals and venture deeper into the mine.'\
                'The path narrows,and you must squeeze through a tight space to proceed.'\
                'You find yourself in a large cavern filled with old mining carts and tools.'\
                'You can either search the carts for useful items or head back to the entrance.')
        NextAction = input('What do you want to do? (search/exit): ').strip().lower()
        if NextAction == 'search':  
            print(f'You search the mining carts and find some old tools and a map of the mine.'\
                   'The map reveals hidden passages and potential treasure locations!')     
        elif NextAction == 'exit':
            print(f'You decide to head back to the entrance,realizing that you have gathered enough information for now.'\
                   'You exit the mine safely,ready to report your findings.')   
        else:
            print(f'Invalid action. Please choose either "search" or "exit".')
elif Response == 'enter the room with mining equipment':
    print(f'You enter the room and find a collection of old mining tools,rusty machinery,and dusty logs.'\
           'You notice old journals belonging to former engineers')
    Action = input('What do you want to do?(open journal/leave):   ').strip().lower()
    if Action =='open journal':
          print(f'As you flip through the pages,you gain insight about the history of the mine and potential harzards.'\
                 'You also discover that the mine was closed due to safety concerns and declining mineral reserves.'\
                 'The engineer mentioned a hidden shaft that might still contain valuable minerals'\
                 'The mine layout and geology are complex,requiring careful planning to reopen')
          NextAction = input('What do you want to do?(design the map of the mine/exit):   ').strip().lower()
          if NextAction =='design the map of the mine':
              print(f'You open a simulation software from your PC and map the mine using parameters in the journal')
              Designparameters = input('Enter material used in designing pillars(wood/concrete):   ')
              if Designparameters =='wood':
                   print(f'The mine pillars has collapsed')
              else:
                   print(f'The mine pillars are still supporting the mine')     
          else:
              print('You are out of the mine')
    elif Action =='leave':
         print('You are out of the mine')
elif Response =='enter room with old substation':
             print(f'You see and old electrical equipment used to supply power to the shafts of the mine')
             Action = input('(explore the equipment/leave):    ').strip().lower()
             if Action =='explore the equipment':
                 print(f'You see coils of copper and aluminum and wires connected')
                 NextAction =input('(Open toolbox to dismantle electrical equipment/leave):   ')
                 if NextAction =='Open toolbox to dismantle electrical equipment':
                      print('Bolts and nuts and wires are discconnected')
                 else:
                      print('You are out of the mine')     
             elif Action =='leave':
                  print(f'You are out of the mine!') 

else:
     print(f'You are out of the mine')         
              



                           