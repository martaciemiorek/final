import csv

def create_force_list(sample):
    force_column = []
    with open(f'{sample}.TRA', 'r') as force:
        reader = csv.reader(force, delimiter=';')
        start_line = ['    Siła standardowa', '   Droga standardowa', '        Czas badania', '                Czas', 'Odległość pomiędzy u']
        start_found = False
        for row in reader:
            if row == start_line:
                start_found = True
                continue
            if start_found:
                force_column.append(float(row[0]))
        return force_column
        #print(len(force_column))
        #print(force_column)




