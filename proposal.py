test_string = input("Enter message here: ")

print("Unfiltered message: "+str(test_string))

dict = {"stupid":"silly","fucker":"fudge", "asshole":"arsewhole", "bitch":"beez" }

#splitting the words
temp = test_string.split()
res = []
for word in temp:
    #search word from dictionary
    res.append(dict.get(word, word))

res = ' '.join(res)

print("Filtered words: "+str(res))