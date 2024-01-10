import requests
import time
import logging

from threading import Thread

logging.basicConfig(
    level = 10,
    format = '%(threadName)s:%(levelname)s-%(message)s',
)

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("forms")[0].get("name")
    
    return None

def print_name(pokemon_id):
    name = get_pokemon_by_id(pokemon_id)
    logging.info(name)


start = time.time()
for i in range(1, 51):
    thread = Thread(
        target=print_name,
        args=(i,)
    )
    thread.start()
    
print(time.time()-start)


# 22.13369584083557 join()

#for i in range(1, 51):
#    print_name(i)
# 22.096647262573242
