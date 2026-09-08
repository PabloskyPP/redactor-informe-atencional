# Generador de Informe atencional

Este programa procesa los datos del cuestionario ACS y las pruebas conductuales ANT, CPT, FourFigures y DUAL-TASK, y genera un informe profesional en formato Word (.docx) y PDF.

## 📋 Requisitos

- Python 3.7 o superior
- Las siguientes bibliotecas de Python:
  - pandas
  - openpyxl
  - python-docx
  - Pillow

## 🚀 Instalación

Instalar las dependencias de Python:
```bash
pip install -r requirements.txt
```

Para generar informes en formato PDF en Windows se necesita también tener instalado Microsoft Word y el paquete `pywin32`:
```bash
pip install pywin32
```

## 📁 Estructura del Proyecto

```
proyecto_dual_task/
│
├── main.py                      # Programa principal
├── lector_datos.py              # Lee y procesa datos del Excel
├── reglas_psicometricas.py      # Conversión PD -> Clasificación
├── textos.py                    # Textos fijos y condicionales del informe
├── generador_imagen_final.py            # Genera la imagen CPT para el informe
├── generador_docx.py            # Genera el documento Word
├── generador_pdf.py             # Convierte Word a PDF (sólo Windows)
├── requirements.txt             # Dependencias del proyecto
├── Ejemplo.xlsx                 # Archivo de ejemplo
├── informes_generados/          # Carpeta para informes (ignorada en git)
└── README.md                    # Este archivo
```

## 📊 Formato del Archivo Excel

El archivo Excel debe tener al menos **5 hojas**: puedes revisar el formato en el documento GUIA_RAPIDA.txt



### Paso 1: Configurar la ruta del archivo

Editar el archivo `main.py` y modificar la variable `RUTA_EXCEL`:

```python
RUTA_EXCEL = r"C:\ruta\a\tu\archivo.xlsx"
```

### Paso 2: Ejecutar el programa

```bash
python main.py
```

El programa ejecutará automáticamente los siguientes pasos:
1. Leer datos del archivo Excel (hojas `info`, `ACS`, `ANT`, `CPT`, `DUAL-TASK`, `FourFIgures`)
2. Calcular puntuaciones directas (Precisión, Latencia de Respuesta, Posiciones del cursor, Índices Compuestos...)
3. Generar informe en formato Word con párrafos adaptativos
4. Guardar el informe Word en `informes_generados/`
5. Convertir a PDF (solo disponible en Windows con Microsoft Word)

## 📈 Puntuaciones Calculadas

### Cuestionario 1 - ACS

| Índice | Descripción |
|--------|-------------|
| **Atención en general** | Puntuación directa o total del cuestionario |
| **Foco atencional** | Puntuación directa o total del factor Foco Atencional |
| **Cambio atencional** | Puntuación directa o total del factor Cambio Atencional |

### Prueba 1 - ANT

| Índice | Descripción |
|--------|-------------|
| **A** | Puntuación directa del total de aciertos (accuracy) |
| **E** | Puntuación directa o total de errores (omisión + comisión) |
| **O** | Puntuación directa o total de errores de omisión. Sirve como índice de la Velocidad de Procesamiento.  |
| **C** | Puntuación directa o total de errores de comisión. Sirve de índice de Control Ejecutivo. |
| **TR** | Puntuación directa del tiempo o latencia de respuesta promedio. Sirve de índice de la Velocidad de Procesamiento  |
| **TR_CvsA** | Significativad diferencia TR promedio ante C frente A. Permíte distinguir si los errores de comisión (dificultades Control Ejecutivo) se deben a la Atención Discriminativa, dificultades para discriminar la info relevante vs distractora (diferencia positiva), o al Control Inhibitorio (diferencia negativa) |
| **Red_alerta** | Puntuación directa de la diferencia promedio (en milisegundos) en el tiempo de respuesta ante eventos en condición de doble asterisco menos los eventos en condición de ningún asterisco. Vinculado teóricamente a la eficiencia de la red de alerta, sirve de índice del grado de activación general o Arousal |
| **Red_orientación** | Puntuación directa de la diferencia promedio en el tiempo de respuesta ante eventos con pista espacial (aparición de un asterisco del lado que aparecerá la flecha) frente eventos sin pista espacial (aparición de un asterisco en el centro de la pantalla). Vinculado teóricamente a la eficiencia de la red de orientación. |
| **Red_control_ejecutivo** | Puntuación directa de la diferencia promedio en el tiempo de respuesta ante eventos con flechas adicionales distractoras (incongruentes) frente eventos con flechas adicionales facilitadoras (congruentes). Vinculado teóricamente a la eficiencia de la red de control ejecutivo.|
| **Fatiga** | Significatividad diferencia en Precisión y TR entre el primer primer vs tercer tercio de la prueba. Sirve como índice de Fatiga y de Atención Sostenida. También si diferencia negativa en Precisión y positiva en TR hablamos de prevalencia por un estilo reflexivo compensatorio ante el cansancio. Si Precisión positiva y TR negativa hablamos de prevalencia por un estilo impulsivo. |

