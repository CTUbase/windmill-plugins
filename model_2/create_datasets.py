import csv
from analyze_data import create_input

with open('input.txt', 'r', encoding='utf-8') as file:
    articles = [line.strip() for line in file.readlines()]

with open('datasets/datasets.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['death', 'injuries', 'property_large', 'property_medium', 'property_small', 'keyword', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if csvfile.tell() == 0:
        writer.writeheader()

    for article in articles:

        data = create_input(article)

        csv_data = {
            'death': data['deaths'],
            'injuries': data['injuries'],
            'property_large': data['property'][0],
            'property_medium': data['property'][1],
            'property_small': data['property'][2],
            'keyword': data['keyword'],
            'label': 3
        }

        writer.writerow(csv_data)

print("Successfully write to datasets/datasets.csv")