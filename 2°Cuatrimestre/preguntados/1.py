import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame

win = tk.Tk()
win.title("🎯 Preguntados - Juego de Conocimiento")
win.configure(bg="#F5F5F5")

# Variables globales para el juego
puntaje_jugador1 = 0
puntaje_jugador2 = 0
turno_actual = 1  # 1 para jugador 1, 2 para jugador 2
categoria_actual = None
pregunta_actual = None
respuesta_correcta = None
numero_pregunta_actual = None  # Para rastrear qué pregunta se está mostrando

# Contadores de respuestas correctas por categoría para cada jugador
respuestas_correctas_jugador1 = {
    "ia": 0,
    "seguridad": 0,
    "programacion": 0,
    "redes": 0
}

respuestas_correctas_jugador2 = {
    "ia": 0,
    "seguridad": 0,
    "programacion": 0,
    "redes": 0
}

# Categorías completadas por cada jugador (para deshabilitar botones)
categorias_completadas_jugador1 = {
    "ia": False,
    "seguridad": False,
    "programacion": False,
    "redes": False
}

categorias_completadas_jugador2 = {
    "ia": False,
    "seguridad": False,
    "programacion": False,
    "redes": False
}

# Preguntas ya respondidas por cada jugador (por categoría y número de pregunta)
preguntas_respondidas_jugador1 = {
    "ia": [],
    "seguridad": [],
    "programacion": [],
    "redes": []
}

preguntas_respondidas_jugador2 = {
    "ia": [],
    "seguridad": [],
    "programacion": [],
    "redes": []
}

label_titulo = tk.Label(win, text="🎯 Bienvenido a Preguntados", font=("Arial", 28, "bold"), 
                       fg="#2E7D32", bg="#F5F5F5")
label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Contador de insignias
label_puntajes = tk.Label(win, text=f"Jugador 1: {puntaje_jugador1}/4 🏅                 Jugador 2: {puntaje_jugador2}/4 🏅", 
                         font=("Arial", 16, "bold"), fg="#1976D2", bg="#F5F5F5")
label_puntajes.grid(row=1, column=0, columnspan=2, pady=15)

# Botones de categorías
label_categorias = tk.Label(win, text="📚 Elige una categoría:", font=("Arial", 18, "bold"), 
                           fg="#424242", bg="#F5F5F5")
label_categorias.grid(row=2, column=0, columnspan=2, pady=15)

# Frame para los botones de categorías
frame_categorias = tk.Frame(win, bg="#F5F5F5")
frame_categorias.grid(row=3, column=0, columnspan=2, pady=10)

#____________________IA_____________________
ia_pregun = {
    1:{"¿Qué significa la sigla “IA”?" : "B"},
    2:{"¿Quién es considerado uno de los padres fundadores de la inteligencia artificial?" : "A"},
    3:{"¿Cuál de las siguientes es una aplicación común de la IA en la vida cotidiana?" : "B"},
    4:{"¿Cómo se llama la IA capaz de aprender de la experiencia y mejorar sus resultados?" : "C"},
    5:{"¿Cuál es uno de los principales desafíos éticos de la IA?" : "C"}
}

ia_resp = {
    1:{"A": "Inteligencia Automatica", "B": "Inteligencia Artificial", "C": "Integracion Algoritmica","D": "Interface Autonoma"},
    2:{"A": "Alan Turing", "B": "Albert Einstein", "C": "Bill Gates","D": "Isaac Asimov"},
    3:{"A": "Lavarropas automático", "B": "Asistentes virtuales como Siri o Alexa", "C": "Lámpara inteligente sin conexión","D": "Microondas convencional"},
    4:{"A": "IA débil", "B": "IA simbólica", "C": "Aprendizaje automático (Machine Learning)","D": "IA estática"},
    5:{"A": "La velocidad de procesamiento", "B": "El consumo energético", "C": "El sesgo en los algoritmos","D": "El costo de fabricación"}
}

