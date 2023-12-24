from dataclasses import dataclass, field


@dataclass(order=True)
class Competitor:
    sort_index: int = field(init=False, repr=False)
    firstname: str
    lastname: str
    wins: int

    def __post_init__(self):
        self.sort_index = self.wins


class ShoppingCart:
    def __init__(self):
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def remove(self, item):
        self.contents.remove(item)

    def checkout(self):
        print(" OFORMLENIE POKUPOK")
        for index, item in enumerate(self.contents, start=1):
            print(f"{index}. {item}.")


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    jack = Competitor(firstname="Jack", lastname="Paterson", wins=7)
    paul = Competitor("Paul", "Brown", 5)
    print(jack > paul)
    print(jack, "- is Jack", "\n ", paul, "- is Paul")
