#! /usr/bin/env python3

import pandas as pd
import pokebase as pb
import pickle
import sys
arguments = sys.argv

def save_data_to_file(data, filename):
    with open(f"{filename}.pickle", 'wb') as handle:
        pickle.dump(data, handle)
def load_file_to_data(filename):
    with open(f"{filename}.pickle", 'rb') as handle:
        data = pickle.load(handle)
    return data

if "-m" in arguments:
    pokemon = {}

    for i in range(1,808):
        p = pb.pokemon(i)
        types = []
        
        for j in p.types:
            types.append(j.type.name)

        pokemon[p.name] = (i,
                            types,
                            p.stats[5].base_stat,
                            p.stats[4].base_stat,
                            p.stats[3].base_stat,
                            p.stats[2].base_stat,
                            p.stats[1].base_stat,
                            p.stats[0].base_stat
                            )
        print((i/807) * 100)


    save_data_to_file(pokemon, "pokemon")

pokemon = load_file_to_data("pokemon")

df = pd.DataFrame.from_dict(
    data=pokemon,
    orient='index',
    columns=("Number", "Type", "HP", "Attack", "Defense",
    "Sp. Attack", "Sp. Defense", "Speed")
)
