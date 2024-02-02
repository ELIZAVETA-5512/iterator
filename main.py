class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.item_nom = 0
        self.subitem_nom = -1
        return self

    def __next__(self):
        self.subitem_nom += 1
        if self.subitem_nom >= len(self.list_of_lists[self.item_nom]):
            self.item_nom += 1
            self.subitem_nom = 0
        if self.item_nom >= len(self.list_of_lists):
            raise StopIteration
        item = self.list_of_lists[self.item_nom][self.subitem_nom]
        return item



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()