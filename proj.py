import random
import math

def game():
    user=input("whats ur choice? 'r' for rock 'p' for paper 's' for scissor\n")
    user=user.lower()
    comp=random.choice(['r','p','s'])
    if user==comp:
        return (0,user,comp)
    elif is_Win(user,comp):
        return (1,user,comp)
    else:
      return (-1,user,comp)

def is_Win(player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
       return True
    return False
    
def bestofGame(n):
    pw=0
    cw=0
    wn=math.ceil(n/2)
    while pw<wn and cw<wn:
        result,user,comp=game()
        if result==0:
            print('Tie.You and computer both have chosen {}.\n'.format(comp))
        elif result==1:
            pw+=1
            print('You have Win.You chose {} and computer chose {}.\n'.format(user,comp))
        else:
            cw+=1
            print('You have Lost.You chose {} and computer chose{}.\n'.format(user,comp))
            print("/n")
    if(pw>cw):
        print('You have Won best of {} games'.format(n))
    else:
        print('You have Lost best of {} games'.format(n))
if __name__ == "__main__":
    bestofGame(5)
