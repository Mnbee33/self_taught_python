import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain.
it's a bad idea.
If the implementation
is easy to explain,
it may be a good,
it may be a good
idea. Namespace
are one honking
great idea -- let's
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."
m = re.findall("t[wo]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)
