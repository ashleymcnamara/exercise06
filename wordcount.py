from sys import argv
#Renamed Exercise06 to wordcount.py to match Instructions.

#open our text file
script, filename = argv
f = open(filename, "r")

#read the file and store in "wholefile" variable
wholefile = f.read()
#close the file
f.close()
#make all letters lowercase
wholefile = wholefile.lower()

# replace dashes with whitespace, so we can split the string properly. text uses --
# between two words. strip() only removes punctuation from beginning and end.

wholefile = wholefile.replace("-", " ") 

#split the string/file at whitespace -- this includes all new lines and tabs.
#to do this, we use split() with no argument, because that includes ALL whitespace.

split_file = wholefile.split()

# put words in dictionary. start by declaring an empty dictionary.

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

#for key, value in words.iteritems():
    #print key, value

#working on extra credit, sorting by values    
sorted_values = {}

# print sorted(words.values())
#print words.keys()
list_of_words = [(v, k) for k, v in words.items()]
list_of_words.sort()
list_of_words.reverse() #makes largest occurence first

for item in list_of_words:
    if not sorted_values.get(item[0]):
        sorted_values[item[0]] = [item[1]]
 
    else:
       current_value = [item[1]]
       sorted_values[item[0]] = current_value.append([item[1]])
print sorted_values       

#     #print item






# use d.items() to get list of dictionary's items
# invert the ordering of each item's tuple, from (key, value) into (value, key)
# sort the list

