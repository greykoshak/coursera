class Value:
    """Дескриптор данных, который устанавливает и возвращает
       значение после вычитания комиссии.
    """

    def __init__(self, amount=0):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value * (1 - obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


def _main():
    new_account = Account(0.2)
    new_account.amount = 200

    print(new_account.amount)


if __name__ == "__main__":
    _main()
