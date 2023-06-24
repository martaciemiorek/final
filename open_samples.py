import csv
def create_samples_data():
    samples_names = []
    cross_section_list = []
    samples_list =[]


    with open('spis_probek.csv', newline='') as samples:
        reader = csv.DictReader(samples)
        for row in reader:
            #print(row['Nazwa '], row['a'], row['b'])
            samples_names.append(row['Nazwa '])
            dimension_a = float(row['a'])
            dimension_b = float(row['b'])
            cross_section = dimension_a * dimension_b
            cross_section_list.append(cross_section)

        #for i in samples_names:
         #   temp = '\''+str(i) +'\''
          #  samples_list.append(temp)
            #print(temp)
    #print(samples_list)
    return samples_names, cross_section_list
    #print(samples_names)
    #print(cross_section_list)


create_samples_data()