import glob
from tkinter import messagebox
import matplotlib.pyplot as plt
plt.switch_backend("TkAgg")
import customtkinter
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TextFileHandler:
    """
    This class handles files

    """

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


class WaterTracker:
    def __init__(self):
        self.text_file_handler = TextFileHandler()
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        root.geometry("800x600")

        self.frame = customtkinter.CTkFrame(master=root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Water tracker", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Water amount", font=("Roboto", 15))
        self.entry.pack(pady=12, padx=15)

        self.totalLabel = customtkinter.CTkLabel(master=self.frame, text="Total: 0.0", font=("Roboto", 15))
        self.totalLabel.pack(pady=12, padx=15)

        self.statsButton = customtkinter.CTkButton(master=self.frame, text="Daily stats", command=self.dailyStats)
        self.statsButton.pack(pady=12, padx=15)

        self.addButton = customtkinter.CTkButton(master=self.frame, text="Add", command=self.add)
        self.addButton.pack(pady=12, padx=15)

        self.quitButton = customtkinter.CTkButton(master=self.frame, text="Quit", command=self.quit)
        self.quitButton.pack(pady=12, padx=15)

        self.total()

    def add(self):
        number = self.entry.get()
        if number.isdigit() and int(number) >= 0:
            self.text_file_handler.write(number + '\n')
        elif number.lower() == "glass":
            number = str(330)
            self.text_file_handler.write(number + '\n')
        elif number.lower() == "bottle":
            number = str(750)
            self.text_file_handler.write(number + '\n')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
        self.text_file_handler.close()
        self.text_file_handler.open()
        self.total()

    def total(self):
        total = self.text_file_handler.total()
        self.totalLabel.configure(text=f"Total: {total} ml")

    def quit(self):
        self.text_file_handler.close()
        self.frame.quit()

    def dailyStats(self):

        statsWindow = customtkinter.CTkToplevel(self.frame)
        statsWindow.title("Daily statistics")

        statsLabel = customtkinter.CTkLabel(statsWindow, text="Daily statistics", font=("Roboto", 18))
        statsLabel.pack(pady=12, padx=10)

        statsText = customtkinter.CTkLabel(statsWindow, text="", font=("Roboto", 18))
        statsText.pack(pady=12, padx=10)

        file_name_pattern = "*.txt"
        stats = []
        dates = []
        totals = []
        for filename in glob.glob(file_name_pattern):
            with open(filename, "r") as file:
                file_total = 0
                for row in file:
                    numbers = row.strip().split()
                    for number in numbers:
                        if number.isdigit():
                            file_total += int(number)
                filename = filename.replace(".txt", "")
                stats.append(f"{filename}, total ml drank: {file_total} ml")
                dates.append(filename)
                totals.append(file_total)

        statsText.configure(text="\n\n".join(stats))


        plt.plot(dates, totals)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Total ml", fontsize=14)
        plt.title("Daily ml drank", fontsize=14)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.ylim(0, max(totals))
        canvas = FigureCanvasTkAgg(plt.gcf(), master=statsWindow)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        plt.close()
        plt.show()


if __name__ == "__main__":
    root = customtkinter.CTk()
    tracker = WaterTracker()
    root.mainloop()
