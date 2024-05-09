'''
def remove_duplicate_designs(file_path):
    designs = set()
    unique_designs = []

    with open(file_path, 'r') as file:
        for line in file:
            design = ' '.join(line.strip().split(' ')[:5])
            if design not in designs:
                designs.add(design)
                unique_designs.append(line)

    with open(file_path, 'w') as file:
        file.writelines(unique_designs)

txt_file = 'result/dataset.txt'
remove_duplicate_designs(txt_file)

def merge_files(file1, file2, dataset_file):
    designs = set()

    # Read file1 and store designs
    with open(file1, 'r') as f1:
        for line in f1:
            design = ' '.join(line.strip().split(' ')[:5])
            designs.add(design)

    # Read file2 and append unique designs to dataset
    with open(file2, 'r') as f2, open(dataset_file, 'w') as dataset:
        for line in f2:
            design = ' '.join(line.strip().split(' ')[:5])
            if design not in designs:
                dataset.write(line)

    # Append file1 to dataset
    with open(file1, 'r') as f1, open(dataset_file, 'a') as dataset:
        for line in f1:
            dataset.write(line)


file1 = 'result/dataset1.txt'
file2 = 'result/dataset2.txt'
dataset_file = 'result/dataset.txt'

merge_files(file1, file2, dataset_file)
'''
import random

def split_dataset(dataset_file, test_file, train_file):
    with open(dataset_file, 'r') as dataset:
        lines = dataset.readlines()
        random.shuffle(lines)

        test_lines = lines[100001:]
        train_lines1 = lines[:100001]
        #train_lines2 = lines[:50000]
        #train_lines3 = lines[:75000]
        #train_lines4 = lines[:100000]


    with open(test_file, 'w') as test:
        test.writelines(test_lines)
    with open(train_file, 'w') as train:
        train.writelines(train_lines1)



dataset_file = 'dataset/dataset.txt'
test_file = 'dataset/test.txt'
train_file = 'dataset/train.txt'


split_dataset(dataset_file, test_file, train_file)

