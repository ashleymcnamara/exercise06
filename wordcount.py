#Renamed Exercise06 to wordcount.py to match Instructions.

#open our text file
f = open('twain.txt')

#read the file and store in "wholefile" variable. it's a string!
wholefile = f.read()

#replace dashes with whitespace, so we can split the string properly. text uses --
# between two words. strip() only removes punctuation from beginning and end.

wholefile = wholefile.replace("-", " ") 

#split the string/file at whitespace -- this includes all new lines and tabs.
#to do this, we use split() with no argument, because that includes ALL whitespace.
# all whitespace = spaces, tabs, new lines, etc.

split_file = wholefile.split()

#we need to get our words into a dictionary! start by declaring an empty dictionary.
#we'll call it words
words = {}
#write our for loop to strip words of punctuation at beginning and end, and count

for word in split_file:
    stripped_word = word.strip("!,.';:\"-_?")
  #if the word does not exist as a key in our dictionary, add it, and set its value
  #to one.

    if not words.get(stripped_word):
        words[stripped_word] = 1
    #else, the word DOES exist and is a key. add one to its value to count the occurence.    
    else:
        words[stripped_word] += 1

print words
    


 

#count how many times word appears in file
#word is defined as space-separated


#then we print counts to the screen as pair, with the value and number of times 
#it occurs

