"""
Módulo con las reglas psicométricas del test atencional.
"""
from lector_datos import 




def pd_a_pct_acs(pd_value):
    """Convierte puntuación directa a porcentaje/percentil (0-100)."""
    if pd_value is None:
        return 0
    return round((pd_value / X) * 100)


def clasificar_pct(pct):
    """Clasifica un porcentaje en una etiqueta descriptiva."""
    if pct is None:
        return "N/D"
    if pct <= 25:
        return "Bajo"
    if pct <= 75:
        return "Medio"
    return "Alto"


def obtener_ajuste_edad(edad):
    """Ajuste por edad (identidad en la versión actual)."""
    return {}


# ---------------------------------------------------------------------------
# Pipeline completo: PD → porcentajes → clasificaciones
# ---------------------------------------------------------------------------

def obtener_puntuaciones(resultados):
    """
    Calcula porcentajes, clasificaciones y top3 para todos los índices,
    añadiéndolos a ``resultados`` in-place.

    Args:
        resultados: Dict con puntuaciones directas (devuelto por
                    calcular_puntuaciones_directas).

    Returns:
        dict: Sub-diccionario de clasificaciones (para uso en generador_docx).
    """

    # ---- Porcentajes y clasificaciones --------------------------------
    for indice in ANT_TR_indices:
        pd_ANT_TR = resultados.get(f'ANT_TR_{indice}', 0) or 0
        pct    = pd_a_pct_ANT_TR(pd_ANT_TR)
        resultados[f'PCT_{indice}']            = pct
        resultados[f'Clasificacion_{indice}']  = clasificar_pct(pct)

