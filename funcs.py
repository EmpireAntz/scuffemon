import requests
import random

base_url = "https://pokeapi.co/api/v2/"


def get_poke_info(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"failed to retrieve data | Status: {response.status_code}")


def get_id(info):
    print("======ID======")
    print(f"{info["id"]:03}")


def get_name(info):
    print("======Name======")
    print(f"{info["name"].capitalize()}")


def get_types(info):
    print("======Types======")
    poke_types = info["types"]
    for poke_type in poke_types:
        print(f"{poke_type["type"]["name"]}".capitalize())


def get_stats(info):
    print("======Stats======")
    stats = info["stats"]
    for stat in stats:
        print(f"{stat["stat"]["name"].capitalize()}: {stat["base_stat"]}")


def get_all_abilities(info):
    print("======Abilities======")
    ablilities = info["abilities"]
    for i, ability in enumerate(ablilities):
        print(f"{i + 1}. {ability["ability"]["name"].capitalize()}")


def get_all_moves(info):
    moves = info["moves"]
    all_moves_list = [move["move"]["name"].capitalize() for move in moves]
    return all_moves_list


def get_random_moveset(all_moves):
    print("======Moves======")
    move_set = random.sample(all_moves, k = 4)
    for i, move in enumerate(move_set):
        print(f"{i + 1}. {move}")
