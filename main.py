import pandas as pd
from json import dump


def main():
    print("Выберите задачу для решения:")
    print("Если вы хотите запустить парсинг FASTA, введите F")
    print("Если вы хотите рассчитать GC-состав, введите G")
    print("Если вы хотите построить таблицу частот нуклеотидов, введите N")
    print("Если вы хотите обработать файл выравнивания, введите H")
    print("Для выхода введите Q")

    while True:
        choice = input("Ваш выбор: ").upper()

        if choice == 'F':
            print("Запуск парсинга FASTA...")
            result = clo()
            with open('sample2.json', 'w') as fp:
                dump(result, fp)
            print("Результат сохранен в sample1.json")
            break

        elif choice == 'G':
            print("Запуск расчёта GC-состава...")
            data = clo()
            matrix = mat(data)
            for item in matrix:
                print(f"Sequence ID: {item[0]}, GC-content: {item[1]}")
            break

        elif choice == 'N':
            print("Запуск построения таблицы частот нуклеотидов...")
            data = clo()
            m = mat(data)
            df = poe(m)
            itt(df)
            break

        elif choice == 'H':
            print("Запуск обработки файла выравнивания...")
            matrix1 = cvv()
            gvv(matrix1)
            break

        elif choice == 'Q':
            print("Выход из программы...")
            return

        else:
            print("Неверный ввод. Пожалуйста, выберите одну из предложенных опций.")


# Функция парсинга FASTA
def clo():
    ict = dict()
    with open(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\mature.txt', 'r') as f:
        for line in f:
            m = line.strip()
            if len(m) != 0 and m[0] == '>':
                m = m.split()
                key = m[0][1:]
                ict[key] = ""
            else:
                ict[key] += m
    return ict


# Функция расчета GC-состава
def mat(ict):
    matrix = []
    for key, value in ict.items():
        g = value.count('G')
        c = value.count('C')
        k = (g + c) / len(value)
        gc = round(k, 4)
        row = [key, gc, *list(value)]
        matrix.append(row)
    return matrix


# Функция создания DataFrame
def poe(matrix):
    df = pd.DataFrame(matrix)
    return df


# Функция расчета частот нуклеотидов
def itt(df):
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
    print("Частота A:", aaa)
    print("Частота T:", ttt)
    print("Частота C:", ccc)
    print("Частота G:", ggg)


# Функция обработки файла выравнивания
def cvv():
    Alignment_and_Query = []
    Line_number = 0
    matrix1 = []
    with open(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\CALM2P2_Callithrix_12.txt',
              'r') as file:
        sas = file.readlines()
        cleaned_file = [s.replace('\n', '') for s in sas]
        for line in sas:
            Line_number += 1
            if line.startswith("  Alignment:"):
                Alignment1 = Line_number + 1
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
        Alignment_and_Query.append(cleaned_file[Alignment1 - 1])
    return matrix1

# Функция сохранения результатов выравнивания
def gvv(matrix1):
    df1 = pd.DataFrame(matrix1)
    df1.to_csv(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\df1.csv', index=False)
    print("Результаты сохранены в df1.csv")
    print(df1)

if __name__ == "__main__":
    main()

