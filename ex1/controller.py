
import model
import vive


def main_menu():
    while True:
        print('1. Добавить контакт ')
        print('2. Удалить контакт ')
        print('3. Сохранить в файл ')
        print('4. Изменить контакт ')
        print('5. Поиск контакта ')
        print('0. Выйти')
        choise = int(input('Выбрать дествие: '))
        match(choise):
            case 1:
                add_contact()
                print('\n Контакт добавлен \n')
            case 2:
                delete_contact()
                print('\n Контакт удален \n')
            case 3:
                save_contact()
                print('\n Контакт сохранен \n')
            case 4:
                chang_contact()
                print('\n Контакт изменен \n')
            case 5:
                search_contact()
                print('\n Результат поиска: \n')

            case 0:
                break


def start():
    open_file()
    vive.openPhonebook()
    print()
    main_menu()



def open_file():
    with open(model.path, 'r', encoding="UTF8") as data:
        contact_list = data.read().split('\n')
        model.phonebook = contact_list
        

def save_contact():
     with open(model.path, 'w', encoding="UTF8") as data:
        data.write(('\n'.join(model.phonebook)))

    
def add_contact():
    name =  input('Введите имя: ')
    subname =  input('Введите отчество: ')
    last_name =  input('Введите фамилмия: ')
    phone =  input('Введите телефун: ')
    contact = f'{name}; {subname}; {last_name}; {phone};\n'
    model.phonebook.append(contact)
    vive.openPhonebook()

def delete_contact():
    choise = int(input('выбери контакт для удаления: '))
    model.phonebook.pop(choise)
    vive.openPhonebook()

def chang_contact():
    choise = int(input('Выбери контакт для изменения: '))
    choise2 = int(input('Выбери что будем менять: 0 - имя, 1 - отчество, 2 - фамилия, 3 - телефон: '))
    contact = model.phonebook.pop(choise).split(';')
    contact[choise2] = input('Введите новый элемент')
    model.phonebook.insert(choise, ';'.join(contact))
    vive.openPhonebook()

# def search_contact():
#     choise = input('Введиет имя или телефон контакта: ')
#     for i in range(len(model.phonebook)):
#         if i == choise:
#             return i
#         else:
#             print('Контакта нет')
#             exit()
#     print(i)
#     vive.openPhonebook()   