from math import abs
import random

def calculate_compatibility(name1, name2):
    names = [name1, name2]
    seed = "".join(names)
    gen = random.Random(seed)
    compatibility = (gen.random()) * 100 + 1
    return int(compatibility)

    #TODO Add compatibility calculator

if __name__ == "__main__":
    print("Hello, world!")
    #pass
    #TODO Add your main section code here