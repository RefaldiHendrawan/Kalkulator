from tkinter import *

window = Tk()
window.title("Kalkulator Python")
window.attributes('-fullscreen', True)  

def tombol_klik(item):
    global ekspresi
    ekspresi += str(item)
    input_text.set(ekspresi)
    label2.config(fg="white", bg="gray") 

def tombol_hapus():
    global ekspresi
    ekspresi = ""
    input_text.set("")
    label2.config(fg="black", bg="white") 

def tombol_samadengan():
    global ekspresi
    try:
        hasil = str(eval(ekspresi.replace('%', '/100')))  
        
        input_text.set(hasil)
        ekspresi = ""
        label2.config(fg="black", bg="white")  
        
    except:
        input_text.set("Salah Bang")
        ekspresi = ""
        label2.config(fg="black", bg="white")  

def tombol_ubah_tanda():
    global ekspresi
    if ekspresi and ekspresi[0] == '-':
        ekspresi = ekspresi[1:] 
    else:
        ekspresi = '-' + ekspresi 
    input_text.set(ekspresi)

def tombol_persen():
    global ekspresi
    ekspresi += "%"  
    input_text.set(ekspresi)

ekspresi = ""
input_text = StringVar()

frame = Frame(window, bg="white")
frame.pack(fill="both", expand=False)

frame2 = Frame(window, bg="black")
frame2.pack(fill="both", expand=True)

label = Label(frame, text="Kalkulator Refaldi PPLG 1", font=("Arial", 17), bg="orange")
label.pack(pady=5)

label2 = Label(frame, textvariable=input_text, font=("Arial", 32), bg="white", width=24, height=2, anchor='e', justify='right')
label2.pack(pady=5)

def create_button(text, command, row, col, colspan=1, rowspan=1, bg="lightgray", fg="black", font_size=17):
    Button(frame2, text=text, command=command, width=5, height=2, bg=bg, fg=fg, font=("Arial", font_size)).grid(
        row=row, column=col, columnspan=colspan, rowspan=rowspan, padx=2, pady=2, sticky="nsew"
    )

create_button("AC", tombol_hapus, 0, 0, colspan=1, bg="black", fg="white", font_size=18)
create_button("+/-", tombol_ubah_tanda, 0, 1, colspan=1, bg="black", fg="white", font_size=18)
create_button("%", tombol_persen, 0, 2, colspan=1, bg="black", fg="white", font_size=18)

create_button("÷", lambda: tombol_klik("/"), 0, 3, bg="orange", fg="white", font_size=18)
create_button("*", lambda: tombol_klik("*"), 1, 3, bg="orange", fg="white", font_size=18)  
create_button("-", lambda: tombol_klik("-"), 2, 3, bg="orange", fg="white", font_size=18) 
create_button("+", lambda: tombol_klik("+"), 3, 3, bg="orange", fg="white", font_size=18) 
create_button("=", tombol_samadengan, 4, 3, bg="orange", fg="white", font_size=18)  

create_button(",", lambda: tombol_klik(","), 4, 2, bg="gray", fg="white", font_size=18)  
create_button("0", lambda: tombol_klik("0"), 4, 0, colspan=2, bg="gray", fg="white", font_size=18)
create_button("1", lambda: tombol_klik("1"), 3, 0, bg="gray", fg="white", font_size=18)
create_button("2", lambda: tombol_klik("2"), 3, 1, bg="gray", fg="white", font_size=18)
create_button("3", lambda: tombol_klik("3"), 3, 2, bg="gray", fg="white", font_size=18)
create_button("4", lambda: tombol_klik("4"), 2, 0, bg="gray", fg="white", font_size=18)
create_button("5", lambda: tombol_klik("5"), 2, 1, bg="gray", fg="white", font_size=18)
create_button("6", lambda: tombol_klik("6"), 2, 2, bg="gray", fg="white", font_size=18)
create_button("7", lambda: tombol_klik("7"), 1, 0, bg="gray", fg="white", font_size=18)
create_button("8", lambda: tombol_klik("8"), 1, 1, bg="gray", fg="white", font_size=18)
create_button("9", lambda: tombol_klik("9"), 1, 2, bg="gray", fg="white", font_size=18)

for i in range(5):
    frame2.grid_columnconfigure(i, weight=1)
for i in range(5):
    frame2.grid_rowconfigure(i, weight=1)

window.mainloop()
