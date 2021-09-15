import csv

if __name__ == '__main__':
    read_file = '/home/group3/Test/test_set.csv'
    output_file = '/home/group3/zhuyichen/test.csv'
    rows = []
    targets = []
    with open(read_file, 'r') as rfile:
        csvreader = csv.reader(rfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    line_num = 0
    with open(output_file, mode='a+') as ofile:
        writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['image_name', 'target'])
        for target in targets:
            writer.writerow([rows[line_num][0], target])
            line_num += 1

