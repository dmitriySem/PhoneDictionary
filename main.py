def input_surname():
    return input('Введите фамилию контакта: ')

def input_name():
    return input('Введите имя контакта: ')

def input_patronymic():
    return input('Введите отчество контакта: ')

def input_phone():
    return input('Введите телефон контакта: ')

def input_adress():
    return input('Введите адрес(город) контакта: ')
def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_adress()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'


def add_contact():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(create_contact())



def print_contact():
    pass
   
        

def search_contact():
    pass



def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '4':
        print(
            'Возможные варианты: \n'
            '1. Добавить контакт \n'
            '2. Вывести на экран \n'
            '3. Поиск контакта \n'
            '4. Вывод '
            )
        
        var = input('Выберите вариант действий: ')
        while var not in ('1', '2', '3', '4'):
            print('Некоректный ввод!')
            var = input('Выберите вариант действий: ')

        match var:
            case '1':
                add_contact()
            case '2':
                print_contact()
            case '3':
                search_contact()
            case '4':
                print('До cвидания')
                exit




    
if __name__ == '__main__':
    interface()