import string

with open('./Day 5/sample_text.txt') as file:
    content = file.read().translate(str.maketrans('','',string.punctuation))

    word_dict ={}
    for word in content.split():
            word_dict[word] = word_dict.get(word,0)+1
            
    print(word_dict)