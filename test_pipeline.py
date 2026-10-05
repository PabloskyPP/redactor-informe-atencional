import os
import tempfile
import unittest
from datetime import datetime

import pandas as pd
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from PIL import Image
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

from generador_docx import agregar_portada, crear_informe_docx, guardar_informe
from generador_imagen_final import generar_imagen_final
from generador_pdf import generar_pdf_desde_docx
from lector_datos import calcular_puntuaciones_directas, leer_datos_excel
from reglas_psicometricas import (
    _clasificar_ant_fatiga,
    _clasificar_cpt_var,
    _clasificar_dualtask,
    obtener_puntuaciones,
)
from textos import (
    PARRAFO_ANT_F,
    PARRAFO_CPT_TR,
    PARRAFO_CPT_VAR,
    PARRAFO_DigitsMemorization_consistencia,
    PARRAFO_DUALTASK_General_PSV_y_A,
    PARRAFO_DUALTASK_Fatiga,
    PARRAFO_DUALTASK_automatización,
    PARRAFO_DUALTASK_estilo_atencional_cuando_concurrencia,
    PARRAFO_DUALTASK_si_inestable,
    PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK,
    PARRAFO_FourFigures_C,
)


REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_XLSX = os.path.join(REPO_DIR, 'excel ejemplo.xlsx')


