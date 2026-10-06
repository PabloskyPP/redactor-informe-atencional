"""
Módulo con la capa provisional PD → PT → clasificación.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class BaremoProvisional:
    minimo: float
    maximo: float
    invertir: bool = False


# TODO: sustituir por baremos reales.
BAREMOS_PROVISIONALES: Dict[str, BaremoProvisional] = {
    'ACS_atenciongeneral': BaremoProvisional(20, 80),
    'ACS_foco': BaremoProvisional(6, 24),
    'ACS_cambio': BaremoProvisional(6, 24),
    'ANT_A': BaremoProvisional(0, 108),
    'ANT_C': BaremoProvisional(0, 20, invertir=True),
    'ANT_O': BaremoProvisional(0, 20, invertir=True),
    'ANT_E': BaremoProvisional(0, 25, invertir=True),
    'ANT_TR': BaremoProvisional(250, 900, invertir=True),
    'ANT_TR_alerta': BaremoProvisional(-60, -10, invertir=True),
    'ANT_TR_orientacion': BaremoProvisional(-25, -10, invertir=True),
    'ANT_TR_ejecutivo': BaremoProvisional(40, 70, invertir=True),
    'CPT_CON': BaremoProvisional(120, 190),
    # Baremo temporal: una desviación estándar CON mayor se clasifica como más baja.
    'CPT_VAR': BaremoProvisional(0, 50, invertir=True),
    'CPT_O': BaremoProvisional(2, 6, invertir=True),
    'CPT_C': BaremoProvisional(3, 5, invertir=True),
    'CPT_E': BaremoProvisional(5, 11, invertir=True),
    'CPT_N': BaremoProvisional(300, 500),
    'FourFigures_A': BaremoProvisional(0, 128),
    'FourFigures_C': BaremoProvisional(0, 32, invertir=True),
    'FourFigures_TR': BaremoProvisional(500, 3500, invertir=True),
    'FourFigures_P4_A_obtenido_vs_esperado': BaremoProvisional(-1, 1),
    'DigitsMemorization_directo': BaremoProvisional(0, 12),
    'DigitsMemorization_inverso': BaremoProvisional(0, 12),
    'DigitsMemorization_creciente': BaremoProvisional(0, 12),
    'Digits_Memorization_M': BaremoProvisional(0, 12),
    'DUALTASK_PSV': BaremoProvisional(0, 30, invertir=True),
    'DUALTASK_A': BaremoProvisional(0, 12),
    'DUALTASK_C': BaremoProvisional(0, 12, invertir=True),
    'DUALTASK_O': BaremoProvisional(0, 12, invertir=True),
    'DUALTASK_TR': BaremoProvisional(0.2, 1.2, invertir=True),
    'DUALTASK_A_cuando_concurrencia': BaremoProvisional(0, 1),
    'DUALTASK_TR_cuando_concurrencia': BaremoProvisional(0.2, 1.2, invertir=True),
}


# TODO: sustituir por matriz percentílica real.
# Matriz improvisada PD (ms) -> percentil de eficiencia (mayor percentil = red más eficiente).
# Cada lista son pares (PD, percentil) con PD ascendente; se interpola linealmente entre ellos.
PERCENTILES_PROVISIONALES: Dict[str, list] = {
    'ANT_TR_alerta': [(-80, 95), (-60, 84), (-45, 69), (-30, 50), (-15, 31), (0, 16), (15, 5)],
    'ANT_TR_orientacion': [(-40, 95), (-30, 84), (-22, 69), (-15, 50), (-8, 31), (0, 16), (10, 5)],
    'ANT_TR_ejecutivo': [(20, 95), (40, 84), (60, 69), (80, 50), (100, 31), (125, 16), (160, 5)],
}


def pd_a_percentil_provisional(pd_value, clave: str):
    """
    Convierte PD a percentil con la matriz provisional; None si no hay matriz o dato.
    """
    tabla = PERCENTILES_PROVISIONALES.get(clave)
    if pd_value is None or not tabla:
        return None
    valor = float(pd_value)
    if valor <= tabla[0][0]:
        return tabla[0][1]
    if valor >= tabla[-1][0]:
        return tabla[-1][1]
    for (x0, p0), (x1, p1) in zip(tabla, tabla[1:]):
        if x0 <= valor <= x1:
            return int(round(p0 + (p1 - p0) * (valor - x0) / (x1 - x0)))
    return None


def pd_a_pt_provisional(pd_value, baremo: Optional[BaremoProvisional]):
    """
    Convierte PD a PT con una plantilla provisional.
    """
    if pd_value is None or baremo is None:
        return None

    if baremo.maximo == baremo.minimo:
        return 50

    ratio = (float(pd_value) - baremo.minimo) / (baremo.maximo - baremo.minimo)
    ratio = max(0.0, min(1.0, ratio))
    if baremo.invertir:
        ratio = 1.0 - ratio
    return int(round(ratio * 100))


def clasificar_pt(pt):
    if pt is None:
        return 'N/D'
    if pt <= 30:
        return 'bajo'
    if pt >= 70:
        return 'alto'
    return 'normal'


def _clasificar_diferencia(value: Optional[float], negativo_umbral: float, positivo_umbral: float) -> str:
    if value is None:
        return 'normal'
    if value <= negativo_umbral:
        return 'bajo'
    if value >= positivo_umbral:
        return 'alto'
    return 'normal'


def _nivel_a_numero(nivel: str) -> int:
    return {'bajo': -1, 'normal': 0, 'alto': 1}.get(nivel, 0)


def _combinar_estilo_tr_control(tr_nivel: str, c_nivel: str) -> str:
    if tr_nivel == 'bajo':
        return 'TR bajo y C alto' if c_nivel == 'alto' else 'TR bajo y C bajo o normal'
    if tr_nivel == 'normal':
        return 'TR normal y C bajo' if c_nivel == 'bajo' else 'TR normal y C normal o alto'
    return 'TR alto'


def _combinar_control_tr(c_nivel: str, tr_nivel: str) -> str:
    if c_nivel == 'bajo':
        return 'C bajo y TR alto' if tr_nivel == 'alto' else 'C bajo y TR bajo o normal'
    if c_nivel == 'alto':
        return 'C alto y TR bajo' if tr_nivel == 'bajo' else 'C alto y TR normal o alto'
    return 'C normal'


def _clasificar_special_tr(key_prefix: str, resultados: dict, clasificaciones: dict) -> None:
    tr = clasificaciones.get(f'{key_prefix}_TR')
    c = clasificaciones.get(f'{key_prefix}_C')
    if tr:
        clasificaciones[f'{key_prefix}_TR_texto'] = _combinar_estilo_tr_control(tr, c or 'normal')
    if c:
        clasificaciones[f'{key_prefix}_C_texto'] = _combinar_control_tr(c, tr or 'normal')


def _clasificar_ant_fatiga(resultados: dict, clasificaciones: dict) -> None:
    a_nivel = _clasificar_diferencia(resultados.get('PD_ANT_A_principio_vs_final'), -0.1, 0.1)
    tr_nivel = _clasificar_diferencia(resultados.get('PD_ANT_TR_principio_vs_final'), -50, 50)
    clasificaciones['ANT_A_principio_vs_final'] = a_nivel
    clasificaciones['ANT_TR_principio_vs_final'] = tr_nivel

    nivel_a_texto = {'bajo': 'negativo', 'normal': 'no sign', 'alto': 'positivo'}
    a_texto = nivel_a_texto[a_nivel]
    tr_texto = nivel_a_texto[tr_nivel]
    clave_texto = f'F_A {a_texto} y F_TR {tr_texto}'

    if a_texto == 'positivo' and tr_texto == 'no sign':
        if clasificaciones.get('ANT_TR') in ('bajo', 'normal'):
            clave_texto += ' y TR bajo o normal'

    clasificaciones['ANT_F_texto'] = clave_texto


def _clasificar_cpt_var(resultados: dict, clasificaciones: dict) -> None:
    """Clasifica CPT_VAR (variabilidad) y CPT_VAR_condicion (evolución de CON).

    CPT_VAR: desviación típica del CON entre series; >5 'bajo', <3 'alto', resto 'normal'.
    Condición: diferencia significativa (p < 0.05) del CON medio entre las primeras y
    últimas 4 series. Positiva = fatiga; negativa = automatismo, salvo que CPT_CON
    sea bajo, entonces dificultad inicial.
    """
    sd = resultados.get('PD_CPT_VAR_SD_CON')
    if sd is not None:
        if sd > 5:
            clasificaciones['CPT_VAR'] = 'bajo'
        elif sd < 3:
            clasificaciones['CPT_VAR'] = 'alto'
        else:
            clasificaciones['CPT_VAR'] = 'normal'

    diff = resultados.get('PD_CPT_CON_principio_vs_final')
    pvalue = resultados.get('P_CPT_CON_principio_vs_final')
    if diff is None or pvalue is None or pvalue >= 0.05 or diff == 0:
        clasificaciones['CPT_CON_principio_vs_final'] = 'normal'
    else:
        clasificaciones['CPT_CON_principio_vs_final'] = 'bajo' if diff > 0 else 'alto'
    if diff is None or pvalue is None or pvalue >= 0.05:
        clasificaciones['CPT_VAR_condicion'] = 'nada'
    elif diff > 0:
        clasificaciones['CPT_VAR_condicion'] = 'fatiga'
    elif diff < 0:
        tot_nivel = clasificaciones.get('CPT_CON')
        if tot_nivel in ('normal', 'alto'):
            clasificaciones['CPT_VAR_condicion'] = 'automatismo'
        elif tot_nivel == 'bajo':
            clasificaciones['CPT_VAR_condicion'] = 'dificultadinicial'
        else:
            clasificaciones['CPT_VAR_condicion'] = 'nada'
    else:
        clasificaciones['CPT_VAR_condicion'] = 'nada'


def _clasificar_cpt_diferencias(resultados: dict, clasificaciones: dict) -> None:
    clasificaciones['CPT_A_principio_vs_final'] = _clasificar_diferencia(
        resultados.get('PD_CPT_A_principio_vs_final'), -0.1, 0.1
    )
    clasificaciones['CPT_TR_principio_vs_final'] = _clasificar_diferencia(
        resultados.get('PD_CPT_TR_principio_vs_final'), -50, 50
    )

# Si tal añadir una función con algún índices o pruebas ()
def _clasificar_omisiones(resultados: dict, clasificaciones: dict) -> None:
    limites = {
        'ANT_O': (1, 4),
        'CPT_O': (3, 5),
        'DUALTASK_O': (1, 3),
    }
    for clave, (max_bajo, max_normal) in limites.items():
        valor = resultados.get(f'PD_{clave}')
        if valor is None:
            clasificaciones[clave] = 'N/D'
        elif valor <= max_bajo:
            clasificaciones[clave] = 'alto'
        elif valor <= max_normal:
            clasificaciones[clave] = 'normal'
        else:
            clasificaciones[clave] = 'bajo'


def _clasificar_digits_consistencia(resultados: dict, clasificaciones: dict) -> None:
    errores = resultados.get(
        'PD_DigitsMemorization_directo_errores_antes_ultimas_dos'
    )
    if errores is None:
        return
    if errores == 0:
        nivel = 'alto'
    elif errores <= 2:
        nivel = 'normal'
    else:
        nivel = 'bajo'
    clasificaciones['Digits_Memorization_consistencia'] = nivel


def _clasificar_dualtask(resultados: dict, clasificaciones: dict) -> None:
    psv = clasificaciones.get('DUALTASK_PSV', 'normal')
    a = clasificaciones.get('DUALTASK_A', 'normal')
    c = clasificaciones.get('DUALTASK_C', 'normal')
    o = {'bajo': 'alto', 'normal': 'normal', 'alto': 'bajo'}.get(
        clasificaciones.get('DUALTASK_O', 'normal'), 'normal'
    )
    tr = clasificaciones.get('DUALTASK_TR', 'normal')

    psv_num = _nivel_a_numero(psv)
    t2_num = round((_nivel_a_numero(a) + _nivel_a_numero(c) + _nivel_a_numero(o) + _nivel_a_numero(tr)) / 4)
    diff = abs(psv_num - t2_num)
    promedio = psv_num + t2_num

    if diff >= 2:
        clasificaciones['DUALTASK_General_PSV_y_A'] = 'Muy inestable' if promedio <= -1 else 'Inestable y positivo'
    elif promedio <= -1:
        clasificaciones['DUALTASK_General_PSV_y_A'] = 'Estable y negativo'
    elif promedio >= 1:
        clasificaciones['DUALTASK_General_PSV_y_A'] = 'Estable y positivo'
    else:
        clasificaciones['DUALTASK_General_PSV_y_A'] = 'Estable y normal'

    if diff >= 1:
        clasificaciones['DUALTASK_si_inestable'] = 'T1_mas_T2' if psv_num > t2_num else 'T2_mas_T1'

    diff_conc = resultados.get('PD_DUALTASK_PSV_cuando_concurrencia')
    t2_mal_p = clasificaciones.get('DUALTASK_A') == 'bajo'
    t2_mal_tr = clasificaciones.get('DUALTASK_TR') == 'bajo'
    if diff_conc is not None:
        if diff_conc > 2:
            direccion = 'deterioro'
        elif diff_conc < -2:
            direccion = 'mejora'
        else:
            direccion = 'no deterioro'

        if not t2_mal_p and not t2_mal_tr:
            condicion_t2 = 'buen T2'
        elif t2_mal_p and t2_mal_tr:
            condicion_t2 = 'mal T2 P y TR'
        elif t2_mal_p:
            condicion_t2 = 'mal T2 P'
        else:
            condicion_t2 = 'mal T2 TR'
        clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = (
            f'{direccion} y {condicion_t2}'
        )

    avg_concurrent_pts = [
        resultados.get('PT_DUALTASK_A_cuando_concurrencia'),
        pd_a_pt_provisional(resultados.get('PD_DUALTASK_PSV_cuando_concurrencia'), BaremoProvisional(-10, 10, invertir=True)),
        resultados.get('PT_DUALTASK_TR_cuando_concurrencia'),
    ]
    avg_concurrent_pts = [value for value in avg_concurrent_pts if value is not None]
    if avg_concurrent_pts:
        media = sum(avg_concurrent_pts) / len(avg_concurrent_pts)
        clasificaciones['DUALTASK_Rendimiento_General_cuando_concurrencia'] = clasificar_pt(media)

    diff_tr = resultados.get('PD_DUALTASK_TR_A_vs_C')
    if diff_tr is not None:
        if diff_tr > 0.03:
            clasificaciones['DUALTASK_TR_A_vs_C'] = 'positivo'
        elif diff_tr < -0.03:
            clasificaciones['DUALTASK_TR_A_vs_C'] = 'negativo'

    clasificaciones['DUALTASK_A_principio_vs_final'] = _clasificar_diferencia(
        resultados.get('PD_DUALTASK_A_principio_vs_final'), -0.1, 0.1
    )
    clasificaciones['DUALTASK_PSV_principio_vs_final'] = _clasificar_diferencia(
        resultados.get('PD_DUALTASK_PSV_principio_vs_final'), -2, 2
    )

    fatiga_flags = []
    auto_flags = []
    diferencias_temporales = (
        ('PSV', 'F PSV', 'Automatización PSV', False),
        ('A', 'F A', 'Automatización P', True),
        ('TR', 'F TR', 'Automatización TR', False),
    )
    for indice, clave_fatiga, clave_automatizacion, positivo_es_fatiga in diferencias_temporales:
        diferencia = resultados.get(f'PD_DUALTASK_{indice}_principio_vs_final')
        if diferencia is None:
            continue
        # PSV y A usan la misma significación que la tabla de resultados; TR no tiene umbral en la tabla.
        if indice == 'TR':
            pvalue = resultados.get('P_DUALTASK_TR_principio_vs_final')
            significativa = pvalue is not None and pvalue < 0.05
        else:
            significativa = clasificaciones.get(f'DUALTASK_{indice}_principio_vs_final') in ('bajo', 'alto')
        if not significativa:
            continue
        if (diferencia > 0) == positivo_es_fatiga:
            fatiga_flags.append(clave_fatiga)
        else:
            auto_flags.append(clave_automatizacion)

    def combinar_flags(flags):
        if len(flags) == 3:
            return f'{flags[0]}, {flags[1]} y {flags[2]}'
        return ' y '.join(flags)

    dimensiones_automatizadas = {
        'Automatización PSV': 'seguimiento visomotor',
        'Automatización P': 'aciertos',
        'Automatización TR': 'velocidad de respuesta',
    }
    nombres_auto = [
        dimensiones_automatizadas[f]
        for f in ('Automatización PSV', 'Automatización P', 'Automatización TR')
        if f in auto_flags
    ]
    clasificaciones['DUALTASK_dimension_automatizada'] = (
        ', '.join(nombres_auto[:-1]) + ' y ' + nombres_auto[-1]
        if len(nombres_auto) > 1 else (nombres_auto[0] if nombres_auto else '')
    )
    if fatiga_flags:
        clasificaciones['DUALTASK_Fatiga'] = combinar_flags(fatiga_flags)
    elif auto_flags:
        clasificaciones['DUALTASK_Fatiga'] = 'automatismo PSV, TR o A'
    else:
        clasificaciones['DUALTASK_Fatiga'] = 'no F'
    orden_automatizacion = ('Automatización PSV', 'Automatización TR', 'Automatización P')
    auto_flags.sort(key=orden_automatizacion.index)
    clasificaciones['DUALTASK_automatización'] = combinar_flags(auto_flags) if auto_flags else None

    t1 = _nivel_a_numero(psv)
    t2 = round((_nivel_a_numero(a) + _nivel_a_numero(tr)) / 2)
    clasificaciones['DUALTASK_inestable_negativo_o_muy_inestable'] = diff >= 2 and promedio <= 0
    clasificaciones['DUALTASK_inestable_mejor_T1_y_T2_positivo'] = diff >= 1 and t1 > t2 and t2 >= 0
    clasificaciones['DUALTASK_inestable_mejor_T1_y_T2_negativo'] = diff >= 1 and t1 > t2 and t2 < 0
    clasificaciones['DUALTASK_inestable_mejor_T2_y_T1_positivo'] = diff >= 1 and t2 > t1 and t1 >= 0
    clasificaciones['DUALTASK_inestable_mejor_T2_y_T1_negativo'] = diff >= 1 and t2 > t1 and t1 < 0
    clasificaciones['DUALTASK_concurrencia_peorT1_malT2'] = diff_conc is not None and diff_conc > 2 and (t2_mal_p or t2_mal_tr)
    clasificaciones['DUALTASK_PSV_bajo'] = psv == 'bajo'


def obtener_puntuaciones(resultados):
    """
    Calcula PT provisionales, clasificaciones y condiciones derivadas.
    """
    clasificaciones = {}

    for test in resultados.get('report_tests', []):
        for indice in test['indices']:
            key = indice['key']
            pd_value = indice['pd']
            baremo = BAREMOS_PROVISIONALES.get(key)
            pt = pd_a_percentil_provisional(pd_value, key)
            if pt is None:
                pt = pd_a_pt_provisional(pd_value, baremo)
            resultados[indice['pt_key']] = pt
            clasificaciones[key] = clasificar_pt(pt)

    for clave_pd, baremo_key in [
        ('PD_ANT_E', 'ANT_E'),
        ('PD_CPT_E', 'CPT_E'),
        ('PD_DUALTASK_A_cuando_concurrencia', 'DUALTASK_A_cuando_concurrencia'),
        ('PD_DUALTASK_TR_cuando_concurrencia', 'DUALTASK_TR_cuando_concurrencia'),
    ]:
        if clave_pd in resultados:
            pt = pd_a_pt_provisional(
                resultados[clave_pd],
                BAREMOS_PROVISIONALES.get(baremo_key),
            )
            resultados[f'PT_{clave_pd[3:]}'] = pt
            clasificaciones[baremo_key] = clasificar_pt(pt)

    _clasificar_special_tr('ANT', resultados, clasificaciones)
    _clasificar_special_tr('FourFigures', resultados, clasificaciones)
    _clasificar_special_tr('DUALTASK', resultados, clasificaciones)
    _clasificar_ant_fatiga(resultados, clasificaciones)
    _clasificar_cpt_var(resultados, clasificaciones)
    _clasificar_cpt_diferencias(resultados, clasificaciones)
    _clasificar_omisiones(resultados, clasificaciones)
    _clasificar_digits_consistencia(resultados, clasificaciones)
    _clasificar_dualtask(resultados, clasificaciones)

    return clasificaciones
