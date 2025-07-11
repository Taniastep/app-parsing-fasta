# app-parsing-fasta
## Описание программного продукта

### 1. Назначение
Программа предназначена для комплексного анализа биологических последовательностей, включая обработку FASTA файлов и анализ множественных выравниваний. Она решает следующие задачи:

- Парсинг и обработка FASTA файлов.
- Вычисление процентного содержания GC-нуклеотидов.
- Анализ частот нуклеотидов (A, T, C, G).
- Создание матриц данных для последующего анализа.
- Преобразование данных в удобочитаемый формат.
- Экспорт результатов в различные форматы (JSON, CSV).

### 2. Функциональные возможности

#### 2.1. Основные функции

- **clo()**: Парсит FASTA файл, формирует словарь последовательностей, сохраняет результат в JSON и выводит пары ключ-значение.
- **mat()**: Рассчитывает процентное содержание GC-нуклеотидов в последовательностях, создавая матрицу данных с округлёнными значениями.
- **poe()**: Преобразует матрицу в DataFrame библиотеки Pandas для удобной последующей обработки.
- **itt()**: Анализирует частоту нуклеотидов (A, T, C, G), игнорируя пропущенные позиции ('-'), выводя проценты по каждому типу нуклеотидов.
- **cvv()**: Обрабатывает файлы о парном локальном выравниваниии, формируя матрицу данных на основе полей "Alignment" и "Query".
- **gvv()**: Преобразует матрицу в DataFrame и экспортирует её в CSV файл.


### 3. Технические характеристики

#### 3.1. Входные данные
- **FASTA файлы**: Последовательности в формате FASTA, каждая последовательность начинается с символа ">".
- **Файлы множественного выравнивания**: Файлы с результатами выравнивания последовательностей.

#### 3.2. Выходные данные
- **JSON файлы**: Словарь последовательностей в формате JSON.
- **Матрицы данных**: Массивы данных с результатом анализа.
- **DataFrames**: Таблицы Pandas для удобного отображения и обработки данных.
- **CSV файлы**: Итоговые таблицы в формате CSV.
- **Частоты нуклеотидов**: Распределение нуклеотидов (A, T, C, G) в процентах.

#### 3.3. Обработка данных
- Подсчёт GC-содержания (%GC).
- Анализ распределения нуклеотидов (частоты A, T, C, G).
- Игнорирование пропусков (символ "-").
- Группировка и агрегация данных для статистической оценки.

### 4. Пример использования

#### 4.1. Исходные данные FASTA файла и множественного выравнивания
```
>seq1
ATGCATGC
>seq2
ATGCATGC

Alignment:
Query: Seq1 Callithrix jacchus (marmoset)
1   QKTD--LLLLL----GGHHHTAAAAAAAEEEEEFFFFFFFFFFFFFF
2   RKLQDLLLLL------GGHHHTAAAAAAAEEEEEFFFFFFFFFFFFF
3   TKTDLLLLLLLL---GGHHHTAAAAAAAEEEEEFFFFFFFFFFFF--

Alignment:
Query: Seq2 Homo sapiens (human)
1   AGCCCGGGG-----LLLLLLLLL--------AAAAAAAAAAAAABBBBCCCCDDDDEEEEEEEFFFGGGGHIIIJJJJKKKLLLMMMNOOOPPPQQQRRRSSSTTTUUUWWWXXYYYZZZ
2   ----CCCCCCCCGGGGGGGGGGGGGGGGGGGGAAAAAAAAAAAAAAAAAAAAAAABBBCDDDEEFFFGGGHHHIIJJJJKKKLLLLMMMNNOOOOPPPQQQRRRSSSTTTUUUWWWXXYYYZZZ
3   AGCCC---------GGGGGGGGGGGGGGGGGGGGAAAAAAAAAAAAAAAAAAAAAAABBBCDDDEEFFFGGGHHHIIJJJJKKKLLLLMMMNNOOOOPPPQQQRRRSSSTTTUUUWWWXXYYYZZZ
```

#### 4.2. Результаты работы
```python
# clo()
{'seq1': 'ATGCATGC', 'seq2': 'ATGCATGC'}

# mat()
[['seq1', 0.5000, 'A', 'T', 'G', 'C', 'A', 'T', 'G', 'C'],
 ['seq2', 0.5000, 'A', 'T', 'G', 'C', 'A', 'T', 'G', 'C']]

# poe()
   0    1  2  3  4  5  6  7  8
0 seq1 0.5  A  T  G  C  A  T  G  C
1 seq2 0.5  A  T  G  C  A  T  G  C

# itt()
aaa: [0.25, 0.25]
ttt: [0.25, 0.25]
ccc: [0.25, 0.25]
ggg: [0.25, 0.25]

# cvv():
[['MGVKALG', '1', '7'], 
 ['LKASDFG', '2', '14'], 
 ['PQRSTUV', '3', '21'], 
 ['ABCDEFG', '4', '28'], 
 ['HIJKLMN', '5', '35']]

# gvv():
 0,1,2
 MGVKALG,1,7
 LKASDFG,2,14
 PQRSTUV,3,21
 ABCDEFG,4,28
 HIJKLMN,5,35
```

### 5. Особенности реализации

#### 5.1. Используемые технологии
- Язык программирования: Python.
- Библиотеки: Pandas для работы с таблицами, NumPy для численных операций.
- Форматы данных: JSON, CSV.

### 6. Ограничения
-На вход берет только определенный формат FASTA(заголовок >, первое значение после заголовка это id) 
-Зависящий от конкретного пути к файлам (необходимо указывать полный путь).
-Ограничения по объему обрабатываемых данных.
-Требуется правильный формат последовательностей в FASTA файлах.

### 7. Рекомендации по использованию
- Обязательно проверять правильность формата входных данных.
- Обращать внимание на ограничение размера файлов.
- Соблюдать правильную структуру заголовков FASTA файлов.

### 8. Заключение
Представленный программный продукт служит мощным инструментом для глубокого анализа биологических последовательностей и предлагает пользователям следующий функционал:

- **Парсинг FASTA файлов**: Автоматическая обработка и хранение последовательностей в формате словарей.
- **Вычисление процентного содержания GC**: Определение доли гуанинов и цитозинов в последовательности.
- **Анализ частот нуклеотидов**: Оценка распространенности каждого нуклеотида (A, T, C, G) среди всей выборки.
- **Структурирование данных**: Представление полученных данных в удобных формах (таблица, матрица).
- **Парсинг отчетов о локальном выравнивание**: Запись трех значений(Последовательность, начало и конец последовательности) в таблицу
