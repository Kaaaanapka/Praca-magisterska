import tkinter as tk
from kamera import uruchom_kamere
from facelet import naklejka
from kociemba import Kociemba

#Dostepne kolory
kolor_scianek = ['white', 'green', 'orange', 'red', 'blue', 'yellow']

#UKŁAD ŚCIAN KOSTKI GÓRNA LEWA PRAWA FRONT TYLNIA ETC
#      U
#    L F R B
#      D

#Kociemba patern
#UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'

#Najpierw:
#U - gorna
#R - prawa 
#F - front
#D - dolna
#L - lewa
#B - tylna

#Nasz patern:
#Kolory scianki: UUUUUUUUUFFFFFFFFFLLLLLLLLLRRRRRRRRRBBBBBBBBBDDDDDDDDD

#U nas:

#U - gorna - poprawnie
#F - front - powinnen być PRAWO
#L - lewo - powinno byc FRONT
#R - prawo - powinne byc DOL
#B - tyl - powinnien byc LEWO
#D - dol - powinne byc BACK 




mapowanie_kolorow = {
    'white': 'U',
    'red': 'R',
    'green': 'F',
    'yellow':'D',
    'orange': 'L',
    'blue': 'B'
}

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

            canvas.itemconfig(kwadrat, fill=kolor)  # Wymuszenie ustawienia koloru
            naklejki.append(kwadrat)        #Dodaje ID naklejki do listy

            # Poprawione - używa poprawnej funkcji
            canvas.tag_bind(kwadrat, "<Button-1>", lambda event, canvas=canvas, kw=kwadrat: wypelnij(event, canvas, kw))

    return naklejki

#Funkcja do wypelnienia kwadracika kolorkiem (naklejki)
def wypelnij(event, canvas, kwadrat):

    global aktualny_kolor
    item = canvas.find_closest(event.x, event.y)[0]  # Znajduje najbliższy obiekt
    canvas.itemconfig(item, fill=aktualny_kolor)  # Zmienia jego kolor

#Funkcja do zmiany kolorow pojedynczej naklejki
def zmien_kolor(nowy_kolor):

    global aktualny_kolor
    aktualny_kolor = nowy_kolor

#Funkcja do odczytywanie kolorow z naklejek dla kociemba.py w celu rozwiazania kostki
def odczytaj_kolor(canvas, naklejki):
    kolory = []
    for naklejka in naklejki:
        kolor = canvas.itemcget(naklejka, "fill")       #Pobiera aktualny kolor naklejki

        #print(f"ID Naklejki: {naklejka}, Kolor: {kolor}")  # Debugowanie

        kolory.append(mapowanie_kolorow.get(kolor, "?"))  # Mapowanie na oznaczenie Kociemby
        

    return "".join(kolory)      #Łaczy w ciąg znaków

#Pokazuje cubestring (kod_kostki) po wprowadzeniu kolorow
def pokaz_kolor(canvas, wszystkie_naklejki):
    wszystkie_naklejki_flat = [id for sciana in wszystkie_naklejki for id in sciana]  # Spłaszczenie listy
    kod_kostki = odczytaj_kolor(canvas, wszystkie_naklejki_flat)
    print("Kolory scianki:", kod_kostki)
    

# Funkcja do dodawania przycisków
def dodaj_przycisk(root, canvas, wszystkie_naklejki):       
    kamera = tk.Button(root, text="Uruchom kamerę", command=lambda: uruchom_kamere()) 
    kamera.pack(pady=5)

    facelet = tk.Button(root, text="Wyswietl naklejke", command=lambda: naklejka())
    facelet.pack(pady=5)

    pokaz_kolory = tk.Button(root, text="Pokaz kod kostki", command=lambda: pokaz_kolor(canvas, wszystkie_naklejki))
    pokaz_kolory.pack(pady=5)

    rozwiaz = tk.Button(root, text="Rozwiaz kostke", command=lambda: Kociemba())
    rozwiaz.pack(pady=5)

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
    naklejki2 = generuj_naklejke(canvas, 390, 220, 'red')  # 2. Ścianka
    naklejki3 = generuj_naklejke(canvas, 220, 220, 'green')  # 3. Ścianka
    naklejki4 = generuj_naklejke(canvas, 220, 390, 'yellow')  # 4. Ścianka
    naklejki5 = generuj_naklejke(canvas, 50, 220, 'orange')  # 5. Ścianka
    naklejki6 = generuj_naklejke(canvas, 560, 220, 'blue')  # 6. Ścianka

    wszystkie_naklejki = [naklejki1, naklejki2, naklejki3, naklejki4, naklejki5, naklejki6]

    # Uruchomienie pętli głównej aplikacji
    dodaj_przycisk(root, canvas, wszystkie_naklejki)
    dodaj_kwadracik(root)

    root.mainloop()

# Uruchom aplikację
if __name__ == "__main__":
    main()
