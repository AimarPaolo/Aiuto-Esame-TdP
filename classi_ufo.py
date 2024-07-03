from dataclass import dataclass

@dataclass
class Avvistamenti:
    id: int
    datetime: int
    #importare datetime
    city: str
    state: str
    country: str
    shape: str
    duration: int
    duration_hm: str
    comments: str
    date_posted: str
    latitude: float
    longitude: float

    def __hash__(self):
        return hash(self.id)


#####################################
    from dataclasses import dataclass

    @dataclass
    class Anno:
        anno: int
        avvistamenti: int

#####################################
from dataclasses import dataclass


@dataclass
class Stato:
    id: str
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: int
    Population: int
    Neighbors: str

    def __hash__(self):
       return hash(id)

#####################################
from dataclasses import dataclass

from model.stato import Stato
@dataclass
class Confine:
    _c1: Stato
    _c2: Stato

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    def __hash__(self):
        return hash((self._c1.id, self._c2.id))

    def __str__(self):
        return f"Border: {self._c1} - {self._c2}"

#####################################
