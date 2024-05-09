
import random

def split_dataset(dataset_file, test_file, train_file):
    with open(dataset_file, 'r') as dataset:
        lines = dataset.readlines()
        random.shuffle(lines)

        test_lines = lines[:-4000]
        train_lines1 = lines[:36001]
        #train_lines2 = lines[:50000]
        #train_lines3 = lines[:75000]
        #train_lines4 = lines[:100000]


    with open(test_file, 'w') as test:
        test.writelines(test_lines)
    with open(train_file, 'w') as train:
        train.writelines(train_lines1)



dataset_file = 'dataset/ssim.txt'
test_file = 'dataset/test.txt'
train_file = 'dataset/train.txt'


split_dataset(dataset_file, test_file, train_file)

