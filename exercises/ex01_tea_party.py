"""The purpose of this exericse is to practice several concepts, ultimately resulting in a program that will help plan a cozy tea party."""

__author__: str = "730707069"


def main_planner(guests: int) -> None:
    """Entrypoint of the program, total number of guests attending the tea party"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags" + ": " + str(tea_bags(guests)))
    print("Treats" + ": " + str(treats(guests)))
    print("Cost" + ": " + "$" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of total teabags when each guest is given two bags"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed based on the number of teabags guests are expected to use"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
