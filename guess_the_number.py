import random

ART = '''
d s  b d       b d s   sb d ss.  d sss   d ss.         sSSSs   d s.   d s   sb d sss   
S  S S S       S S  S S S S    b S       S    b       S     S  S  ~O  S  S S S S       
S   SS S       S S   S  S S    P S       S    P      S         S   `b S   S  S S       
S    S S       S S      S S sSS' S sSSs  S sS'       S         S sSSO S      S S sSSs  
S    S S       S S      S S    b S       S   S       S    ssSb S    O S      S S       
S    S  S     S  S      S S    P S       S    S       S     S  S    O S      S S       
P    P   "sss"   P      P P `SS  P sSSss P    P        "sss"   P    P P      P P sSSss 
                                                                                       
'''

print(ART)

RANDOM_NUM = random.randint(1, 100)
life_left = 0

while life_left == 0 :
  DIFFICULTY = input('1. Easy or 2. Hard  --  Hit 1 or 2\n')

  if DIFFICULTY == '1' :
    life_left = 10
  elif DIFFICULTY == '2':
    life_left = 5

user_won = False

while not user_won and life_left > 0 :
  GUESSED_NUMBER = int(input('Guess the number! \n'))
  
  if GUESSED_NUMBER > RANDOM_NUM :
    print('Your number is too large!')
    life_left -= 1
  elif GUESSED_NUMBER < RANDOM_NUM :
    life_left -= 1
    print('Your number is too small')
  else :
    user_won = True
    
if user_won :
  print('Congratiration! You entered correct number!')
else :
  print(f'You lost! The correct number is {RANDOM_NUM}')