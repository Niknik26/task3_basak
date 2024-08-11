Итоговое задание №3
Реализованны функции:
read_sales_data(file_path), которая принимает путь к файлу и возвращает список продаж. Продажи в свою очередь являются словарями с ключами product_name, quantity, price, date (название, количество, цена, дата).
total_sales_per_product(sales_data), которая принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта.
sales_over_time(sales_data), которая принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату.

Входные данные хранятся в файле: sale.txt 

В ходе анализа данных из файла расчитаны два значения:
1. Продукт, который принес наибольшую выручку.
2. День, в который была наибольшая сумма продаж.

Построины два графика:

1. График общей суммы продаж по каждому продукту.
2. График общей суммы продаж по дням.
