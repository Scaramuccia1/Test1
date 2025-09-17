from PetManager import PetManager
from Food import  FOOD_TYPES

def main():
    manager = PetManager()
    cat = manager.add_pet("Мурзик")
    dog = manager.add_pet("Шарик")
    print("Начальный статус:")
    print(cat.status())
    print()
    cat.feed(FOOD_TYPES['обычная'])
    dog.feed()