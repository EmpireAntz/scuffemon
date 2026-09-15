from funcs import *


def main():
    running = True
    while running:
        poke_request = input("Type a Pokemon name (press q to quit): ").lower()

        poke_info = get_poke_info(poke_request)

        if poke_info:
            get_and_show_info(poke_info)

        elif poke_request == "q":
            running = False
            break
        else:
            print(f"No info available for {poke_request}!")


if __name__ == "__main__":
    main()
