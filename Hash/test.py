from hashtable import HashTable

def main():
    hTable = HashTable(37)
    hTable.insertItem(hTable.hashItem(48), 48)
    hTable.insertItem(hTable.hashItem(92), 92)
    hTable.insertItem(hTable.hashItem('louis'), 'louis')

    print(hTable)

if __name__ == '__main__':
    main()
