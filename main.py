from funcs import *


def main():
    running = True
    while running:
        poke_name = input("Type a Pokemon name (press q to quit): ").lower()

        poke_info = get_poke_info(poke_name)

        if poke_info:
            get_id(poke_info)
            get_name(poke_info)
            get_types(poke_info)
            get_stats(poke_info)
            get_all_abilities(poke_info)
            all_moves = get_all_moves(poke_info)
            get_random_moveset(all_moves)
        elif poke_name == "q":
            running = False
            break
        else:
            print(f"No info available for {poke_name}!")


if __name__ == "__main__":
    main()
