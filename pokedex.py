from funcs import *


def main():
    all_pokemon = show_all_pokemon()["results"]
    for pokemon in all_pokemon:
        poke = get_poke_info(pokemon['name'])
        get_and_show_info(poke)


if __name__ == "__main__":
    main()
