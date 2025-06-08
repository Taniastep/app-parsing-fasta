import pandas as pd
def clo():
    """
    Входные данные:None,
    выходные данные:словарь ict(ключ-значение),
    функция возращает значение словаря ict,
    функция открывает заданный файл и считывает каждую строку(парсит), если строка начинается с ">", то она является заголовком(ключом),
    остальное игнарируется и записывается в значение. При завершении выводится словарь ict"""

    ict = dict()
    with open(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\mature.txt','r') as f:
      for line in f:
         m = line.strip()
         if len(m) != 0 and m[0] == '>':
           m = m.split()
           key = m[0][1:]
           ict[key] = ""
         else:
           ict[key] += m

      for key, value in ict.items():
         print(key, '*', value)
    return ict

def mat(ict):
    """
    Входные данные: словарь ict,
    Выходные данные: matrix(list of lists)
    Функция возращает значение matrix
    Функция преобразует словарь в матрицу. Для каждой пары ключ-значение функция считает долю gc, которая огругляется до 4 знаков после запятой
    """

    matrix = []
    for key, value in ict.items():
        g = value.count('G')
        c = value.count('C')
        k = (g + c) / len(value)
        gc = round(k, 4)
        row = [key, gc, *list(value)]
        matrix.append(row)
    return matrix



def poe(matrix):
    """
    Входные данные: matrix(list of lists)
    Выходные данные: df (pd.Dataframe (таблица Pandas))
    Функция возрощает значениу   df(Dataframe)
    Из матрицы(matrix) создает dataframe(df), который состоит из таблицы , где элементы каждого внутреннего списка соответствуют столбцам
    """
    df = pd.DataFrame(matrix)
    return df




def itt(df):
    """
   Входные данные: df (pd.Dataframe (таблица Pandas)
    Выходные данные: None
    Функция частоту встречаемости нуклеотидов 'A', 'T', 'C', 'G' в каждом столбце таблицы, в случае где пропусков >50%, столбец пропускается
    """
    aaa = []
    ttt = []
    ccc = []
    ggg = []
    for i in range(2, len(df.columns)):
        aa, tt, gg, cc, gap = 0, 0, 0, 0, 0
        st = list(df.iloc[:, i])
        aa += st.count('A')
        tt += st.count('T')
        cc += st.count('C')
        gg += st.count('G')
        gap += st.count('-')
        if gap / df.shape[0] < 0.5:
            aaa.append(aa / df.shape[0])
            ttt.append(tt / df.shape[0])
            ccc.append(cc / df.shape[0])
            ggg.append(gg / df.shape[0])
    print(aaa)
    print(ttt)
    print(ccc)
    print(ggg)



from json import *
with open('sample1.json', 'w') as fp:
    dump(clo(), fp)

gtre = itt(poe(mat(clo())))
def cvv():
    """
    Входные данные: None
    Выходные данные: matrix1(list of lists)
    Функция возрощает значение matrix1
    Функция считывает файл с положением о фрагментах последовательности, есть три значения(последовательность, начало и конец последовательности),
    Просчитав файл построчно, определяет позицию ключевых секций ("Alignment:", "Query:"),
    Поочередно обрабатывает строки файла, выделяя нужные фрагменты и записывая их в итоговую матрицу(matrix1).
    """
    Alignment_and_Query = []
    Line_number = 0
    matrix1 = []
    row = []
    file = open(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\CALM2P2_Callithrix_12.txt', 'r')
    sas = file.readlines()
    cleaned_file = [s.replace('\n', '') for s in sas]
    for line in sas:
        Line_number += 1
        if line.startswith("  Alignment:"):
            Alignment1 = Line_number + 1
            Alignment = Line_number
        if line.startswith("Query:"):
            Query = Line_number - 1
    s = cleaned_file[Alignment1 - 4]
    d = s.split()
    end = int(d[5])
    for i in range(0, len(sas) - Alignment1, 5):
        split_Alignment = cleaned_file[Alignment1 + i].split()
        row = []
        row.append(split_Alignment[2])
        row.append(split_Alignment[1])
        row.append(split_Alignment[3])
        matrix1.append(row)
        a = int(split_Alignment[3])
        row = []
        split_Alignment = cleaned_file[Alignment1 + i + 2].split()
        row.append(split_Alignment[2])
        row.append(split_Alignment[1])
        row.append(split_Alignment[3])
        matrix1.append(row)
        if a == end:
            break
    Alignment_and_Query.append(cleaned_file[Query])
    Alignment_and_Query.append(cleaned_file[Alignment])
    print(Alignment_and_Query)
    return matrix1

def gvv(matrix1):
    """
    Входные данные: matrix1(list of lists)
    Выходные данные: None
    Функция делает из полученного аргумента(matrix1) dataframe(df1), далее этот dataframe(df1) сохраняется в формат CSV
    """
    df1 = pd.DataFrame(matrix1)
    df1.to_csv(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\df1_csv', index='False')
    print(df1)

ghhh = gvv(cvv())
