def vowels(s):
    count = 0
    for c in s:
        if c in "aieou":
            count = count + 1
    return count


word = input("Enter a word:")
print(f"There are {vowels(word)} vowels in your word")
