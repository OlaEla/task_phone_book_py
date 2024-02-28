# ЗАДАЧА:

# Создать телефонный справочник в формате .txt. Фамилия, имя, отчество, номер
# телефона, комментарий - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Создавать новый контакт
# 5. Изменение контакта
# 6. Удаление контакта
# 7. Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Функция для чтения контактов из файла
def read_contacts():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]  # Удаляем символ новой строки и пробельные символы

def write_contacts(contacts):
  with open('contacts.txt', 'w', encoding='utf-8') as file:
    for contact in contacts:
      file.write(f"{contact}\n")

# Функция для отображения всех контактов
def show_contacts():
    contacts = read_contacts()
    for contact in contacts:
        print(contact.strip())

# Функция для создания нового контакта
def create_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    
    new_contact = f"{name}, {surname}, {phone}, {comment}\n"
    with open('contacts.txt', 'a', encoding='utf-8') as file:  # Открываем файл для добавления нового контакта в конец
        file.write(new_contact)
    print("Контакт успешно добавлен.")


# Функция для поиска контакта
def search_contacts():
    query = input("Введите имя или фамилию для поиска: ").strip().lower()  # Обрабатываем регистр и удаляем пробельные символы
    contacts = read_contacts()
    found = False
    for contact in contacts:
        if query in contact.lower():  # Приводим контакт к нижнему регистру для сравнения
            print(contact)
            found = True
    if not found:
        print("Контакт не найден.")


def edit_contact():
    query = input("Введите имя и фамилию контакта для изменения: ")

    # Разделяем введенные данные на имя и фамилию
    name, *surname_parts = query.split()  # Разделяем по пробелу

    # Проверяем, что было введено как минимум два слова (имя и фамилия)
    if len(surname_parts) == 0:
        print("Ошибка: введите и имя, и фамилию контакта.")
        return

    # Склеиваем оставшиеся части в фамилию
    surname = ' '.join(surname_parts)

    # Преобразуем имя и фамилию к нижнему регистру для сравнения
    name = name.lower()
    surname = surname.lower()
    # name = parts[1].lower()
    # surname = parts[0].lower()

    contacts = read_contacts()
    edited = False
    for i, contact in enumerate(contacts):

        # Разделяем контакт на части по запятой и удаляем лишние пробелы
        parts = [part.strip() for part in contact.split(',')]
        # Проверяем, если имя и фамилия совпадают (учитывая регистр)
        if len(parts) >= 2 and parts[0].lower() == name and parts[1].lower() == surname:
            new_phone = input("Введите новый номер телефона: ")
            new_comment = input("Введите новый комментарий: ")
            contacts[i] = f"{name.title()}, {surname.title()}, {new_phone}, {new_comment}"
            edited = True
            break  # Прекращаем цикл после изменения первого найденного контакта
    if edited:
        write_contacts(contacts)
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")
        
# Функция для удаления контакта
def delete_contact():
    full_name = input("Введите имя и фамилию контакта для удаления (через пробел): ")
    first_name, last_name = full_name.split(maxsplit=1)  # Разделяем ввод на имя и фамилию

    contacts = read_contacts()
    deleted = False
    for contact in contacts[:]:  # Создаем копию списка контактов для безопасного удаления
        if first_name.lower() in contact.lower() and last_name.lower() in contact.lower():
            # Проверяем, содержится ли имя и фамилия в контакте (регистронезависимо)
            contacts.remove(contact)
            deleted = True

    if deleted:
        write_contacts(contacts)
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")
     

# Функция для копирования контакта из одного файла в другой
import os
def copy_contact():
    line_number = int(input("Введите номер строки для копирования: "))
    contacts = read_contacts()
    if 1 <= line_number <= len(contacts):
        with open('new_contacts.txt', 'a', encoding='utf-8') as target_file:
            if os.path.isfile('new_contacts.txt') and os.stat('new_contacts.txt').st_size != 0:
                # Проверяем, существует ли файл и не является ли он пустым
                target_file.write('\n')  # Добавляем пустую строку перед добавлением строки
            target_file.write(contacts[line_number - 1].rstrip())  # Записываем строку без пробельных символов справа
        print("Строка успешно скопирована.")
    else:
        print("Неверный номер строки. Попробуйте снова.")


# Основная функция
def main():
    while True:
        print("\nМеню:")
        print("1. Показать все контакты")
        print("2. Создать новый контакт")
        print("3. Поиск по контактам")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Копировать контакт")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_contacts()
        elif choice == '2':
            create_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            copy_contact()
        elif choice == '7':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

# Запуск основной функции
if __name__ == "__main__":
    main()




