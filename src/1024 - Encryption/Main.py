nReads = int(input())

i = 0

while i < nReads:
    i = i + 1

    word = input()

    word1 = ""
    
    for letter in word:
        if ord(letter.upper()) >= 65 and ord(letter.upper()) <= 90:
            word1 = word1 + chr(ord(letter) + 3)
        else:
            word1 = word1 + letter

    word2_word1_reversed = word1[::-1]

    nHalf = len(word2_word1_reversed) // 2

    word2 = word2_word1_reversed[0:nHalf]

    for letter in word2_word1_reversed[nHalf:]:
        word2 = word2 + chr(ord(letter) -1)

    print(word2)
