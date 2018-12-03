import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0

        if self.body_whl:
            whl = self.body_whl.split('x')
            self.body_width = float(whl[0])
            self.body_height = float(whl[1])
            self.body_length = float(whl[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


# car_type(0)	brand(1) passenger_seats_count(2) photo_file_name(3) body_whl(4) carrying(5) extra(6)
class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def car_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)  # пропускаем заголовок
        try:
            for row in reader:
                if len(row) == 7:
                    if row[0] == "car":
                        new_car = Car(row[1], row[3], row[5], row[2])
                    elif row[0] == "truck":
                        new_car = Truck(row[1], row[3], row[5], row[4])
                    elif row[0] == "spec_machine":
                        new_car = SpecMachine(row[1], row[3], row[5], row[6])
                    else:
                        raise ValueError("Fault car_type: ", row[0])

                    car_list.append(new_car)

        except ValueError as err:
            message, value = err.args[0], err.args[1]
            print(message, value)

    return car_list


def _main():
    cars = car_car_list("cars.csv")


if __name__ == "__main__":
    _main()
