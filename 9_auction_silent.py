import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print('AUCTION! Started')
auction_player = {}


def max_bid(auction_player):
    max_money = 0
    winner = ''
    for name in auction_player:
        if auction_player[name] > max_money:
            max_money = auction_player[name]
            winner = name
    print(f'Champion is {winner} with a bid {max_money}')


playmore = True
while playmore:

    name = input('What is your name?: \n')
    bid = int(input('How many do you want to bid?: \n'))

    auction_player[name] = bid

    add_name = input('Add one more person? \n')
    if add_name != 'Yes'.lower():
        max_bid(auction_player)
        playmore = False
    else:
        os.system('cls')
