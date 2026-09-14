from funcs import *


def main():
    running = True
    while running:
        poke_request = input("Type a Pokemon name (press q to quit): ").lower()

        poke_info = get_poke_info(poke_request)

        if poke_info:
            poke_id = get_id(poke_info)
            poke_name = get_name(poke_info)
            poke_types = get_types(poke_info)
            poke_stats = get_stats(poke_info)
            all_poke_abilities = get_all_abilities(poke_info)
            poke_ability = get_random_ability(all_poke_abilities)
            all_poke_moves = get_all_moves(poke_info)
            poke_moveset = get_random_moveset(all_poke_moves)

            show_poke_id(poke_id)
            show_poke_name(poke_name)
            show_poke_type(poke_types)
            show_poke_stats(poke_stats)
            show_poke_ability(poke_ability)
            show_poke_moves(poke_moveset)

        elif poke_request == "q":
            running = False
            break
        else:
            print(f"No info available for {poke_request}!")


if __name__ == "__main__":
    main()
