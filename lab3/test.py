import re
operators = {
    "=" : "EQUAL",
    "+" : "PLUS",
    "-" : "MINUS",
    "<" : "LT"
}
keywords = {
    "def" : "FUNCTION_DECLARATION",
    "var" : 'VAR_DECLARATION',
    "if" : "IF",
    "else" : "ELSE",
    "then" : "THEN",
    "return" : "RETURN"
}
delimeters = {
    "(" : "LPAREN",
    ")" : "RPAREN",
    "{" : "LBRACE",
    "}" : "RBRACE",
    ";" : "SEMICOLON"
}

tokens = []
content = ""
with open('test.txt', 'r') as file:
    content = file.read()
source_code = content.split()
           
source_index = 0
while source_index < len(source_code):
    word = source_code[source_index]
    #print(word)
    for item in keywords:
        if word == item:
            tokens.append([keywords[word], word])
    for item in operators:
        if word == item:
            tokens.append([operators[word], word])
    for item in delimeters:
        if word == item:
            tokens.append([delimeters[word], word])
        #elif word[len(word) - 1] == item:
        #    tokens.append([delimeters[word], word])
    if re.match('[a-z]', word) or re.match('[A-Z]', word):
        if word not in keywords.keys():
            if word[len(word) - 1] == ";":
                tokens.append(["IDENTIFIER", word[0:len(word) - 1]])
            else:
                tokens.append(["IDENTIFIER", word])
    elif re.match("[0-9]", word):
        if word[len(word) - 1] == ";":
            tokens.append(['INTEGER', word[0:len(word) - 1]])
        else: 
            tokens.append(['INTEGER', word])
    if word[len(word) - 1] == ";":
                tokens.append(['STATEMENT_END', ";"])
    source_index +=1
print(tokens)