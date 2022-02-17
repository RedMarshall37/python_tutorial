class Nikola:
    __Nikola = "Николай"

    def __init__(self, name, age):
        self.age = age
        if not name.upper() == "НИКОЛАЙ":
            self.name = f"Я не {name}, я - Император и самодержец Всеройскийский, Московский, Киевский ... Николай II"
        else:
            self.name = "Николай"

Petya = Nikola("Петя", 19)
print(Petya.name)

Petya = Nikola("нИколАй", 19)
print(Petya.name)