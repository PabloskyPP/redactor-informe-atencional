"""
Módulo para generar la imagen final grafico_D2_final.png con superposiciones gráficas

Este módulo toma como base grafico_D2.png y genera una versión final con:
- Textos de puntuaciones globales (TR_total, TA_total, O_total, C_total, TOT, CON, VAR, TR_max, TR_min, E_total)
- Cuadros de texto por fila para cada índice (TR, TA, O, C)
- Puntos negros en posiciones donde selected == True (items seleccionados)
- Líneas conectando últimos puntos de filas consecutivas

El módulo utiliza las estructuras explícitas de datos proporcionadas por lector_datos
para identificar celdas seleccionadas de forma clara y eficiente.

Nota: El Excel usa valores booleanos True/False en la columna 'selected'
"""

import os  # Módulo para operaciones del sistema de archivos
from PIL import Image, ImageDraw, ImageFont  # Librerías para manipulación de imágenes
import pandas as pd  # Librería para manipulación de datos tabulares


# ============================================================================
# CONFIGURACIÓN DE COORDENADAS Y DIMENSIONES
# ============================================================================

# Dimensiones de la imagen base (estas se detectan automáticamente)
# grafico_D2.png tiene 804x562 pixels

# Configuración del grid de la imagen D2
# El test D2 tiene 14 filas y aproximadamente 47 posiciones por fila
FILAS = 14  # Número de filas en el test D2
COLUMNAS_MAX = 47  # Número máximo de columnas en el test D2

# Márgenes y área útil del gráfico (ajustar según la imagen real)
# Estos valores mapean el área donde están dibujadas las filas del test
MARGEN_SUPERIOR = 60  # Píxeles desde el top hasta la primera fila
MARGEN_INFERIOR = 75  # Píxeles desde la última fila hasta el bottom
MARGEN_IZQUIERDO = 65  # Píxeles desde el left hasta la primera columna
MARGEN_DERECHO = 143  # Píxeles desde la última columna hasta el right

# Posiciones para textos rotados de totales (ajustables)
# Formato: (x, y) en píxeles desde la esquina superior izquierda


POSICIONES_TOTALES = { 
    'TR_total': (104, 511),  #  658
    'TR_total2': (659, 512),  # 
    'TA_total': (287, 511),  # 
    'TA_total2': (696, 512),  # 277
    'O_total': (139, 511),  # 
    'O_total2': (721, 512),  # 
    'C_total': (171, 511), 
    'C_total2': (327, 511),  #381
    'C_total3': (743, 512),  
    'TOT_total2': (67, 510),  # Hay que calcular y declarar este y siguientes índices
    'CON_total2': (254, 511), 
    'VAR_total': (428, 510),   
    'TR_min': (465, 510),  
    'TR_max': (494, 510),  
    'E_total2': (774, 512), 
}

# Tamaño de fuente para textos
FUENTE_TOTALES_TAMANIO = 9  # Tamaño de fuente para textos de totales
FUENTE_INDICES_TAMANIO = 9  # Tamaño de fuente para textos de índices

# Configuración de puntos y líneas
RADIO_PUNTO = 2  # Radio de los puntos negros en píxeles
COLOR_PUNTO = (0, 0, 0, 255)  # Color negro para los puntos
GROSOR_LINEA = 2  # Grosor de las líneas conectoras en píxeles
COLOR_LINEA = (0, 0, 0, 255)  # Color negro para las líneas

# Configuración de rotaciones (en grados, siguiendo convención PIL)
ROTACION_TEXTO_VERTICAL = 0  # Rotación antihoraria para texto vertical
ROTACION_IMAGEN_FINAL = -90  # Rotación horaria de la imagen final antes de guardar


# ============================================================================
# FUNCIONES DE MAPEO DE COORDENADAS
# ============================================================================

