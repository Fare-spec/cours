import random as rng


def random_int(start: int, end: int) -> int:
    return rng.randint(start, end)


start = 0
end = 100
number = random_int(start, end)


def is_number(guess) -> int:
    if number == guess:
        return 0
    elif number < guess:
        return 1
    else:
        return -1


def dumb_ai(start: int, end: int) -> int:
    tries = 0
    while True:
        guess = rng.randint(start, end)
        tries += 1
        if is_number(guess) == 0:
            return tries


def guess_number(start: int, end: int) -> int:
    tries = 0
    while True:
        guess = (start + end) // 2

        tries += 1
        hint = is_number(guess)
        if hint == 0:
            return tries
        elif hint == -1:
            start = guess + 1
        else:
            end = guess - 1


def main(start, end) -> int:
    print(f"Number to guess: {number}")
    return guess_number(start, end)


if __name__ == "__main__":
    n = int(input("Number of games: "))
    tries_global = list()
    for _ in range(n):
        tries_smart = main(start, end)
        tries_dumb = dumb_ai(start, end)
        print(tries_dumb, tries_smart)
        print("*" * tries_smart)
        print("-" * tries_dumb)
        tries_global.append(tries_smart)

    print(f"{sum(tries_global) / len(tries_global)}")
