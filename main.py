"""
Programa principal para generar informe atencional.
"""
import sys
import os
import traceback
from lector_datos import leer_datos_excel, calcular_puntuaciones_directas
from reglas_psicometricas import obtener_puntuaciones
from generador_imagen_final import generar_desde_resultados
from generador_docx import crear_informe_docx, guardar_informe
from generador_pdf import generar_pdf_desde_docx


def main():
    """
    Función principal que ejecuta todo el proceso de generación del informe.
    """
    # ------------------------------------------------------------------ #
    # Configuración                                                        #
    # ------------------------------------------------------------------ #
    RUTA_EXCEL = os.environ.get(
        'RUTA_EXCEL',
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Paco Fiestas-ANT, CPT, DUAL-TASK, FourFigures.xlsx')
    )
    script_dir       = os.path.dirname(os.path.abspath(__file__))
    carpeta_informes = os.path.join(script_dir, "informes_generados")
    os.makedirs(carpeta_informes, exist_ok=True)

    carpeta_pdf = os.path.join(os.path.expanduser("~"), "Desktop",
                               "Informes ConCiencia", "Atencional")
    os.makedirs(carpeta_pdf, exist_ok=True)

    print("=" * 70)
    print("GENERADOR DE INFORME ATENCIONAL")
    print("=" * 70)
    print()
    print(f"Archivo Excel:      {RUTA_EXCEL}")
    print(f"Carpeta informes:   {carpeta_informes}")
    print(f"Carpeta PDF:        {carpeta_pdf}")
    print()

    # ------------------------------------------------------------------ #
    # Paso 1: Leer datos del Excel                                         #
    # ------------------------------------------------------------------ #
    print("Paso 1: Leyendo datos del archivo Excel...")
    try:
        datos = leer_datos_excel(RUTA_EXCEL)
        print(f"    Edad del evaluado: {datos.get('edad')} años")
        if datos.get('nombre_completo'):
            print(f"    Nombre completo:   {datos['nombre_completo']}")
        print("    Datos cargados correctamente")
    except Exception as e:
        print(f"   X Error al leer el archivo: {e}")
        sys.exit(1)

    print()

    nombre_caso  = datos.get('nombre_completo') or 'Informe'
    nombre_base  = "Informe_ATENCIONAL"
    RUTA_SALIDA_DOCX = os.path.join(carpeta_informes,
                                    f"{nombre_base}_{nombre_caso}.docx")
    RUTA_SALIDA_PDF  = os.path.join(carpeta_pdf,
                                    f"{nombre_base}_{nombre_caso}.pdf")

    # ------------------------------------------------------------------ #
    # Paso 2: Calcular puntuaciones directas                               #
    # ------------------------------------------------------------------ #
    print("Paso 2: Calculando puntuaciones directas...")
    try:
        resultados = calcular_puntuaciones_directas(datos)
        for factor in ('R', 'I', 'A', 'S', 'E', 'C'):
            print(f"    PD_{factor}: {resultados.get(f'PD_{factor}')}")
    except Exception as e:
        print(f"   X Error al calcular puntuaciones: {e}")
        sys.exit(1)

    print()

    # ------------------------------------------------------------------ #
    # Paso 3: Aplicar reglas psicométricas (porcentajes, clasificaciones) #
    # ------------------------------------------------------------------ #
    print("Paso 3: Calculando porcentajes y clasificaciones...")
    try:
        clasificaciones = obtener_puntuaciones(resultados)
        top3_r  = resultados.get('top3_riasec', [])
        top3_im = resultados.get('top3_inteligencia_multiple', [])
        print(f"    PD_ANT  {ANT_PD}")
        print(f"    PD_CPT   {CPT_PD}")
        print(f"    PD_DUAL-TASK  {DUALTASK_PD}")
        print(f"    PD_FourFigures      {FourFigures_PD}")

    except Exception as e:
        print(f"   X Error al calcular clasificaciones: {e}")
        sys.exit(1)

    print()

    # ------------------------------------------------------------------ #
    # Paso 4: Generar gráfico CPT                                      #
    # ------------------------------------------------------------------ #
    print("Paso 4: Generando gráfico CPT...")
    try:
        ok = generar_desde_resultados(resultados, script_dir)
        if ok:
            print("    Gráfico CPT generado correctamente")
        else:
            print("    Advertencia: gráfico Ikigai no generado (se omitirá en el DOCX)")
    except Exception as e:
        print(f"    Advertencia: {e}")

    print()

    # ------------------------------------------------------------------ #
    # Paso 5: Generar informe DOCX                                        #
    # ------------------------------------------------------------------ #
    print("Paso 5: Generando informe en formato Word...")
    try:
        documento = crear_informe_docx(resultados, clasificaciones,
                                       nombre_caso, script_dir)
        print("    Documento generado correctamente")
    except Exception as e:
        print(f"   X Error al generar el documento: {e}")
        traceback.print_exc()
        sys.exit(1)

    print()

    # ------------------------------------------------------------------ #
    # Paso 6: Guardar el informe Word                                     #
    # ------------------------------------------------------------------ #
    print("Paso 6: Guardando informe Word...")
    try:
        guardar_informe(documento, RUTA_SALIDA_DOCX)
        print(f"    Informe Word guardado en: {RUTA_SALIDA_DOCX}")
    except Exception as e:
        print(f"   X Error al guardar el informe Word: {e}")
        sys.exit(1)

    print()

    # ------------------------------------------------------------------ #
    # Paso 7: Generar PDF                                                 #
    # ------------------------------------------------------------------ #
    print("Paso 7: Generando informe en formato PDF...")
    try:
        resultado_pdf = generar_pdf_desde_docx(RUTA_SALIDA_DOCX,
                                               RUTA_SALIDA_PDF, verbose=False)
        if resultado_pdf:
            print(f"    Informe PDF generado en: {RUTA_SALIDA_PDF}")
        else:
            print("    El informe Word se generó correctamente, "
                  "pero la conversión a PDF no está disponible en este sistema.")
    except Exception as e:
        print(f"    Advertencia PDF: {e}")
        print("    El informe Word está disponible y es el resultado principal.")

    print()
    print("=" * 70)
    print("PROCESO COMPLETADO")
    print("=" * 70)
    print()
    print(f"Informe Word: {RUTA_SALIDA_DOCX}")
    if os.path.exists(RUTA_SALIDA_PDF):
        print(f"Informe PDF:  {RUTA_SALIDA_PDF}")


if __name__ == "__main__":
    main()
