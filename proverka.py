import pandas as pd
import os

class Obrabotka:
    def __init__(self,file_path):
        self.file = file_path
    
    def found(self):
        try:
            df = pd.read_csv(self.file, encoding="utf-8")
            
            # Дополнительная проверка: если в файле есть только строка заголовков, 
            if df.empty:
                print(f"Файл '{self.file}' содержит только заголовки, но в нем нет данных.")
                return False
                
            print('Все хорошо, файл найден и содержит данные.')

            
        except FileNotFoundError:
            print(f"Возникла следующая ошибка: [Errno 2] No such file or directory: '{self.file}'")

            
        except pd.errors.EmptyDataError: #умный модуль, который сам проверяет
            print(f"Ошибка: Файл '{self.file}' абсолютно пустой.")

        
            

        
x = Obrabotka('var10.csv')
x.found()




#except pd.errors.EmptyDataError: Этот блок сработает автоматически, если в файле физически нет ни одного символа или там записаны только невидимые пробелы/переносы строк.if df.empty: Эта проверка нужна на случай, если файл не пустой (в нем есть одна строка с названиями колонок), но самих строк с данными внутри не