import tkinter as tk
from tkinter import messagebox
import random

class Clan:#atributos de principal
    def __init__(self, name, fuerza, HP):
        self.name = name
        self.fuerza = fuerza
        self.HP = HP

class Enemigo:
    def __init__(self, nombre, fuerza, HP):
        self.nombre = nombre
        self.fuerza = fuerza
        self.HP = HP

class Game:# llamo a mis atributos y los especifico
    def __init__(self):
        self.clan = Clan("Lobos de Hierro", 12, 40)
        self.player_clan = None
        self.enemigos = [
            #parametros de los enemigos  hp y golpes(aleatorios)
            Enemigo("Lobo Oscuro", random.randint(5, 15), random.randint(20, 30)),
            Enemigo("Orco", random.randint(5, 15), random.randint(20, 30)),
            Enemigo("tiranidos",random.randint(5,15),random.randint(20,30))
        ]
        self.current_enemigo_index = 0
        self.puntaje_total = 0 #puntaje inicial

    def start_game(self): # se asigna el clan
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
                messagebox.showinfo("Ataque", f"Has infligido {daño_infligido} puntos de daño. Enemigo HP: {self.enemigo.HP}")

                if self.enemigo.HP <= 0:
                    messagebox.showinfo("Victoria", f"¡Has derrotado a {self.enemigo.nombre}!")
                    self.puntaje_total += 4  # Aumentar puntaje
                    self.current_enemigo_index += 1 # orden de los enemigos
                    self.start_battle()
                    return

                # Turno del enemigo
                daño_recibido = random.randint(1, self.enemigo.fuerza)
                self.player_clan.HP -= daño_recibido
                messagebox.showinfo("Ataque Enemigo", f"El enemigo te ha infligido {daño_recibido} puntos de daño. Tu HP: {self.player_clan.HP}")

                if self.player_clan.HP <= 0:
                    messagebox.showinfo("Derrota", "¡Has sido derrotado!")
                    return

            elif action == 'no':  # Defenderse
                messagebox.showinfo("Defensa", "Te preparas para defenderte.")
                daño_recibido = random.randint(1, self.enemigo.fuerza) // 2  # Menos daño al defender
                self.player_clan.HP -= daño_recibido
                messagebox.showinfo("Daño Recibido", f"{self.enemigo.nombre} te ha infligido {daño_recibido} puntos de daño. Tu HP: {self.player_clan.HP}")

                if self.player_clan.HP <= 0:
                    messagebox.showinfo("Derrota", "¡Has sido derrotado!")
                    return

    def mostrar_puntaje(self):
        messagebox.showinfo("Puntaje Total", f"Tu puntaje total es: {self.puntaje_total}")

def mostrar_bienvenida():
    bienvenida = tk.Tk()
    bienvenida.title("Bienvenida")
    bienvenida.geometry("800x600")
    bienvenida.resizable(False, False)

    frame = tk.Frame(bienvenida)
    frame.pack(fill="both", expand=True)

    inner_frame = tk.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)

    etiqueta = tk.Label(inner_frame, text="¡Bienvenido a 'Lobos de Hierro'!\nPrepárate para la batalla!", font=("Helvetica", 16))
    etiqueta.pack(pady=20) # cartel de bienvenida

    btn_continue = tk.Button(inner_frame, text="Continuar", command=lambda: [bienvenida.destroy(), mostrar_ventana_principal()])
    btn_continue.pack(pady=10) # boton para acceder a la ventana prinvipal

    bienvenida.mainloop()

def mostrar_ventana_principal():
    global root, game  # Declarar las variables globales aquí
    root = tk.Tk()
    root.title("Lobos de Hierro")
    root.geometry("800x600")

    game = Game()  # Inicializar el juego aquí
#botones
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
