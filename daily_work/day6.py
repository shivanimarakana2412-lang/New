                              #string data types
               
# String is a sequence of characters that is used for storing and manipulating text. 
# It's immutable
# strings are write in multiple way --> 1. single quote , 2.double quote , 3.tripal quote

single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
multi_line_string = '''This is a string that spans multiple lines.'''
multi_line_string1 = """This is also a string that spans multiple lines."""
 
print(single_quote_string)
print(double_quote_string)
print(multi_line_string)
print(multi_line_string1)

str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2 
print(combined)

repeated = "Ha" * 3 
print(repeated)

text = "Python"
print(text)
print(text[0])  
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

text = "Hello World" # print word in small latters
print(text.lower())

text = "Hello World"  # print word in capital latters
print(text.upper())

text = "hello world" # print word in normal latters
print(text.title())

text = "hello world" # print word first latter capital and next all are small latters
print(text.capitalize())

text = "   Hello World   "
print(text.strip())

text = "Hello World" # for comma between two words
print(text.split())

words = ['Hello', 'World'] # merge two words
print(' '.join(words))