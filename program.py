import sys
map = {
    "A": 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, "I": 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
    "O": 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, "W": 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}
alphabet = list(map.keys())
alphabet.sort()

def displayresults(alphabet, map):
    templist = []
    for x in range(12,-1,-1):
        for y in alphabet:
            if map[y] == x:
                templist.append(str(y))
        if len(templist) > 0:
            finalstring = str(x) + ":"
            for y in templist:
                finalstring = finalstring + ' ' + y + ','

            print(finalstring[:-1])
        templist = []

usedtiles = input()
for letter in usedtiles:
    map[letter] -= 1
    if map[letter] < 0:
        print ("Invalid input. More %s's have been taken from the bag than possible." %letter)
        sys.exit()
displayresults(alphabet, map)
