print("--No.1--")
his_name = "Camus"
print(his_name[0])
print(his_name[1])
print(his_name[2])
print(his_name[3])
print(his_name[4])

print("--No.2--")
what = input("what:")
who = input("who:")
message = "Yesterday I wrote {} and send it to {}.".format(what, who)
print(message)

print("--No.3--")
print("aldous Huxley was born in 1894.".title())

print("--No.4--")
w_word_line = "where? who? when?"
words = w_word_line.split(" ")
print(words)

print("--No.5--")
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox_move = " ".join(words[:len(words)-1])
fox_move += words[len(words)-1] 
print(fox_move)

print("--No.6--")
before_line = "A screaming comes across the sky."
print(before_line.replace("s", "$"))

print("--No.7--")
print("Hemingway".index("m"))

print("--No.8--")
title = "The Adventure of \"The Western Star\""
print(title)

print("--No.9--")
three = "three "
print((three + three + three).strip())
print((three * 3).strip())

print("--No.10--")
before_str = "It was a bright cold day in April, and the clocks were striking thirtheen"
slice_str = before_str[:before_str.index(",")]
print(slice_str)
