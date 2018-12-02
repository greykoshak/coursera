class FileReader:
    """Класс FileReader помогает читать из файла"""

    def __init__(self, path_to):
        self.path_to = path_to

    def read(self):
        try:
            with open(self.path_to, "r") as f:
                data = f.read()
        except IOError:
            return ""
        else:
            return data


if __name__ == "__main__":
    reader = FileReader("example.txt")
    print(reader.read())
