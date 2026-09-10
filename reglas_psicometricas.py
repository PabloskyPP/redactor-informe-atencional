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
    'ANT_TR_alerta': BaremoProvisional(-50, 250, invertir=True),
    'ANT_TR_orientacion': BaremoProvisional(-50, 250, invertir=True),
    'ANT_TR_ejecutivo': BaremoProvisional(0, 350, invertir=True),
    'CPT_CON': BaremoProvisional(-50, 100),
    'CPT_VAR': BaremoProvisional(0, 50, invertir=True),
    'CPT_O': BaremoProvisional(0, 120, invertir=True),
    'CPT_C': BaremoProvisional(0, 120, invertir=True),
    'CPT_TR': BaremoProvisional(0, 658),
    'CPT_TOT': BaremoProvisional(-50, 658),
    'FourFigures_A': BaremoProvisional(0, 128),
    'FourFigures_C': BaremoProvisional(0, 32, invertir=True),
    'FourFigures_TR': BaremoProvisional(500, 3500, invertir=True),
    'FourFigures_P4_A_obtenido_vs_esperado': BaremoProvisional(-1, 1),
    'DigitsMemorization_directo': BaremoProvisional(0, 12),
    'DigitsMemorization_inverso': BaremoProvisional(0, 12),
    'DigitsMemorization_creciente': BaremoProvisional(0, 12),
    'DigitsMemorization_promedio': BaremoProvisional(0, 12),
    'DUALTASK_PSV': BaremoProvisional(0, 30, invertir=True),
    'DUALTASK_A': BaremoProvisional(0, 12),
    'DUALTASK_C': BaremoProvisional(0, 12, invertir=True),
    'DUALTASK_O': BaremoProvisional(0, 12, invertir=True),
    'DUALTASK_TR': BaremoProvisional(0.2, 1.2, invertir=True),
    'DUALTASK_A_cuando_concurrencia': BaremoProvisional(0, 1),
    'DUALTASK_TR_cuando_concurrencia': BaremoProvisional(0.2, 1.2, invertir=True),
}


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
    clasificaciones['ANT_F_texto'] = f'F_A {a_nivel} y F_TR {tr_nivel}'


def _clasificar_cpt_var(resultados: dict, clasificaciones: dict) -> None:
    diff = resultados.get('PD_CPT_CON_principio_vs_final')
    if diff is None:
        clasificaciones['CPT_VAR_condicion'] = 'nada'
        return
    if diff >= 5:
        clasificaciones['CPT_VAR_condicion'] = 'fatiga'
    elif diff <= -5:
        clasificaciones['CPT_VAR_condicion'] = 'automatismo'
    else:
        clasificaciones['CPT_VAR_condicion'] = 'nada'


def _clasificar_dualtask(resultados: dict, clasificaciones: dict) -> None:
    psv = clasificaciones.get('DUALTASK_PSV', 'normal')
    a = clasificaciones.get('DUALTASK_A', 'normal')
    c = clasificaciones.get('DUALTASK_C', 'normal')
    o = clasificaciones.get('DUALTASK_O', 'normal')
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
    if diff_conc is not None and diff_conc > 2:
        if not t2_mal_p and not t2_mal_tr:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'deterioro y buen T2'
        elif t2_mal_p and t2_mal_tr:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'deterioro y mal T2 P y TR'
        elif t2_mal_p:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'deterioro y mal T2 P'
        else:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'deterioro y mal T2 TR'
    else:
        if not t2_mal_p and not t2_mal_tr:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'no deterioro y buen T2'
        elif t2_mal_p and t2_mal_tr:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'no deterioro y mal T2 P y TR'
        elif t2_mal_p:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'no deterioro y mal T2 P'
        else:
            clasificaciones['DUALTASK_PSV_cuando_concurrencia'] = 'no deterioro y mal T2 TR'

    avg_concurrent_pts = [
        resultados.get('PT_DUALTASK_A_cuando_concurrencia'),
        pd_a_pt_provisional(resultados.get('PD_DUALTASK_PSV_cuando_concurrencia'), BaremoProvisional(-10, 10, invertir=True)),
        resultados.get('PT_DUALTASK_TR'),
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

    fatiga_flags = []
    auto_flags = []
    psv_diff = resultados.get('PD_DUALTASK_PSV_principio_vs_final')
    if psv_diff is not None:
        if psv_diff >= 2:
            fatiga_flags.append('F_PSV')
        elif psv_diff <= -2:
            auto_flags.append('Automatización_PSV')
    a_diff = resultados.get('PD_DUALTASK_A_principio_vs_final')
    if a_diff is not None:
        if a_diff >= 0.1:
            fatiga_flags.append('F_A')
        elif a_diff <= -0.1:
            auto_flags.append('Automatización_P')
    tr_diff = resultados.get('PD_DUALTASK_TR_principio_vs_final')
    if tr_diff is not None:
        if tr_diff >= 0.05:
            fatiga_flags.append('F_TR')
        elif tr_diff <= -0.05:
            auto_flags.append('Automatización_TR')

    clasificaciones['DUALTASK_Fatiga'] = 'no F' if not fatiga_flags else ' y '.join(flag.replace('F_', 'F_') for flag in fatiga_flags)
    clasificaciones['DUALTASK_automatización'] = None if not auto_flags else '_y_'.join(auto_flags).replace('_y_', '_y_')

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
            pt = pd_a_pt_provisional(pd_value, baremo)
            resultados[indice['pt_key']] = pt
            clasificaciones[key] = clasificar_pt(pt)

    for clave_pd, baremo_key in [
        ('PD_ANT_E', 'ANT_E'),
        ('PD_DUALTASK_A_cuando_concurrencia', 'DUALTASK_A_cuando_concurrencia'),
        ('PD_DUALTASK_TR_cuando_concurrencia', 'DUALTASK_TR_cuando_concurrencia'),
    ]:
        if clave_pd in resultados:
            resultados[f'PT_{clave_pd[3:]}'] = pd_a_pt_provisional(resultados.get(clave_pd), BAREMOS_PROVISIONALES.get(baremo_key))

    _clasificar_special_tr('ANT', resultados, clasificaciones)
    _clasificar_special_tr('FourFigures', resultados, clasificaciones)
    _clasificar_special_tr('DUALTASK', resultados, clasificaciones)
    _clasificar_ant_fatiga(resultados, clasificaciones)
    _clasificar_cpt_var(resultados, clasificaciones)
    _clasificar_dualtask(resultados, clasificaciones)

    return clasificaciones
