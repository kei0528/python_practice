import os
all_biddings = []

all_participants_entered = False


def add_bidding () :
  name = input('What is your name?\n')
  bid_input = input('What\'s your bid?\n')
  
  while(not bid_input.isdigit()) :
    bid_input = input('Please enter bid amount in number \n')
    
  bid = int(bid_input)
  
  all_biddings.append({
    "name": name,
    "bid": bid
  })
  
  exists_more_participants = input('Are there any other bidders? Type "Yes" or "No \n').lower()
  
  if(exists_more_participants == 'no') :
    global all_participants_entered
    all_participants_entered = True

  os.system('clear')


while (not all_participants_entered) :
  add_bidding()
  
  
highest_bids = [
  {
  "name": "",
  "bid": 0
  }
]    

for bidding in all_biddings :
  for index_of_heighest_bid in range(len(highest_bids)) :
    if highest_bids[index_of_heighest_bid]["bid"] == bidding["bid"] :
      highest_bids.append(bidding)
    else :
      highest_bids[index_of_heighest_bid] = bidding

if len(highest_bids) > 1 :
  winners = ""
  for winner in highest_bids :
    winners += winner["name"] + " "
    
  print(f"{winners} bidded same amount!")
else :
  print(f"{highest_bids[0]['name']} won!")