def calcular_dimensiones_grid(img_width, img_height):
    """
    Calcula las dimensiones útiles del grid en la imagen
    
    Args:
        img_width: Ancho de la imagen en píxeles
        img_height: Alto de la imagen en píxeles
        
    Returns:
        tuple: (area_util_width, area_util_height, x_inicio, y_inicio)
    """
    # Calcular el ancho y alto del área útil restando los márgenes
    area_util_width = img_width - MARGEN_IZQUIERDO - MARGEN_DERECHO
    area_util_height = img_height - MARGEN_SUPERIOR - MARGEN_INFERIOR
    
    # Coordenadas de inicio del área útil
    x_inicio = MARGEN_IZQUIERDO
    y_inicio = MARGEN_SUPERIOR
    
    return area_util_width, area_util_height, x_inicio, y_inicio


def mapear_fila_columna_a_coordenadas(row, column, img_width, img_height):
    """
    Mapea una posición (fila, columna) del test D2 a coordenadas (x, y) en la imagen
    
    Args:
        row: Número de fila (1-14)
        column: Número de columna/letra (1-47)
        img_width: Ancho de la imagen en píxeles
        img_height: Alto de la imagen en píxeles
        
    Returns:
        tuple: (x, y) coordenadas en píxeles
    """
    # Obtener dimensiones útiles del grid
    area_util_width, area_util_height, x_inicio, y_inicio = calcular_dimensiones_grid(img_width, img_height)
    
    # Calcular espaciado entre filas y columnas
    espaciado_vertical = area_util_height / (FILAS - 1) if FILAS > 1 else area_util_height
    espaciado_horizontal = area_util_width / (COLUMNAS_MAX - 1) if COLUMNAS_MAX > 1 else area_util_width
    
    # Convertir de índices 1-based a 0-based
    fila_idx = row - 1  # Ajustar fila a índice 0-based
    columna_idx = column - 1  # Ajustar columna a índice 0-based

    # Calcular coordenadas
    x = x_inicio + (columna_idx * espaciado_horizontal)  # Coordenada x basada en el espaciado horizontal
    y = y_inicio + (fila_idx * espaciado_vertical)  # Coordenada y basada en el espaciado vertical

    return int(x), int(y)  # Retornar coordenadas como enteros

def obtener_posicion_cuadro_texto_fila(row, indice, img_width, img_height):
    """
    Obtiene la posición para un cuadro de texto de índice en una fila específica
    
    Args:
        row: Número de fila (1-14)
        indice: Nombre del índice ('TR', 'TA', 'O', 'C')
        img_width: Ancho de la imagen
        img_height: Alto de la imagen
        
    Returns:
        tuple: (x, y) coordenadas en píxeles para el cuadro de texto
    """
    # Posición base: a la derecha de la fila
    _, _, _, y_inicio = calcular_dimensiones_grid(img_width, img_height)  # Obtener coordenada inicial y
    area_util_height = img_height - MARGEN_SUPERIOR - MARGEN_INFERIOR  # Altura útil del área
    espaciado_vertical = area_util_height / (FILAS - 1) if FILAS > 1 else area_util_height  # Espaciado entre filas

    fila_idx = row - 1  # Ajustar fila a índice 0-based
    y = y_inicio + (fila_idx * espaciado_vertical)  # Coordenada y basada en la fila

    # Offset horizontal según el índice
    offsets = {
        'TR': img_width - 123,  # Offset para TR
        'TA': img_width - 98,  # Offset para TA
        'O': img_width - 71,  # Offset para O
        'C': img_width - 50,  # Offset para C
    }

    x = offsets.get(indice, 5)  # Obtener el offset correspondiente al índice

    return int(x), int(y - 8)  # Ajuste vertical para centrar texto

# ============================================================================
# FUNCIONES DE DIBUJO
# ============================================================================

def cargar_fuente(tamanio):
    """
    Carga una fuente TrueType o usa fuente por defecto
    
    Args:
        tamanio: Tamaño de la fuente en puntos
        
    Returns:
        ImageFont: Objeto fuente
    """
    try:
        # Intentar cargar fuente TrueType del sistema
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", tamanio)
    except:
        try:
            # Alternativa: fuente arial
            return ImageFont.truetype("arial.ttf", tamanio)
        except:
            # Si falla, usar fuente por defecto
            return ImageFont.load_default()

