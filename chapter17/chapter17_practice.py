import re

print("--No.2--")
text = "Arizona 479, 501, 870. California 209, 213, 650."
match = re.findall("\d", text)
print(match)

print("--No.3--")
text = "the ghost that says boo haunts the loo"
match = re.findall(".oo", text)
print(match)
