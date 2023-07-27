def countalpha(text):
    text_cap = text.upper()
    numbers = []
    for char in text_cap:
        nums = list(text_cap).count(char)
        numbers.append(nums)

    zip_1 = list(zip(numbers, text_cap))
    print(zip_1)

countalpha('aaajshjhjh')



