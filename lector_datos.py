"""
Módulo para leer datos del test vocacional desde archivos Excel.

Hojas esperadas en el Excel:
  - 'info'                 → edad y nombre del participante
  - 'RIASEC'               → respuestas por enunciado del cuestionario (36 ítems)
  - 'Inteligencia Multiple' → respuestas por enunciado del cuestionario (24 ítems)
  - 'Ikigai'               → respuestas por enunciado (opcional)
"""
import math
import pandas as pd


# ---------------------------------------------------------------------------
# Constantes de mapeo ítem → factor
# ---------------------------------------------------------------------------

# Cuestionario Escala de Control Atencional (ACS)
ACS_ITEMS = {
    'focalización': range(1, 7),
    'cambio atencional': range(7, 13),
    'división atencional': range(13, 20),
}

# ---------------------------------------------------------------------------
# Lectura del archivo Excel
# ---------------------------------------------------------------------------

def leer_datos_excel(ruta_archivo):
    """
    Lee los datos del archivo Excel del test vocacional.

    Args:
        ruta_archivo: Ruta al archivo Excel.

    Returns:
        dict con claves:
            'edad', 'sub_num', 'nombre_completo', 'nombre',

 -->           Añadir resto del dict con claves resto de páginas del excel, consultables en excel_ejemplo
    """
    try:
        xl = pd.ExcelFile(ruta_archivo)
        sheet_names = xl.sheet_names

        # --- Hoja info ---------------------------------------------------
        df_info = pd.read_excel(ruta_archivo, sheet_name='info')
        edad = df_info['age'].iloc[0] if 'age' in df_info.columns else None
        sub_num = df_info['sub_num'].iloc[0] if 'sub_num' in df_info.columns else None

        # Nombre completo / nombre corto
        if sub_num is not None and not (isinstance(sub_num, float) and math.isnan(sub_num)):
            nombre_completo = str(sub_num).strip()
            tokens = nombre_completo.split()
            nombre = tokens[0] if tokens else nombre_completo
        else:
            nombre_completo = None
            nombre = None

        # --- Hoja ANT ----------------------------------
        ANT_TR = pd.read_excel(ruta_archivo, sheet_name='ANT')
        ANT_A = pd.read_excel(ruta_archivo, sheet_name='ANT')

        # --- Hoja Inteligencia Multiple -----------------------------------
        df_CPT = pd.read_excel(ruta_archivo, sheet_name='CPT')

        return {
            'edad': edad,
            'sub_num': sub_num,
            'nombre_completo': nombre_completo,
            'nombre': nombre,
            'ANT_TR': ANT_TR,
            'ANT_C': ANT_C,
            'ANT_O': ANT_O,
            'CPT_A': CPT_A,
        }
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        raise


# ---------------------------------------------------------------------------
# Cálculo de puntuaciones directas
# ---------------------------------------------------------------------------

def _suma_factor(df, items):
    """Suma las respuestas para los ítems del factor dado."""
    item_resp = dict(zip(df['numero_del_enunciado'], df['respuesta']))
    return int(sum(item_resp.get(i, 0) for i in items))


def calcular_puntuaciones_directas(datos):
    """
    Calcula todas las puntuaciones directas del test atencional ACS.

    Respuestas: 1=Nada, 2=Algo, 3=Mucho

    Args:
        datos: Dict devuelto por leer_datos_excel.

    Returns:
        dict con todas las puntuaciones directas (prefijo 'PD_') y metadatos.
    """
    df_acs = datos['df_ACS'].copy()

    resultados = {
        'edad':            datos['edad'],
        'sub_num':         datos.get('sub_num'),
        'nombre_completo': datos.get('nombre_completo'),
        'nombre':          datos.get('nombre'),
    }

    # ---- PD ACS --------------------------------------------------------
    for factor, items in ACS_ITEMS.items():
        resultados[f'PD_{factor}'] = _suma_factor(df_acs, items)


# ---------------------------------------------------------------------------
# Utilidad: resumen textual
# ---------------------------------------------------------------------------

def obtener_resumen_indices(resultados):
    """
    Devuelve un resumen legible de todas las puntuaciones directas.

    Args:
        resultados: Dict devuelto por calcular_puntuaciones_directas.

    Returns:
        str con el resumen formateado.
    """
    lineas = [
        "=" * 70,
        "RESUMEN — Puntuaciones Directas",
        "=" * 70,
        "",
        "ANT",
        f"  ANT TR:             {resultados.get('ANT_TR')}",
        "",
        "CPT",
        "",
        "",
    ]
    return "\n".join(lineas)