print("--No.1--")
channels = ["walking dead", "entrage", "the soprano", "vampire diaries"]
for channel in channels:
    print(channel)

print("--No.2--")
for i in range(25, 51):
    print(i)

print("--No.3--")
for i, channel in enumerate(channels):
    print("{}: {}".format(i, channel))

print("--No.4--")
corrects = [1, 4, 10, 7]
while True:
    answer = input("Type number: ")

    if answer == 'q':
        break
    
    try:
        answer = int(answer)
    except ValueError:
        print("Type number, or type q to quit: ")
        continue
    
    if answer in corrects:
        print("that's right")
    else:
        print("miss! Try agein")

print("--No.5--")
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multipled = []

for i in list1:
    for j in list2:
        multipled.append(i * j)

print(multipled)
