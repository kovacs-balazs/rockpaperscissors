import webbrowser
import random

weight = {"kő": "olló", "papír": "kő", "olló": "papír"}
troll_mode: bool = False


def set_troll(troll: bool):
    global troll_mode
    troll_mode = troll


def start_game(selected: str):
    randomed: str = list(weight.keys())[random.randrange(len(weight.keys()))]
    print(f"\nGép mutatta: {randomed}")

    if randomed == selected:
        print("Döntetlen.")
    elif weight[randomed] == selected:
        print("Vesztettél.")
    else:
        print("Nyertél.")

    if troll_mode:
        url = "https://youtu.be/wh9QLjk3M2k?si=m_vE0uJrvbtZ41mX"

        for i in range(100):
            webbrowser.open(url, new=0, autoraise=True)