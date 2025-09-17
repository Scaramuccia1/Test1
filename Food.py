class Food:
    def __init__(self, name, nutrition, health_effect, happiness_effect):
        self.name = name
        self.nutrition = nutrition
        self.health_effect = health_effect
        self.happiness_effect = happiness_effect
    def __str__(self):
        return f"{self.name},{self.nutrition},{self.health_effect},{self.happiness_effect}"
    def to_dict(self) -> dict:
        return {
            'Имя': self.name,
            'Питание': self.nutrition,
            'Оздоровительный эффект': self.health_effect,
            'Эффект счастья': self.happiness_effect
        }
    def from_dict(cls, data: dict) -> 'Food':
        return cls(name=data['name'],nutrition=data['nutrition'],health_effect=data.get('health_effect', 0),happiness_effect=data.get('happiness_effect', 0))
FOOD_TYPES = {'обычная': Food("Обычная еда", nutrition=30, health_effect=2, happiness_effect=1),
    'полезная': Food("Полезная еда", nutrition=25, health_effect=10, happiness_effect=0),}