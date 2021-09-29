import json
from csv import DictWriter


if __name__ == '__main__':
    with open("actors.json", "r") as infile:
        actors = json.load(infile)

    csv_list = []
    for key, val in actors.items():
        csv_list.append({
            'Friendly Name': key,
            'Actor Name': val
        })


    with open("actors.csv", "w") as outfile_csv:
        writer = DictWriter(outfile_csv,
                            fieldnames=['Friendly Name', 'Actor Name'],
                            delimiter=',', lineterminator='\n')
        writer.writeheader()
        writer.writerows(csv_list)
