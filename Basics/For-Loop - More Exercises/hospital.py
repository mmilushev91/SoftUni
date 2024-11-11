days = int(input())

doctors = 7
treated = 0
untreated = 0

for day in range(1, days + 1):
  pations_count = int(input())
  
  if day % 3 == 0 and untreated > treated:
    doctors += 1
  
  if pations_count >= doctors:
    untreated += pations_count - doctors
    treated += doctors
  else:
    treated += pations_count

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
