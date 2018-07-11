#Для данных в строках PYTHON3
import xlrd

DATA = []
DATA1 = []
data = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
data11 = []
z = []
zero = []
#Прописать путь в Windows для файла с которого будет считываться информация
wb = xlrd.open_workbook('D:DataWork1.0.xlsx')
sheet = wb.sheet_by_index(0)

z.append(str(0))
zero = z*26280
            #кол-во строк/столбцов - sheet.nrows
k = 1       #с какого столбца начинать
def read_file(sheet):
    if sheet.ncols > 0:
        for col in range(k, sheet.ncols):
            data.append(str(sheet.col_values((col))[0]))
            data1.append(str(sheet.col_values((col))[1]))
            data2.append(str(sheet.col_values((col))[2]))
            data3.append(str(sheet.col_values((col))[3]))
            data4.append(str(sheet.col_values((col))[4]))
            data5.append(str(sheet.col_values((col))[5]))
            data6.append(str(sheet.col_values((col))[6]))
            data7.append(str(sheet.col_values((col))[7]))
            data8.append(str(sheet.col_values((col))[8]))
            data9.append(str(sheet.col_values((col))[9]))
            data10.append(str(sheet.col_values((col))[10]))
            data11.append(str(sheet.col_values((col))[11]))

read_file(sheet)

Jan = data*31
Feb = data1*28
Mar = data2*31
Apr = data3*30
May = data4*31
Jun = data5*30
Jul = data6*31
Aug = data7*31
Sep = data8*30
Oct = data9*31
Nov = data10*30
Dec = data11*31

DATA1 = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec
DATA = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec + zero
#Прописать путь в Windows для файла куда будут записываться данные
my_file = open('D:DATA3.2.txt', 'w')
my_file.write(str('\n'.join(DATA)))
my_file.close()

print('\n'.join(DATA))
print("Колличество данных: ", len(DATA1), '/ 8760')
print("Колличество данных: ", len(DATA), '/ 35040')
