FIRST_ZONE_OUTFITS = {
    "Morning": {
        "Outfit": "Sweatshirt",
        "Shoes": "Sneakers"
    },
    
    "Afternoon": {
        "Outfit": "Shirt",
        "Shoes": "Moccasins",
    },
    
     "Evening": {
        "Outfit": "Shirt",
        "Shoes": "Moccasins",
    },
}

SECOND_ZONE_OUTFITS = {
    "Morning": {
        "Outfit": "Shirt",
        "Shoes": "Moccasins"
    },
    
    "Afternoon": {
        "Outfit": "T-Shirt",
        "Shoes": "Sandals",
    },
    
     "Evening": {
        "Outfit": "Shirt",
        "Shoes": "Moccasins",
    },
}

THIRD_ZONE_OUTFITS = {
    "Morning": {
        "Outfit": "T-Shirt",
        "Shoes": "Sandals"
    },
    
    "Afternoon": {
        "Outfit": "Swim Suit",
        "Shoes": "Barefoot",
    },
    
     "Evening": {
        "Outfit": "Shirt",
        "Shoes": "Moccasins",
    },
}

LOW_DEGREES = 10
MID_DEGREES = 18
HIGH_DEGREES = 24

OUTFIT = "Outfit"
SHOES = "Shoes"

degrees = int(input())
time = input()

outfit = ""
shoes = ""

if LOW_DEGREES <= degrees <= MID_DEGREES:
    outfit = FIRST_ZONE_OUTFITS[time][OUTFIT]
    shoes = FIRST_ZONE_OUTFITS[time][SHOES]
elif degrees <= HIGH_DEGREES:
    outfit = SECOND_ZONE_OUTFITS[time][OUTFIT]
    shoes = SECOND_ZONE_OUTFITS[time][SHOES]
elif degrees > HIGH_DEGREES:
    outfit = THIRD_ZONE_OUTFITS[time][OUTFIT]
    shoes = THIRD_ZONE_OUTFITS[time][SHOES]

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
