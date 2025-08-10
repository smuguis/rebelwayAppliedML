from dataclasses import dataclass, field
from library.random_number_utils import RandomUtils

@dataclass(frozen=True, order=True, slots=True)
class Book:
    title: str
    author: str
    genre: str
    _price: float = 0.0
    id:str = field(default_factory=RandomUtils.generate_random_id)

    @property
    def price(self):
        return round(self._price, 2)

    @property
    def search_string(self):
        return f"{self.title} {self.author} {self.genre} {self.title}"
