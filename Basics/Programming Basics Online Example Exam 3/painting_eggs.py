batch_prices = {
  "Large": {
    "Red": 16,
    "Green": 12,
    "Yellow": 9,
  },
  
  "Medium": {
    "Red": 13,
    "Green": 9,
    "Yellow": 7,
  },

  "Small": {
    "Red": 9,
    "Green": 8,
    "Yellow": 5,
  }
}

eggs_size = input()
eggs_color = input()
batches_count = int(input())

eggs_price = batches_count * batch_prices[eggs_size][eggs_color]

costs = eggs_price * 0.35

final_price = eggs_price - costs

print(f"{final_price:.2f} leva.")
