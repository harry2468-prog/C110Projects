


#Function that prompts the user for an action and validates the input
#This code is a simple text-based adventure game where the player explores an abandoned mine.


def get_action(prompt: str, valid_choices: tuple[str, ...]) -> str:
    """
    Prompt user until they enter a valid choice.
    If input is invalid, prints the invalid input and asks again.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in valid_choices:
            return response
        else:
            print(f'Invalid input: "{response}". Please enter one of: {", ".join(valid_choices)}.')
#Function to start the adventure game
def mine_adventure():
    print('You are a Mining Engineer specializing in abandoned mine exploration.')
    print('You have been hired to assess the feasibility of reopening the century-old Oakwood Mine.')
    print('You are standing at the entrance of the Oakwood Mine, and you see:')
    print('- A narrow path leading deeper into the mine.')
    print('- A sign that reads "Danger: Keep Out!" leading to a room with old used substation.')
    print('- A room filled with old mining equipment.')

    # Top-level choice
    response = get_action(
        'What do you want to do? (explore narrow tunnel/enter mining equipment room/enter substation room/leave): ',
        ('explore narrow tunnel', 'enter mining equipment room', 'enter substation room', 'leave')
    )

    if response == 'explore narrow tunnel':
        print('You decide to explore the mine further.')
        print('As you walk deeper into the mine, you hear a faint dripping sound.')
        print('You find a small pool of water with strange glowing crystals around it.')
        action = get_action(
            'What do you want to do? (collect/continue): ',
            ('collect', 'continue')
        )
        if action == 'collect':
            print('You carefully collect some of the glowing crystals, noticing their unique properties.')
            print('These could be valuable for research or sale!')
        else:  # continue
            print('You leave the crystals and venture deeper into the mine.')
            print('The path narrows, and you must squeeze through a tight space.')
            print('You find a large cavern filled with old mining carts and tools.')
            next_action = get_action(
                'What do you want to do? (search/exit): ',
                ('search', 'exit')
            )
            if next_action == 'search':
                print('You search the mining carts and find some old tools and a map.')
                print('The map reveals hidden passages and potential treasure locations!')
            else:
                print('You head back to the entrance, ready to report your findings.')

    elif response == 'enter mining equipment room':
        print('You enter the room: old mining tools, rusty machinery, and dusty logs.')
        action = get_action('What do you want to do? (open journal/leave): ', ('open journal', 'leave'))
        if action == 'open journal':
            print('You flip through old journals, learning the mine’s history and hazards.')
            print('The mine was closed due to safety concerns and declining mineral reserves.')
            print('You discover a hidden shaft that might contain valuable minerals.')
            next_action = get_action(
                'What do you want to do? (design map/exit): ',
                ('design map', 'exit')
            )
            if next_action == 'design map':
                print('You open your simulation software and map the mine using journal parameters.')
                design = get_action('Enter material for pillars (wood/concrete): ', ('wood','concrete'))
                if design == 'wood':
                    print('Uh-oh—wooden pillars collapse under pressure!')
                else:
                    print('Concrete pillars seem solid and are supporting the structure.')
            else:
                print('You exit the mine.')
        else:
            print('You exit the mine.')

    elif response == 'enter substation room':
        print('You see old electrical equipment that once powered the mine shafts.')
        action = get_action('What do you want to do? (explore equipment/leave): ', ('explore equipment','leave'))
        if action == 'explore equipment':
            print('You inspect coils of copper and aluminum and see exposed wiring.')
            next_action = get_action('Open toolbox to dismantle electrical equipment or leave? (dismantle/leave): ', ('dismantle','leave'))
            if next_action == 'dismantle':
                print('You dismantle some components—bolts, nuts, and wires are disconnected.')
            else:
                print('You leave the room without dismantling anything.')
        else:
            print('You exit the mine.')

    else:  # leave
        print('You decide this isn’t the right time and leave the mine safely.')

if __name__ == '__main__':
    mine_adventure()
