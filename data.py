
if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        data = f.readlines()
        d = {}
        for line in data:
            name, age = line.rsplit(maxsplit=1)
            d[name] = int(age)
        as_age = sorted(d.items(), key=lambda p: p[1])
        file = open('data_age.txt', 'a')
        for line in as_age:
            file.write(line[0] + ' ' + str(line[1]) + '\n')
        file.close()