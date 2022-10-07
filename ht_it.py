nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# Итератор
class FlatIterator:

    def __init__(self, n_list):
        self.n_list = n_list

    def __iter__(self):
        self.iter_list = iter(self.n_list)
        self.str_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.str_list) == self.cursor:
            self.str_list = None
            self.cursor = 0
            while not self.str_list:
                self.str_list = next(self.iter_list)
        return self.str_list[self.cursor]


# Генератор
def flat_generator(n_list):

    for s_list in n_list:
        for element in s_list:
            yield element


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


for item in flat_generator(nested_list):
    print(item)
