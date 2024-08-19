import tkinter as tk
from tkinter import colorchooser, simpledialog, messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw
import random

def create_maze(width, height, cell_size, wall_colors, path_color, complexidade = 3):
    # Número de células no labirinto
    cols = width // cell_size
    rows = height // cell_size

    # Cria uma imagem em branco
    maze = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(maze)

    # Cria uma matriz para o labirinto
    maze_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def carve_maze(cx = 0, cy = 0):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < cols and 0 <= ny < rows and maze_grid[ny][nx] == 0:
                maze_grid[cy + dy][cx + dx] = 1
                maze_grid[ny][nx] = 1
                carve_maze(nx, ny)

    # Inicializa o labirinto
    maze_grid[0][0] = 1
    carve_maze(0, 0)

    # Desenha as paredes do labirinto
    
    for x in range(rows):
        for y in range(cols):
            if maze_grid[x][y] == 0:
                color_index = (x + y * complexidade) % len(wall_colors) 
                color = (wall_colors[color_index])
                draw.rectangle(
                    [y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size],
                    fill=color
                )
            else:
                draw.rectangle(
                    [y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size],
                    fill=path_color
                )
    
    return maze

def update_image():
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Correção que garante que a cor não será a mesma em um pixel
    
    aleatorio = [0,1,2]
    random.shuffle(aleatorio)
    
    cell_size = int(cell_size_var.get())
    wall_colors = [color_vars[i].get() for i in aleatorio if color_vars[i].get()]
    path_color = path_color_var.get()
    
    if not wall_colors:
        wall_colors = ['#000000']  # Cor padrão (preto)
    
    maze = create_maze(width, height, cell_size, wall_colors, path_color)
    photo = ImageTk.PhotoImage(maze)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

def choose_color(index):
    color = colorchooser.askcolor(title=f"Escolha a Cor {index + 1}")[0]
    if color:
        color_vars[index].set(f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}')
        update_image()

def choose_path_color():
    color = colorchooser.askcolor(title="Escolha a Cor do Caminho")[0]
    if color:
        path_color_var.set(f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}')
        update_image()

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        width = root.winfo_width()
        height = root.winfo_height()
        cell_size = int(cell_size_var.get())
        wall_colors = [color_vars[i].get() for i in range(5) if color_vars[i].get()]
        path_color = path_color_var.get()
     
        
        if not wall_colors:
            wall_colors = ['#000000']
        
        maze = create_maze(width, height, cell_size, wall_colors, path_color)
        maze.save(file_path)
        
def opcoes_usuario():

    # CORES
    
    for i in range(3):
        tk.Button(root, text=f"Escolha a cor {i + 1}", command=lambda i=i: choose_color(i)).pack()

    # COR DO CAMINHO
    
    tk.Button(root, text="Cor do caminho", command=choose_path_color).pack()

    
    # TAMANHO/COMPLEXIDADE
    
    tk.Label(root, text="Tamanho").pack()
    tk.Scale(root, from_=10, to_=30, orient=tk.HORIZONTAL, variable=cell_size_var, resolution=1).pack()

    # GERADOR DA ARTE
    
    tk.Button(root, text="Gerar uma nova arte", command=generate_art).pack()

    # SALVAR IMAGEM
    
    tk.Button(root, text="Salvar arquivo", command=save_image).pack()

    # Atualiza a imagem ao redimensionar a janela
    
    root.bind('<Configure>', lambda event: update_image())

def generate_art():
    update_image()

# Nome principal

root = tk.Tk()
root.title("Arte gerativa - Labirínto")

# Variáveis padrão

color_vars = [tk.StringVar(value='') for _ in range(5)]     # Até 3 cores
path_color_var = tk.StringVar(value='#FFFFFF')              # Cor do caminho padrão (branco)
cell_size_var = tk.IntVar(value=10)                         # Tamanho da célula padrão

# Cria um canvas para desenhar o labirinto

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

opcoes_usuario()

root.mainloop()
