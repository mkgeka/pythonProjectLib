#!/usr/bin/env python
def replacer(s: str) -> str:
    message = ""
    for symbol in s:
        if symbol.find("\"") != -1:
            character = symbol.replace("\"", "\'")
            message = message + character
        elif symbol.find("\'") != -1:
            character = symbol.replace("\'", "\"")
            message = message + character
        else:
            message = message + symbol
    return message
output = replacer('\'"\'\'"\'\'"\'\'"\'\'"\'\'"\'\'"\'')
print(output)