import csv

def radom_word():
    with open("Project Code/App/Flash Card/data/french_words.csv","r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        index = headers.index('English')
        data = [row[index] for row in reader]
        print(data)

print(radom_word())