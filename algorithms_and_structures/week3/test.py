def slogan(words, L):
    print(words, L)
    if len(words) == 1 or len(words[-1]) == L:
        return len(words[-1]) == L
    last_word = words[-1]
    without_last_word = words[:-1]
    return (
        slogan(without_last_word, L-len(last_word) - 1) or
        slogan(without_last_word, L)
    )


# should print True
print(slogan(["modern", "cool", "abysmal"], 12))
# should print False
print(slogan(["modern", "cool", "abysmal"], 13))
