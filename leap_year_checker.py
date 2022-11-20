# current_year = int(input('Which year is it now?'))
year = 2024

if (year % 100 == 0) :
  print('Not leap year.')
elif (year % 400 == 0 or year % 4 == 0) :
  print('Leap year.')
else :
  print('Not leap year.')