from array import array
from warnings import catch_warnings


class ListWorker:
    def __init__(self, *list):
        self.array = list

    def only_numbers(self):
        result= []
        for i in self.array:
            if isinstance(i, int):
                result.append(i)
        return result

    def only_strings(self):
        result= []
        for i in self.array:
            if isinstance(i, str):
                result.append(i)
        return result

    def not_string_and_not_number(self):
        result= []
        for i in self.array:
            if not isinstance(i, int) and not isinstance(i , str):
                result.append(i)
        return result

a = ListWorker(13, "a", 666, 1917, "b", "c", [1,2,3])

print(f"a.only_numbers() = {a.only_numbers()}")
print(f"a.only_strings() = {a.only_strings()}")
print(f"a.not_string_and_not_number() = {a.not_string_and_not_number()}")