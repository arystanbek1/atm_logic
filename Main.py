from bank import BankAccount, CityBankAccount, NationalBankAccount, DataBase

my_account = 0
choose_bank_class = 0
count_for_break = 0
true = True
count_error_pin = 0
account = 0

a = input('Введите номер аккаунта: ')
for i in DataBase.all_accounts:
    if i.account_number == a:
        account = i
        break
else:
    print('Invalid value')
    exit(0)


while True:
    b = input('Введите ваш пин код: ')
    count_error_pin += 1

    if account.pin_code == b and isinstance(account, CityBankAccount):
        my_account = account
        choose_bank_class = 1
        break
    elif account.pin_code == b and isinstance(account, NationalBankAccount):
        my_account = account
        choose_bank_class = 2
        break
    if len(b) == 4 and b != account.pin_code:
        print('Неверный пароль, у вас осталось', 3 - count_error_pin, 'попытки(-ок), после вы будете заблокированы')

    elif len(b) > 4 or len(b) < 4:
        print('Неверный пароль, у вас осталось', 3 - count_error_pin, 'попытки(-ок), после вы будете заблокированы')

    else:
        print('Неверный пароль, у вас осталось', 3 - count_error_pin, 'попытки(-ок), после вы будете заблокированы')
    count_for_break += 1
    if count_for_break == 3:
        break

if choose_bank_class == 1:
    while True:
        x = input("PRESS [1] TO CASH WITHDRAWAL\nPRESS [2] TO VIEW BALANCE\n"
                  "PRESS [3] TO CHANGE PIN CODE\nPRESS [4] TO CASH IN ACCOUNT\n"
                  "PRESS [5] TO VIEW ACCOUNT DATA\nPRESS [6] TO EXIT\n")

        if x == '1':
            my_account.credit_balance(int(input('Введите сумму которую вы хотите снять: ')))

        elif x == '2':
            my_account.total_balance()

        elif x == '3':
            my_account.set_pin_code(int(input('Введите новый пин код:')))

        elif x == '4':
            my_account.debet_balance(int(input('User должен в банкомате поставить свою купюру')))

        elif x == '5':
            my_account.account_data()

        elif x == '6':
            break

elif choose_bank_class == 2:
    while True:
        x = input("PRESS [1] TO CASH WITHDRAWAL\nPRESS [2] TO VIEW BALANCE\nPRESS [3] TO EXIT\n")

        if x == '1':
            my_account.credit_balance(int(input('Введите сумму которую вы хотите снять: ')))
            my_account.balance -= 200

        elif x == '2':
            my_account.total_balance()

        elif x == '3':
            break
