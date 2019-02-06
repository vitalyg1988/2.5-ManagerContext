from time import time

class MyOpen:
    def __init__(self, file_path, mode, encode):
        self.file_path = file_path
        self.mode = mode
        self.encode = encode

    def __enter__(self):
        self.start_programm = time()
        print(f'Время запуска кода: {self.start_programm}')
        self.file = open(self.file_path, self.mode, encoding=self.encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_programm = time()
        print(f'Время окончания работы кода: {self.end_programm}')
        print(f'Время, затраченное на выполнение кода: {self.end_programm - self.start_programm}')

if __name__ == '__main__':
    with MyOpen('test.txt', 'r', 'UTF-8') as file:
        for line in file:
            student = line.strip()
            ratings = file.readline().strip()
            print(f'Оценки студента {student} следующие: {ratings}')
            int_ratings = [int(rate) for rate in ratings.split()]
            print(f'Средний балл {student} по успеваемости равен {(sum(int_ratings)/len(int_ratings)).__round__(2)}')