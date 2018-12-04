class File:
    """ Class with predefined properties """

    # 1. Initial with full path
    def __init__(self, path):
        self.path_to = path

    # 2. Method write
    def write(self, line):
        with open(self.path_to, "w") as fw:
            fw.write(line)

    # 4. Iteration
    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to, "r") as fr:
            try:
                line = fr.readline()
            except EOFError:
                raise StopIteration
        return line

    # 5. print(obj)
    def __str__(self):
        return "class File: {}".format(self.path_to)


def _main():
    new_class = File("/Users/iagarkov/PycharmProjects/coursera/temp.txt")
    print(new_class)

    for line in new_class:
        print(line)

if __name__ == "__main__":
    _main()
