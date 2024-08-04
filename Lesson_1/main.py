class Roomba:
    pass


class Plumber:
    pass


def main():
    hetti = Roomba("Hetti")
    olga = Roomba("Olga")
    bob = Roomba("Bob")
    print(hetti)  # Hi my name is Hetti and I am feeling fine
    print(olga)  # Hi my name is Olga and I am feeling fine
    print(bob)  # Hi my name is Bob and I am feeling fine

    merio = Plumber("Merio")
    merio.squash(olga)

    print(hetti)  # Hi my name is Hetti and I am feeling fine
    print(olga)  # Hi my name is Olga and I am squashed
    print(bob)  # Hi my name is Bob and I am feeling fine


if __name__ == "__main__":
    main()