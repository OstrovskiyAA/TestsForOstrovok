import dataclasses


@dataclasses.dataclass
class Search:
    destination:str
    month:str
    date_of_start:int
    date_of_finish:int
    amount_of_int:int
    aim_of_trip:str