import csv

def no1():
    print("--No.1--")
    with open("st.csv", "r") as f:
        print(f.read())

def no2():
    print("--No.2--")
    color = input("What color is your favarite?: ")
    with open("color.txt", "w") as f:
        f.write(color)

def no3():
    print("--No.3--")
    movies = [["Top Gun", "Risky Business", "Minority Report"],
              ["Titanic", "The Revenant", "Inception"],
              ["Training Day", "Man on Fire", "Flight"]]

    with open("movie.csv", "w", newline="") as f:
        w = csv.writer(f, delimiter=",")
        for title in movies:
            w.writerow(title)

def no4():
    print("--No.4--")
    movies = [["トップガン", "リスキービジネス", "マイノリティーリポート"],
              ["タイタニック","レヴェナント","インセプション"],
              ["トレーニングデー","マン　オン　ファイア","フライト"]]

    with open("movieJp.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=",")
        for title in movies:
            w.writerow(title)

# practice
no1()
#no2()
no3()
no4()
