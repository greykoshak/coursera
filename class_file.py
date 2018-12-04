class File:
    """ Class with predefined properties """

    # 1. Initial with full path
    def __init__(self, path):
        self.path_to = path


    # 2. Method write
    def write(self, line):
        with open(self.path_to, "w") as fw:
            fw.write(line)
            fw.write(line)

    # 3. Adding (__add__)
    def __add__(self, other_file):
        with open(other_file) as fd:
            pass

        return True

        # 4. Iteration (__iter__)

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
    new_class = File("/home/gk/PycharmProjects/coursera/temp.txt")
    print(new_class)
    new_class.write("Trying...")

    for line in new_class:
        print(line)


if __name__ == "__main__":
    _main()
