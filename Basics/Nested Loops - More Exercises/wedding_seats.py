START_SECTOR = 65
START_SEAT = 97

sector = ord(input()) + 1 
sector_rows = int(input())
odd_row_seats = int(input())

even_row_seats = odd_row_seats + 2

end_seats = START_SEAT
total_seats = 0

for sect in range(START_SECTOR, sector):
  
  for row in range(1, sector_rows + 1):
    end_seats = START_SEAT
    
    if row % 2 != 0:
      end_seats += odd_row_seats
    else:
      end_seats += even_row_seats
    
    for seat in range(START_SEAT, end_seats):
      
      sector_letter = chr(sect)
      seat_letter = chr(seat)
      
      total_seats += 1
      
      print(f"{sector_letter}{row}{seat_letter}")
  
  sector_rows += 1
  
print(total_seats)
