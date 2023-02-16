#-----------------[1 - 'cat apple monkey banana' Example]-----------------#

import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

    """
    Comments: 
    
    Similarity is high between cat and monkey as they're both animals. - Result: 0.59;
    Similarity is high between apple and banana as they're both fruits. - Result: 0.66;
    Cat shows low similarity with apple and banana as they're not foods associated with what cats eat. - Results: 0.20 / 0.22
    However, banana has a higher similarity with monkey as this is a food normally associated with what monkeys eat. - Result: 0.40.

    """


#-----------------[1.1 - My own example]-----------------#

import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp("football golf club net")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

    """
    Comments: 

    This was an attempt to see if the model would pick up similarities between two sports (football and golf) - Result: 0.38;
    any similarity between football and club (as in 'footbal club' = a team) - Result: 0.60;
    and any similarity between golf and club (as in 'golf club' = the actual equipment used to hit the golf ball). - Result: 0.33;
    Net is only associated with footbal, but the result was interestingly very low - Result: 0.07;
    Net should have no similarity with golf, as the result shows - Result: 0.06.

    """


#-----------------[2 - 'sentence_to_compare' example]-----------------#

import spacy
nlp = spacy.load('en_core_web_md')

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

    """
    Comments: 
    The highest similarity here is with the sentence 'Hello, there is my car' (Result: 0.80)
    followed by 'I've lost my car in my car' (Result: 0.67).
    This is probably because both contain the word 'car' in it.
    
    """