#____________________SEGURIDAD_____________________
seguridad_pregun = {
    1:{"¿Qué es lo más importante al crear una contraseña segura?" : "C"},
    2:{"¿Qué es un virus informático?" : "C"},
    3:{"¿Qué intenta hacer un correo de phishing?" : "B"},
    4:{"¿Qué significa el candado al lado de la dirección web en el navegador?" : "B"},
    5:{"¿Qué deberías evitar compartir públicamente en redes sociales?" : "B"}
}

seguridad_resp = {
    1:{"A": "Que sea corta y fácil de recordar", "B": "Usar solo letras minúsculas", "C": "Combinar letras, números y símbolos","D": "Repetir la misma en todas las cuentas"},
    2:{"A": "Un programa que acelera tu computadora", "B": "Un archivo que limpia tu sistema", "C": "Un software que daña o altera el funcionamiento del equipo","D": "Un tipo de videojuego"},
    3:{"A": "Felicitarte por tu cumpleaños", "B": "Robar tus datos personales o contraseñas", "C": "Instalar actualizaciones del sistema","D": "Ofrecerte ayuda técnica gratuita"},
    4:{"A": "Que el sitio está en mantenimiento", "B": "Que la conexión es segura (usa HTTPS)", "C": "Que la página está bloqueada","D": "Que es una página del gobierno"},
    5:{"A": "Fotos de tus mascotas", "B": "Tu dirección o número de documento", "C": "Memes y chistes","D": "Gustos musicales"}
}

#___________________PROGRAMACION___________________
programacion_pregun = {
    1:{"¿Qué es un programa?" : "B"},
    2:{"¿Cuál de los siguientes es un lenguaje de programación?" : "C"},
    3:{"¿Para qué sirve un bucle (loop) en programación?" : "A"},
    4:{"¿Qué es una variable en programación?" : "B"},
    5:{"¿Cómo se llama un error en el código que impide que el programa funcione correctamente?" : "A"}
}

programacion_resp = {
    1:{"A": "Una lista de compras", "B": "Un conjunto de instrucciones que una computadora puede ejecutar", "C": "Un tipo de archivo de texto","D": "Un dibujo digital"},
    2:{"A": "HTML", "B": "Excel", "C": "Python","D": "PowerPoint"},
    3:{"A": "Para repetir una acción varias veces", "B": "Para borrar datos", "C": "Para decorar el código","D": "Para traducir el programa"},
    4:{"A": "Una carpeta con archivos", "B": "Un valor que puede cambiar durante la ejecución del programa", "C": "Un error del código","D": "Un tipo de teclado"},
    5:{"A": "Bug", "B": "Loop", "C": "Byte","D": "Pixel"}
}

#______________________REDES_______________________
redes_pregun = {
    1:{"¿Qué es una red de computadoras?" : "B"},
    2:{"¿Qué es Internet?" : "C"},
    3:{"¿Qué permite la conexión Wi-Fi?" : "A"},
    4:{"¿Cuál es la función principal de un router?" : "B"},
    5:{"¿Qué es una dirección IP?" : "B"}
}

redes_resp = {
    1:{"A": "Un grupo de personas que usan Internet", "B": "Un conjunto de computadoras conectadas entre sí para compartir recursos", "C": "Un programa para hacer dibujos","D": "Una página web"},
    2:{"A": "Un videojuego", "B": "Una red social", "C": "Una red mundial de computadoras interconectadas","D": "Un lenguaje de programación"},
    3:{"A": "Conectarse sin cables a una red", "B": "Aumentar la velocidad del procesador", "C": "Instalar programas automáticamente","D": "Jugar sin conexión"},
    4:{"A": "Guardar archivos", "B": "Conectar diferentes redes y distribuir Internet", "C": "Limpiar la memoria de la computadora","D": "Crear contraseñas seguras"},
    5:{"A": "Un tipo de virus", "B": "Un número que identifica a cada dispositivo en una red", "C": "Un programa para navegar en Internet","D": "Una contraseña del Wi-Fi"}
}

# Audios
pygame.mixer.init()

