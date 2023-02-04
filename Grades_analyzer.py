import csv
# For the average
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='' ) as fout:
        writer = csv.writer(fout)
        with open(input_file_name) as fin:
            reader = csv.reader(fin)
            list_name_averages = []
            for row in reader:
                name = row[0]+','
                numbers= []
                for grade in row[1:]:
                    numbers.append(float(grade))
                    average = mean(numbers)
                    str_name_average = name+str(average)
                    name_average = str_name_average.split()
                list_name_averages = list_name_averages + name_average
            fout.write('\n'.join(list_name_averages))
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='' ) as fout:
        writer = csv.writer(fout)
        with open(input_file_name) as fin:
            reader = csv.reader(fin)
            list_name_averages = []
            odict = OrderedDict()
            for row in reader:
                name = row[0]+','
                numbers= []
                for grade in row[1:]:
                    numbers.append(float(grade))
                    average = mean(numbers)
                    str_name_average = name+str(average)
                    name_average = str_name_average.split()
                    odict[name] = float(average)
                list_name_averages = list_name_averages + name_average
            odict_list_tuple = list(odict.items())
            for i in range(0, len(odict_list_tuple)-1):
                for j in range(i+1, len(odict_list_tuple)):
                    if odict_list_tuple[i][1] > odict_list_tuple[j][1]:                    
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
                    elif odict_list_tuple[i][1] == odict_list_tuple[j][1] and odict_list_tuple[i][0] > odict_list_tuple[j][0]:
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
            list_javab = []
            for item in dict(odict_list_tuple):
                javab = item+str(dict(odict_list_tuple)[item])
                list_javab = list_javab + javab.split()
            fout.write('\n'.join(list_javab))
def calculate_three_best(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='' ) as fout:
        writer = csv.writer(fout)
        with open(input_file_name) as fin:
            reader = csv.reader(fin)
            list_name_averages = []
            odict = OrderedDict()
            for row in reader:
                name = row[0]+','
                numbers= []
                for grade in row[1:]:
                    numbers.append(float(grade))
                    average = mean(numbers)
                    str_name_average = name+str(average)
                    name_average = str_name_average.split()
                    odict[name] = float(average)
                list_name_averages = list_name_averages + name_average
            odict_list_tuple = list(odict.items())
            for i in range(0, len(odict_list_tuple)-1):
                for j in range(i+1, len(odict_list_tuple)):
                    if odict_list_tuple[i][1] < odict_list_tuple[j][1]:                    
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
                    elif odict_list_tuple[i][1] == odict_list_tuple[j][1] and odict_list_tuple[i][0] > odict_list_tuple[j][0]:
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
            list_javab = []
            for item in dict(odict_list_tuple):
                javab = item+str(dict(odict_list_tuple)[item])
                list_javab = list_javab + javab.split()
            fout.write('\n'.join(list_javab[:3]))
def calculate_three_worst(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='' ) as fout:
        writer = csv.writer(fout)
        with open(input_file_name) as fin:
            reader = csv.reader(fin)
            list_name_averages = []
            odict = OrderedDict()
            for row in reader:
                name = row[0]+','
                numbers= []
                for grade in row[1:]:
                    numbers.append(float(grade))
                    average = mean(numbers)
                    str_name_average = name+str(average)
                    name_average = str_name_average.split()
                    odict[name] = float(average)
                list_name_averages = list_name_averages + name_average
            odict_list_tuple = list(odict.items())
            for i in range(0, len(odict_list_tuple)-1):
                for j in range(i+1, len(odict_list_tuple)):
                    if odict_list_tuple[i][1] > odict_list_tuple[j][1]:                    
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
                    elif odict_list_tuple[i][1] == odict_list_tuple[j][1] and odict_list_tuple[i][0] > odict_list_tuple[j][0]:
                        odict_list_tuple[i], odict_list_tuple[j] = odict_list_tuple[j], odict_list_tuple[i]
            list_javab = []
            for item in dict(odict_list_tuple):
                javab = str(dict(odict_list_tuple)[item])
                list_javab = list_javab + javab.split()
            fout.write('\n'.join(list_javab[:3]))
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(output_file_name, 'w', newline='' ) as fout:
        writer = csv.writer(fout)
        with open(input_file_name) as fin:
            reader = csv.reader(fin)
            list_averages = []
            for row in reader:
                numbers= []
                for grade in row[1:]:
                    numbers.append(float(grade))
                    average = str(mean(numbers)).split()
                list_averages = list_averages + average
            list_avg = []
            for averages in list_averages:
                list_avg.append(float(averages))
                avg_avg = mean(list_avg)
            fout.write(str(avg_avg))