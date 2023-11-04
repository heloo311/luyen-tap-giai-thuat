import re

keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
number_pattern = r'[-+]?\d*\.\d+([eE][-+]?\d+)?|[-+]?\d+\.\d*([eE][-+]?\d+)?|[-+]?\d+[eE][-+]?\d+|\d+'


with open("C:/Users/Acer/Desktop/New Text Document (2).tx"
          ""
          "t") as file:
    code = file.read()


tokens = re.findall(r'\b\w+\b|[-+*/%=<>(){};,.]', code)


for token in tokens:
    if token in keywords:
        print(f"keyword : {token}")
    elif re.match(identifier_pattern, token):
        print(f"identifier : {token}")
    elif re.match(number_pattern, token):
        print(f"num : {token}")
    else:
        print(f"{token} : {token}")


