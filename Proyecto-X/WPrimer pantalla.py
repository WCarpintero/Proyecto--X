from ursina import *
import time

app = Ursina()

def primera_pantalla():
    
    cubo = Entity(model='cube', color=color.rgb(0, 0, 255), scale=(3, 3, 3), collider='box', position=(0,0,5))

    cubo.animate_rotation((360, 360, 360), duration=4)
    cubo.animate_scale((15, 10, 10), duration=4)
        
    abrir_suma = Button( 
        text='Suma de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(-0.5,0.3,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )
    
    abrir_resta = Button( 
        text='Resta de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(0,0.3,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )
    
    abrir_multiplicacion = Button( 
        text='Multiplicación de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(0.5,0.3,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )

    abrir_diagonales = Button( 
        text='Diagonales de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(-0.5,0 ,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )
    
    abrir_inversa = Button( 
        text='Inversa de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(0,0 ,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )
    
    abrir_transpuesta = Button( 
        text='Inversa de matrices',
        scale=(0.4,0.2), 
        color=color.gray,
        position=(0.5,0 ,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )
    
    regresar = Button( 
        text='Soltar calculadora y elegir otra',
        scale=(0.4,0.1), 
        color=color.red,
        position=(0.6,-0.3 ,0), 
        shape="rounded_cube",  
        highlight_color=color.azure,  
        font='assets/Faculty.ttf',
        visible=False
    )

    def mostrar_botones():
        
        abrir_suma.visible = True
        abrir_resta.visible = True
        abrir_multiplicacion.visible = True
        abrir_diagonales.visible = True
        abrir_inversa.visible = True
        abrir_transpuesta.visible = True
        regresar.visible = True
        
    invoke(mostrar_botones, delay=5)
    
primera_pantalla()

app.run()
