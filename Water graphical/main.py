from tkinter import messagebox
import customtkinter
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

class WaterTracker():
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

        self.addButton = customtkinter.CTkButton(master=self.frame, text="Add", command=self.add)
        self.addButton.pack(pady=12, padx=15)
        self.addButton.pack()

        self.totalButton = customtkinter.CTkButton(master=self.frame, text="Total", command=self.total)
        self.totalButton.pack(pady=12, padx=15)
        self.totalButton.pack()

        self.quitButton = customtkinter.CTkButton(master=self.frame, text="Quit", command=self.quit)
        self.quitButton.pack(pady=12, padx=15)
        self.quitButton.pack()

    def add(self):
        number = self.entry.get()
        if number.isdigit() and int(number) >= 0:
            self.text_file_handler.write(number + '\n')
            self.text_file_handler.close()
            self.text_file_handler.open()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number")

    def total(self):
        total = self.text_file_handler.total()
        messagebox.showinfo("Total", f"Total milliliters drank: {total} ml")

    def quit(self):
        self.text_file_handler.close()
        self.frame.quit()


if __name__ == "__main__":
    root = customtkinter.CTk()
    tracker = WaterTracker()
    root.mainloop()