def dibujar_textos_rotados_totales(draw, resultados, img_width, img_height):
    """
    Dibuja los textos rotados verticalmente con las puntuaciones totales
    
    Args:
        draw: Objeto ImageDraw
        resultados: Dict con puntuaciones (TR_total, TA_total, O_total, C_total, TOT, CON, VAR, TR_max, TR_min, E_total)
        img_width: Ancho de la imagen
        img_height: Alto de la imagen
    """
    fuente = cargar_fuente(FUENTE_TOTALES_TAMANIO)  # Cargar la fuente para los textos

    textos = {
        'TR_total': f"{resultados['TR_total']}",  # Texto para TR_total
        'TR_total2': f"{resultados['TR_total']}",  # Texto para TR_total
        'TA_total': f"{resultados['TA_total']}",  # Texto para TA_total
        'TA_total2': f"{resultados['TA_total']}",  # Texto para TA_total
        'O_total': f"{resultados['O_total']}",  # Texto para O_total
        'O_total2': f"{resultados['O_total']}",  # Texto para O_total
        'C_total': f"{resultados['C_total']}",  # Texto para C_total
        'C_total2': f"{resultados['C_total']}",  # Texto para C_total
        'C_total3': f"{resultados['C_total']}",  # Texto para C_total
        'TOT_total2': f"{resultados['TOT']}",  # Texto para TOT (TR - (O+C))
        'CON_total2': f"{resultados['CON']}",  # Texto para CON (TA - C)
        'VAR_total': f"{resultados['VAR']}",  # Texto para VAR (TR_max - TR_min)
        'TR_min': f"{resultados['TR_min']}",  # Texto para TR_min
        'TR_max': f"{resultados['TR_max']}",  # Texto para TR_max
        'E_total2': f"{resultados['E_total']}",  # Texto para E_total (O + C)
    }

    for clave, texto in textos.items():
        x, y = POSICIONES_TOTALES[clave]  # Obtener posición del texto

        # Crear imagen temporal para el texto rotado
        # Calcular tamaño del texto
        bbox = draw.textbbox((0, 0), texto, font=fuente)  # Bounding box del texto
        text_width = bbox[2] - bbox[0]  # Ancho del texto
        text_height = bbox[3] - bbox[1]  # Altura del texto

        # Crear imagen temporal con el texto
        txt_img = Image.new('RGBA', (text_width + 10, text_height + 10), (255, 255, 255, 0))  # Imagen transparente
        txt_draw = ImageDraw.Draw(txt_img)  # Objeto de dibujo para la imagen temporal
        txt_draw.text((5, 5), texto, font=fuente, fill=(0, 0, 0, 255))  # Dibujar el texto en la imagen temporal

        # Rotar la imagen 90 grados antihorario para texto vertical
        # (PIL: valores positivos = rotación antihoraria, valores negativos = horaria)
        txt_img_rotated = txt_img.rotate(ROTACION_TEXTO_VERTICAL, expand=True)

        # Pegar la imagen rotada en la imagen principal
        # Usar la imagen rotada como máscara para transparencia
        draw._image.paste(txt_img_rotated, (x, y), txt_img_rotated)  # Pegar el texto rotado en la posición calculada

def dibujar_cuadros_texto_por_fila(draw, resultados, img_width, img_height):
    """
    Dibuja cuadros de texto para cada índice en cada fila
    
    Args:
        draw: Objeto ImageDraw
        resultados: Dict con puntuaciones por fila (TR_por_fila, TA_por_fila, O_por_fila, C_por_fila)
        img_width: Ancho de la imagen
        img_height: Alto de la imagen
    """
    fuente = cargar_fuente(FUENTE_INDICES_TAMANIO)  # Cargar la fuente para los textos

    for row in range(1, FILAS + 1):  # Iterar sobre cada fila
        idx = row - 1  # Índice 0-based en las listas

        # Obtener valores de esta fila
        tr_val = resultados['TR_por_fila'][idx] if idx < len(resultados['TR_por_fila']) else 0  # Valor TR
        ta_val = resultados['TA_por_fila'][idx] if idx < len(resultados['TA_por_fila']) else 0  # Valor TA
        o_val = resultados['O_por_fila'][idx] if idx < len(resultados['O_por_fila']) else 0  # Valor O
        c_val = resultados['C_por_fila'][idx] if idx < len(resultados['C_por_fila']) else 0  # Valor C

        valores = {
            'TR': tr_val,  # Asignar valor TR
            'TA': ta_val,  # Asignar valor TA
            'O': o_val,  # Asignar valor O
            'C': c_val,  # Asignar valor C
        }

        for indice, valor in valores.items():  # Iterar sobre cada índice y su valor
            x, y = obtener_posicion_cuadro_texto_fila(row, indice, img_width, img_height)  # Calcular posición
            texto = str(valor)  # Convertir valor a texto
            draw.text((x, y), texto, font=fuente, fill=(0, 0, 0, 255))  # Dibujar el texto en la posición calculada

