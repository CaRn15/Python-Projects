import datetime

class TextFileHandler:
    def __init__(self):
        self.filename = datetime.date.today().strftime("%Y-%m-%d.txt")
        self.file = None

    def open(self):
        try:
            self.file = open(self.filename, 'a')
        except FileNotFoundError:
            self.file = open(self.filename, 'w')

    def write(self, text):
        if self.file:
            self.file.write(text)

    def close(self):
        if self.file:
            self.file.close()

    def print(self):
        total = 0
        with open(self.filename, "r") as file:
            for row in file:
                numbers = row.strip().split()
                for number in numbers:
                    if number in ["exit", "total"]:
                        total += 0
                    else:
                        total += int(number)
        print(total, "ml","/",3000,"ml")
