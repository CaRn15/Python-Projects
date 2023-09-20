import datetime
class TextFileHandler:
    def __init__(self):
        self.filename = datetime.date.today().strftime("%Y-%m-%d.txt")

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


def main():
    file_handler = TextFileHandler()
    file_handler.open()
    while True:
        userInput = input("Write how many millilitres of water have you drank, exit or total:")
        if userInput not in ["exit", "total"] and (not userInput.isdigit() or int(userInput) < 0):
            print("Invalid input")
            continue
        if userInput.lower() == "total":
            file_handler.print()
            continue
        if userInput.lower() == 'exit':
            break
        file_handler.write(userInput + '\n')
        file_handler.close()
        file_handler.open()
        file_handler.print()
    file_handler.close()


if __name__ == "__main__":
    main()
