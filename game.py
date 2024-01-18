import random

weight = {"kő": "olló", "papír": "kő", "olló": "papír"}


def start_game(selected: str):
    randomed: str = list(weight.keys())[random.randrange(len(weight.keys()))]
    print(f"\nGép mutatta: {randomed}")

    if randomed == selected:
        print("Döntetlen.")
    elif weight[randomed] == selected:
        print("Vesztettél.")
    else:
        print("Nyertél.")