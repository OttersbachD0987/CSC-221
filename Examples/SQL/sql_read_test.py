import sqlite3 as sql3
import textwrap
import timeit
import os

connection = sql3.connect("test.db")
cursor = connection.cursor()
row1 = "="*30
row2 = "-"*30
setup = r'''
cursor.execute("""
    SELECT name, description
    FROM TEST
""")

'''

end = r'''
'''

whileTest = r'''
while (row := cursor.fetchone()) != None:
    print(f"{"\n":=>30}{row[0]}{"\n":-<30}\n{"\n".join(textwrap.wrap(row[1], 30))}{"\n":=<30}")

''' + end
smartTest = r'''
print(f"{row1}\n{f"\n{row1}\n".join([f"{row[0]}\n{row2}\n{"\n".join(textwrap.wrap(row[1], 30))}" for row in cursor.fetchall()])}\n{row1}")

''' + end

fa = open(os.path.devnull, "w")

glob = {
    "cursor": cursor,
    "connection": connection,
    "row1": row1,
    "row2": row2,
    "textwrap": textwrap,
    "print": lambda a: print(a, file=fa)
}

print(f"While Test: {timeit.timeit(setup, whileTest, number=100, globals=glob)}")

print(f"Smart Test: {timeit.timeit(setup, smartTest, number=100, globals=glob)}")


cursor.close()
connection.close()