### Prueba 2 - CPT

| Índice | Descripción |
|--------|-------------|
### Por cada fila (1-14):
- **TR**: Número del último elemento intentado en la fila. Sirve de índice de la Velocidad de Procesamiento 
- **TA**: Total de aciertos (targets marcados correctamente)
- **O**: Errores de omisión (targets no marcados). Sirve como índice de Atención Selectiva
- **C**: Errores de comisión (no-targets marcados incorrectamente). Sirve como índice de Control Ejecutivo (dimensión que engloba Atención Selectiva y Control Inhibitorio).
### Totales e índices compuestos:
- **TR_total**: Suma de TR de todas las filas. Sirve como índice de Velocidad de Procesamiento.
- **TA_total**: Suma de TA de todas las filas
- **O_total**: Suma de O de todas las filas. Sirve como índice Atención Selectiva, aunque otros autores proponen este como índice de Arousal.
- **C_total**: Suma de C de todas las filas. Sirve como índice de Control Inhibitorio
- **E_total**: Total de errores (O + C)
- **TOT**: TR_total - E_total
- **CON**: TA_total - C_total. Sirve como índice de Arousal.
- **TR_max**: TR más alto entre todas las filas
- **TR_min**: TR más bajo entre todas las filas
- **VAR**: Variabilidad (TR_max - TR_min). Sirve de índice de Atención Sostenida
| **Fatiga** | Significatividad diferencia en Precisión y TR entre el primer primer vs tercer tercio de la prueba. Si negativa en Precisión y positiva en TR hablamos de prevalencia por un estilo reflexivo compensatorio ante el cansancio. Si Precisión positiva y TR negativa hablamos de prevalencia por un estilo impulsivo. |

### Prueba 3 - FourFigures

| Índice | Descripción |
|--------|-------------|
| **A** | Puntuación directa del total de aciertos (accuracy). También calculada específicamente para cada parte del programa, p.ej. los A para P1 sirve como índice del Arousal o Grado de Activación.  |
| **E** | Puntuación directa o total de errores (omisión + comisión) |
| **TR** | Puntuación directa del tiempo o latencia de respuesta promedio. Sirve como índice de Velocidad de Procesamiento. También calculada específicamente para cada parte del programa, p.ej. los A para P1 sirve como índice del Arousal o Grado de Activación.  | |
| **TR_CvsA** | Significativad diferencia TR promedio ante C frente A. Permíte distinguir si los errores de comisión se deben a la atención discriminativa, dificultades para discriminar la info relevante vs distractora (diferencia positiva), o al control inhibitorio (diferencia negativa) |
| **Dif_A_congruencia_vs_discrepancia** | Puntuación típica de la diferencia de aciertos (precisión) en las partes P2 y P3 de la prueba ante estímulos congruentes vs discrepantes. Sirve para medir calidad Atención Selectiva.
| **Red_control_ejecutivo** | Puntuación directa de la diferencia promedio en el tiempo de respuesta ante eventos discrepantes (diferente forma figura interna y externa) frente eventos congruentes (misma forma). Vinculado teóricamente a la eficiencia de la red de control ejecutivo.|
| **Dif_P4_MitadInsideTargeted_vs_ MitadOutsideTargeted** | Significatividada de la diferencia de estas dos mitades de la parte P4 que junto el valor de otra prueba adicional PVR (percepción de verticalidad relativa) pueden informar sobre la prevalencia por una percepción más particular o global |
| **Dif_A_congruencia_vs_discrepancia** | Diferencia entre la puntuación obtenida en P4 y la esperada según baremos a partir de puntuación obtenida en P2 y P3. Sirve como índice de la Flexibilidad Cognitiva |
| **Movimiento_cursor** | Se pueden tomar múltiples medidas de posicionamiento del cursor a lo largo de la prueba para calcular el movimiento innecesario del ratón durante la prueba. Esto sirve de índice de Hiperactividad  |
| **Fatiga** | Significatividad diferencia en Precisión y TR entre el primer primer vs tercer tercio de P4 de la prueba. Sirve como índice de Fatiga y de Atención Sostenida. También si diferencia negativa en Precisión y positiva en TR hablamos de prevalencia por un estilo reflexivo compensatorio ante el cansancio. Si Precisión positiva y TR negativa hablamos de prevalencia por un estilo impulsivo. |