correcto = pygame.mixer.Sound("audios/correcto.mp3")
error = pygame.mixer.Sound("audios/error.mp3")
victoria = pygame.mixer.Sound("audios/victoria.mp3")

def reproducir(audio):
    if audio == "correcto":
        correcto.play()
    if audio == "error":
        error.play()
    if audio == "victoria":
        victoria.play()

# Función para actualizar el contador de insignias
def actualizar_puntajes():
    label_puntajes.config(text=f"Jugador 1: {puntaje_jugador1}/4 🏅                 Jugador 2: {puntaje_jugador2}/4 🏅 ")

# Función para verificar si un jugador ha ganado (4 insignias)
def verificar_ganador():
    global puntaje_jugador1, puntaje_jugador2
    
    if puntaje_jugador1 == 4:
        return 1  # Jugador 1 gana
    elif puntaje_jugador2 == 4:
        return 2  # Jugador 2 gana
    else:
        return 0  # Nadie ha ganado aún

# Función para mostrar pantalla de victoria
def mostrar_victoria(ganador):
    # Limpiar toda la ventana
    for widget in win.winfo_children():
        widget.destroy()
    
    # Configurar fondo de la ventana
    win.configure(bg="#1A1A1A")
    
    # Crear pantalla de victoria
    label_victoria = tk.Label(win, text="🎉 ¡FELICITACIONES! 🎉", font=("Arial", 32, "bold"), 
                             fg="#FFD700", bg="#1A1A1A")
    label_victoria.pack(pady=40)
    
    label_ganador = tk.Label(win, text=f"🏆 ¡{ganador} HA GANADO! 🏆", font=("Arial", 28, "bold"), 
                            fg="#00FF00", bg="#1A1A1A")
    label_ganador.pack(pady=25)
    
    label_descripcion = tk.Label(win, text="🎯 Ha logrado obtener las 4 insignias\n(una de cada categoría)", 
                                font=("Arial", 18), fg="#FFFFFF", bg="#1A1A1A")
    label_descripcion.pack(pady=25)
    
    # Botones de opciones
    frame_opciones = tk.Frame(win, bg="#1A1A1A")
    frame_opciones.pack(pady=40)
    
    boton_jugar_nuevo = tk.Button(frame_opciones, text="🔄 Jugar Nuevo Juego", font=("Arial", 16, "bold"), 
                                 width=18, height=2, command=reiniciar_juego, bg="#4CAF50", fg="white", 
                                 relief="raised", bd=3)
    boton_jugar_nuevo.pack(side=tk.LEFT, padx=15)
    
    boton_salir = tk.Button(frame_opciones, text="🚪 Salir", font=("Arial", 16, "bold"), 
                           width=18, height=2, command=win.quit, bg="#F44336", fg="white", 
                           relief="raised", bd=3)
    boton_salir.pack(side=tk.LEFT, padx=15)
    
    # Audio de victoria
    reproducir("victoria")

