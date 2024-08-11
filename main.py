# Принимает путь к файлу и возвращает список продаж.
# Продажи являются словарями с ключами product_name, quantity, price, date (название, количество, цена, дата).
def read_sales_data(file_path):
    file = file_path #путь к файлу
    keys = ['product_name', 'quantity', 'price', 'date'] # список ключей
    sales = [] # список для хранения словарей
    with open(file, 'r') as file: # открытие файла
        for line in file: # построчное чтение
            lines = line.strip().split(', ') # удаление символов новой строки и пробелов, разделение строки через ', ' на список
            sale = dict(zip(keys, lines)) # создание словаря для каждого элемента из списка ключей и списка значений
            sales.append(sale) # добавление словарей в список

    return sales

# функция принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта.
def total_sales_per_product(sales_data):
    sales = sales_data 
    result = {}   
    for item in sales: 
        product_name = item['product_name']  
        quantity = int(item['quantity'])  # Преобразуем значение в целое число, для выполнения мат. операций
        # если значение для ключа 'product_name' уже есть в словаре result, то суммируем количество, иначе копируем из sales в result
        if product_name in result:
            result[product_name] += quantity
        else:
            result[product_name] = quantity
    return result

# функция принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату.
def sales_over_time(sales_data):  
    sales = sales_data
    result = {}
    for item in sales:
        date = item['date']
        quantity = int(item['quantity'])
        # если значение ключа 'date' уже есть в словаре result, то суммируем количество, иначе в result создается новая запись из sales
        if date in result:
            result[date] += quantity
        else:
            result[date] = quantity
    return result

# определить, какой продукт принес наибольшую выручку.
max_tspp = total_sales_per_product(read_sales_data('sales.txt'))  # обращение к функции, для получения словаря('название продукта':сумма продаж) 
max_value = 0
max_value1 = 0
max_quant = 0
max_day = 0
for i in max_tspp: 
    if max_tspp[i] > max_value:  # если текущее значение больше максимального
        max_value = max_tspp[i]  # перезаписать максимальное текущим значением
        max_quant = i  # получаем название продукта(ключ) текущего значения
print(f'Продукт, который принес наибольшую выручку: {max_quant}.')

# определить, в какой день была наибольшая сумма продаж.
max_sot = sales_over_time(read_sales_data('sales.txt'))  # обращение к функции, для получения словаря('дата':сумма продаж) 
for j in max_sot:
    if max_sot[j] > max_value1: # если текущее значение больше максимального
        max_value1 = max_sot[j] # перезаписать максимальное текущим значением
        max_day = j # получаем дату (ключ) текущего значения
print(f'День, в который была наибольшая сумма продаж: {max_day}.')

import matplotlib.pyplot as plt # импорт библиотеки для построения графиков

# график по продуктам
quant = list(max_tspp.values()) #список значений: количество продаж
name = list(max_tspp.keys()) # список ключей: название продукта 
plt.plot(name, quant) # координаты точек для графика
plt.xlabel('Name')  # название оси X
plt.ylabel('Quantity') # название оси Y
plt.title('total_sales_per_product') # название графика
plt.show() # Отображение графика на экране

#график по дням
dates = list(max_sot.keys()) # список ключей: день продажи
sales_val = list(max_sot.values()) #список значений: количество продаж
plt.plot(dates, sales_val) # координаты точек для графика
plt.xlabel('Date')  # название оси X
plt.xticks(rotation=45) # поворот подписей оси X, что бы не накладывались подписи дург на друга
plt.tight_layout()  # автоматическое расположение подписей
plt.ylabel('Quantity') # название оси Y
plt.title('sales_over_time') # название графика
plt.show() # Отображение графика на экране
