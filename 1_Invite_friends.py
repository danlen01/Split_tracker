import random
i_friends = ""
friends = {}
def invite():
    try:
        num_friends = int(input('Enter the number of friends joining (including you):'))
    except ValueError:
        print('No one is joining for the party')

    count = 0
    num_friendsc = num_friends - 1
    if num_friends == 0 or num_friends <= 0:
        print('No one is joining for the party')
    elif num_friends > 0:
        print('Enter the name of every friend (including you), each on a new line:')
        while count <= num_friendsc:
            i_friends= input()
            friends.update({i_friends: 0})
            count += 1
    if num_friends > 0:
        total = float(input('Enter the total value:'))
        lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        if lucky == "Yes":
            print(f'{random.choice(list(friends.keys()))} is the lucky one!')
        else:
            print('No one is going to be lucky')
            total = total / num_friends
            for i in friends:
                friends[i] = total
            print(f'Each person will have to pay: ${total:.2f}')

invite()





