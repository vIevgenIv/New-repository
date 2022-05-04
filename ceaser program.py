from tkinter import *
class Sezar(Frame):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LETTERS_RU ="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    LETTERS_EN ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"



    def __init__(self, pencere):
        Frame.__init__(self, pencere)
        self.pencere = pencere

        Label(pencere, text="Enter your message: ", bg="coral", relief=GROOVE, width=20).place(x=20, y=30)
        self.Ent1 = Entry(pencere, width=30)
        self.Ent1.place(x=170, y=30)
        

        Label(pencere, text="Enter key: ", bg="coral", relief=GROOVE, width=20).place(x=20, y=90)
        self.Ent2 = Entry(pencere, width=30)
        self.Ent2.place(x=170, y=90)

        Button(pencere, text="Encrypt", bg="pink", relief=GROOVE, font="bold", command=self.Encrypt).place(x=20, y=150)
        Button(pencere, text="Decrypt", bg="pink", relief=GROOVE, font="bold", command=self.Decrypt).place(x=110, y=150)

        self.RESULT = Entry(pencere, width=30)
        self.RESULT.place(x=170, y=200)

    def Encrypt(self):
        key = int(self.Ent2.get())
        fild=self.Ent1.get()
        
        if self.LETTERS_RU.find(fild[0]):
            self.LETTERS = self.LETTERS_RU
        else:
            self.LETTERS = self.LETTERS_EN
        length = len(self.LETTERS)

        translation = ''

        for character in self.Ent1.get():
            if character.upper() in self.LETTERS:
                sayı = self.LETTERS.find(character.upper())
                sayı = (sayı + key) % length
                translation += self.LETTERS[sayı]
            else:
                translation += character

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)

    def Decrypt(self):
        key = int(self.Ent2.get())
        length = len(self.LETTERS)

        translation = ''

        for character in self.Ent1.get():
            if character.lower() in self.LETTERS:
                sayı = self.LETTERS.find(character.lower())
                sayı = (sayı - key) % length
                translation += self.LETTERS[sayı]
            else:
                translation += character

        self.RESULT.delete(0, END)
        self.RESULT.insert(0, translation)

if __name__ == "__main__":
    root = Tk()
    root.title("Sezar")
    root.geometry("720x480+50+50")
    Sezar(root).pack(side="top", fill="both")
    root.mainloop()