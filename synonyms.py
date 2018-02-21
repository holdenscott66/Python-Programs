
#Scott Holden UCID:30051473
# All parts of assignment solved
# function names and arguments are from synonyms_starter.py

def norm(vec): #norm function from synonyms_starter.py modified slightly so it no longer requires math module
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return sum_of_squares ** 0.5


def cosine_similarity(vec1, vec2):  # returns the cosine similarity between vec1 and vec2, stored as dictionaries
    vector_1 = list(vec1.values()) #takes values from vector dictionary and converts to list
    vector_2 = list(vec2.values())
    dot = 0.0
    if len(vector_2) > len(vector_1): #uses length of the smaller vector to calculate dot product
        for i in range(len(vector_1)):
            dot += (vector_1[i] * vector_2[i]) #for each component of the vector, they are mulitplied
    elif len(vector_1) >= len(vector_2):
        for i in range(len(vector_2)):
            dot += (vector_1[i] * vector_2[i])
    return dot / (norm(vec1) * norm(vec2))


def build_semantic_descriptors(sentences): #builds dictionary of semantic descriptor from argument-- list of sentences
    desc = {} #empty dictionary
    for k in sentences:
        for i in k:
            if i not in desc: #if the word is not already in the dictionary, it adds a nested dictionary
                desc[i] = {}
            for j in k:
                if (j in desc[i]) and j != i: #if that word is in the nested dictionary and not equal to the key, it adds 1
                    desc[i][j] += 1
                elif j != i: #if not already in the nested dictionary and not equal to the key, it creates key and value
                    desc[i][j] = 1
    return desc #returns dictionary


def build_semantic_descriptors_from_files(filenames): #builds dictionary of semantic descriptor from argument -- list of names of files
    mlst = [] #creates empty list of sentences
    for i in range(len(filenames)): #for each file
        book = open(filenames[i], "r", encoding="utf-8") #open the file
        content = book.read()
        book.close()
        content = content.replace('.', '<stop>').replace('!', '<stop>').replace('?', '<stop>') \
            .replace(',', ' ').replace('-', ' ').replace('--', ' ') \
            .replace(':', '').replace('"', ' ').replace("'", '').replace(';', '') \
            .lower().split('<stop>') # replaces all terminating punctuation with <stop> and all other punctuation is removed.
            #  all words are made lowercase. separated into lists  wherever there is <stop>
        for x in content:
            if len(x) != 0: #if there is contents in the line
                mlst.append(x.split()) #separate into another list, and add to master list
    return build_semantic_descriptors(mlst) #calls build_semantic_descriptor function to create dictionary based on the master list( mlst)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn): #finds most similar word based on the choice word,
                                                                            # options to choose from, and 2 required function
    cosval = {} #empty dict
    vect_1 = semantic_descriptors.get(word) # creates vector for choice word
    for x in choices:
        vect_2 = semantic_descriptors.get(x) #for each of the choices, create vector and compare to vector 1
        try:
            cosval[x] = similarity_fn(vect_1, vect_2) #try and find the cosine similarity
        except: #if it doesnt work, return value -1
            cosval[x] = -1
    max_value = max(cosval.values()) #find the value with highest cosine similarity
    for (key, value) in cosval.items(): #iterate through all items in dict, finds the first occurence of the highest cosine similarity and returns that key
        if value == max_value:
            return key


def run_similarity_test(filename, semantic_descriptors, similarity_fn): #run similarity test based on a single file name of quesitons/ correct answers
    file = open(filename, "r", encoding="utf-8")
    correct = [0, 0] #table to see how may are correct
    while True: #while there are still lines
        line = file.readline()
        line = line.split() #separate line into list
        if len(line) == 0:
            break
        correct[1] += 1 #this is the total count, correct[0] will be divided by this to return percentage
        answer = similarity_fn(line[0], line[2:], semantic_descriptors, cosine_similarity) #run similarity function, choice word is the first word in line,
                                                                                            # options to choose form are the last two words
        if answer == line[1]: #if the answer is the same as whats in the file, add one to correct
            correct[0] += 1
    file.close()
    return correct[0] / correct[1] #returns percentage of correct