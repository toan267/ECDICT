import csv

def load_words():
    # with open('words_alpha.txt') as word_file:
    with open('../english-wordlists/COCA_20000.txt') as word_file:
        # valid_words = set(word_file.read().split())
        valid_words = word_file.readlines()
        # print(valid_words)

    return valid_words
  
# reading data from a csv file 'Data.csv'
with open('ecdict.csv', newline='') as file:
    
    reader = csv.reader(file, delimiter = ',')
      
    # store the headers in a separate variable,
    # move the reader object to point on the next row
    headings = next(reader)
      
    # output list to store all rows
    Output = []
    Output.append(headings[:2])
    for row in reader:
        if row[1] != "":
            Output.append([row[0], "["+row[1]+"]"])
  
# for row_num, rows in enumerate(Output):
    # print('data in row number {} is {}'.format(row_num+1, rows))
  
english_words = load_words()

# print('policy\n' in english_words)
# if 'phone' in english_words:
    # print("fate")

# all words with phonetic only
with open('20k_word_phonetic.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for line in Output:
        if line[0]+'\n' in english_words:
            employee_writer.writerow(line)

## all worlds without chinese words
# with open("all.txt", "w") as txt_file:
    # for line in Output:
        # txt_file.write(", ".join(line) + "\n")

