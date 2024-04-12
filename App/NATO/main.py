import pandas
with open("Project Code/App/NATO/nato_phonetic_alphabet.csv") as data:
    data_dict = pandas.read_csv(data)
    final_data = pandas.DataFrame(data_dict)

def NATO():
    while True:
        try:
            words = input("Enter a word: ").upper()
            nato = {row.letter:row.code for (index,row) in final_data.iterrows()}
            last_check = [nato[letter] for letter in words]
            print(last_check)
            break
        except KeyError as error:
            print(f"{error} is not string, please input onlyy letters in the alphabet.")

print(NATO())