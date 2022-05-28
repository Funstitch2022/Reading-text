# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    openfile = open(filename, 'r')
    read_file = openfile.read()
    return read_file

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    split_text = text.split (' ')
    dict_words ={}
    for word in split_text:
        dict_words.update({word: split_text.count(word)})
    return dict_words

# output_read = read_file_content("story.txt")
# print(output_read)

output2 = count_words ()

print(output2)




    
    


