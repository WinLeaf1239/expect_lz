import pandas as pd

class Obrabotka:
    def __init__(self,file_path):
        self.file = file_path
    
    def found(self):
        try:
            self.df = pd.read_csv(self.file, sep=',')

        except FileNotFoundError:
            print(f"Возникла следующая ошибка: No such file or directory: '{self.file}'")
     
        except pd.errors.EmptyDataError:
            print(f"Ошибка: Датафрейм {self.file} пуст.")

        else:

            try:
                self.df = pd.read_csv(self.file, sep=',')
                column = [ 'Участники гражданского оборота',   
                            'Тип операции',
                            'Сумма операции',
                            'Вид расчета',
                            'Место оплаты',
                            'Терминал оплаты',
                            'Дата оплаты',
                            'Время оплаты',
                            'Результат операции',
                            'Cash-back',
                            'Сумма cash-back']

                if list(self.df.columns) != column:
                    raise ValueError(f"Названия стобцов не совпадают.\nОжидаемые: {column}\nФактические: {list(self.df.columns)}")
            
                
                type = {'Участники гражданского оборота' : 'str',
                         'Тип операции' : 'str',
                         'Сумма операции' : 'float64',
                         'Вид расчета' : 'str',
                         'Место оплаты' : 'str',
                         'Терминал оплаты' : 'str',
                         'Дата оплаты' : 'str',
                         'Время оплаты' : 'str',
                         'Результат операции' : 'str',
                         'Cash-back' : 'str',
                         'Сумма cash-back' : 'float64'}
            
                for i,true_type in type.items():
                    our_type = str(self.df[i].dtypes)
                    if our_type != true_type:
                        raise TypeError(f"В столбце: '{i}' тип данных не соответствует оиждаемому\nОжидается: {true_type}, Фактически: {our_type}\n")


            
            except ValueError as e:
                print(f"Возникла ошибка: {e} ")

            except TypeError as e:
                print(f"Возникла ошибка: {e} ")
            
            else: 
                self.df = pd.read_csv(self.file, sep=',')
                print('В датафрейме ошибок не найдено')
        



def main():
    x = Obrabotka('var10.csv')
    x.found()
if __name__ == "__main__":
    main()


