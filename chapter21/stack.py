class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

word_stack = Stack()
for c in "Hello":
    word_stack.push(c)

reverse = ""
while word_stack.size():
    reverse += word_stack.pop()

print(reverse)


print("--practice No.1--")
string = "yesterday"
str_stack = Stack()

for c in string:
    str_stack.push(c)

reverse_string = ""
while str_stack.size():
    reverse_string += str_stack.pop()

print(reverse_string)


print("--practice No.2--")
items = [1, 2, 3, 4, 5]

item_stack = Stack()
for i in items:
    item_stack.push(i)

reverse_item = []
while item_stack.size():
    reverse_item.append(item_stack.pop())

print(reverse_item)
