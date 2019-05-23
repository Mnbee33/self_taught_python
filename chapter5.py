print("--No.1--")
musicians = ["Mr.children", "RadWhindps", "T.M.Revolution"]
print(musicians)

print("--No.2--")
my_travel = [("35.632896", "139.880394")]
print(my_travel)

print("--No.3--")
my_profile = {"height":"176.5", "weight":"61.5", "color": "red", "age":"28"}
print(my_profile)

print("--No.4--")
keyword = input("What question is for me? :")

if keyword in my_profile:
    print(keyword + ":" + my_profile[keyword])
else:
    print("I can't answer.")

print("--No.5--")
mrc_songs = ["Singles", "yourthful days", "Hero"]
tmv_songs = ["invoke", "Hot Limit"]
favorite_artists = {"Mr.children": mrc_songs,
                  "T.M.Revolution": tmv_songs}
print(favorite_artists)
