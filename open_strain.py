import csv
import numpy as np
def create_array_from_strain_file(sample):   #creates list of strain from DIC .csv file and calculates number of records in .csv file
    with open(f'{sample}.csv', 'r') as strain:
        reader = csv.reader(strain, delimiter=',')
        for _ in range(2):  # Skip the first two rows
            next(reader)
        selected_columns = np.array([(row[1], row[4]) for row in reader])
        return selected_columns
        #print(selected_columns)
        #print('---------')



