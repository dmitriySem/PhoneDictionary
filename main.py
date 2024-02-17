def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ').title()

def input_adress():
    return input('Введите адрес(город) контакта: ').title()
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
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        
        for number, letter in enumerate(file.read().rstrip().replace(':', '').split('\n\n'), 1):
            print(''.join('{} {}').format(number, letter))
        # print(file.read())
   
        

def search_contact():
    print(
            'Возможные варианты поиска: \n'
            '1. По Фамилии \n'
            '2. По имени \n'
            '3. По отчеству \n'
            '4. По телефону \n'
            '5. По адресу(город)'
            )
    var = input('Выберите вариант действий: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некоректный ввод!')
        var = input('Выберите вариант действий: ')
    i_var = int(var) - 1 

    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().replace(':', '').split('\n\n')

        for str_contact in contacts_list:
            list_contact = str_contact.split()
            # print([list_contact])
            if search in list_contact[i_var]:
                print(str_contact)



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
            '4. Выход '
            )
        print()
        
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
        print()




    
if __name__ == '__main__':
    interface()