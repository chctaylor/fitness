# import_weight.py

import csv
from fitness.models import BodyComposition

def import_weight(file_path):
    print("Hello World")

    BodyComposition.objects.all().delete()

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
                
            if row['fat_mass'] == '':
                BodyComposition.objects.create (
                date = row['date'],
                weight = row['weight']
                )
            else:
                BodyComposition.objects.create(
                    date = row['date'],
                    weight = row['weight'],
                    fat_mass = row['fat_mass'],
                    bone_mass = row['bone_mass'],
                    muscle_mass = row['muscle_mass'],
                    hydration = row['hydration']
                )

csv_file_path = '/Users/chase/Desktop/weight1.csv'
import_weight(csv_file_path)