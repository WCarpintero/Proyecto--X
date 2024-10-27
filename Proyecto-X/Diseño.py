from ursina import *

app = Ursina()

window.color = color.blue

# Primera pantalla 
texo1 = Text(text='Bienvenido', scale=3, color=color.black, position=(-0.2, 0.2))


def continuar():
    # Ocultar los elementos de la primera pantalla
    texo1.enabled = False
    boton_continuar.enabled = False
    
    # Mostrar los elementos de la siguiente pantalla
    boton_matrices.enabled = True
    boton_vectores.enabled = True
    boton_basicas.enabled = True

# Botón "Continuar" personalizado
boton_continuar = Button(
    text='Continuar',
    scale=(0.2, 0.1),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, -0.3),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=continuar  # Acción al hacer clic
)

#menu suma
def suma_dimesiones():
    #eliminar elementos de la tercera pantalla
    boton_suma.enabled = False
    boton_resta.enabled = False
    boton_multiplicacion.enabled = False
    boton_inversa.enabled = False
    boton_diagonal.enabled = False
    boton_transpuesta.enabled = False
    
    #crear campo de entrada para suma
    

boton_suma=Button(
    text='Sumas de matrices',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(-0.5, 0.2),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: suma_dimesiones(),  # Cerrar la aplicación al hacer clic
    enabled=False
)    
    
boton_resta=Button(
    text='Resta de matrices',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, 0.2),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)   

boton_multiplicacion=Button(
    text='Multiplicación de matrices',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0.5, 0.2),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
) 

boton_inversa=Button(
    text='Inversa de una matriz',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(-0.5, -0.1),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)

boton_diagonal=Button(
    text='Diagonal de una matriz',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, -0.1),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)

boton_transpuesta=Button(
    text='Transpuesta de una matriz',
    scale=(0.4, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0.5, -0.1),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)
def menu_matrices():
    #ocultar elementos de la segunda pantalla
    boton_matrices.enabled = False
    boton_vectores.enabled = False
    boton_basicas.enabled = False
    
    #mostrar elementos de la tercera pantalla
    boton_suma.enabled = True
    boton_resta.enabled = True
    boton_multiplicacion.enabled = True
    boton_inversa.enabled = True
    boton_diagonal.enabled = True
    boton_transpuesta.enabled = True
    
# Segunda pantalla (inicialmente oculta)
boton_matrices = Button(
    text='Entrar a la calculadora de Matrices',
    scale=(0.7, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, 0.3),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: menu_matrices(),  # Cerrar la aplicación al hacer clic
    enabled=False
)

boton_vectores = Button(
    text='Entrar a la calculadora de vectores',
    scale=(0.7, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, 0),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda:app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)

boton_basicas = Button(
    text='Entrar a la calculadora de operaciones Basicas',
    scale=(0.7, 0.2),  # Tamaño del botón (ancho, alto)
    color=color.red,  # Color del botón
    position=(0, -0.3),  # Posición en la ventana
    shape="rounded_cube",  # Forma personalizada (puede ser 'square', 'circle', 'rounded_cube')
    highlight_color=color.azure,  # Color al pasar el mouse
    on_click=lambda: app.quit(),  # Cerrar la aplicación al hacer clic
    enabled=False
)

app.run()

