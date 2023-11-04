import re

class Token:
    def __init__(self, class_name, lexeme):
        self.class_name = class_name
        self.lexeme = lexeme

def read_tokens(input_file_path):
    tokens = []
    with open(input_file_path, "r") as f:
        for line in f:
            # Split the line into tokens using regular expressions.
            tokens_in_line = re.findall(r"\w+|\W+", line)
            for token in tokens_in_line:
                # Classify the token into one of the following categories:
                #   * keyword
                #   * identifier
                #   * number
                #   * operator
                #   * other
                if token in ["while", "if", "else", "return", "break", "continue", "int", "float", "void"]:
                    class_name = "keyword"
                elif re.match(r"[A-Za-z][A-Za-z0-9_]*", token):
                    class_name = "identifier"
                elif re.match(r"\d+\.?\d*", token):
                    class_name = "num"
                elif token in ["+", "-", "*", "/"]:
                    class_name = "addop"
                elif token in ["<", ">", "<=", ">=", "==", "!="]:
                    class_name = "relop"
                elif token == "&&":
                    class_name = "and"
                elif token == "||":
                    class_name = "or"
                elif token == "!":
                    class_name = "not"
                elif token in ["(", ")", "{", "}", "[", "]"]:
                    class_name = "other"
                else:
                    class_name = "unknown"

                # Create a Token object and add it to the list of tokens.
                token_object = Token(class_name, token)
                tokens.append(token_object)

    return tokens

def print_tokens(tokens):
    for token in tokens:
        print(f"{token.class_name} : {token.lexeme}")


if __name__ == "__main__":
    input_file_path = r"C:\Users\Acer\Desktop\New Text Document (2).txt"

    # Read the tokens from the input file.
    tokens = read_tokens(input_file_path)

    # Print the tokens to the console.
    print_tokens(tokens)