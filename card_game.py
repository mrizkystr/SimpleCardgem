import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Definisikan kartu dan poin dengan nama file yang sesuai
cards = {
    'blessing_80': {'points': 80, 'image': 'blessing80.jpg'},
    'blessing_50': {'points': 50, 'image': 'blessing50.jpg'},
    'blessing_30': {'points': 30, 'image': 'blessing30.jpg'},
    'blessing_10': {'points': 10, 'image': 'blessing10.jpg'},
    'bomb': {'points': -10, 'image': 'bomb.jpg'}
}

class CardGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Permainan Kartu")
        self.geometry("400x500")
        
        self.score = 0
        self.target_score = 100
        self.delay_draw = 1  # delay untuk mengambil kartu
        self.delay_show = 2  # delay untuk menunjukkan hasil

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Selamat datang di permainan kartu!")
        self.label.pack(pady=10)
        
        self.score_label = tk.Label(self, text=f"Skor Anda: {self.score}")
        self.score_label.pack(pady=10)

        self.draw_button = tk.Button(self, text="Ambil Kartu", command=self.draw_card)
        self.draw_button.pack(pady=10)

        self.card_label = tk.Label(self)
        self.card_label.pack(pady=10)

    def draw_card(self):
        self.draw_button.config(state=tk.DISABLED)
        self.after(self.delay_draw * 1000, self.show_card)

    def show_card(self):
        card = random.choice(list(cards.keys()))
        card_info = cards[card]

        image = Image.open(card_info['image'])
        image = image.resize((200, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.card_label.config(image=photo)
        self.card_label.image = photo
        self.label.config(text=f"Anda mendapatkan kartu: {card.replace('_', ' ').title()} ({card_info['points']} poin)")

        self.after(self.delay_show * 1000, self.update_score, card_info['points'])

    def update_score(self, card_points):
        self.score += card_points

        if self.score < 0:
            self.score = 0  # Skor tidak bisa negatif

        self.score_label.config(text=f"Skor Anda: {self.score}")
        self.draw_button.config(state=tk.NORMAL)

        if self.score >= self.target_score:
            messagebox.showinfo("Selamat!", "Anda mencapai target dan menang!")
            self.reset_game()

    def reset_game(self):
        self.score = 0
        self.score_label.config(text=f"Skor Anda: {self.score}")
        self.label.config(text="Selamat datang di permainan kartu!")
        self.card_label.config(image='')

if __name__ == "__main__":
    game = CardGame()
    game.mainloop()
