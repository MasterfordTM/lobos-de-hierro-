import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import random


class Clan:  # atributos del clan principal
    def __init__(self, name, fuerza, HP):
        self.name = name
        self.fuerza = fuerza
        self.HP = HP
        self.hp_original = HP  # Guardamos el HP original


class Enemigo:
    def __init__(self, nombre, fuerza, HP):
        self.nombre = nombre
        self.fuerza = fuerza
        self.HP = HP


class Game:  # se definen atributos
    def __init__(self):
        self.clan = Clan("Lobos de Hierro", 12, 30)
        self.player_clan = None
        self.enemigos = [
            Enemigo("Lobo Oscuro", random.randint(5, 15), random.randint(20, 30)),
            Enemigo("Orco", random.randint(5, 15), random.randint(20, 35)),
            Enemigo("Tiranidos", random.randint(5, 15), random.randint(20, 40))
        ]
        self.current_enemigo_index = 0
        self.puntaje_total = 0  # puntuación inicial

    def start_game(self):
        self.player_clan = self.clan
        messagebox.showinfo("Clan Seleccionado", f"Se escogió un clan: {self.player_clan.name}")
        self.start_battle()

    def start_battle(self):
        if self.current_enemigo_index >= len(self.enemigos):
            messagebox.showinfo("Fin del Juego", "¡Has derrotado a todos los enemigos!")
            return

        self.enemigo = self.enemigos[self.current_enemigo_index]
        messagebox.showinfo("Batalla Iniciada", f"Te enfrentas a un {self.enemigo.nombre} con HP: {self.enemigo.HP}")

        while self.enemigo.HP > 0 and self.player_clan.HP > 0:
            action = messagebox.askquestion("Es tu turno de atacar", "¿Quieres atacar (sí) o defenderte (no)?")

            if action == 'yes':  # Atacar
                daño_infligido = random.randint(1, self.player_clan.fuerza)
                self.enemigo.HP -= daño_infligido
                messagebox.showinfo("Ataque",
                                    f"Has infligido {daño_infligido} puntos de daño. Enemigo HP: {self.enemigo.HP}")

                if self.enemigo.HP <= 0:
                    messagebox.showinfo("Victoria", f"¡Has derrotado a {self.enemigo.nombre}!")
                    self.puntaje_total += 4  # puntos que dan al derrotar a un enemigo
                    self.current_enemigo_index += 1  # orden de los enemigos
                    self.player_clan.HP = self.player_clan.hp_original  # Regresar HP a su valor original
                    self.start_battle()
                    return

                # Turno del enemigo
                daño_recibido = random.randint(1, self.enemigo.fuerza)
                self.player_clan.HP -= daño_recibido
                messagebox.showinfo("Ataque Enemigo",
                                    f"El enemigo te ha infligido {daño_recibido} puntos de daño. Tu HP: {self.player_clan.HP}")

                if self.player_clan.HP <= 0:
                    messagebox.showinfo("Derrota", "¡Has sido derrotado!")
                    return

            elif action == 'no':  # Defenderse
                messagebox.showinfo("Defensa", "Te preparas para defenderte.")
                daño_recibido = random.randint(1, self.enemigo.fuerza) // 2
                self.player_clan.HP -= daño_recibido
                messagebox.showinfo("Daño Recibido",
                                    f"{self.enemigo.nombre} te ha infligido {daño_recibido} puntos de daño. Tu HP: {self.player_clan.HP}")

                if self.player_clan.HP <= 0:
                    messagebox.showinfo("Derrota", "¡Has sido derrotado!")
                    return

    def mostrar_puntaje(self):
        messagebox.showinfo("Puntaje Total", f"Tu puntaje total es: {self.puntaje_total}")


# ventana de bienvenida
def mostrar_bienvenida():
    bienvenida = tk.Tk()
    bienvenida.title("Bienvenida")
    bienvenida.geometry("800x600")
    bienvenida.resizable(False, False)

    frame = tk.Frame(bienvenida)
    frame.pack(fill="both", expand=True)
    # Cargar la imagen
    img_path = r"C:\Users\csarr\OneDrive\Escritorio\codigospy\Lobos de Hierro\pythonProject\imagenes\OIP.jpg"
    img = Image.open(img_path)
    img = img.resize((800, 600), Image.LANCZOS)  # Ajustar el tamaño de la imagen
    img_tk = ImageTk.PhotoImage(img)


    inner_frame = tk.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)

    etiqueta = tk.Label(inner_frame, text="¡Bienvenido a 'Lobos de Hierro'!\nPrepárate para la batalla!",
                        font=("Helvetica", 16))
    etiqueta.pack(pady=20)

    btn_continue = tk.Button(inner_frame, text="Continuar",
                             command=lambda: [bienvenida.destroy(), mostrar_instrucciones()])
    btn_continue.pack(pady=10)

    bienvenida.mainloop()


# ventana de instrucciones
def mostrar_instrucciones():
    instrucciones = tk.Tk()
    instrucciones.title("Instrucciones")
    instrucciones.geometry("800x600")
    instrucciones.resizable(False, False)

    frame = tk.Frame(instrucciones)
    frame.pack(fill="both", expand=True)

    inner_frame = tk.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)

    texto_instrucciones = (
        "Instrucciones del juego:\n\n"
        "1. Selecciona 'Jugar' para iniciar la batalla.\n"
        "2. Durante tu turno, puedes elegir atacar o defenderte.\n"
        "3. Si atacas, infligirás daño al enemigo.\n"
        "4. Si te defiendes, recibirás menos daño en el siguiente ataque del enemigo.\n"
        "5. Tu objetivo es derrotar a todos los enemigos para ganar.\n"
        "6. Tu puntaje aumentará con cada enemigo derrotado.\n"
        "7. ¡Por el emperador!"
    )

    etiqueta = tk.Label(inner_frame, text=texto_instrucciones, font=("Helvetica", 14), justify="left")
    etiqueta.pack(pady=20)

    btn_continue = tk.Button(inner_frame, text="a darle",
                             command=lambda: [instrucciones.destroy(), mostrar_ventana_principal()])
    btn_continue.pack(pady=10)

    instrucciones.mainloop()


def iniciar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\csarr\OneDrive\Escritorio\codigospy\Lobos de Hierro\pythonProject\musica_de_juego.mp3\ytmp3free.cc_overture-from-tron-legacyscore-youtubemp3free.org.mp3")
    pygame.mixer.music.set_volume(0.5)# Cambia a la ruta correcta
    pygame.mixer.music.play(-1)  # Reproduce en bucle


# ventana principal
def mostrar_ventana_principal():
    global root, game
    root = tk.Tk()
    root.title("Lobos de Hierro")
    root.geometry("800x600")

    iniciar_musica()


    game = Game()

    btn_play = tk.Button(root, text="Jugar", command=inicio_juego, width=20)
    btn_play.pack(pady=10)

    btn_score = tk.Button(root, text="Ver Puntaje", command=game.mostrar_puntaje, width=20)
    btn_score.pack(pady=10)

    btn_exit = tk.Button(root, text="Salir", command=root.quit, width=10)
    btn_exit.pack(pady=10)

    root.mainloop()


def inicio_juego():
    game.start_game()


# Iniciar mostrando la ventana de bienvenida
mostrar_bienvenida()