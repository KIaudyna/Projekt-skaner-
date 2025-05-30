import tkinter as tk
from PIL import Image, ImageTk

#trzeba bedzie podlaczyc do naszego arkusza!!!===================================================================================
def akcja_1():
    print("Kliknięto Przycisk 1")

def akcja_2():
    print("Kliknięto Przycisk 2")

def akcja_3():
    print("Kliknięto Przycisk 3")

def akcja_4():
    print("Kliknięto Przycisk 4")

def akcja_5():
    print("Kliknięto Przycisk 5")

def akcja_6():
    print("Kliknięto Przycisk 6")

def akcja_7():
    print("Kliknięto Przycisk 7")

okno = tk.Tk()
okno.title("Program do inwentaryzacji baru")
okno.geometry("1000x600")

gorny_panel = tk.Frame(okno, width=1000, height=70, bg="#291612", bd=2, relief="raised", highlightthickness=3, highlightbackground="black")
gorny_panel.place(x=0, y=0)

lewy_panel = tk.Frame(okno, width=600, height=530, highlightthickness=3, highlightbackground="black")
lewy_panel.place(x=0, y=70)

prawy_panel = tk.Frame(okno, width=400, height=530, highlightthickness=3, highlightbackground="black")
prawy_panel.place(x=600, y=70)



grafika_lewy_panel = Image.open("tlol2.jpeg")
grafika_lewy_panel = grafika_lewy_panel.resize((600, 600), Image.Resampling.LANCZOS)
tlo_lewy_panel = ImageTk.PhotoImage(grafika_lewy_panel)

grafika_prawy_panel = Image.open("tlop.jpg")
grafika_prawy_panel = grafika_prawy_panel.resize((400, 600), Image.Resampling.LANCZOS)
tlo_prawy_panel = ImageTk.PhotoImage(grafika_prawy_panel)

grafika_gorny_panel = grafika_prawy_panel.resize((1000, 70), Image.Resampling.LANCZOS)
tlo_gorny_panel = ImageTk.PhotoImage(grafika_gorny_panel)

tlo_lewe = tk.Label(lewy_panel, image=tlo_lewy_panel)
tlo_lewe.place(x=0, y=0, relwidth=1, relheight=1)

tlo_prawe = tk.Label(prawy_panel, image=tlo_prawy_panel)
tlo_prawe.place(x=0, y=0, relwidth=1, relheight=1)

gorny_panel = tk.Label(gorny_panel, image=tlo_gorny_panel)
gorny_panel.place(x=0, y=0, relwidth=1, relheight=1)


btn1 = tk.Button(gorny_panel, text="Lista produktów", command=akcja_1, bg="#261d1c", fg="#b3685b", activebackground="#453735")
btn1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

btn2 = tk.Button(gorny_panel, text="Nowa inwentaryzacja", command=akcja_2, bg="#261d1c", fg="#b3685b", activebackground="#453735")
btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

btn3 = tk.Button(gorny_panel, text="Edytuj inwentaryzacje", command=akcja_3, bg="#261d1c", fg="#b3685b", activebackground="#453735")
btn3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

btn4 = tk.Button(gorny_panel, text="Wyeksportuj", command=akcja_4, bg="#261d1c", fg="#b3685b", activebackground="#453735")
btn4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

btn5 = tk.Button(gorny_panel, text="Wyświetl statystyki", command=akcja_5, bg="#261d1c", fg="#b3685b", activebackground="#453735")
btn5.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# mozemy dodawac przyciski do woli======================================================================================================
# btn6 = tk.Button(gorny_panel, text="Przycisk 6", command=akcja_6, bg="#261d1c", fg="#b3685b")
# btn6.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# btn7 = tk.Button(gorny_panel, text="Przycisk 7", command=akcja_7, bg="#261d1c", fg="#b3685b")
# btn7.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

okno.mainloop()
