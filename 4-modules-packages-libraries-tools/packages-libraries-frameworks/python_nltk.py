###########################################################################################################################################
# NLTK -> used for Natural Language Processing
###########################################################################################################################################

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

###########################################################################################################################################
# Print statement 1
print(word_tokenize(text))

# OUTPUT:
'''
['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.']
'''
###########################################################################################################################################

# Print statement 2
print(nltk.tokenize.sent_tokenize(text))

# OUTPUT:
'''
['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."]
'''
###########################################################################################################################################

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)

# OUTPUT:
'''
['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry.', 'Lorem', 'Ipsum', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', '1500s,', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book.']
'''

###########################################################################################################################################

# CODE EXPLANATION:
'''
NLTK is a huge library and it is inadvisable to import all its packages and subpackages. If you examine the code, you will realize that only the required functionalities from the subpackages such as corpus and tokenize are imported within the code.
    - First a block of text is copied inside the code-block and assigned to a variable called text.
    
    - The first function used is word_tokenize(). This takes this text and produces the first part of the output in which the words are ‘tokenized’ or simply separated by a whitespace. The same can be done with the split() function in the string, but the use of the package is far more efficient when it comes to larger blocks of code.
     
    - The second function sent_tokenize() takes this block of text and tokenizes by ‘sentences’.
    
    - For the third output, I first split the code and remove what is called ‘stopwords’. Stopwords are words in the English language that can be considered redundant and adding little value while you are undertaking natural language processing. These include words such as ‘a’, ‘the’, ‘him’. First I'll create a list of these stopwords and then remove them using a for loop to form a new list called new_text. You will notice the difference by comparing the first and the final output of the code.

We have covered only a couple of examples here from couple of libraries and there is a plethora of options available with different packages in Python. The best way to learn them is through practice and exploration. 
'''
