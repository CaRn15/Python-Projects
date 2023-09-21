from text_file_handler import TextFileHandler
class Main:
    def main(self):
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
    Main().main()