### Prueba 4 - Dual Task

| Índice | Descripción |
|--------|-------------|
| **A** | Puntuación directa del total de aciertos (Precisión) en la tarea 2 de la prueba |
| **E** | Puntuación directa o total de errores (omisión + comisión) en la tarea 2 de la prueba |
- **O**: Errores de omisión (targets no marcados). Sirve como índice de Arousal. |
- **C**: Errores de comisión (no-targets marcados incorrectamente). Sirve como índice de Control Ejecutivo (dimensión que engloba Atención Selectiva y Control Inhibitorio).
| **TR** | Puntuación directa del tiempo o latencia de respuesta promedio en la tarea 2 de la prueba. Sirve como índice de la Velocidad de Procesamiento |
| **TR_CvsA** | Significativad diferencia TR promedio ante C frente A. Permíte distinguir si los errores de comisión se deben a la atención discriminativa, dificultades para discriminar la info relevante vs distractora (diferencia positiva), o al control inhibitorio (diferencia negativa) |
| **PSV** | Precisión Seguimiento Visomotor. Medición del promedio de la distancia existente en varios momentos entre el cursor (ratón) y el objetivo a seguir en la pantalla durante la tarea 1 de la prueba. |
| **PSV_cuandoSimultaneidadTareas** | Diferencia significativa en la Precisión del Seguimiento Visomotor entre el rendimiento general en esta tarea 1, frente el rendimiento durante momentos de mayor demanda cognitiva por simultaneidad con la aparición de estímulos a responder en la T2. Si diferencia significativa cabe mirar a la TR. Si dif sign y rendimiento (A o TR) en T2 igual o mejor a los esperado se señala una prevalencia de un Estilo de Distribución de la Atención Intermitente. Si dif no sign y rendimiento (A o TR) en T2 igual o peor a los esperado se señala una prevalencia por un Estilo de Distribución de la Atención en Paralelo. Si aquí rendimiento T2 peor a lo esperado señalar déficit Memoria Opertativa |
| **Fatiga** | Significatividad diferencia en Precisión y TR entre el primer primer vs tercer tercio de la prueba. Sirve como índice de Fatiga y de Atención Sostenida. Además si negativa en Precisión y positiva en TR hablamos de prevalencia por un estilo reflexivo compensatorio ante el cansancio. Si Precisión positiva y TR negativa hablamos de prevalencia por un estilo impulsivo. |

### Prueba 4 - Digits memorization

| Índice | Descripción |
|--------|-------------|
| **PD_Total** | Puntuación directa o total de aciertos entre las tres partes de la prueba |
| **PD_Directo** | Puntuación directa o total de aciertos en la P1 de la prueba. Sirve de índice de la Memoria Inmediata. |
| **PD_Inverso** | Puntuación directa o total de aceirtos en la P2 de la prueba. Sirve como índice de Memoria Operativa?    |
| **PD_Creciente** | Puntuación directa o total de aceirtos en la P3 de la prueba. Es la parte de mayor complejidad cognitiva y por tanto se considera el más fiable índice de Memoria Operativa. ¿¿Establecer respecto baremos a través de una puntuación esperada en base a rendimiento en P1 y P2?? |



### Clasificación

Para los índices / factores del programa:
3. Clasifica la puntuación típica en: **bajo** (PD ≤ 30), **normal** (30 < PD < 70), **alto** (PD ≥ 70).

## 📄 Contenido del Informe

El informe incluye:

1. **Portada** — nombre, edad y fecha del informe.
2. **Objetivo de la prueba** — descripción del instrumento.
3. **Descripción de los cuestionarios** — procedimiento del cuestionario y las 4 pruebas conductuales.
4. **Índices obtenidos** — explicación de cada medida dimensión / factor evaluado.
5. **Tabla de resultados** — PD, PT, clasificación y valores de cada índice.
6. **Interpretación adaptativa** — párrafos condicionales, seleccionados automáticamente según el las respuestas dadas (el perfil del evaluado).
7. **Recomendaciones** — sugerencias de estudios o futuro trabajo individualizadas.


## 🐛 Solución de Problemas

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError` | Ejecutar `pip install -r requirements.txt` |
| `FileNotFoundError` | Verificar la ruta en `RUTA_EXCEL` en `main.py` |
| `KeyError: 'age'` | Verificar que la hoja `info` tiene la columna `age` |
| `KeyError: 'Dual Task - Responses'` | Verificar que el Excel tiene la hoja con ese nombre exacto |
| Error al convertir a PDF | El Word se genera igualmente; la conversión a PDF requiere Windows + Microsoft Word |

## 📞 Contacto

Para dudas o sugerencias sobre el programa, contactar al desarrollador.