# Función para reiniciar el juego
def reiniciar_juego():
    global puntaje_jugador1, puntaje_jugador2, turno_actual
    global respuestas_correctas_jugador1, respuestas_correctas_jugador2
    global categorias_completadas_jugador1, categorias_completadas_jugador2
    global preguntas_respondidas_jugador1, preguntas_respondidas_jugador2
    
    # Resetear todas las variables del juego
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    turno_actual = 1
    
    respuestas_correctas_jugador1 = {
        "ia": 0, "seguridad": 0, "programacion": 0, "redes": 0
    }
    respuestas_correctas_jugador2 = {
        "ia": 0, "seguridad": 0, "programacion": 0, "redes": 0
    }
    
    categorias_completadas_jugador1 = {
        "ia": False, "seguridad": False, "programacion": False, "redes": False
    }
    categorias_completadas_jugador2 = {
        "ia": False, "seguridad": False, "programacion": False, "redes": False
    }
    
    preguntas_respondidas_jugador1 = {
        "ia": [], "seguridad": [], "programacion": [], "redes": []
    }
    preguntas_respondidas_jugador2 = {
        "ia": [], "seguridad": [], "programacion": [], "redes": []
    }
    
    # Limpiar ventana y volver al inicio
    for widget in win.winfo_children():
        widget.destroy()
    
    # Restaurar fondo original
    win.configure(bg="#F5F5F5")
    
    # Recrear la interfaz inicial
    label_titulo = tk.Label(win, text="🎯 Bienvenido a Preguntados", font=("Arial", 28, "bold"), 
                           fg="#2E7D32", bg="#F5F5F5")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=20)
    
    label_puntajes = tk.Label(win, text=f"Jugador 1: {puntaje_jugador1}/4  🏅                 Jugador 2: {puntaje_jugador2}/4  🏅 ", 
                             font=("Arial", 16, "bold"), fg="#1976D2", bg="#F5F5F5")
    label_puntajes.grid(row=1, column=0, columnspan=2, pady=15)
    
    label_categorias = tk.Label(win, text="📚 Elige una categoría:", font=("Arial", 18, "bold"), 
                               fg="#424242", bg="#F5F5F5")
    label_categorias.grid(row=2, column=0, columnspan=2, pady=15)
    
    frame_categorias = tk.Frame(win, bg="#F5F5F5")
    frame_categorias.grid(row=3, column=0, columnspan=2, pady=10)
    
    # Mostrar categorías
    mostrar_categorias()

# Función para mostrar una pregunta aleatoria de la categoría seleccionada
def mostrar_pregunta(categoria):
    global categoria_actual, pregunta_actual, respuesta_correcta
    
    categoria_actual = categoria
    
    if categoria == "ia":
        preguntas = ia_pregun
        respuestas = ia_resp
    elif categoria == "seguridad":
        preguntas = seguridad_pregun
        respuestas = seguridad_resp
    elif categoria == "programacion":
        preguntas = programacion_pregun
        respuestas = programacion_resp
    elif categoria == "redes":
        preguntas = redes_pregun
        respuestas = redes_resp
    
    # Obtener preguntas ya respondidas por el jugador actual
    if turno_actual == 1:
        preguntas_respondidas = preguntas_respondidas_jugador1[categoria]
    else:
        preguntas_respondidas = preguntas_respondidas_jugador2[categoria]
    
    # Obtener números de preguntas disponibles (no respondidas)
    preguntas_disponibles = []
    for num in range(1, len(preguntas) + 1):
        if num not in preguntas_respondidas:
            preguntas_disponibles.append(num)
    
    # Verificar si hay preguntas disponibles
    if not preguntas_disponibles:
        messagebox.showinfo("📚 Sin preguntas", f"😅 No hay más preguntas disponibles en esta categoría para el Jugador {turno_actual}.")
        return
    
    # Seleccionar una pregunta aleatoria de las disponibles
    num_random = random.choice(preguntas_disponibles)
    
    # Guardar el número de la pregunta actual
    global numero_pregunta_actual
    numero_pregunta_actual = num_random
    
    # Obtener la pregunta aleatoria
    pregunta_actual = list(preguntas[num_random].keys())[0]
    respuesta_correcta = list(preguntas[num_random].values())[0]
    respuestas_actuales = respuestas[num_random]
    
    # Limpiar la ventana de categorías
    for widget in win.winfo_children():
        if widget != label_titulo and widget != label_puntajes and widget != label_categorias and widget != frame_categorias:
            widget.destroy()
    
    # Mostrar la pregunta
    label_pregunta = tk.Label(win, text=pregunta_actual, font=("Arial", 18, "bold"), wraplength=650, 
                             fg="#2E7D32", bg="#F5F5F5", justify="center")
    label_pregunta.grid(row=4, column=0, columnspan=2, pady=25)
    
    # Crear los 4 botones con las respuestas
    boton_a = tk.Button(win, text=f"🅰️ {respuestas_actuales['A']}", font=("Arial", 13, "bold"), width=70, height=2, 
                       command=lambda: verificar_respuesta('A'), bg="#E3F2FD", fg="#1976D2", relief="raised", bd=2)
    boton_a.grid(row=5, column=0, columnspan=2, pady=8, padx=20)
    
    boton_b = tk.Button(win, text=f"🅱️ {respuestas_actuales['B']}", font=("Arial", 13, "bold"), width=70, height=2, 
                       command=lambda: verificar_respuesta('B'), bg="#FFF3E0", fg="#F57C00", relief="raised", bd=2)
    boton_b.grid(row=6, column=0, columnspan=2, pady=8, padx=20)
    
    boton_c = tk.Button(win, text=f"🅲 {respuestas_actuales['C']}", font=("Arial", 13, "bold"), width=70, height=2, 
                       command=lambda: verificar_respuesta('C'), bg="#F3E5F5", fg="#7B1FA2", relief="raised", bd=2)
    boton_c.grid(row=7, column=0, columnspan=2, pady=8, padx=20)
    
    boton_d = tk.Button(win, text=f"🅳 {respuestas_actuales['D']}", font=("Arial", 13, "bold"), width=70, height=2, 
                       command=lambda: verificar_respuesta('D'), bg="#E8F5E8", fg="#2E7D32", relief="raised", bd=2)
    boton_d.grid(row=8, column=0, columnspan=2, pady=8, padx=20)

