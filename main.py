import random

list = []
deck = [
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'K', 'P',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'K', 'P',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'K', 'P',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'K', 'P'
]

bot1 = 0
bot2 = 0
player = 0

users = [bot1, bot2, player]

def asciiTable(player, bot1, bot2):

    print(
        """
                                _____
                                |A .  | _____
                                | /.\ ||A ^  | _____
                                |(_._)|| / \ ||A _  | _____
                                |  |  || \ / || ( ) ||A_ _ |
                                |____V||  .  ||(_'_)||( v )|
                                       |____V||  |  || \ / |
                                              |____V||  .  |
                                                     |____V|                                          
        """,
        "                               "f'Bot1 >> {bot1}',
        """ 
                    -'-------------------------------------------------`-
                  _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
               _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
            _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
         _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
        :-----------------------------------------------------------------------------:
        """,
          f'You >> {player}' + "                                                    " + f'Bot2 >> {bot2}', )


def pickACard():                #pick a random card from deck

    c = random.choice(deck)
    deck.remove(c)
    return c

def AI_draw_or_pass():                  #defining a function to AI pass or hit in round

    trueorfalse = [0, 1]
    choice = random.choice(trueorfalse)
    c = random.choice(deck)
    if choice == 0:
        return 0            #0 means pass the round
    if choice == 1:
        return c

def addCount(card):

    try:
        if int(card):           #if cards is integer, return it
            return card

        if card == 0:        #if card is 0, return it as none
            return 0

    except ValueError:              #if card is string (V,K,P,A) return 10 for 'V, K, P'. return 1 or 11 for 'A'

        if card == "A":
            q = int(input("You picked A, 1 or 11?\n"))
            if q == 1:
                return 1
            elif q == 11:
                return 11
        elif card == "V" or "K" or "P":
            return 10

def checkTable():                               #win or lose checkers
    if bot1 < 21 and bot2 < 21 and player < 21:
        return 0
    elif bot1 < 21 and bot2 > 21 and player > 21:
        print('Bot1 won')
        return 1
    elif bot2 < 21 and player > 21 and bot1 > 21:
        print('Bot2 won.')
        return 1
    elif player < 21 and bot1 > 21 and bot2 > 21:
        print('Player won.')
        return 1
    elif bot1 == 21 or bot2 == 21 or player == 21:
        print('Blackjack!')
        return 2

print(""" 
                         $$$$$$\    $$\   
                        $$  __$$\ $$$$ |  
                        \__/  $$ |\_$$ |  
                         $$$$$$  |  $$ |  
                        $$  ____/   $$ |  
                        $$ |        $$ |  
                        $$$$$$$$\ $$$$$$\ 
                        \________|\______|
        """)

login = input("""                      Type 'start' to play                                                                              
                                           
""")

if login.lower() == 'start':
    for i in range(1):
        bot1 = bot1 + addCount(
                                pickACard()
                                )
        bot2 = bot2 + addCount(
                                pickACard()
                                )
        player = player + addCount(
                                pickACard()
                                )
        print(asciiTable(player=player, bot1=bot1, bot2=bot2))
        break

    while True:
        def Func():

            if checkTable() == 0:
                return True
            elif checkTable() != 0:
                return False

        if Func() == False:
            break
        elif Func() == True:
            wannadraw = input(f'You got {player}, draw or pass?\n')

            if wannadraw.lower() == 'draw' and checkTable() == 0:
                for i in range(1):

                    bot1 = bot1 + addCount(
                        AI_draw_or_pass()
                    )
                    bot2 = bot2 + addCount(
                        AI_draw_or_pass()
                    )
                    player = player + addCount(
                        pickACard()
                    )
                    print(asciiTable(bot1=bot1, bot2=bot2, player=player))
                    print(f'value{checkTable()}')

            elif wannadraw.lower() == 'pass' and checkTable() == 0:
                for i in range(1):
                    bot1 = bot1 + addCount(
                        pickACard()
                    )
                    bot2 = bot2 + addCount(
                        pickACard()
                    )
                    print(asciiTable(player=player, bot1=bot1, bot2=bot2)),
                    print(f'value = {checkTable()}')

elif login.lower() != 'start':
    print('dude u high?')







