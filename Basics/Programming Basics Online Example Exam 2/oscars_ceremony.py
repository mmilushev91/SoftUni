rent = int(input())

statuettes = rent - rent * 0.30
kettering = statuettes - statuettes * 0.15
sound = kettering / 2

total_price = rent + statuettes + kettering + sound

print(f"{total_price:.2f}")
