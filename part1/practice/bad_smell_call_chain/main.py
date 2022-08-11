# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_population: str, room_num: int):
        self.city_popultaion = city_population
        self.room_num = room_num

    def get_person_room(self) -> int:
        return self.room_num

    def get_city_population(self) -> str:
        return self.city_popultaion


# после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

new_person = Person("Moscow", 55)
print(new_person.city_popultaion)
print(new_person.room_num)
