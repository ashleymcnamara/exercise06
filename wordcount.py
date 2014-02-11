#Renamed Exercise06 to wordcount.py to match Instructions.

#open our text file
f = open('twain.txt')

#read the file
wholefile = f.read()

#split the file at whitespace

wholefile = wholefile.replace("-", " ") 
split_file = wholefile.split()


#strip each word/string of its punctuation 
words = {}
for word in split_file:
   words[word.strip("!,.';:\"-_?")] = 0

print words
    


 

#count how many times word appears in file
#word is defined as space-separated


#then we print counts to the screen as pair, with the value and number of times 
#it occurs

