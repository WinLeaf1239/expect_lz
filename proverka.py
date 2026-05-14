import pandas as pd
import os

class Obrabotka:
    def __init__(self,file_path):
        self.file = file_path
    
    def found(self):
        try:
            pd.read_csv(self.file, encoding="utf-8")
            print('Все хорошо')
        except FileNotFoundError:
            print(f'Возникла следующая ошибка: [Errno2] No such file or directory: {self.file}')

        

        


x = Obrabotka('var10.csv')
x.found()
