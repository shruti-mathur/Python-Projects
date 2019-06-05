import csv

data = ["First Name, Last Name".split(","),
    "Sachin, Tendulkar".split(","),
    "Virat, Kohli".split(","),
    "MS, Dhoni".split(","),
    "John, Cena".split(",")
]
with open('data.csv', 'w', newline = '')as file:
    writer = csv.writer(file)

    for w in data:
        writer.writerow(w)