import self

class Pet:
    def __init__(self, id, name, age, hunger, happiness, health, alive, last_action_time):
        self.id = id
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.alive = alive
        self.last_action_time = last_action_time
    def __str__(self):
        return f"{self.id},{self.name},{self.age},{self.hunger},{self.happiness}, {self.health}, {self.alive}, {self.last_action_time}"

    def _clamp_value(self, value: int) -> int:
        return max(0, min(100, value))

    def status(self) -> str:
        status_str = f"{self.name} (ID: {self.id}) - {'Жив' if self.alive else 'Мертв'}\n"
        status_str += f"Возраст: {self.age} дней\n"
        status_str += f"Голод: {self.hunger}/100\n"
        status_str += f"Счастье: {self.happiness}/100\n"
        status_str += f"Здоровье: {self.health}/100\n"
        status_str += f"Последнее действие: {self.last_action_time}"
        return status_str

    def feed(self, food) -> None:
        if not self.alive:
            print(f"{self.name} мертв и не может есть")
            return

        if isinstance(food, dict):
            nutrition = food.get('nutrition', 0)
            health_effect = food.get('health_effect', 0)
            happiness_effect = food.get('happiness_effect', 0)
        else:
            nutrition = food.nutrition
            health_effect = food.health_effect
            happiness_effect = food.happiness_effect

        self.hunger = self._clamp_value(self.hunger - nutrition)
        self.health = self._clamp_value(self.health + health_effect)
        self.happiness = self._clamp_value(self.happiness + happiness_effect)
        self.last_action_time += 1

    def play(self, duration: int = 1) -> None:
        if not self.alive:
            return

        self.happiness = self._clamp_value(self.happiness + 5 * duration)
        self.hunger = self._clamp_value(self.hunger + 10 * duration)

        if self.hunger > 70:
            self.health = self._clamp_value(self.health - 5)

        self.last_action_time += duration

    def heal(self) -> None:
        if not self.alive:
            return

        self.health = self._clamp_value(self.health + 20)
        self.happiness = self._clamp_value(self.happiness - 5)
        self.last_action_time += 1

    def time_tick(self) -> None:
        if not self.alive:
            return

        self.age += 1
        self.hunger = self._clamp_value(self.hunger + 5)
        self.happiness = self._clamp_value(self.happiness - 2)

        if self.hunger >= 80:
            self.health = self._clamp_value(self.health - 5)

        if self.happiness <= 10:
            self.health = self._clamp_value(self.health - 2)

        self.check_alive()
        self.last_action_time += 1

    def check_alive(self) -> None:
        if self.health <= 0 or (self.hunger >= 100 and self.health <= 10):
            self.alive = False

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'health': self.health,
            'alive': self.alive,
            'last_action_time': self.last_action_time
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Pet':
        return cls(
            data['id'],
            data['name'],
            data.get('age', 0),
            data.get('hunger', 0),
            data.get('happiness', 100),
            data.get('health', 100),
            data.get('alive', True),
            data.get('last_action_time', 0)
        )