def dibujar_puntos_seleccionados(draw, resultados, img_width, img_height):
    """
    Dibuja puntos negros en las posiciones donde selected == True
    
    Esta función utiliza la estructura explícita de celdas seleccionadas 
    proporcionada por lector_datos para un acceso eficiente y claro.
    
    Args:
        draw: Objeto ImageDraw
        resultados: Dict con resultados que incluye 'celdas_seleccionadas' o 'datos_d2'
        img_width: Ancho de la imagen
        img_height: Alto de la imagen
        
    Returns:
        dict: Diccionario con {row: [(x, y), ...]} de puntos dibujados por fila
    """
    puntos_por_fila = {}  # Inicializar diccionario para almacenar puntos por fila

    # Usar la estructura explícita de celdas seleccionadas si está disponible
    if 'celdas_seleccionadas' in resultados:
        celdas_seleccionadas = resultados['celdas_seleccionadas']['seleccionadas']
        
        for celda in celdas_seleccionadas:
            row, column = celda
            
            # Mapear a coordenadas
            x, y = mapear_fila_columna_a_coordenadas(row, column, img_width, img_height)
            
            # Dibujar punto (círculo relleno)
            draw.ellipse(
                [(x - RADIO_PUNTO, y - RADIO_PUNTO),
                 (x + RADIO_PUNTO, y + RADIO_PUNTO)],
                fill=COLOR_PUNTO
            )
            
            # Guardar punto para posterior conexión
            if row not in puntos_por_fila:
                puntos_por_fila[row] = []
            puntos_por_fila[row].append((x, y))
    else:
        # Fallback: usar DataFrame directamente (compatibilidad hacia atrás)
        datos_d2 = resultados.get('datos_d2')
        if datos_d2 is None:
            return puntos_por_fila
            
        df_seleccionados = datos_d2[datos_d2['selected'] == True].copy()
        
        for _, fila in df_seleccionados.iterrows():
            row = int(fila['row'])
            column = int(fila['letter_num'])
            
            # Mapear a coordenadas
            x, y = mapear_fila_columna_a_coordenadas(row, column, img_width, img_height)
            
            # Dibujar punto (círculo relleno)
            draw.ellipse(
                [(x - RADIO_PUNTO, y - RADIO_PUNTO),
                 (x + RADIO_PUNTO, y + RADIO_PUNTO)],
                fill=COLOR_PUNTO
            )
            
            # Guardar punto para posterior conexión
            if row not in puntos_por_fila:
                puntos_por_fila[row] = []
            puntos_por_fila[row].append((x, y))

    return puntos_por_fila


