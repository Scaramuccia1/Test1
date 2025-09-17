import json
from typing import List, Optional
class PetManager:
    def __init__(self, pets, next_id):
        self.pets = pets
        self.next_id = next_id
    def __str__(self):
        return f"{self.pets},{self.next_id}"

    def add_pet(self, name: str):
        from Pet import Pet
        pet = Pet(self.next_id, name, 0, 0, 100, 100, True, 0)
        self.pets.append(pet)
        self.next_id += 1
        return pet

    def remove_pet(self, pet_id: int) -> bool:
        for i, pet in enumerate(self.pets):
            if pet.id == pet_id:
                self.pets.pop(i)
                return True
        return False

    def get_pet(self, pet_id: int):
        for pet in self.pets:
            if pet.id == pet_id:
                return pet
        return None

    def list_pets(self) -> List[dict]:
        return [{'id': p.id, 'name': p.name, 'alive': p.alive, 'age': p.age} for p in self.pets]

    def tick_all(self) -> None:
        for pet in self.pets:
            pet.time_tick()

    def save(self, filename: str) -> bool:
        try:
            data = {
                'next_id': self.next_id,
                'pets': [pet.to_dict() for pet in self.pets]
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
            return True
        except:
            return False

    def load(self, filename: str) -> bool:
        try:
            from Pet import Pet
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.next_id = data['next_id']
            self.pets = [Pet.from_dict(pet_data) for pet_data in data['pets']]
            return True
        except:
            return False