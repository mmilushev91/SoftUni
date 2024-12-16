deck = input().split()
shuffles_count = int(input())

deck_to_shuffle = deck[1:len(deck) - 1]
mid_index = int(len(deck_to_shuffle) / 2)

for _ in range(shuffles_count):

  first_half = deck_to_shuffle[:mid_index]
  second_half = deck_to_shuffle[mid_index:]
  
  shuffled_deck = []
  
  for index in range(mid_index):
    shuffled_deck.append(second_half[index])
    shuffled_deck.append(first_half[index])
  
  deck_to_shuffle = shuffled_deck

deck[1:len(deck) - 1] = deck_to_shuffle

print(deck)