def conectar_puntos_entre_filas(draw, puntos_por_fila):
    """
    Dibuja líneas conectando el último punto de cada fila con el último de la siguiente
    
    Args:
        draw: Objeto ImageDraw
        puntos_por_fila: Dict con {row: [(x, y), ...]} de puntos por fila
    """
    # Ordenar filas
    filas_ordenadas = sorted(puntos_por_fila.keys())
    
    for i in range(len(filas_ordenadas) - 1):
        fila_actual = filas_ordenadas[i]
        fila_siguiente = filas_ordenadas[i + 1]
        
        # Obtener último punto de cada fila
        if puntos_por_fila[fila_actual] and puntos_por_fila[fila_siguiente]:
            # El último punto es el que tiene mayor coordenada X
            ultimo_actual = max(puntos_por_fila[fila_actual], key=lambda p: p[0])  # Último punto de la fila actual
            ultimo_siguiente = max(puntos_por_fila[fila_siguiente], key=lambda p: p[0])  # Último punto de la fila siguiente

            # Dibujar línea entre los últimos puntos de filas consecutivas
            draw.line(
                [ultimo_actual, ultimo_siguiente],  # Coordenadas de los puntos a conectar
                fill=COLOR_LINEA,  # Color de la línea
                width=GROSOR_LINEA  # Grosor de la línea
            )

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def generar_imagen_final(resultados, datos_d2, ruta_grafico_base='grafico_D2.png', 
                        ruta_salida=r'C:\Users\Pablo\OneDrive\Escritorio\informes D2\grafico_D2_final.png'):
    """
    Genera la imagen final grafico_D2_final.png con todas las superposiciones
    
    Args:
        resultados: Dict con puntuaciones directas y por fila
        datos_d2: DataFrame con los datos del test D2
        ruta_grafico_base: Ruta a la imagen base grafico_D2.png
        ruta_salida: Ruta donde guardar grafico_D2_final.png
        
    Returns:
        bool: True si se generó correctamente, False en caso contrario
    """
    try:
        # 1. Cargar imagen base
        if not os.path.exists(ruta_grafico_base):  # Verificar si la imagen base existe
            print(f"Error: No se encuentra la imagen base en {ruta_grafico_base}")
            return False

        img = Image.open(ruta_grafico_base)  # Abrir la imagen base

        # Convertir a RGBA si no lo está (para soportar transparencia)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')  # Convertir el modo de la imagen

        img_width, img_height = img.size  # Obtener dimensiones de la imagen

        # 2. Crear objeto de dibujo
        draw = ImageDraw.Draw(img)  # Crear objeto para dibujar sobre la imagen

        # 3. Dibujar textos rotados de totales
        dibujar_textos_rotados_totales(draw, resultados, img_width, img_height)

        # 4. Dibujar cuadros de texto por fila
        dibujar_cuadros_texto_por_fila(draw, resultados, img_width, img_height)

        # 5. Dibujar puntos donde selected == True (usa estructura explícita de celdas)
        puntos_por_fila = dibujar_puntos_seleccionados(draw, resultados, img_width, img_height)

        # 6. Conectar puntos entre filas
        conectar_puntos_entre_filas(draw, puntos_por_fila)

        # 7. Rotar imagen 90 grados en sentido horario antes de guardar
        # (PIL: valores negativos = rotación horaria, valores positivos = antihoraria)
        img = img.rotate(ROTACION_IMAGEN_FINAL, expand=True)

        # 8. Guardar imagen final
        img.save(ruta_salida, 'PNG')  # Guardar la imagen generada

        print(f" Imagen final generada exitosamente: {ruta_salida}")
        return True

    except Exception as e:
        print(f" Error al generar imagen final: {e}")  # Imprimir error si ocurre
        import traceback
        traceback.print_exc()  # Mostrar traza del error
        return False

# ============================================================================
# FUNCIÓN DE UTILIDAD PARA INTEGRACIÓN
# ============================================================================

def generar_desde_resultados(resultados, script_dir=None):
    """
    Función de conveniencia para generar la imagen desde resultados ya calculados
    
    Args:
        resultados: Dict con puntuaciones y datos_d2 DataFrame
        script_dir: Directorio donde están los archivos (opcional)
        
    Returns:
        bool: True si se generó correctamente
    """
    if script_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener directorio del script actual

    ruta_base = os.path.join(script_dir, 'grafico_D2.png')  # Ruta de la imagen base
    ruta_salida =  os.path.join(r"C:\Users\Pablo\OneDrive\Escritorio\informes D2", "grafico_D2_final.png")  # Ruta de la imagen final


    # Los resultados deben incluir el DataFrame datos_d2
    if 'datos_d2' not in resultados:
        print("Error: Se necesita el DataFrame 'datos_d2' en resultados")  # Verificar existencia de datos_d2
        return False

    return generar_imagen_final(
        resultados,  # Puntuaciones y datos
        resultados['datos_d2'],  # DataFrame con datos del test
        ruta_base,  # Ruta de la imagen base
        ruta_salida  # Ruta de salida para la imagen final
    )