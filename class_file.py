import os
import tempfile


class File:
    """ Class with predefined properties """

    # 1. Initial with full path
    def __init__(self, path):
        self.path_to = path  # Полное имя файла
        self.current_line = 1  # Указатель на текущую строку для считывания

        # Прочитать содержимое файла для реализации __add__
        with open(self.path_to) as f:
            self.value = f.readlines()

    # 2. Method write
    def write(self, line):
        with open(self.path_to, "a+") as fw:
            fw.write(line)

    # 3. Adding (__add__)
    def __add__(self, obj):
        third = os.path.join(tempfile.gettempdir(), 'third.txt')

        with open(third, "w+") as fd:
            fd.writelines(self.value)
            fd.writelines(obj.value)
        return File(third)

    # 4. Iteration (__iter__)
    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to) as fr:
            try:
                for _ in range(1, self.current_line):
                    fr.readline()
                line = fr.readline()
                if not line:
                    raise StopIteration

                self.current_line += 1
            except:
                raise StopIteration
        return line

    # 5. print(obj)
    def __str__(self):
        return "class File: {}".format(self.path_to)


def _main():
    first_class = File(os.path.join(tempfile.gettempdir(), 'first.txt'))
    first_class.write("Trying123...\n")

    second_class = File(os.path.join(tempfile.gettempdir(), 'second.txt'))
    second_class.write("Trying213...\n")

    third = first_class + second_class

    for line in third:
        print(line)


if __name__ == "__main__":
    _main()
