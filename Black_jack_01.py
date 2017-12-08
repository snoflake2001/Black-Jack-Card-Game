print(
    """
      _____   ______  ______  ______  ___  ___   _____    ___    ___  ___  ______   __       ______  ______    _____
     |  __ \ |  __  ||  __  ||  ____| \  \/  /  |  __ \  / _ \  |   \/   ||  __  \ |  |     |  ____||  __  \  /  ___|
     | |  \/ | |  | || |  | || |__     \    /   | |  \/ / /_\ \ | |\  /| || |_/  / |  |     | |__   | |_/  /  \  `--.
     | | __  | |  | || |  | ||  __|     |  |    | | __  |  _  | | | \/ | ||     /  |  |____ |  __|  |     /    `__.  |
     | |_\ \ | |__| || |__| ||  |       |  |    | |_\ \ | | | | | |    | || |\  \  |       || |____ | |\  \   /\__/  |
     \_____/ |______||______||__|       |__|     \____/ |_| |_| |_|    |_||_| \__\ |______/ |______||_| \__\  \_____/

     
                             _____    ___     _____    ___    __   __  _______   ___
                            /  __ \  /   |   /  ___|  / _ \  |  \ |  ||__   __| / - `
                            \_/ / /  `|  |   \ `--.  / /_\ \ |   \|  |  |   |  | /_\ |
                               / /    |  |    `--  \ |  _  | |  . `  |  |   |  |  _  |
                            __/ /_   _|  |_  /\__/ / | | | | |  |\   |  |   |  | | | |
                           |______|  \____/  \____/  |_| |_| |__| \__|  |___|  |_| |_|
    """
    )

import random

#variables

ace_of_hearts = 11
ace_of_spades = 11
ace_of_clubs = 11
ace_of_diamonds = 11


king_of_hearts = 10
king_of_spades = 10
king_of_diamonds = 10
king_of_clubs = 10


queen_of_hearts = 10
queen_of_diamonds = 10
queen_of_spades = 10
queen_of_clubs = 10


jack_of_hearts = 10
jack_of_spades = 10
jack_of_clubs = 10
jack_of_diamonds = 10


ten_of_hearts = 10
ten_of_clubs = 10
ten_of_diamonds = 10
ten_of_spades = 10


nine_of_hearts = 9
nine_of_spades = 9
nine_of_clubs = 9
nine_of_diamonds = 9


eight_of_hearts = 8
eight_of_clubs = 8
eight_of_diamonds = 8
eight_of_spades = 8


seven_of_hearts = 7
seven_of_clubs = 7
seven_of_spades = 7
seven_of_diamonds = 7


six_of_hearts = 6
six_of_diamonds = 6
six_of_clubs = 6
six_of_spades = 6


five_of_hearts = 5
five_of_diamonds = 5
five_of_clubs = 5
five_of_spades = 5


four_of_hearts = 4
four_of_diamonds = 4
four_of_spades = 4
four_of_clubs = 4


three_of_hearts = 3
three_of_spades = 3
three_of_clubs = 3
three_of_diamonds = 3


two_of_hearts = 2
two_of_clubs = 2
two_of_diamonds = 2
two_of_spades = 2



list_of_cards = [two_of_spades, two_of_diamonds, two_of_clubs, two_of_hearts,three_of_diamonds,
                 three_of_clubs, three_of_spades, three_of_hearts, four_of_clubs, four_of_spades,
                 four_of_diamonds, four_of_hearts, five_of_spades, five_of_clubs,  five_of_diamonds,
                 five_of_hearts, six_of_spades, six_of_clubs, six_of_diamonds, six_of_hearts,
                 seven_of_diamonds, seven_of_spades, seven_of_clubs, seven_of_hearts,
                 eight_of_spades, eight_of_diamonds, eight_of_clubs, eight_of_hearts,
                 nine_of_diamonds, nine_of_clubs, nine_of_spades, nine_of_hearts,
                 ten_of_spades, ten_of_diamonds, jack_of_spades, ten_of_hearts,
                 jack_of_diamonds, jack_of_clubs, jack_of_spades,  jack_of_hearts,
                 queen_of_clubs, queen_of_spades, queen_of_diamonds, queen_of_hearts,
                 king_of_clubs, king_of_diamonds, king_of_spades, king_of_hearts,
                 ace_of_diamonds, ace_of_clubs, ace_of_spades, ace_of_hearts]


#print list out

def print_list(cards):
    for i in cards:
        print(i, end = " ")


#print_list(list_of_cards) 

#random_card = random.choice(list_of_cards)
def delete_cards():
    random_card = two_of_clubs
    print(random_card)

    if random_card == two_of_spades:
        del list_of_cards[random_card]

    elif random_card == two_of_clubs:
        del list_of_cards[random_card]

print_list(list_of_cards)
    


