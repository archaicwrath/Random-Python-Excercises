
def main():
    with open('data/temp.csv', 'r') as file:
        data = [line.strip().rsplit(',') for line in file]

    dataList = []

    for i in data:
        listElem = []
        for j in i:
            listElem.append(float(j))
        dataList.append(listElem)

    newList = avg(dataList, 10)

    print(newList)


def avg(data, amnt):
    sublist = []
    for i in range((len(data) + amnt - 1) // amnt):
        sublist.append(sum(data[i*amnt:(i+1)*amnt]) / amnt)
        return sublist


if __name__ == '__main__':
    main()