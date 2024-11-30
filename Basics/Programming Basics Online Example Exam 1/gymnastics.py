grades = {
    "ribbon": {
        "Russia": [9.1, 9.4],
        "Bulgaria": [9.6, 9.4],
        "Italy": [9.2, 9.5],
    },
    "hoop": {
        "Russia": [9.3, 9.8],
        "Bulgaria": [9.550, 9.750],
        "Italy": [9.450, 9.350],
    },

    "rope": {
        "Russia": [9.6, 9],
        "Bulgaria": [9.5, 9.4],
        "Italy": [9.7, 9.150],
    },
}

country = input()
instrument = input()

country_final_score = sum(grades[instrument][country])
percent_needed = (20 - country_final_score) / 20 * 100

print(f"The team of {country} get {country_final_score:.3f} on {instrument}.")
print(f"{percent_needed:.2f}%")
