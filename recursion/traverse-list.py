def count_leaf_items(linked_list: list) -> int:
    length = 0
    for item in linked_list:
        if type(item) is not list:
            length += 1
        else:
            length += count_leaf_items(item)
    return length


if __name__ == '__main__':
    names = [
        'Adam',
        [
            'Bob',
            ['Chet', 'Cat', 'Hick'],
            'Barb',
            'Bert',
        ],
        'Alex',
        ['Bea', 'Bill'],
        'Ann',
    ]

    print(count_leaf_items(names))
