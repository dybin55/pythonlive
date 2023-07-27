def count_character(text, char):
    # return text.count(char)
    count = 0
    for t in text:
        if t == char:
            count += 1
    return count        


result = count_character("Hello, World!", "o")
print(result) # 2