# Función para verificar la respuesta
def verificar_respuesta(opcion):
    global puntaje_jugador1, puntaje_jugador2, turno_actual
    
    # Registrar la pregunta como respondida por el jugador actual
    if turno_actual == 1:
        if numero_pregunta_actual not in preguntas_respondidas_jugador1[categoria_actual]:
            preguntas_respondidas_jugador1[categoria_actual].append(numero_pregunta_actual)
    else:
        if numero_pregunta_actual not in preguntas_respondidas_jugador2[categoria_actual]:
            preguntas_respondidas_jugador2[categoria_actual].append(numero_pregunta_actual)
    
    if opcion == respuesta_correcta:
        # Incrementar contador de respuestas correctas para la categoría actual
        if turno_actual == 1:
            respuestas_correctas_jugador1[categoria_actual] += 1
            contador_actual = respuestas_correctas_jugador1[categoria_actual]
            jugador = "Jugador 1"
            puntaje_jugador = puntaje_jugador1
        else:
            respuestas_correctas_jugador2[categoria_actual] += 1
            contador_actual = respuestas_correctas_jugador2[categoria_actual]
            jugador = "Jugador 2"
            puntaje_jugador = puntaje_jugador2
        
        # Verificar si ha completado 3 respuestas correctas en esta categoría
        if contador_actual == 3:
            # Otorgar insignia
            if turno_actual == 1:
                puntaje_jugador1 += 1
            else:
                puntaje_jugador2 += 1
            
            # Obtener nombre de la categoría para mostrar
            nombres_categorias = {
                "ia": "Inteligencia Artificial",
                "seguridad": "Ciberseguridad", 
                "programacion": "Programación",
                "redes": "Redes"
            }
            nombre_categoria = nombres_categorias[categoria_actual]
            
            messagebox.showinfo("🎉 ¡Excelente!", f"✅ ¡Respuesta correcta!\n🏆 ¡{jugador} completa 3 respuestas correctas en {nombre_categoria} y gana una insignia!")
            
            # Audio de respuesta correcta
            reproducir("correcto")
            
            # Marcar categoría como completada y resetear contador
            if turno_actual == 1:
                respuestas_correctas_jugador1[categoria_actual] = 0
                categorias_completadas_jugador1[categoria_actual] = True
            else:
                respuestas_correctas_jugador2[categoria_actual] = 0
                categorias_completadas_jugador2[categoria_actual] = True
            
            actualizar_puntajes()
            
            # Verificar si hay un ganador
            ganador = verificar_ganador()
            if ganador == 1:
                mostrar_victoria("JUGADOR 1")
                return
            elif ganador == 2:
                mostrar_victoria("JUGADOR 2")
                return
        else:
            # Mostrar progreso
            nombres_categorias = {
                "ia": "Inteligencia Artificial",
                "seguridad": "Ciberseguridad", 
                "programacion": "Programación",
                "redes": "Redes"
            }
            nombre_categoria = nombres_categorias[categoria_actual]
            faltan = 3 - contador_actual
            
            messagebox.showinfo("✅ ¡Correcto!", f"🎯 ¡Respuesta correcta!\n📊 {jugador}: {contador_actual}/3 respuestas correctas en {nombre_categoria}.")
            
            # Audio de respuesta correcta
            reproducir("correcto")
        
        # Cambiar turno
        turno_actual = 2 if turno_actual == 1 else 1
        
        # Volver a mostrar las categorías
        mostrar_categorias()
    else:        
        messagebox.showwarning("❌ Incorrecto", "😔 Respuesta incorrecta")
        # Audio de error
        reproducir("error")
        
        # Cambiar turno
        turno_actual = 2 if turno_actual == 1 else 1
        # Volver a mostrar las categorías
        mostrar_categorias()

