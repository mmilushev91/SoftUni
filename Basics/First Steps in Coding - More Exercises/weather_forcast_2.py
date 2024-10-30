degrees = float(input())

if degrees < 5 or degrees > 35:
  print("unknown")
elif degrees < 12:
  print("Cold")
elif degrees < 15:
  print("Cool")
elif degrees <= 20:
  print("Mild")
elif degrees < 26:
  print("Warm")
elif degrees <= 35:
  print("Hot")
