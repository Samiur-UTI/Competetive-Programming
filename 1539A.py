test = input()
arr = [int(char) for char in test.split()]
song = input()
calSong = [int(char) for char in song.split()]
alphVal = {}
for letter in calSong:
    number = ord(letter) - 96
    alphVal[letter] = number
for i in range(arr[1]):
    charm = input()
    case = [int(char) for char in charm.split()]
    
    