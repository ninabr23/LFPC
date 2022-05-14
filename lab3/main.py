from utils.lexer import Lexer


# Read the current flow source code in test.lang and store it in a variable
content = ""
# parameter r means read only and save the file as a variable called file
with open('test.txt', 'r') as file:
    content = file.read()
    
lex = Lexer(content)
tokens = lex.tokenize()
    
for token in tokens:
    print(token)
  