class PipelineTests(unittest.TestCase):
    @staticmethod
    def _count_pdf_pages(path):
        return len(PdfReader(path).pages)

    @staticmethod
    def _pdf_has_xobject(path):
        reader = PdfReader(path)
        for page in reader.pages:
            resources = page.get('/Resources')
            if resources and resources.get('/XObject'):
                return True
        return False

    def test_sample_workbook_end_to_end(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)
        clasificaciones = obtener_puntuaciones(resultados)

        self.assertIn('ACS', resultados['available_tests'])
        self.assertIn('CPT', resultados['available_tests'])
        self.assertIn('PT_ANT_A', resultados)
        self.assertIn('CPT_VAR_condicion', clasificaciones)
        self.assertIn('DUALTASK_PSV_cuando_concurrencia', clasificaciones)
        for indice in ('PSV', 'A', 'TR'):
            self.assertIn(f'P_DUALTASK_{indice}_principio_vs_final', resultados)

        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_docx = os.path.join(tmpdir, 'informe.docx')
            ruta_pdf = os.path.join(tmpdir, 'informe.pdf')
            doc = crear_informe_docx(resultados, clasificaciones, resultados['nombre_completo'], REPO_DIR)
            guardar_informe(doc, ruta_docx)
            self.assertTrue(os.path.exists(ruta_docx))
            self.assertTrue(generar_pdf_desde_docx(ruta_docx, ruta_pdf, verbose=False))
            self.assertTrue(os.path.exists(ruta_pdf))

    def test_parts_table_centering_is_scoped_to_four_figures_variants(self):
        for display_name in ('FourFigures', 'NamingNumbers'):
            with self.subTest(display_name=display_name):
                doc = crear_informe_docx(
                    {
                        'available_tests': ['FourFigures', 'DigitsMemorization'],
                        'display_names': {'FourFigures': display_name},
                    },
                    {},
                    'caso',
                )
                parts_table = next(
                    table for table in doc.tables
                    if len(table.rows) == 5
                    and len(table.columns) == 2
                    and table.cell(0, 1).text == 'Puntuación obtenida'
                )
                for row in parts_table.rows:
                    for cell in row.cells:
                        self.assertEqual(
                            cell.vertical_alignment,
                            WD_CELL_VERTICAL_ALIGNMENT.CENTER,
                        )
                        for paragraph in cell.paragraphs:
                            self.assertEqual(
                                paragraph.alignment,
                                WD_PARAGRAPH_ALIGNMENT.CENTER,
                            )

                digits_table = next(
                    table for table in doc.tables
                    if table.cell(0, 1).text == 'Filas acertadas'
                )
                self.assertNotEqual(
                    digits_table.cell(1, 0).paragraphs[0].alignment,
                    WD_PARAGRAPH_ALIGNMENT.CENTER,
                )
                self.assertNotEqual(
                    digits_table.cell(1, 0).vertical_alignment,
                    WD_CELL_VERTICAL_ALIGNMENT.CENTER,
                )

    def test_sintesis_incluye_indices_completos_y_temporales_por_signo(self):
        resultados = {
            'available_tests': [],
            'display_names': {'FourFigures': 'NamingNumbers'},
            'PD_ANT_A_principio_vs_final': 0.2,
            'PD_ANT_TR_principio_vs_final': 25,
            'PD_CPT_TOT_principio_vs_final': -5,
            'PD_DUALTASK_PSV_principio_vs_final': 3,
            'P_DUALTASK_PSV_principio_vs_final': 0.01,
            'PD_DUALTASK_A_principio_vs_final': -0.2,
            'P_DUALTASK_A_principio_vs_final': 0.01,
            'PD_DUALTASK_TR_principio_vs_final': -0.3,
            'P_DUALTASK_TR_principio_vs_final': 0.01,
        }
        clasificaciones = {
            'ANT_TR_alerta': 'alto',
            'CPT_TOT': 'bajo',
            'DUALTASK_O': 'bajo',
            'DUALTASK_PSV': 'bajo',
            'DUALTASK_A': 'alto',
            'FourFigures_A': 'alto',
            'CPT_VAR': 'normal',
            'ANT_TR_ejecutivo': 'bajo',
            'ANT_TR_orientacion': 'alto',
            'ANT_C': 'bajo',
            'CPT_C': 'bajo',
            'CPT_O': 'bajo',
            'DUALTASK_C': 'alto',
            'FourFigures_C': 'bajo',
            'ANT_TR': 'bajo',
            'ANT_O': 'alto',
            'CPT_N': 'bajo',
            'DUALTASK_TR': 'bajo',
            'FourFigures_TR': 'alto',
        }

        doc = crear_informe_docx(resultados, clasificaciones, 'caso')
        parrafos_doc = [paragraph.text for paragraph in doc.paragraphs]
        texto_doc = '\n'.join(parrafos_doc)

        for etiqueta in (
            'ANT - Red de alerta',
            'CPT - TOT',
            'DUALTASK - omisiones',
            'DUALTASK - seguimiento visomotor',
            'NamingNumbers - precisión',
            'DUALTASK - aciertos',
            'ANT - fatiga en la precisión',
            'ANT - automatización en la velocidad',
            'CPT - automatización',
            'DUALTASK - fatiga en el seguimiento visomotor',
            'DUALTASK - automatización en la precisión',
            'DUALTASK - fatiga en la velocidad',
            'ANT - red ejecutiva',
            'ANT - red orientación',
            'ANT - comisiones',
            'CPT - comisiones',
            'CPT - omisiones',
            'DUALTASK - comisiones',
            'NamingNumbers - comisiones',
            'ANT - omisiones',
            'CPT - elementos procesados',
            'DUALTASK - tiempo de respuesta',
            'NamingNumbers - tiempo de respuesta',
        ):
            with self.subTest(etiqueta=etiqueta):
                self.assertIn(etiqueta, texto_doc)

        self.assertNotIn('DUALTASK - automatización en la velocidad', texto_doc)
        self.assertIn('El siguiente aspecto a revisar es el de la atención sostenida', texto_doc)
        parrafos_sintesis = [
            texto for texto in parrafos_doc
            if texto.startswith((
                'Primeramente, en cuestión de arousal',
                'El siguiente aspecto a revisar es el de atención sostenida',
                'Con respecto al control ejecutivo',
                'Seguidamente está el aspecto de la flexibilidad cognitiva',
                'Otro aspecto a mencionar es el de la memoria de trabajo',
                'Finalmente, en relación a la velocidad de procesamiento',
            ))
        ]
        self.assertEqual(len(parrafos_sintesis), 6)

    def test_detecta_pruebas_sustitutivas_y_ausentes(self):
        info = pd.DataFrame([{
            'datetime': '2026-01-01 10:00',
            'sub_num': 'Caso Sustituto',
            'age': 10,
        }])
        d2 = pd.DataFrame([
            {'row': 1, 'letter_num': 1, 'selected': True, 'timestamp': 100, 'target': 'si'},
            {'row': 1, 'letter_num': 2, 'selected': False, 'timestamp': 0, 'target': 'no'},
        ])
        naming_numbers = pd.DataFrame([
            {
                'part': 1, 'trial_type': 'experimental', 'contour': '0', 'content': '0',
                'discrepancy': 'no', 'response_given': '0', 'correct_response': '1',
                'correct': 'no', 'TR': 900,
            },
            {
                'part': 2, 'trial_type': 'experimental', 'contour': '1', 'content': '1',
                'discrepancy': 'no', 'response_given': '1', 'correct_response': '1',
                'correct': 'yes', 'TR': 1000,
            },
            {
                'part': 3, 'trial_type': 'experimental', 'contour': '2', 'content': '2',
                'discrepancy': 'no', 'response_given': '2', 'correct_response': '2',
                'correct': 'yes', 'TR': 1100,
            },
            {
                'part': 4, 'trial_type': 'experimental', 'contour': '3', 'content': '3',
                'discrepancy': 'yes', 'response_given': '3', 'correct_response': '3',
                'correct': 'yes', 'TR': 1200,
            },
        ])

        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_xlsx = os.path.join(tmpdir, 'sustituto.xlsx')
            with pd.ExcelWriter(ruta_xlsx) as writer:
                info.to_excel(writer, sheet_name='info', index=False)
                d2.to_excel(writer, sheet_name='D2', index=False)
                naming_numbers.to_excel(writer, sheet_name='NamingNumbers', index=False)

            datos = leer_datos_excel(ruta_xlsx)
            self.assertEqual(datos['display_names']['CPT'], 'D2')
            self.assertEqual(datos['display_names']['FourFigures'], 'NamingNumbers')
            self.assertFalse(datos['test_presence']['DUALTASK'].present)

            resultados = calcular_puntuaciones_directas(datos)
            clasificaciones = obtener_puntuaciones(resultados)
            doc = crear_informe_docx(resultados, clasificaciones, 'Caso Sustituto', REPO_DIR)
            texto = "\n".join(p.text for p in doc.paragraphs)
            self.assertIn('D2 - prueba de rendimiento continuo', texto)
            self.assertIn('Naming Numbers - prueba de control y flexibilidad cognitiva', texto)
            self.assertNotIn('Dual Task - prueba multitarea de atención dividida', texto)
            tabla_partes = next(
                table for table in doc.tables
                if table.rows[0].cells[0].text == 'Parte'
            )
            self.assertEqual(
                [cell.text for cell in tabla_partes.rows[0].cells],
                ['Parte', 'Puntuación obtenida'],
            )
            self.assertEqual(
                [[cell.text for cell in row.cells] for row in tabla_partes.rows[1:]],
                [['1', '0 / 1'], ['2', '1 / 1'], ['3', '1 / 1'], ['4', '1 / 1']],
            )
            self.assertTrue(all(
                run.bold
                for cell in tabla_partes.rows[0].cells
                for run in cell.paragraphs[0].runs
            ))
            for row in tabla_partes.rows[1:]:
                self.assertTrue(row.cells[0].paragraphs[0].runs[0].bold)
                self.assertEqual(
                    row.cells[0].paragraphs[0].alignment,
                    1,
                )

    def test_tabla_y_pt_provisional_se_generan(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)
        clasificaciones = obtener_puntuaciones(resultados)
        doc = crear_informe_docx(resultados, clasificaciones, resultados['nombre_completo'], REPO_DIR)
        self.assertGreaterEqual(len(doc.tables), 1)
        table_text = "\n".join(cell.text for row in doc.tables[0].rows for cell in row.cells)
        self.assertIn('Disponible', table_text)
        self.assertIn('PT', table_text)
        self.assertIsInstance(resultados['PT_DUALTASK_A'], int)

    def test_digits_memorization_table_uses_trial_rows(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)
        clasificaciones = obtener_puntuaciones(resultados)
        doc = crear_informe_docx(resultados, clasificaciones, 'caso')

        tabla_digitos = next(
            table for table in doc.tables
            if table.rows[0].cells[0].text == 'Parte'
        )
        self.assertEqual(
            [cell.text for cell in tabla_digitos.rows[0].cells],
            ['Parte', 'Filas acertadas', 'Extensión máxima recordada'],
        )
        self.assertEqual(
            [[cell.text for cell in row.cells] for row in tabla_digitos.rows[1:]],
            [
                ['1. Recuerdo directo', '1 / 4', '2'],
                ['2. Recuerdo inverso', '5 / 7', '4'],
                ['3. Recuerdo tras cálculo', '2 / 4', '2'],
            ],
        )
        self.assertEqual(
            resultados['PD_DigitsMemorization_directo_errores_antes_ultimas_dos'],
            1,
        )
        self.assertEqual(clasificaciones['Digits_Memorization_consistencia'], 'normal')
        self.assertIn(
            PARRAFO_DigitsMemorization_consistencia['normal'].format(nombre='caso'),
            [paragraph.text for paragraph in doc.paragraphs],
        )

    def test_digits_memorization_consistency_thresholds(self):
        escenarios = ((0, 'alto'), (1, 'normal'), (2, 'normal'), (3, 'bajo'))
        for errores, esperado in escenarios:
            with self.subTest(errores=errores):
                clasificaciones = obtener_puntuaciones({
                    'report_tests': [],
                    'PD_DigitsMemorization_directo_errores_antes_ultimas_dos': errores,
                })
                self.assertEqual(
                    clasificaciones['Digits_Memorization_consistencia'],
                    esperado,
                )

    def test_dualtask_general_paragraphs_are_added_in_order(self):
        clasificaciones = {
            'DUALTASK_PSV': 'normal',
            'DUALTASK_A': 'alto',
            'DUALTASK_Rendimiento_General_cuando_concurrencia': 'alto',
            'DUALTASK_PSV_cuando_concurrencia': 'no deterioro y buen T2',
        }

        doc = crear_informe_docx({'available_tests': ['DUALTASK']}, clasificaciones, 'caso')
        parrafos = [paragraph.text for paragraph in doc.paragraphs]
        esperados = [
            PARRAFO_DUALTASK_General_PSV_y_A['PSV normal y T2 P alto'].format(nombre='caso'),
            PARRAFO_DUALTASK_si_inestable['PSV normal o bajo y T2 P alto'].format(nombre='caso'),
            PARRAFO_DUALTASK_estilo_atencional_cuando_concurrencia[
                'no deterioro y T2 P y TR normal o alto'
            ].format(nombre='caso'),
        ]

        posiciones = [parrafos.index(texto) for texto in esperados]
        self.assertEqual(posiciones, sorted(posiciones))

    def test_dualtask_concurrence_paragraph_covers_all_conditions(self):
        directions = (
            (3, 'deterioro'),
            (0, 'no deterioro'),
            (-3, 'mejora'),
        )
        t2_levels = (
            ('normal', 'normal'),
            ('alto', 'normal'),
            ('normal', 'alto'),
            ('alto', 'alto'),
            ('bajo', 'normal'),
            ('normal', 'bajo'),
            ('bajo', 'bajo'),
        )
        for diferencia, direccion in directions:
            for nivel_a, nivel_tr in t2_levels:
                clasificaciones = {
                    'DUALTASK_PSV': 'normal',
                    'DUALTASK_A': nivel_a,
                    'DUALTASK_TR': nivel_tr,
                    'DUALTASK_C': 'normal',
                    'DUALTASK_O': 'normal',
                }
                _clasificar_dualtask(
                    {'PD_DUALTASK_PSV_cuando_concurrencia': diferencia},
                    clasificaciones,
                )
                if nivel_a == 'bajo' and nivel_tr == 'bajo':
                    condicion_t2 = 'mal T2 P y TR'
                    sufijo_texto = 'P y TR bajo'
                elif nivel_a == 'bajo':
                    condicion_t2 = 'mal T2 P'
                    sufijo_texto = 'P bajo'
                elif nivel_tr == 'bajo':
                    condicion_t2 = 'mal T2 TR'
                    sufijo_texto = 'TR bajo'
                else:
                    condicion_t2 = 'buen T2'
                    sufijo_texto = (
                        'normal o alto'
                        if direccion == 'deterioro'
                        else 'P y TR normal o alto'
                    )
                clave_clasificacion = f'{direccion} y {condicion_t2}'
                clave_texto = (
                    f'{direccion} y T2 {sufijo_texto}'
                    if condicion_t2 != 'buen T2' or direccion != 'deterioro'
                    else 'deterioro y T2 normal o alto'
                )

                with self.subTest(
                    diferencia=diferencia,
                    nivel_a=nivel_a,
                    nivel_tr=nivel_tr,
                ):
                    self.assertEqual(
                        clasificaciones['DUALTASK_PSV_cuando_concurrencia'],
                        clave_clasificacion,
                    )
                    doc = crear_informe_docx(
                        {'available_tests': ['DUALTASK']}, clasificaciones, 'caso'
                    )
                    self.assertIn(
                        PARRAFO_DUALTASK_estilo_atencional_cuando_concurrencia[
                            clave_texto
                        ].format(nombre='caso'),
                        [paragraph.text for paragraph in doc.paragraphs],
                    )

    def test_dualtask_skips_optional_paragraphs_without_matching_conditions(self):
        clasificaciones = {'DUALTASK_PSV': 'normal', 'DUALTASK_A': 'normal'}
        doc = crear_informe_docx({'available_tests': ['DUALTASK']}, clasificaciones, 'caso')
        parrafos = [paragraph.text for paragraph in doc.paragraphs]

        self.assertIn(
            PARRAFO_DUALTASK_General_PSV_y_A['PSV normal y T2 P normal'],
            parrafos,
        )
        self.assertFalse(any(text.startswith('Se señala un desbalance') for text in parrafos))
        self.assertFalse(any(text.startswith('Respecto a la memoria de trabajo') for text in parrafos))
        self.assertFalse(any(text.startswith('Por otro lado, en estos momentos') for text in parrafos))
        self.assertNotIn('🔹 Recomendaciones', parrafos)
        self.assertNotIn(
            PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK['intro'].format(nombre='caso'),
            parrafos,
        )

    # Comprueba dirección, significación y texto DOCX de fatiga/automatización.
    def test_dualtask_fatigue_and_automation_directions_match_text_keys(self):
        scenarios = (
            ('PSV', 0.5, 'F PSV', 'Automatización PSV', True),
            ('A', 0.01, 'F A', 'Automatización P', True),
            ('TR', 0.001, 'F TR', 'Automatización TR', False),
        )
        result_key = {
            'PSV': 'PD_DUALTASK_PSV_principio_vs_final',
            'A': 'PD_DUALTASK_A_principio_vs_final',
            'TR': 'PD_DUALTASK_TR_principio_vs_final',
        }
        pvalue_key = {
            indice: f'P_DUALTASK_{indice}_principio_vs_final'
            for indice, _, _, _, _ in scenarios
        }
        fatigue_text_key = {
            'PSV': 'F PSV',
            'A': 'F A',
            'TR': 'F TR',
        }
        automation_text_key = {
            'PSV': 'Automatización PSV',
            'A': 'Automatización P',
            'TR': 'Automatización TR',
        }

        for indice, umbral, clave_fatiga, clave_auto, positivo_es_fatiga in scenarios:
            cambios = (
                (umbral, clave_fatiga if positivo_es_fatiga else clave_auto),
                (-umbral, clave_auto if positivo_es_fatiga else clave_fatiga),
            )
            for diferencia, esperado in cambios:
                with self.subTest(indice=indice, diferencia=diferencia):
                    resultados = {
                        result_key[indice]: diferencia,
                        pvalue_key[indice]: 0.01,
                    }
                    clasificaciones = {
                        'DUALTASK_PSV': 'normal',
                        'DUALTASK_A': 'normal',
                        'DUALTASK_C': 'normal',
                        'DUALTASK_O': 'normal',
                        'DUALTASK_TR': 'normal',
                    }
                    _clasificar_dualtask(resultados, clasificaciones)

                    es_fatiga = (diferencia > 0) == positivo_es_fatiga
                    if es_fatiga:
                        self.assertEqual(clasificaciones['DUALTASK_Fatiga'], esperado)
                        diccionario = PARRAFO_DUALTASK_Fatiga
                        clave_texto = fatigue_text_key[indice]
                    else:
                        self.assertEqual(clasificaciones['DUALTASK_automatización'], esperado)
                        diccionario = PARRAFO_DUALTASK_automatización
                        clave_texto = automation_text_key[indice]

                    doc = crear_informe_docx(
                        {'available_tests': ['DUALTASK']}, clasificaciones, 'caso'
                    )
                    self.assertIn(
                        diccionario[clave_texto].format(nombre='caso'),
                        [paragraph.text for paragraph in doc.paragraphs],
                    )

    def test_dualtask_nonsignificant_change_is_not_fatigue_or_automation(self):
        resultados = {
            'PD_DUALTASK_PSV_principio_vs_final': 10,
            'P_DUALTASK_PSV_principio_vs_final': 0.05,
            'PD_DUALTASK_A_principio_vs_final': -1,
            'P_DUALTASK_A_principio_vs_final': 0.2,
            'PD_DUALTASK_TR_principio_vs_final': 1,
            'P_DUALTASK_TR_principio_vs_final': None,
        }
        clasificaciones = {
            'DUALTASK_PSV': 'normal',
            'DUALTASK_A': 'normal',
            'DUALTASK_C': 'normal',
            'DUALTASK_O': 'normal',
            'DUALTASK_TR': 'normal',
        }

        _clasificar_dualtask(resultados, clasificaciones)

        self.assertEqual(clasificaciones['DUALTASK_Fatiga'], 'no F')
        self.assertIsNone(clasificaciones['DUALTASK_automatización'])

    def test_cpt_var_selecciona_parrafo_segun_con(self):
        for clave_parrafo, texto_esperado in PARRAFO_CPT_VAR.items():
            var_nivel, condicion_esperada = clave_parrafo[:2]
            tot_nivel = (
                'bajo' if len(clave_parrafo) == 3 and clave_parrafo[2] == 'TOT bajo'
                else 'normal'
            )
            diferencia = {
                'nada': 0,
                'fatiga': 5,
                'automatismo': -5,
                'dificultadinicial': -5,
            }[condicion_esperada]
            clasificaciones = {'CPT_TOT': tot_nivel, 'CPT_VAR': var_nivel}
            _clasificar_cpt_var(
                {'PD_CPT_TOT_principio_vs_final': diferencia},
                clasificaciones,
            )
            with self.subTest(clave_parrafo=clave_parrafo):
                self.assertEqual(clasificaciones['CPT_VAR_condicion'], condicion_esperada)

                doc = crear_informe_docx(
                    {'available_tests': ['CPT']},
                    clasificaciones,
                )
                texto_esperado = texto_esperado.format(nombre='caso')
                self.assertIn(texto_esperado, [paragraph.text for paragraph in doc.paragraphs])

    def test_cpt_var_uses_per_series_tot_standard_deviation_and_change(self):
    def test_cpt_tr_totals_and_var_use_attempted_row_extents(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)

        tr_por_fila = resultados['TR_por_fila']
        tot_por_fila = [
            tr - omisiones - comisiones
            for tr, omisiones, comisiones in zip(
                tr_por_fila,
                resultados['O_por_fila'],
                resultados['C_por_fila'],
            )
        ]
        self.assertEqual(len(tot_por_fila), 14)
        self.assertEqual(resultados['TOT_por_fila'], tot_por_fila)
        self.assertEqual(resultados['TR_total'], sum(tr_por_fila))
        self.assertEqual(resultados['PD_CPT_N'], resultados['TR_total'])
        self.assertEqual(resultados['CPT_TR_max'], max(tr_por_fila))
        self.assertEqual(resultados['CPT_TR_min'], min(tr_por_fila))
        self.assertEqual(
            resultados['VAR'],
            resultados['CPT_TR_max'] - resultados['CPT_TR_min'],
        )
        self.assertEqual(resultados['PD_CPT_VAR'], resultados['VAR'])
        self.assertAlmostEqual(
            resultados['PD_CPT_TOT_principio_vs_final'],
            sum(tot_por_fila[:4]) / 4 - sum(tot_por_fila[-4:]) / 4,
        )

    def test_cpt_var_uses_tot_difference_and_tot_level(self):
        cases = (
            (5, 'normal', 'fatiga'),
            (4.99, 'normal', 'nada'),
            (-5, 'alto', 'automatismo'),
            (-5, 'bajo', 'dificultadinicial'),
            (-5, 'N/D', 'nada'),
        )
        for difference, tot_level, expected in cases:
            classifications = {'CPT_TOT': tot_level}
            _clasificar_cpt_var(
                {'PD_CPT_TOT_principio_vs_final': difference},
                classifications,
            )
            with self.subTest(difference=difference, tot_level=tot_level):
                self.assertEqual(classifications['CPT_VAR_condicion'], expected)

    def test_cpt_errores_totales_se_clasifican_desde_omisiones_y_comisiones(self):
        for errores, expected in ((5, 'alto'), (8, 'normal'), (11, 'bajo')):
            with self.subTest(errores=errores):
                clasificaciones = obtener_puntuaciones({
                    'report_tests': [],
                    'PD_CPT_E': errores,
                })
                self.assertEqual(clasificaciones['CPT_E'], expected)

    def test_cpt_rendimiento_general_usa_elementos_procesados_y_errores_totales(self):
        escenarios = (
            ('alto', 'alto', 'alto y E alto o normal'),
            ('alto', 'normal', 'alto y E bajo'),
            ('normal', 'bajo', 'normal'),
            ('bajo', 'alto', 'bajo y E normal o alto'),
            ('bajo', 'bajo', 'bajo y E bajo'),
        )

        for nivel_n, nivel_e, clave_texto in escenarios:
            with self.subTest(nivel_n=nivel_n, nivel_e=nivel_e):
                doc = crear_informe_docx(
                    {'available_tests': ['CPT']},
                    {'CPT_N': nivel_n, 'CPT_E': nivel_e},
                    'caso',
                )
                self.assertIn(
                    PARRAFO_CPT_TR[clave_texto].format(nombre='caso'),
                    [paragraph.text for paragraph in doc.paragraphs],
                )

    def test_cpt_rendimiento_general_uses_classified_processed_elements(self):
        resultados = {
            'available_tests': ['CPT'],
            'report_tests': [{
                'indices': [{
                    'key': 'CPT_N',
                    'pd': 350,
                    'pt_key': 'PT_CPT_N',
                }],
            }],
            'PD_CPT_E': 11,
        }
        clasificaciones = obtener_puntuaciones(resultados)

        self.assertEqual(resultados['PT_CPT_N'], 100)
        self.assertEqual(clasificaciones['CPT_N'], 'alto')
        self.assertEqual(clasificaciones['CPT_E'], 'bajo')

        doc = crear_informe_docx(resultados, clasificaciones, 'caso')

        self.assertIn(
            PARRAFO_CPT_TR['alto y E bajo'].format(nombre='caso'),
            [paragraph.text for paragraph in doc.paragraphs],
        )

    def test_fourfigures_commission_paragraph_uses_existing_c_tr_keys(self):
        escenarios = (
            ('alto', 'bajo', 'C alto y TR bajo'),
            ('alto', 'normal', 'C alto y TR bajo o normal'),
            ('alto', 'alto', 'C alto y TR bajo o normal'),
            ('normal', 'alto', 'C normal'),
            ('bajo', 'alto', 'C bajo y TR alto'),
            ('bajo', 'normal', 'C bajo y TR normal o bajo'),
            ('bajo', 'bajo', 'C bajo y TR normal o bajo'),
        )

        for nivel_c, nivel_tr, clave_texto in escenarios:
            with self.subTest(nivel_c=nivel_c, nivel_tr=nivel_tr):
                doc = crear_informe_docx(
                    {'available_tests': ['FourFigures']},
                    {
                        'FourFigures_A': 'normal',
                        'FourFigures_C': nivel_c,
                        'FourFigures_TR': nivel_tr,
                    },
                    'caso',
                )
                self.assertIn(
                    PARRAFO_FourFigures_C[clave_texto].format(nombre='caso'),
                    [paragraph.text for paragraph in doc.paragraphs],
                )

    def test_ant_fatiga_resuelve_clave_con_sufijo_de_tr(self):
        clasificaciones = {'ANT_TR': 'normal'}
        _clasificar_ant_fatiga(
            {
                'PD_ANT_A_principio_vs_final': 1,
                'PD_ANT_TR_principio_vs_final': 0,
            },
            clasificaciones,
        )

        doc = crear_informe_docx({'available_tests': ['ANT']}, clasificaciones)

        self.assertEqual(
            clasificaciones['ANT_F_texto'],
            'F_A positivo y F_TR no sign y TR bajo o normal',
        )
        self.assertIn(
            PARRAFO_ANT_F['F_A positivo y F_TR no sign'].format(nombre='caso'),
            [paragraph.text for paragraph in doc.paragraphs],
        )

    def test_pdf_export_con_imagen_y_ruta_sin_directorio(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)
        clasificaciones = obtener_puntuaciones(resultados)

        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_docx = os.path.join(tmpdir, 'con_imagen.docx')
            ruta_docx_sin = os.path.join(tmpdir, 'sin_imagen.docx')
            guardar_informe(
                crear_informe_docx(resultados, clasificaciones, resultados['nombre_completo'], tmpdir),
                ruta_docx_sin,
            )
            self.assertTrue(generar_pdf_desde_docx(ruta_docx_sin, os.path.join(tmpdir, 'sin_imagen.pdf'), verbose=False))

            ruta_imagen = os.path.join(tmpdir, 'grafico_CPT_final.png')
            self.assertTrue(generar_imagen_final(
                resultados,
                resultados['datos_d2'],
                os.path.join(REPO_DIR, 'imagenes', 'grafico_CPT.png'),
                ruta_imagen,
            ))
            guardar_informe(
                crear_informe_docx(resultados, clasificaciones, resultados['nombre_completo'], tmpdir),
                ruta_docx,
            )

            cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                self.assertTrue(generar_pdf_desde_docx(ruta_docx, 'solo_nombre.pdf', verbose=False))
                self.assertTrue(os.path.exists(os.path.join(tmpdir, 'solo_nombre.pdf')))
                self.assertFalse(self._pdf_has_xobject(os.path.join(tmpdir, 'sin_imagen.pdf')))
                self.assertTrue(self._pdf_has_xobject(os.path.join(tmpdir, 'solo_nombre.pdf')))
                paginas = PdfReader(os.path.join(tmpdir, 'solo_nombre.pdf')).pages
                pagina_cpt = next(
                    indice for indice, pagina in enumerate(paginas)
                    if 'CPT - prueba de rendimiento continuo'
                    in ' '.join((pagina.extract_text() or '').split())
                )
                self.assertTrue(
                    paginas[pagina_cpt + 1].get('/Resources', {}).get('/XObject')
                )
            finally:
                os.chdir(cwd)

    def test_formato_fecha_aplicacion_en_portada(self):
        doc = Document()
        agregar_portada(doc, 'Ana García', {'edad': 36, 'fecha_aplicacion': datetime(2024, 3, 5, 14, 30)})
        texto = '\n'.join(p.text for p in doc.paragraphs)
        self.assertIn('Fecha de aplicación: 05/03/2024 14:30', texto)
        self.assertNotIn('2024-03-05 14:30', texto)

    def test_leyenda_rendimiento_en_tabla(self):
        datos = leer_datos_excel(SAMPLE_XLSX)
        resultados = calcular_puntuaciones_directas(datos)
        clasificaciones = obtener_puntuaciones(resultados)

        doc = crear_informe_docx(resultados, clasificaciones, resultados['nombre_completo'], REPO_DIR)
        textos = '\n'.join(p.text for p in doc.paragraphs)
        self.assertIn('Rendimiento deficiente', textos)
        self.assertIn('Rendimiento excelente', textos)
        self.assertTrue(textos.count('■') >= 2)

    def test_pdf_inserta_grafico_cpt_despues_de_pagina_con_titulo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_original = os.path.join(tmpdir, 'original.pdf')
            ruta_imagen = os.path.join(tmpdir, 'grafico_CPT_final.png')
            ruta_final = os.path.join(tmpdir, 'final.pdf')

            pdf = canvas.Canvas(ruta_original, pagesize=(595, 842))
            for indice in range(12):
                texto = (
                    'CPT - prueba de rendimiento continuo'
                    if indice == 5 else f'PAGINA ORIGINAL {indice + 1}'
                )
                pdf.drawString(72, 760, texto)
                pdf.showPage()
            pdf.save()

            Image.new('RGB', (20, 20), 'white').save(ruta_imagen)

            from generador_pdf import insertar_imagen_en_pagina_3
            self.assertTrue(insertar_imagen_en_pagina_3(ruta_original, ruta_imagen, ruta_final))

            paginas = PdfReader(ruta_final).pages
            self.assertEqual(len(paginas), 13)
            self.assertIn('CPT - prueba de rendimiento continuo', paginas[5].extract_text())
            self.assertTrue(
                paginas[6].get('/Resources') and paginas[6].get('/Resources').get('/XObject')
            )
            self.assertIn('PAGINA ORIGINAL 7', paginas[7].extract_text())

    def test_pdf_preserva_orden_basico_de_parrafos_y_tablas(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_docx = os.path.join(tmpdir, 'orden.docx')
            ruta_pdf = os.path.join(tmpdir, 'orden.pdf')

            doc = Document()
            doc.add_paragraph('PRIMERO')
            table = doc.add_table(rows=1, cols=2)
            table.rows[0].cells[0].text = 'TABLA_A'
            table.rows[0].cells[1].text = 'TABLA_B'
            doc.add_paragraph('ULTIMO')
            guardar_informe(doc, ruta_docx)

            self.assertTrue(generar_pdf_desde_docx(ruta_docx, ruta_pdf, verbose=False))
            texto = "\n".join((page.extract_text() or '') for page in PdfReader(ruta_pdf).pages)
            self.assertLess(texto.index('PRIMERO'), texto.index('TABLA_A'))
            self.assertLess(texto.index('TABLA_B'), texto.index('ULTIMO'))


if __name__ == '__main__':
    unittest.main()
