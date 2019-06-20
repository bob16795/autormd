import ply.lex as lex
import ply.yacc as yacc


class Token():
    def __init__(self, type, value, at):
        self.type = type
        self.value = value
        self.at = at

    def __str__(self):
        return(f"<type: {self.type}, value: {self.value}>")


class Token_List():
    def __init__(self, tokens):
        self.tokens = tokens

    def length(self):
        return len(self.tokens)

    def peek_or(self, choices):
        for i in choices:
            if self.peek(i):
                return True
        return False

    def peek(self, types):
        peeked = [i.type for i in self.tokens[:(len(types))]]
        if peeked == types:
            return True
        return False

    def peek_at(self, index, types):
        return self.offset(index).peek(types)

    def offset(self, index):
        if index == 0:
            return self
        return Token_List(self.tokens[index:])

    def grab(self, index):
        return self.tokens[index]


def tokenize(file_cached):
    token_dict = {
        "_": ["UNDERSCORE", ""],
        "`": ["GRAVE", ""],
        "*": ["STAR", ""],
        "+": ["PLUS", ""],
        "-": ["MINUS", ""],
        "#": ["HASH", ""],
        "<": ["TAGO", ""],
        ">": ["TAGC", ""],
        "\n": ["NEWLINE", ""],
    }
    tokens = []
    ignore = 0
    for x, i in enumerate(file_cached):
        text = ""
        l = i.strip(" ")
        for y, j in enumerate(l):
            if ignore != 0:
                ignore -= 1
                text = f"{text}{j}"
            else:
                if j == "\\":
                    ignore = 1
                elif j in token_dict:
                    if text != "":
                        tokens.append(
                            Token("TEXT", text, f"line {x}, col {y}"))
                        text = ""
                    token = token_dict[j]
                    tokens.append(
                        Token(token[0], token[1], f"line {x}, col {y}"))
                else:
                    text = f"{text}{j}"
        if text != "":
            tokens.append(Token("TEXT", text, f"line {x}, col {y}"))
        tokens.append(Token("NEWLINE", "", f"line {x}, col {y}"))
    tokens.append(Token("EOF", "", f"line {x}, col {y}"))
    return Token_List(tokens)
