import pandas as pd
def cvv():
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
    df1 = pd.DataFrame(matrix1)
    df1.to_csv(r'C:\Users\Tania\AppData\Roaming\JetBrains\PyCharmCE2023.3\scratches\df1_csv', index='False')
    print(df1)

ghhh = gvv(cvv())
