import requests
import random

base_url = "https://pokeapi.co/api/v2/"


def get_poke_info(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)
    if name == "q":
        pass
    elif response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"failed to retrieve data | Status: {response.status_code}")


def show_all_pokemon():
    url = f"{base_url}pokemon?limit=151"
    response = requests.get(url)
    if response.status_code == 200:
        all_poke_data = response.json()
        return all_poke_data
    else:
        print(f"failed to retrieve data | Status: {response.status_code}")


def get_id(info):
    return f"{info["id"]:03}"


def get_name(info):
    return f"{info["name"]}"


def get_types(info):
    poke_types = info["types"]
    types = [poke_type["type"]["name"] for poke_type in poke_types]
    return types


def get_stats(info):
    poke_stats = info["stats"]
    stats = [{stat["stat"]["name"]: stat["base_stat"]} for stat in poke_stats]
    return stats


def get_all_abilities(info):
    poke_ablilities = info["abilities"]
    abilities = [ability["ability"]["name"] for ability in poke_ablilities]
    return abilities


def get_all_moves(info):
    moves = info["moves"]
    all_moves_list = [move["move"]["name"] for move in moves]
    return all_moves_list


def get_random_ability(all_abilities):
    ability = random.choice(all_abilities)
    return ability


def get_random_moveset(all_moves):
    if len(all_moves) < 4:
        poke_move_set = all_moves
    else:
        poke_move_set = random.sample(all_moves, k=4)
    move_set = [move for move in poke_move_set]
    return move_set


def show_poke_id(poke_id):
    print("=====ID=====")
    print(f"#{poke_id}")


def show_poke_name(poke_name):
    print("=====Name=====")
    print(poke_name.capitalize())


def show_poke_type(poke_types):
    print("=====Type=====")
    for poke_type in poke_types:
        print(f"{poke_type.capitalize()}")


def show_poke_stats(poke_stats):
    print("=====Stats=====")
    for stats in poke_stats:
        for stat, value in stats.items():
            print(f"{stat.upper()}: {value}")


def show_poke_ability(poke_ability):
    print("=====Ability=====")
    print(poke_ability.capitalize())


def show_poke_moves(poke_moveset):
    print("=====Moves=====")
    for i, move in enumerate(poke_moveset):
        print(f"{i + 1}. {move.capitalize()}")


def get_and_show_info(poke_info):
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
