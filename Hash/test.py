from hashtable import HashTable


def main():
    hTable = HashTable(17)
    hTable.insertItem(hTable.hashItem(48), 48)
    hTable.insertItem(hTable.hashItem(92), 92)
    hTable.insertItem(hTable.hashItem('louis'), 'louis')
    hTable.insertItem(hTable.hashItem(3.764), 3.764)
    hTable.insertItem(hTable.hashItem([3, 4, 5, 6, 7, 8, 9]), [3, 4, 5, 6, 7, 8, 9])
    hTable.insertItem(hTable.hashItem({'name':'Louis'}), {'name':'Louis'})

    print(hTable)


if __name__ == '__main__':
    main()
