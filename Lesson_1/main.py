class Roomba:

    def __init__(self, name):
        self.name = name
        self._squashed = False

    def __str__(self):
        if self._squashed:
            return f"Hi my name is {self.name} and I am squashed"
        else:
            return f"Hi my name is {self.name} and I feeling fine"

    def squish(self):
        self._squashed = True


class Plumber:

    def __init__(self, name):
        self.name = name

    def squash(self, roomba):
        roomba.squish()


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
