import tkinter as tk

main_window = tk.Tk()

label1 = tk.Label(main_window, text='Label1')
label2 = tk.Label(main_window, text='Label2')

tombol1 = tk.Button(main_window, text='Tombol1')
tombol2 = tk.Button(main_window, text='Tombol2')

# Method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# Method menampilkan GUI
main_window.mainloop()