# Función para mostrar las categorías
def mostrar_categorias():
    # Limpiar widgets de pregunta/respuesta
    for widget in win.winfo_children():
        if widget not in [label_titulo, label_puntajes, label_categorias, frame_categorias]:
            widget.destroy()
    
    # Obtener categorías completadas del jugador actual
    if turno_actual == 1:
        categorias_completadas = categorias_completadas_jugador1
        jugador_actual = "Jugador 1"
    else:
        categorias_completadas = categorias_completadas_jugador2
        jugador_actual = "Jugador 2"
    
    # Mostrar turno actual
    label_turno = tk.Label(win, text=f"🎮 Turno de: {jugador_actual}", font=("Arial", 16, "bold"), 
                          fg="#1976D2", bg="#F5F5F5")
    label_turno.grid(row=4, column=0, columnspan=2, pady=15)
    
    # Crear botones de categorías con estado habilitado/deshabilitado
    boton_ia = tk.Button(frame_categorias, text="🤖 Inteligencia Artificial", font=("Arial", 12, "bold"), width=25, height=2, 
                        command=lambda: mostrar_pregunta("ia"), bg="#E3F2FD", fg="#1976D2", relief="raised", bd=3)
    boton_ia.grid(row=0, column=0, padx=30, pady=5)
    if categorias_completadas["ia"]:
        boton_ia.config(state="disabled", text="🤖 Inteligencia Artificial ✅", bg="#C8E6C9", fg="#388E3C")
    
    boton_seguridad = tk.Button(frame_categorias, text="🔒 Ciberseguridad", font=("Arial", 12, "bold"), width=25, height=2, 
                               command=lambda: mostrar_pregunta("seguridad"), bg="#FFF3E0", fg="#F57C00", relief="raised", bd=3)
    boton_seguridad.grid(row=0, column=1, padx=30, pady=5)
    if categorias_completadas["seguridad"]:
        boton_seguridad.config(state="disabled", text="🔒 Ciberseguridad ✅", bg="#C8E6C9", fg="#388E3C")
    
    boton_programacion = tk.Button(frame_categorias, text="💻 Programación", font=("Arial", 12, "bold"), width=25, height=2, 
                                  command=lambda: mostrar_pregunta("programacion"), bg="#F3E5F5", fg="#7B1FA2", relief="raised", bd=3)
    boton_programacion.grid(row=1, column=0, padx=30, pady=5)
    if categorias_completadas["programacion"]:
        boton_programacion.config(state="disabled", text="💻 Programación ✅", bg="#C8E6C9", fg="#388E3C")
    
    boton_redes = tk.Button(frame_categorias, text="🌐 Redes", font=("Arial", 12, "bold"), width=25, height=2, 
                           command=lambda: mostrar_pregunta("redes"), bg="#E8F5E8", fg="#2E7D32", relief="raised", bd=3)
    boton_redes.grid(row=1, column=1, padx=30, pady=5)
    if categorias_completadas["redes"]:
        boton_redes.config(state="disabled", text="🌐 Redes ✅", bg="#C8E6C9", fg="#388E3C")

# Mostrar categorías al inicio
mostrar_categorias()

win.mainloop()