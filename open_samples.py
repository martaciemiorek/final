import csv
def create_samples_data(file_name):
    samples_names = []
    cross_section_list = []
    samples_list =[]

    with open(f'{file_name}', newline='') as samples:
        reader = csv.DictReader(samples)
        for row in reader:
            samples_names.append(row['Nazwa '])
            dimension_a = float(row['a'])
            dimension_b = float(row['b'])
            cross_section = dimension_a * dimension_b
            cross_section_list.append(cross_section)

    return samples_names, cross_section_list
    #print(samples_names)
    #print(cross_section_list)


