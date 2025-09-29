from ast import dump, parse, AST

"""
a
"""
with open("t.py") as file:
    foobar: AST = parse(file.read())
    print(dump(foobar, indent="  "))