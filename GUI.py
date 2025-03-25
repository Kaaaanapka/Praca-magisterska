import tkinter as tk
from kamera import uruchom_kamere
from facelet import naklejka

#Dostepne kolory
kolor_scianek = ['white', 'green', 'red', 'orange', 'blue', 'yellow']

#zmienna globalna przechowujaca aktualny kolor
aktualny_kolor = "white"


# Funkcja do generowania faceletów na każdej ściance
def generuj_naklejke(canvas, start_x, start_y, kolor="white"):
    rozmiar = 50
    margin = 5
    naklejki = []

    for i in range(3):
        for j in range(3):
            x = start_x + j * (rozmiar + margin)
            y = start_y + i * (rozmiar + margin)
            kwadrat = canvas.create_rectangle(x, y, x + rozmiar, y + rozmiar, fill=kolor, outline="black")

            naklejki.append(kwadrat)        #Dodaje ID naklejki do listy

            # Poprawione - używa poprawnej funkcji
            canvas.tag_bind(kwadrat, "<Button-1>", lambda event, canvas=canvas, kw=kwadrat: wypelnij(event, canvas, kw))

    return naklejki


def wypelnij(event, canvas, kwadrat):

    global aktualny_kolor
    item = canvas.find_closest(event.x, event.y)[0]  # Znajduje najbliższy obiekt
    canvas.itemconfig(item, fill=aktualny_kolor)  # Zmienia jego kolor



def zmien_kolor(nowy_kolor):

    global aktualny_kolor
    aktualny_kolor = nowy_kolor

# Funkcja do dodawania przycisków
def dodaj_przycisk(root, canvas):       
    kamera = tk.Button(root, text="Uruchom kamerę", command=lambda: uruchom_kamere()) 
    kamera.pack(pady=5)

    facelet = tk.Button(root, text="Wyswietl naklejke", command=lambda: naklejka())
    facelet.pack(pady=5)

# Funkcja do dodawania kwadracików z kolorami
def dodaj_kwadracik(root):

    global aktualny_kolor
    
    frame = tk.Frame(root)
    frame.pack(pady=5)

    for kolor in kolor_scianek:
        przycisk = tk.Button(frame, width=5, height=2, bg=kolor, bd=1, command=lambda k=kolor: zmien_kolor(k))
        przycisk.pack(side=tk.LEFT, padx=2)

# Główna funkcja aplikacji
def main():
    
    global aktualny_kolor

    root = tk.Tk()

    root.title ('Aplikacja do kostki rubika')       # Tytuł okna
    
    root.geometry('1800x1200',)           # Wymiary okna
    canvas = tk.Canvas(root, width=750, height=600)  # Canvas do rysowania
    canvas.pack()


    # Rysowanie pustych ścianek kostki (teraz są one niezależne)
    naklejki1 = generuj_naklejke(canvas, 220, 50, 'white')  # 1. Ścianka
    naklejki2 = generuj_naklejke(canvas, 220, 220, 'green')  # 2. Ścianka
    naklejki3 = generuj_naklejke(canvas, 50, 220, 'red')  # 3. Ścianka
    naklejki4 = generuj_naklejke(canvas, 390, 220, 'orange')  # 4. Ścianka
    naklejki5 = generuj_naklejke(canvas, 560, 220, 'blue')  # 5. Ścianka
    naklejki6 = generuj_naklejke(canvas, 220, 390, 'yellow')  # 6. Ścianka

    # Uruchomienie pętli głównej aplikacji
    dodaj_przycisk(root, canvas)
    dodaj_kwadracik(root)

    root.mainloop()

# Uruchom aplikację
if __name__ == "__main__":
    main()
