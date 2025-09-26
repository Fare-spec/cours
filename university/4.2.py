import random as rng


def create_number(start: int, end: int) -> int:
    return rng.randint(start, end)


def main_part(start: int, end: int, max_tries: int) -> (bool, int):
    number_to_guess = create_number(start, end)
    guess = int(input("Entrez votre nombre: "))
    tries = 1
    while guess != number_to_guess and tries < max_tries:
        if guess < number_to_guess:
            print(f"{guess} est trop petit")
            start = max(guess, start)
        else:
            print(f"{guess} est trop grand")
            end = min(guess, end)
        tries += 1
        guess = int(input(f"Entrez votre nombre [{start};{end}]: "))

    if guess == number_to_guess:
        print(
            f"Félicitation vous avez correctement deviner le nombre {number_to_guess} au bout de {tries}"
        )
        return True, tries
    else:
        print("Perdu")
        return False


if __name__ == "__main__":
    start = 0
    end = 100
    max_tries = 5
    again = True
    played_game = 1
    game_won = 0
    stats = []
    while again:
        game = main_part(start, end, max_tries)
        game_won += 1 if game[0] else 0
        stats.append(game[1])
        again = "y" == input("Voulez vous recommencez ? (y/n)")
