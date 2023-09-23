from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import datetime

class TextFileHandler:

    def __init__(self):
        self.filename = datetime.date.today().strftime("%Y-%m-%d.txt")
        self.file = None
        self.open()

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

    def total(self):
        total = 0
        with open(self.filename, "r") as file:
            for row in file:
                numbers = row.strip().split()
                for number in numbers:
                    if number.isdigit():
                        total += int(number)
        return total

class MyRoot(BoxLayout):

    def __init__(self):
        self.text_file_handler = TextFileHandler()
        super(MyRoot, self).__init__()
        self.total()

    def add(self, instance):
        number = self.ids.entry.text
        if number.isdigit() and int(number) >= 0:
            self.text_file_handler.write(number + '\n')
        elif number.lower() == "glass":
            number = str(330)
            self.text_file_handler.write(number + '\n')
        elif number.lower() == "bottle":
            number = str(750)
            self.text_file_handler.write(number + '\n')

        self.text_file_handler.close()
        self.text_file_handler.open()
        self.total()

    def total(self):
        total_value = self.text_file_handler.total()
        self.ids.total.text = f"Total: {total_value} ml"

    def quit(self, instance):
        self.text_file_handler.close()
        App.get_running_app().stop()
class WaterTrackerApp(App):

    def build(self):
        return MyRoot()

if __name__ == "__main__":
    watertracker = WaterTrackerApp()
    watertracker.run()
