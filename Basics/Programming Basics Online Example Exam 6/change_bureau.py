bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input()) / 100

levs = bitcoin_count * 1168 + ((yuan_count * 0.15) * 1.76)
euro = levs / 1.95

euro -= euro * commission

print(f"{euro:.2f}")
