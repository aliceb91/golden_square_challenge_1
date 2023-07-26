def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    new_counter = list(counter.items())
    new_counter.sort(reverse = True, key=lambda item: item[1])
    for entry in new_counter:
        if entry[0].isalpha():
            return entry[0]
print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")