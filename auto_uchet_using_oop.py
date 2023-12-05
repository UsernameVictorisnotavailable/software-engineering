class Auto_uchet:
    def __init__(self, file_name = 'text3.txt'):
        self.file_name = file_name
        file = open(self.file_name, encoding = 'utf-8')
        self.dano = file.readlines()
        file.close()
        car_body = ['Тип кузова', 'Седан', 'Кроссовер', 'Купе', 'Лимузин', 'Пикап', 'Внедорожник']
        trunk = ['Багажник', 'Спереди', 'Сзади', 'Спереди и сзади', 'Отсутствует']
        self.parameters = ['Марка', 'Модель', 'Государственный номер', car_body, 'Цвет', 'Число мест', trunk]

    def input_range(self, a, b, c = 0):
        while True:
            x = c if c != 0 else input()
            if str(x).isdigit():
                if a <= int(x) <= b:
                    return int(x)
                else:
                    print('Введите число в корректном диапазоне')
            else:
                print('Требуется ввести число')

    def count_cars(self):
        if self.dano != []:
            for i in self.dano[::-1]:
                if i[0].isdigit():
                    self.num_of_cars = int(i.split('. ')[0])
                    break
        else:
            self.num_of_cars = 0
        return self.num_of_cars
            
    def add_car(self, mas = []):
        if mas != []:
            for i in range(len(mas)):
                if mas[i] == '':
                    raise ValueError('--Значение параметра не может быть пустой строкой--')
                else:
                    e = self.parameters[i]+': '+mas[i]+'\n' if type(self.parameters[i]) is str else self.parameters[i][0]+': '+mas[i]+'\n'
                    self.dano.append(e)
            return self.dano
        else:
            file = open(self.file_name, 'a', encoding = 'utf-8')
            print('Добавление машины в базу')
            for i in self.parameters:
                if type(i) is list:
                    print(i[0]+': ')
                    for a in range(1,len(i)):
                        print(str(a)+'. '+i[a])
                    value = i[0] + ': ' + i[int(self.input_range(1, len(i)))]
                else:
                    print(i + ': ')
                    enter = input().lower() if i == 'Цвет' else input()
                    value = str(int(self.count_cars())+1) + '. '+ i + ': ' + enter if i == 'Марка' else i + ': ' + enter
                file.write(value+'\n')
                self.dano.append(value+'\n')
            self.num_of_cars += 1
            file.close()
            print('Машина успешно добавлена')

    def show_car(self):
        cars = []
        for i in range(len(self.dano)):
            s = self.dano
            if s[i][0].isdigit():
                a = s[i].split('. ')[0]+'. '+s[i].split(': ')[1][:-1]+' '+s[i+1].split(': ')[1][:-1]+' '+s[i+2].split(': ')[1][:-1]
                print(a)
                cars.append(a)
        return cars

    def car_params(self, out = False, ind = ''):
        if ind != '':
            return self.dano[7*(ind-1)]
        else:
            if not out:
                print('Укажите номер машины')
            self.show_car()
            enter = self.input_range(1, self.count_cars())
            count = 1
            for i in range(len(self.dano)):
                if self.dano[i].split('. ')[0] == str(enter):
                    self.car_number = i
                    print(str(count)+'. '+self.dano[i].split('. ')[1][:-1])
                    for j in range(i+1, len(self.dano)):
                        if not self.dano[j][0].isdigit():
                            count+=1
                            print(str(count)+'. '+self.dano[j][:-1])
                        else:
                            break
                    break
                
    def change_par(self, enter=None, value=''):
        if enter != None and value != '':
            self.dano[enter] = self.dano[enter].split(':')[0] + ': ' + value + '\n'
            return self.dano
        else:
            print('Укажите номер машины, параметр которой вы хотите изменить')
            self.car_params(out = True)
            print('Укажите номер параметра, который вы хоитите изменить')
            enter = int(self.input_range(1,len(self.parameters)))-1
            chosen_par = self.dano[self.car_number + enter].split(':')[0]
            print(chosen_par.split('. ')[-1])
            if type(self.parameters[enter]) is list:
                for i in range(1,len(self.parameters[enter])):
                    print(str(i)+'. '+self.parameters[enter][i])
                new_value = self.parameters[enter][self.input_range(1,len(self.parameters[enter])-1)]
            else:
                new_value = input().lower() if self.parameters[enter] == 'Цвет' else input()
            self.dano[enter+self.car_number] = chosen_par + ': ' + new_value + '\n'
            file = open(self.file_name, 'w', encoding = 'utf-8')
            file.writelines(self.dano)
            file.close()
            print('Параметр успешно изменён')

    def find_car(self, par = ''):
        if par != '':
            count = 0
            for i in self.dano:
                if par+'\n' == i.split(': ')[1]:
                    count += 1
        else:
            print('По какому параметру нужно произвести поиск?')
            for i in range(len(self.parameters)):
                print(str(i+1)+'. '+self.parameters[i]) if type(self.parameters[i]) is str else print(str(i+1)+'. '+self.parameters[i][0])
            enter = int(self.input_range(1,len(self.parameters)))-1
            print('Введите значение данного параметра')
            if type(self.parameters[enter]) is list:
                for i in range(1,len(self.parameters[enter])):
                    print(str(i)+'. '+self.parameters[enter][i])
                value = self.parameters[enter][0] + ': ' + self.parameters[enter][self.input_range(1,len(self.parameters[enter])-1)]
            else:
                value = self.parameters[enter] + ': ' + input().lower() if self.parameters[enter] == 'Цвет' else self.parameters[enter] + ': ' + input()
            count = 0
            for i in range(len(self.dano)):
                if value == self.dano[i].split('. ')[-1][:-1]:
                    count += 1
                    for j in range(i,-1,-1):
                        if self.dano[j][0].isdigit():
                            print(str(count)+'. '+self.dano[j][:-1].split('. ')[-1])
                            while j+1<len(self.dano) and not self.dano[j+1][0].isdigit():
                                print(self.dano[j+1][:-1])
                                j+=1
                            break
            print('Машин с указанным параметром:', count)
        return count

    def delete_car(self):
        print('Укажите номер машины, которую хотите удалить')
        self.show_car()
        enter = self.input_range(1,self.count_cars())

        #удаляем машину
        for i in range(len(self.dano)):
            if self.dano[i].split('. ')[0] == str(enter):
                self.dano.pop(i)
                while i<len(self.dano) and not self.dano[i][0].isdigit():
                    self.dano.pop(i)

                #правим номера
                for j in range(i,len(self.dano)):
                    if self.dano[j][0].isdigit():
                        self.dano[j] = str(int(self.dano[j].split('. ')[0])-1)+'. '+self.dano[j].split('. ')[1]
                break
        file = open(self.file_name, 'w', encoding = 'utf-8')
        file.writelines(self.dano)
        file.close()

    def add_par(self):
        print('Введите новый праметр')
        while True:
            enter = input()
            if enter == '' or enter.count(' ') == len(enter):
                print('Параметр не может быть пустой строкой')
            else:
                for i in self.parameters:
                    if (type(i) is list and i[0] == enter) or (type(i) is str and i == enter):
                        print('Введенный параметр уже существует')
                        break
                else:
                    self.parameters.append(enter)
                    break
        #обновляем файл
        new_dano = []
        for i in range(len(self.dano)):
            if type(self.parameters[-2]) is list:
                if self.dano[i].split(':')[0] == self.parameters[-2][0]:
                    new_dano.append(self.dano[i])
                    new_dano.append((self.parameters[-1]+': '+'\n'))
                else:
                    new_dano.append(self.dano[i])
            else:
                if self.dano[i].split(':')[0] == self.parameters[-2]:
                    new_dano.append(self.dano[i])
                    new_dano.append((self.parameters[-1]+': '+'\n'))
                else:
                    new_dano.append(self.dano[i])
        self.dano = new_dano
        file = open(self.file_name, 'w', encoding='utf-8')
        file.writelines(self.dano)
        file.close()
        print(f'Добавлен новый параметр {enter}')
        print(self.parameters)

    def delete_par(self):
        print('Введите номер параметра который вы хотите удалить')
        for i in range(len(self.parameters)):
            print(f'{str(i+1)}. {self.parameters[i]}') if type(self.parameters[i]) is str else print(f'{str(i+1)}. {self.parameters[i][0]}')
        enter = self.input_range(1,len(self.parameters))
        print('Парамтетр удален')

        #удаление из всего документа
        i = 0
        while i != len(self.dano):
            if self.dano[i].split(':')[0] == self.parameters[enter-1]:
                self.dano.pop(i)
            else:
                i += 1

        #удаляем из списка параметров
        self.parameters.pop(enter-1)
        file = open(self.file_name, 'w', encoding='utf-8')
        file.writelines(self.dano)
        file.close()




a = Auto_uchet()
if __name__ == '__main__':
    while True:
        print('Что вы хотите сделать?')
        print('1. Найти машину\n2. Добавить машину\n3. Изменить параметр машины\n4. Вывести список автомобилей\n5. Вывести параметры конкретной машины\n6. Удалить авто по номеру\n7. Добавить новый параметр\n8.Удалить параметр')
        choice = a.input_range(1,8)
        if choice == 1:
            a.find_car()
        elif choice == 2:
            a.add_car()
        elif choice == 3:
            a.change_par()
        elif choice == 4:
            a.show_car()
        elif choice == 5:
            a.car_params()
        elif choice == 6:
            a.delete_car()
        elif choice == 7:
            a.add_par()
        elif choice == 8:
            a.delete_par()
