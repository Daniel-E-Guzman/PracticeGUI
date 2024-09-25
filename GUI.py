import tkinter as tk
root = tk.Tk()
#root.geometry('800x500')
root.title('Python GUI')

firstButton = tk.Button(root, text='Click Me')
firstButton.grid(pady=20)

label = tk.Label(root, text='Hello World!', font=('Helvetica', 18))
label.grid(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 16), height=5, width=40)
textbox.grid(padx=20, pady=20)

myEntry = tk.Entry(root)
myEntry.grid(pady=20)


root.mainloop()