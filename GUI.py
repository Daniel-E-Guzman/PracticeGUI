import tkinter as tk
root = tk.Tk()
root.geometry('550x400')
root.title('Python GUI')
root.resizable(False, False)

def on_click():
    label.config(text="Button clicked!")


firstButton = tk.Button(root, text='Click Me', command=on_click)
firstButton.pack(pady=20)

label = tk.Label(root, font=('Helvetica', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 16), height=5, width=40)
textbox.pack(padx=20, pady=20)

myEntry = tk.Entry(root)
myEntry.pack(pady=20)



root.mainloop()