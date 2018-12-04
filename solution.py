import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


with open("cars.csv") as csv_fd:
    reader = csv.reader(csv_fd, delimiter=";")
    next(reader)  # пропускаем заголовок
    for row in reader:
        print(row)


def car_car_list(csv_filename):
    car_list = []
    return car_list


def _main():
    print("Main")


if __name__ == "__main__":
    _main()
