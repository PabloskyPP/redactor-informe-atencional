"""
Módulo para leer datos del Excel de evaluación atencional y calcular PD.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import pandas as pd


ACS_ITEMS = {
    'foco': range(1, 7),
    'cambio': range(7, 13),
    'division': range(13, 21),
}

TEST_SLOTS = {
    'ACS': ('ACS',),
    'ANT': ('ANT',),
    'CPT': ('CPT', 'D2'),
    'FourFigures': ('FourFigures', 'FiveDigits'),
    'DUALTASK': ('Dual Task - Tracking', 'Dual Task - Responses'),
    'DigitsMemorization': ('Digits Memorization',),
}

DISPLAY_NAMES = {
    'ACS': 'ACS',
    'ANT': 'ANT',
    'CPT': 'CPT',
    'D2': 'D2',
    'FourFigures': 'Four Figures',
    'FiveDigits': 'FiveDigits',
    'DUALTASK': 'Dual Task',
    'Digits Memorization': 'Memorización de dígitos',
}


@dataclass(frozen=True)
class TestPresence:
    slot: str
    present: bool
    display_name: str
    sheet_names: Tuple[str, ...]


def _present_value(value):
    if pd.isna(value):
        return None
    return value


def _first_present(mapping: dict, *keys):
    for key in keys:
        if key in mapping and not pd.isna(mapping[key]) and str(mapping[key]).strip():
            return mapping[key]
    return None


def _safe_mean(series: pd.Series) -> Optional[float]:
    clean = pd.to_numeric(series, errors='coerce').dropna()
    if clean.empty:
        return None
    return float(clean.mean())


def _mean_bool(series: pd.Series) -> Optional[float]:
    clean = series.dropna()
    if clean.empty:
        return None
    return float(clean.astype(float).mean())


def _difference_or_none(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is None or b is None:
        return None
    return float(a - b)


def _split_first_last(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    if df.empty:
        return df, df
    chunk = max(1, len(df) // 3)
    chunk = min(chunk, max(1, len(df) // 2))
    return df.iloc[:chunk].copy(), df.iloc[-chunk:].copy()


def _ordered_trials(df: pd.DataFrame, preferred_column: str) -> pd.DataFrame:
    if preferred_column in df.columns:
        return df.sort_values(preferred_column).reset_index(drop=True)
    return df.reset_index(drop=True)


def _sort_by_available_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    usable = [column for column in columns if column in df.columns]
    if usable:
        return df.sort_values(usable).reset_index(drop=True)
    return df.reset_index(drop=True)


def _resolve_sheet_map(xl: pd.ExcelFile) -> Dict[str, str]:
    by_lower = {sheet.strip().lower(): sheet for sheet in xl.sheet_names}
    resolved = {}
    for expected in set(sum((list(v) for v in TEST_SLOTS.values()), [])) | {'info', 'PVR'}:
        match = by_lower.get(expected.strip().lower())
        if match:
            resolved[expected] = match
    return resolved


def _build_presence(sheet_map: Dict[str, str]) -> Dict[str, TestPresence]:
    presence: Dict[str, TestPresence] = {}

    presence['ACS'] = TestPresence(
        slot='ACS',
        present='ACS' in sheet_map,
        display_name=DISPLAY_NAMES['ACS'],
        sheet_names=(sheet_map['ACS'],) if 'ACS' in sheet_map else (),
    )
    presence['ANT'] = TestPresence(
        slot='ANT',
        present='ANT' in sheet_map,
        display_name=DISPLAY_NAMES['ANT'],
        sheet_names=(sheet_map['ANT'],) if 'ANT' in sheet_map else (),
    )

    cpt_name = sheet_map.get('CPT') or sheet_map.get('D2')
    presence['CPT'] = TestPresence(
        slot='CPT',
        present=bool(cpt_name),
        display_name=DISPLAY_NAMES.get(cpt_name, 'CPT') if cpt_name else 'CPT',
        sheet_names=(cpt_name,) if cpt_name else (),
    )

    ff_name = sheet_map.get('FourFigures') or sheet_map.get('FiveDigits')
    presence['FourFigures'] = TestPresence(
        slot='FourFigures',
        present=bool(ff_name),
        display_name=DISPLAY_NAMES.get(ff_name, 'Four Figures') if ff_name else 'Four Figures',
        sheet_names=(ff_name,) if ff_name else (),
    )

    tracking = sheet_map.get('Dual Task - Tracking')
    responses = sheet_map.get('Dual Task - Responses')
    presence['DUALTASK'] = TestPresence(
        slot='DUALTASK',
        present=bool(tracking and responses),
        display_name=DISPLAY_NAMES['DUALTASK'],
        sheet_names=tuple(name for name in (tracking, responses) if name),
    )

    digits = sheet_map.get('Digits Memorization')
    presence['DigitsMemorization'] = TestPresence(
        slot='DigitsMemorization',
        present=bool(digits),
        display_name=DISPLAY_NAMES.get(digits, 'Memorización de dígitos') if digits else 'Memorización de dígitos',
        sheet_names=(digits,) if digits else (),
    )
    return presence


def leer_datos_excel(ruta_archivo):
    """
    Lee las hojas relevantes del Excel real y detecta pruebas ausentes/sustitutivas.
    """
    xl = pd.ExcelFile(ruta_archivo)
    try:
        sheet_map = _resolve_sheet_map(xl)
        presence = _build_presence(sheet_map)

        info_sheet = sheet_map.get('info')
        if not info_sheet:
            raise KeyError("El Excel debe incluir la hoja 'info'")

        df_info = pd.read_excel(ruta_archivo, sheet_name=info_sheet)
        first_info = df_info.iloc[0].to_dict() if not df_info.empty else {}

        nombre_completo = _first_present(
            first_info,
            'name',
            'full_name',
            'nombre',
            'nombre_completo',
            'participant_name',
            'sub_num',
        )
        if nombre_completo is not None:
            nombre_completo = str(nombre_completo).strip()
        nombre = nombre_completo.split()[0] if nombre_completo else None

        datos = {
            'ruta_archivo': ruta_archivo,
            'sheet_names': list(xl.sheet_names),
            'sheet_map': sheet_map,
            'test_presence': presence,
            'available_tests': [slot for slot, state in presence.items() if state.present],
            'display_names': {slot: state.display_name for slot, state in presence.items()},
            'edad': _present_value(first_info.get('age')),
            'sub_num': _present_value(first_info.get('sub_num')),
            'nombre_completo': nombre_completo,
            'nombre': nombre,
            'fecha_aplicacion': _present_value(first_info.get('datetime')),
        }

        if presence['ACS'].present:
            datos['df_ACS'] = pd.read_excel(ruta_archivo, sheet_name=presence['ACS'].sheet_names[0])
        if presence['ANT'].present:
            datos['df_ANT'] = pd.read_excel(ruta_archivo, sheet_name=presence['ANT'].sheet_names[0])
        if presence['CPT'].present:
            datos['df_CPT'] = pd.read_excel(ruta_archivo, sheet_name=presence['CPT'].sheet_names[0])
        if presence['FourFigures'].present:
            datos['df_FourFigures'] = pd.read_excel(ruta_archivo, sheet_name=presence['FourFigures'].sheet_names[0])
        if presence['DigitsMemorization'].present:
            datos['df_DigitsMemorization'] = pd.read_excel(
                ruta_archivo,
                sheet_name=presence['DigitsMemorization'].sheet_names[0],
            )
        if presence['DUALTASK'].present:
            tracking, responses = presence['DUALTASK'].sheet_names
            datos['df_DUALTASK_tracking'] = pd.read_excel(ruta_archivo, sheet_name=tracking)
            datos['df_DUALTASK_responses'] = pd.read_excel(ruta_archivo, sheet_name=responses)
        return datos
    finally:
        xl.close()


def _suma_factor(df: pd.DataFrame, items: Iterable[int]) -> int:
    item_resp = dict(zip(df['numero_del_enunciado'], df['respuesta']))
    return int(sum(int(item_resp.get(i, 0) or 0) for i in items))


def _bool_yes(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({'yes', 'si', 'sí', 'true', '1'})


def _dual_task_is_target(series: pd.Series) -> pd.Series:
    values = series.astype(str).str.strip().str.lower()
    return values.isin({'target', 'target_red', 'red_target', 'objetivo', 'objetivo_rojo'})


def _registrar_resultado_prueba(
    resultados: dict,
    slot: str,
    display_name: str,
    indices: List[Tuple[str, str, Optional[float], Optional[str]]],
) -> None:
    resultados.setdefault('report_tests', []).append({
        'slot': slot,
        'display_name': display_name,
        'indices': [
            {'key': key, 'label': label, 'pd': value, 'pt_key': pt_key}
            for key, label, value, pt_key in indices
        ],
    })


def _calcular_acs(resultados: dict, datos: dict) -> None:
    df_acs = datos['df_ACS'].copy()
    resultados['PD_ACS_atenciongeneral'] = int(pd.to_numeric(df_acs['respuesta'], errors='coerce').fillna(0).sum())
    resultados['PD_ACS_foco'] = _suma_factor(df_acs, ACS_ITEMS['foco'])
    resultados['PD_ACS_cambio'] = _suma_factor(df_acs, ACS_ITEMS['cambio'])
    resultados['PD_ACS_division'] = _suma_factor(df_acs, ACS_ITEMS['division'])

    _registrar_resultado_prueba(
        resultados,
        'ACS',
        datos['display_names']['ACS'],
        [
            ('ACS_atenciongeneral', 'Atención general', resultados['PD_ACS_atenciongeneral'], 'PT_ACS_atenciongeneral'),
            ('ACS_foco', 'Foco', resultados['PD_ACS_foco'], 'PT_ACS_foco'),
            ('ACS_cambio', 'Cambio', resultados['PD_ACS_cambio'], 'PT_ACS_cambio'),
        ],
    )


def _calcular_ant(resultados: dict, datos: dict) -> None:
    df = datos['df_ANT'].copy()
    responded = df['response'].notna() & df['response'].astype(str).str.strip().ne('')
    correct = pd.to_numeric(df['correct'], errors='coerce').fillna(0).astype(int).eq(1)
    rt = pd.to_numeric(df['RT'], errors='coerce')

    resultados['PD_ANT_A'] = int(correct.sum())
    resultados['PD_ANT_O'] = int((~responded).sum())
    resultados['PD_ANT_C'] = int((responded & ~correct).sum())
    resultados['PD_ANT_E'] = resultados['PD_ANT_O'] + resultados['PD_ANT_C']
    resultados['PD_ANT_TR'] = _safe_mean(rt[responded])

    resultados['PD_ANT_TR_CvsA'] = _difference_or_none(
        _safe_mean(rt[responded & ~correct]),
        _safe_mean(rt[correct]),
    )
    resultados['PD_ANT_TR_alerta'] = _difference_or_none(
        _safe_mean(rt[df['cue'].astype(str).str.lower() == 'double']),
        _safe_mean(rt[df['cue'].astype(str).str.lower() == 'nocue']),
    )
    resultados['PD_ANT_TR_orientacion'] = _difference_or_none(
        _safe_mean(rt[df['cue'].astype(str).str.lower() == 'center']),
        _safe_mean(rt[df['cue'].astype(str).str.lower() == 'spatial']),
    )
    resultados['PD_ANT_TR_ejecutivo'] = _difference_or_none(
        _safe_mean(rt[df['congruency'].astype(str).str.lower() == 'incongruent']),
        _safe_mean(rt[df['congruency'].astype(str).str.lower() == 'congruent']),
    )

    first, last = _split_first_last(_ordered_trials(df, 'trial'))
    first_correct = _mean_bool(pd.to_numeric(first['correct'], errors='coerce').fillna(0).astype(int).eq(1))
    last_correct = _mean_bool(pd.to_numeric(last['correct'], errors='coerce').fillna(0).astype(int).eq(1))
    resultados['PD_ANT_A_principio_vs_final'] = _difference_or_none(first_correct, last_correct)
    resultados['PD_ANT_TR_principio_vs_final'] = _difference_or_none(
        _safe_mean(pd.to_numeric(last['RT'], errors='coerce')),
        _safe_mean(pd.to_numeric(first['RT'], errors='coerce')),
    )

    _registrar_resultado_prueba(
        resultados,
        'ANT',
        datos['display_names']['ANT'],
        [
            ('ANT_A', 'A', resultados['PD_ANT_A'], 'PT_ANT_A'),
            ('ANT_C', 'C', resultados['PD_ANT_C'], 'PT_ANT_C'),
            ('ANT_O', 'O', resultados['PD_ANT_O'], 'PT_ANT_O'),
            ('ANT_TR', 'TR', resultados['PD_ANT_TR'], 'PT_ANT_TR'),
            ('ANT_TR_alerta', 'Red alerta', resultados['PD_ANT_TR_alerta'], 'PT_ANT_TR_alerta'),
            ('ANT_TR_orientacion', 'Red orientación', resultados['PD_ANT_TR_orientacion'], 'PT_ANT_TR_orientacion'),
            ('ANT_TR_ejecutivo', 'Red control ejecutivo', resultados['PD_ANT_TR_ejecutivo'], 'PT_ANT_TR_ejecutivo'),
        ],
    )


def _calcular_cpt(resultados: dict, datos: dict) -> None:
    df = datos['df_CPT'].copy()
    selected = df['selected'].fillna(False).astype(bool)
    target = df['target'].astype(str).str.strip().str.lower().isin({'si', 'sí', 'yes', 'true', '1'})
    timestamp = pd.to_numeric(df.get('timestamp'), errors='coerce').fillna(0)

    tr_por_fila = []
    ta_por_fila = []
    o_por_fila = []
    c_por_fila = []
    con_por_fila = []

    for _, group in df.sort_values(['row', 'letter_num']).groupby('row'):
        attempted = group.loc[selected.loc[group.index] | timestamp.loc[group.index].gt(0), 'letter_num']
        tr_row = int(attempted.max()) if not attempted.empty else 0
        ta_row = int((target.loc[group.index] & selected.loc[group.index]).sum())
        o_row = int((target.loc[group.index] & ~selected.loc[group.index]).sum())
        c_row = int((~target.loc[group.index] & selected.loc[group.index]).sum())
        con_row = ta_row - c_row

        tr_por_fila.append(tr_row)
        ta_por_fila.append(ta_row)
        o_por_fila.append(o_row)
        c_por_fila.append(c_row)
        con_por_fila.append(con_row)

    resultados['TR_por_fila'] = tr_por_fila
    resultados['TA_por_fila'] = ta_por_fila
    resultados['O_por_fila'] = o_por_fila
    resultados['C_por_fila'] = c_por_fila
    resultados['TR_total'] = int(sum(tr_por_fila))
    resultados['TA_total'] = int(sum(ta_por_fila))
    resultados['O_total'] = int(sum(o_por_fila))
    resultados['C_total'] = int(sum(c_por_fila))
    resultados['E_total'] = resultados['O_total'] + resultados['C_total']
    resultados['TOT'] = resultados['TR_total'] - resultados['E_total']
    resultados['CON'] = resultados['TA_total'] - resultados['C_total']
    resultados['TR_max'] = int(max(tr_por_fila)) if tr_por_fila else 0
    resultados['TR_min'] = int(min(tr_por_fila)) if tr_por_fila else 0
    resultados['VAR'] = resultados['TR_max'] - resultados['TR_min']

    resultados['PD_CPT_TR'] = resultados['TR_total']
    resultados['PD_CPT_A'] = resultados['TA_total']
    resultados['PD_CPT_O'] = resultados['O_total']
    resultados['PD_CPT_C'] = resultados['C_total']
    resultados['PD_CPT_E'] = resultados['E_total']
    resultados['PD_CPT_TOT'] = resultados['TOT']
    resultados['PD_CPT_CON'] = resultados['CON']
    resultados['PD_CPT_VAR'] = resultados['VAR']
    resultados['PD_CPT_R'] = resultados['TA_total']
    resultados['PD_CPT_CON_principio_vs_final'] = (
        float(sum(con_por_fila[:4]) / len(con_por_fila[:4])) - float(sum(con_por_fila[-4:]) / len(con_por_fila[-4:]))
        if len(con_por_fila) >= 4 else None
    )

    resultados['celdas_seleccionadas'] = {
        'seleccionadas': [
            (int(row), int(letter))
            for row, letter in df.loc[selected, ['row', 'letter_num']].itertuples(index=False, name=None)
        ]
    }
    resultados['datos_d2'] = df

    _registrar_resultado_prueba(
        resultados,
        'CPT',
        datos['display_names']['CPT'],
        [
            ('CPT_CON', 'CON', resultados['PD_CPT_CON'], 'PT_CPT_CON'),
            ('CPT_VAR', 'VAR', resultados['PD_CPT_VAR'], 'PT_CPT_VAR'),
            ('CPT_O', 'O', resultados['PD_CPT_O'], 'PT_CPT_O'),
            ('CPT_C', 'C', resultados['PD_CPT_C'], 'PT_CPT_C'),
            ('CPT_TR', 'Elementos procesados', resultados['PD_CPT_TR'], 'PT_CPT_TR'),
            ('CPT_TOT', 'TOT', resultados['PD_CPT_TOT'], 'PT_CPT_TOT'),
        ],
    )


def _calcular_four_figures(resultados: dict, datos: dict) -> None:
    df = datos['df_FourFigures'].copy()
    experimental = df[df['trial_type'].astype(str).str.lower() == 'experimental'].copy()
    correct = _bool_yes(experimental['correct'])
    responded = experimental['response_given'].notna() & experimental['response_given'].astype(str).str.strip().ne('')
    discrepancy = experimental['discrepancy'].astype(str).str.lower().isin({'yes', 'si', 'sí', 'true'})
    tr = pd.to_numeric(experimental['TR'], errors='coerce')

    resultados['PD_FourFigures_A'] = int(correct.sum())
    resultados['PD_FourFigures_O'] = int((~responded).sum())
    resultados['PD_FourFigures_C'] = int((responded & ~correct).sum())
    resultados['PD_FourFigures_E'] = resultados['PD_FourFigures_O'] + resultados['PD_FourFigures_C']
    resultados['PD_FourFigures_TR'] = _safe_mean(tr)
    resultados['PD_FourFigures_TR_CvsA'] = _difference_or_none(_safe_mean(tr[~correct]), _safe_mean(tr[correct]))
    resultados['PD_FourFigures_Red_control_ejecutivo'] = _difference_or_none(
        _safe_mean(tr[discrepancy]),
        _safe_mean(tr[~discrepancy]),
    )
    resultados['PD_FourFigures_Dif_A_congruencia_vs_discrepancia'] = _difference_or_none(
        _mean_bool(correct[~discrepancy]),
        _mean_bool(correct[discrepancy]),
    )

    part_accuracy = {}
    for part, group in experimental.groupby('part'):
        part_accuracy[int(part)] = _mean_bool(_bool_yes(group['correct']))
    expected_p4 = None
    if 2 in part_accuracy and 3 in part_accuracy:
        expected_p4 = (part_accuracy[2] + part_accuracy[3]) / 2
    resultados['PD_FourFigures_P4_A_obtenido_vs_esperado'] = _difference_or_none(
        part_accuracy.get(4),
        expected_p4,
    )

    _registrar_resultado_prueba(
        resultados,
        'FourFigures',
        datos['display_names']['FourFigures'],
        [
            ('FourFigures_A', 'A', resultados['PD_FourFigures_A'], 'PT_FourFigures_A'),
            ('FourFigures_C', 'C', resultados['PD_FourFigures_C'], 'PT_FourFigures_C'),
            ('FourFigures_TR', 'TR', resultados['PD_FourFigures_TR'], 'PT_FourFigures_TR'),
            (
                'FourFigures_P4_A_obtenido_vs_esperado',
                'P4 real vs esperada',
                resultados['PD_FourFigures_P4_A_obtenido_vs_esperado'],
                'PT_FourFigures_P4_A_obtenido_vs_esperado',
            ),
        ],
    )


def _calcular_digits(resultados: dict, datos: dict) -> None:
    row = datos['df_DigitsMemorization'].iloc[0].to_dict()
    directo = int(row.get('forward_span') or 0)
    inverso = int(row.get('backward_span') or 0)
    creciente = int(row.get('ascending_span') or 0)

    resultados['PD_DigitsMemorization_directo'] = directo
    resultados['PD_DigitsMemorization_inverso'] = inverso
    resultados['PD_DigitsMemorization_creciente'] = creciente
    resultados['PD_DigitsMemorization_total'] = directo + inverso + creciente
    resultados['PD_DigitsMemorization_promedio'] = (directo + inverso + creciente) / 3

    _registrar_resultado_prueba(
        resultados,
        'DigitsMemorization',
        datos['display_names']['DigitsMemorization'],
        [
            ('DigitsMemorization_directo', 'Directo', directo, 'PT_DigitsMemorization_directo'),
            ('DigitsMemorization_inverso', 'Inverso', inverso, 'PT_DigitsMemorization_inverso'),
            ('DigitsMemorization_creciente', 'Creciente', creciente, 'PT_DigitsMemorization_creciente'),
            ('DigitsMemorization_promedio', 'Promedio', resultados['PD_DigitsMemorization_promedio'], 'PT_DigitsMemorization_promedio'),
        ],
    )


def _calcular_dualtask(resultados: dict, datos: dict) -> None:
    responses = _sort_by_available_columns(datos['df_DUALTASK_responses'].copy(), ['stimulus', 'stimulus_time_s'])
    tracking = _sort_by_available_columns(datos['df_DUALTASK_tracking'].copy(), ['time_s', 'stimulus'])

    is_target = _dual_task_is_target(responses['stimulus_type'])
    responded = responses['responded'].fillna(False).astype(bool)
    latency = pd.to_numeric(responses['latency_s'], errors='coerce')

    def _correct_target_mask(df_resp: pd.DataFrame) -> pd.Series:
        target_mask = _dual_task_is_target(df_resp['stimulus_type'])
        if 'correct' in df_resp.columns:
            return target_mask & _bool_yes(df_resp['correct'])
        return target_mask & df_resp['responded'].fillna(False).astype(bool)

    correct_target = _correct_target_mask(responses)
    resultados['PD_DUALTASK_A'] = int(correct_target.sum())
    resultados['PD_DUALTASK_O'] = int((is_target & ~responded).sum())
    resultados['PD_DUALTASK_C'] = int((~is_target & responded).sum())
    resultados['PD_DUALTASK_E'] = resultados['PD_DUALTASK_O'] + resultados['PD_DUALTASK_C']
    resultados['PD_DUALTASK_TR'] = _safe_mean(latency[correct_target])
    resultados['PD_DUALTASK_TR_A_vs_C'] = _difference_or_none(
        _safe_mean(latency[correct_target]),
        _safe_mean(latency[~is_target & responded]),
    )

    dist = pd.to_numeric(tracking['distance_px'], errors='coerce')
    concurrent = tracking['measurement_phase'].astype(str).str.lower().eq('concurrent')
    resultados['PD_DUALTASK_PSV'] = _safe_mean(dist)
    resultados['PD_DUALTASK_PSV_cuando_concurrencia'] = _difference_or_none(
        _safe_mean(dist[concurrent]),
        _safe_mean(dist[~concurrent]),
    )

    tracking_first, tracking_last = _split_first_last(tracking)
    resp_first, resp_last = _split_first_last(responses)
    resultados['PD_DUALTASK_PSV_principio_vs_final'] = _difference_or_none(
        _safe_mean(pd.to_numeric(tracking_last['distance_px'], errors='coerce')),
        _safe_mean(pd.to_numeric(tracking_first['distance_px'], errors='coerce')),
    )

    def _target_accuracy(df_resp: pd.DataFrame) -> Optional[float]:
        targets = df_resp[_dual_task_is_target(df_resp['stimulus_type'])]
        if targets.empty:
            return None
        if 'correct' in targets.columns:
            return float(_bool_yes(targets['correct']).mean())
        return float(targets['responded'].fillna(False).astype(bool).mean())

    resultados['PD_DUALTASK_A_principio_vs_final'] = _difference_or_none(
        _target_accuracy(resp_first),
        _target_accuracy(resp_last),
    )
    resultados['PD_DUALTASK_TR_principio_vs_final'] = _difference_or_none(
        _safe_mean(pd.to_numeric(resp_last.loc[resp_last['responded'] == True, 'latency_s'], errors='coerce')),
        _safe_mean(pd.to_numeric(resp_first.loc[resp_first['responded'] == True, 'latency_s'], errors='coerce')),
    )

    concurrent_targets = responses.loc[responses['stimulus'].isin(tracking.loc[concurrent, 'stimulus'].unique())]
    concurrent_target_resp = concurrent_targets[_dual_task_is_target(concurrent_targets['stimulus_type'])]
    resultados['PD_DUALTASK_A_cuando_concurrencia'] = _target_accuracy(concurrent_target_resp)
    resultados['PD_DUALTASK_TR_cuando_concurrencia'] = _safe_mean(
        pd.to_numeric(concurrent_target_resp.loc[_correct_target_mask(concurrent_target_resp), 'latency_s'], errors='coerce')
    )

    _registrar_resultado_prueba(
        resultados,
        'DUALTASK',
        datos['display_names']['DUALTASK'],
        [
            ('DUALTASK_PSV', 'PSV', resultados['PD_DUALTASK_PSV'], 'PT_DUALTASK_PSV'),
            ('DUALTASK_A', 'A', resultados['PD_DUALTASK_A'], 'PT_DUALTASK_A'),
            ('DUALTASK_C', 'C', resultados['PD_DUALTASK_C'], 'PT_DUALTASK_C'),
            ('DUALTASK_O', 'O', resultados['PD_DUALTASK_O'], 'PT_DUALTASK_O'),
            ('DUALTASK_TR', 'TR', resultados['PD_DUALTASK_TR'], 'PT_DUALTASK_TR'),
        ],
    )


def calcular_puntuaciones_directas(datos):
    """
    Calcula las puntuaciones directas de las pruebas disponibles.
    """
    resultados = {
        'edad': datos['edad'],
        'sub_num': datos.get('sub_num'),
        'nombre_completo': datos.get('nombre_completo'),
        'nombre': datos.get('nombre'),
        'fecha_aplicacion': datos.get('fecha_aplicacion'),
        'sheet_names': datos.get('sheet_names', []),
        'display_names': datos.get('display_names', {}),
        'available_tests': datos.get('available_tests', []),
        'test_presence': datos.get('test_presence', {}),
        'report_tests': [],
    }

    if 'df_ACS' in datos:
        _calcular_acs(resultados, datos)
    if 'df_ANT' in datos:
        _calcular_ant(resultados, datos)
    if 'df_CPT' in datos:
        _calcular_cpt(resultados, datos)
    if 'df_FourFigures' in datos:
        _calcular_four_figures(resultados, datos)
    if 'df_DigitsMemorization' in datos:
        _calcular_digits(resultados, datos)
    if 'df_DUALTASK_tracking' in datos and 'df_DUALTASK_responses' in datos:
        _calcular_dualtask(resultados, datos)

    return resultados


def obtener_resumen_indices(resultados):
    lineas = [
        "=" * 70,
        "RESUMEN — Puntuaciones Directas",
        "=" * 70,
    ]
    for test in resultados.get('report_tests', []):
        lineas.append("")
        lineas.append(test['display_name'])
        for indice in test['indices']:
            lineas.append(f"  {indice['label']}: {indice['pd']}")
    return "\n".join(lineas)
