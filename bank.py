class BankAccount:
    def __init__(self, account_number, pin_code, balance):
        self.account_number = account_number
        self.pin_code = pin_code
        self.balance = balance

    def get_account_number(self):
        print(f"Номер счета: {self.account_number}")

    def get_pin_code(self):
        print(f"Пин код карточки: {self.pin_code}")

    def set_pin_code(self, set_pin_code):
        self.pin_code = set_pin_code

    def total_balance(self):
        print(f'Текущий счет: {self.balance}')

    def credit_balance(self, credit):
        if 1000 <= credit <= 300000 and credit % 1000 == 0:
            if self.balance < credit:
                print("У вас не достаточно средств")
            else:
                self.balance -= credit
        elif 300000 < credit <= 990000 and credit % 1000 == 0:
            credit1 = credit - 300000
            credit1 = credit1 * 1.02
            credit2 = 300000 + credit1
            if self.balance < credit2:
                print("У вас не достаточно средств")
            else:
                self.balance -= credit2
        else:
            print('Вы ввели не правильную сумму')

    def debet_balance(self, add_balance):
        self.balance += add_balance

    def account_data(self):
        print(f"Данные о клиенте: {self.account_number} {self.pin_code} {self.balance}")


class CityBankAccount(BankAccount):
    # def __init__(self, name, surname, balance, account_number, pin_code):
    def __init__(self, name, surname, account_number, pin_code, balance):
        super().__init__(account_number, pin_code, balance)
        self.name = name
        self.surname = surname

    def account_data(self):
        print(f"Данные о клиенте: {super().account_data()} {self.name} {self.surname}")


class NationalBankAccount(BankAccount):
    def __init__(self, full_name, account_number, pin_code, balance):
        super().__init__(account_number, pin_code, balance)
        self.full_name = full_name

    def account_data(self):
        print(f"Данные о клиенте: {super().account_data()} {self.full_name}")


CBA1 = CityBankAccount('Altayeva', 'Dinara', '0000', '1111', 250000)
CBA2 = CityBankAccount('Bakytov', 'Nurdaulet', '2222', '1212', 2500000)
CBA3 = CityBankAccount('Soltybek', 'Aruzhan', '3333', '1931', 350000)
CBA4 = CityBankAccount('Shalmen', 'Symbat', '4444', '1287', 450000)
CBA5 = CityBankAccount('Zhabayev', 'Zhanbolat', '5555', '1954', 550000)
CBA6 = CityBankAccount('Altayeva', 'Dinara', '1212', '3482', 120000)
CBA7 = CityBankAccount('Duisenov', 'Sultan', '1313', '1542', 100000)
CBA8 = CityBankAccount('Zhantileuova', 'Dana', '1313', '2000', 2000000)



NB1 = NationalBankAccount('Abdrakhmanov Arystanbek', '6666', '9991', 160000)
NB2 = NationalBankAccount('Bekeshov Rymzhan Talgatuly', '7777', '8081', 260000)
NB3 = NationalBankAccount('Abdrkhamnov Arystanbek Ramazanuly', '8888', '8871', 360000)
NB4 = NationalBankAccount('Borubayev Almat Baqytbekuly', '9999', '8788', 460000)
NB5 = NationalBankAccount('Knyazev Akzhol Ganiuly', '1112', '8900', 560000)


class DataBase:
    all_accounts = [CBA1,
                    CBA2,
                    CBA3,
                    CBA4,
                    CBA5,
                    CBA6,
                    CBA7,
                    CBA8,
                    NB1,
                    NB2,
                    NB3,
                    NB4,
                    NB5
                    ]
