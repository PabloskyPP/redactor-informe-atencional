"""
Textos ejecutables extraídos/adaptados de `textos.py`.

El archivo original contiene anotaciones del desarrollador que se respetan como
fuente de verdad documental. Este módulo ofrece una versión estable para el
flujo de generación.
"""

PARRAFOS_FIJOS = {
    'titulo_general_prueba': "1. Objetivo de la batería de pruebas.",
    'objetivo_prueba': (
        "Este informe integra el cuestionario ACS y las pruebas conductuales "
        "disponibles en el Excel para describir diferentes componentes de la atención."
    ),
    'titulo_procedimiento': "2. Descripción de las tareas.",
    'descripcion_procedimiento0': (
        "La batería combina un cuestionario de autoinforme y pruebas conductuales "
        "de atención sostenida, selectiva, control ejecutivo, memoria operativa y "
        "velocidad de procesamiento."
    ),
    'descripcion_procedimiento1.1': (
        "En ACS la persona responde a 20 enunciados sobre control y regulación atencional."
    ),
    'descripcion_procedimiento2.1': (
        "En ANT se responde a la dirección de una flecha central ignorando información distractora."
    ),
    'descripcion_procedimiento2.2': (
        "La tarea ANT también manipula pistas previas y condiciones de congruencia para estimar redes atencionales."
    ),
    'descripcion_procedimiento3.1': (
        "En CPT o D2 la persona debe detectar el mayor número posible de objetivos evitando falsos positivos."
    ),
    'descripcion_procedimiento4.1': (
        "En FourFigures/FiveDigits se alternan reglas perceptivas que exigen control e incluso flexibilidad cognitiva."
    ),
    'descripcion_procedimiento5.1': (
        "En Dual Task se combinan una tarea de seguimiento visomotor y otra de respuesta rápida ante estímulos."
    ),
    'titulo_indices': "3. Índices que se obtienen.",
    'descripcion_indices': (
        "Se presentan PD, PT provisionales y una clasificación descriptiva. "
        "Las PT de este documento son una baremación provisional de trabajo y no baremos clínicos reales."
    ),
    'titulo_resultados': "Presentación de los resultados de {nombre_completo}",
    'texto_resultados': (
        "A continuación se muestran únicamente las pruebas realmente disponibles en el Excel analizado."
    ),
    'titulo_resultados_especificos': "Profundizando en cada prueba atencional",
    'titulo_ACS': "ACS - cuestionario de control atencional",
    'texto_resultados_ACS': "A través del cuestionario ACS, {nombre} afirma tener la siguiente capacidad atencional:",
    'titulo_ANT': "ANT - prueba de eficiencia de redes neuronales atencionales",
    'titulo_CPT': "CPT/D2 - prueba de rendimiento continuo",
    'titulo_FourFigures': "Four Figures / FiveDigits - prueba de control y flexibilidad cognitiva",
    'titulo_DigitsMemorization': "Memorización de dígitos - prueba de memoria operativa",
    'titulo_DualTask': "Dual Task - prueba multitarea de atención dividida",
    'introduccion_analisis_tareas_DualTask': "A continuación se comenta por separado el rendimiento de cada componente de la prueba.",
    'titulo_sintesis_final': "Síntesis final",
}

PARRAFO_ACS_atenciongeneral = {
    'bajo': "En general, la capacidad atencional autodeclarada es baja.",
    'normal': "En general, la capacidad atencional autodeclarada es adecuada.",
    'alto': "En general, la capacidad atencional autodeclarada es alta.",
}

PARRAFO_ACS_foco = {
    'bajo': "Se aprecian dificultades autodeclaradas en la concentración y el foco sostenido.",
    'normal': "La concentración autodeclarada se sitúa dentro de lo esperable.",
    'alto': "Se describe una muy buena capacidad de concentración voluntaria.",
}

PARRAFO_ACS_cambio = {
    'bajo': "También se describen dificultades para cambiar el foco entre tareas o estímulos.",
    'normal': "La capacidad para cambiar voluntariamente el foco parece adecuada.",
    'alto': "Se describe gran facilidad para alternar la atención entre tareas.",
}

PARRAFO_ANT_TR = {
    'TR bajo y C alto': "El tiempo de respuesta es rápido, aunque acompañado de errores de comisión elevados, lo que sugiere impulsividad.",
    'TR bajo y C bajo o normal': "El tiempo de respuesta es rápido y compatible con una buena velocidad de procesamiento.",
    'TR normal y C bajo': "El tiempo de respuesta es adecuado y además preciso, compatible con un estilo controlado y eficaz.",
    'TR normal y C normal o alto': "El tiempo de respuesta se sitúa dentro de valores esperables.",
    'TR alto': "El tiempo de respuesta es lento y puede reflejar enlentecimiento del procesamiento o un estilo más reflexivo.",
}

PARRAFO_ANT_A = {
    'bajo': "La precisión global en ANT es baja.",
    'normal': "La precisión global en ANT es adecuada.",
    'alto': "La precisión global en ANT es alta.",
}

PARRAFO_ANT_C = {
    'C bajo y TR bajo o normal': "Las comisiones son bajas, lo que indica buen control inhibitorio.",
    'C bajo y TR alto': "Las comisiones son bajas y, junto con la lentitud, sugieren un estilo reflexivo.",
    'C normal': "Las comisiones se sitúan dentro de rangos esperables.",
    'C alto y TR bajo': "Las comisiones son elevadas y, junto con la rapidez, apuntan a impulsividad.",
    'C alto y TR normal o alto': "Las comisiones son elevadas y no parecen explicarse sólo por rapidez.",
}

PARRAFO_ANT_O = {
    'bajo': "Las omisiones son bajas.",
    'normal': "Las omisiones se sitúan dentro de rangos esperables.",
    'alto': "Las omisiones son elevadas y pueden sugerir lentitud o fallos de atención sostenida.",
}

PARRAFO_ANT_F = {
    'F_A bajo y F_TR bajo': "El rendimiento mejora al final de ANT tanto en precisión como en velocidad.",
    'F_A bajo y F_TR normal': "La precisión mejora con estabilidad en la velocidad.",
    'F_A bajo y F_TR alto': "La precisión mejora, pero la velocidad se ralentiza al final de la tarea.",
    'F_A normal y F_TR bajo': "La precisión se mantiene y la velocidad mejora al final.",
    'F_A normal y F_TR normal': "No se aprecian cambios relevantes entre el inicio y el final.",
    'F_A normal y F_TR alto': "La precisión se mantiene, pero la velocidad empeora al final.",
    'F_A alto y F_TR bajo': "La velocidad mejora al final a costa de una peor precisión.",
    'F_A alto y F_TR normal': "La precisión empeora al final sin cambios claros de velocidad.",
    'F_A alto y F_TR alto': "Se observa un patrón compatible con fatiga al final de ANT.",
}

PARRAFO_ANT_alerta = {
    'bajo': "La red de alerta muestra una eficiencia superior.",
    'normal': "La red de alerta muestra una eficiencia esperable.",
    'alto': "La red de alerta muestra una eficiencia reducida.",
}

PARRAFO_ANT_orientacion = {
    'bajo': "La red de orientación muestra una eficiencia superior.",
    'normal': "La red de orientación muestra una eficiencia esperable.",
    'alto': "La red de orientación muestra una eficiencia reducida.",
}

PARRAFO_ANT_ejecutivo = {
    'bajo': "La red de control ejecutivo muestra una eficiencia superior.",
    'normal': "La red de control ejecutivo muestra una eficiencia esperable.",
    'alto': "La red de control ejecutivo muestra una eficiencia reducida.",
}

PARRAFO_CPT_TR = {
    'alto y E bajo o normal': "El número de elementos procesados es elevado y se mantiene una precisión razonable.",
    'alto y E alto': "Se procesan muchos elementos, pero con errores que reducen la calidad del rendimiento.",
    'normal': "La velocidad de exploración es adecuada.",
    'bajo y E normal o alto': "La velocidad de exploración es reducida y además aparece un coste en precisión.",
    'bajo y E bajo': "La velocidad es baja con pocos errores, compatible con un estilo más reflexivo.",
}

PARRAFO_CPT_O = {
    'bajo': "Los errores de omisión son bajos.",
    'normal': "Los errores de omisión son normales.",
    'alto': "Los errores de omisión son altos y sugieren dificultades de atención selectiva.",
}

PARRAFO_CPT_C = {
    'bajo': "Los errores de comisión son bajos.",
    'normal': "Los errores de comisión son normales.",
    'alto': "Los errores de comisión son altos y sugieren menor control inhibitorio.",
}

PARRAFO_CPT_CON = {
    'bajo': "El índice CON es bajo.",
    'normal': "El índice CON es adecuado.",
    'alto': "El índice CON es alto y refleja buen equilibrio entre rapidez y precisión.",
}

PARRAFO_CPT_VAR = {
    ('alto', 'nada'): "{nombre} mostró una variabilidad elevada entre series.",
    ('alto', 'fatiga'): "{nombre} mostró una variabilidad elevada entre series con un patrón compatible con fatiga.",
    ('alto', 'automatismo'): "{nombre} mostró una variabilidad elevada, pero con mejora progresiva compatible con automatización.",
    'normal': "La variabilidad entre series se mantiene en un rango esperable.",
    'bajo': "La variabilidad entre series es baja y el rendimiento resulta estable.",
}

PARRAFO_FourFigures_TR = {
    'TR bajo': "El tiempo de respuesta en la tarea de flexibilidad es rápido.",
    'TR normal y C bajo': "El tiempo de respuesta es adecuado y preciso.",
    'TR normal y C normal o alto': "El tiempo de respuesta es adecuado.",
    'TR alto': "El tiempo de respuesta es lento.",
}

PARRAFO_FourFigures_A = {
    'bajo': "La precisión global es baja.",
    'normal': "La precisión global es adecuada.",
    'alto': "La precisión global es alta.",
}

PARRAFO_FourFigures_C = {
    'C bajo y TR bajo o normal': "Las comisiones son bajas.",
    'C bajo y TR alto': "Las comisiones son bajas pese a la lentitud.",
    'C normal': "Las comisiones se sitúan en rango esperable.",
    'C alto y TR bajo': "Las comisiones son altas y compatibles con impulsividad.",
    'C alto y TR normal o alto': "Las comisiones son altas y sugieren problemas de discriminación o control.",
}

PARRAFO_FourFigures_P4_A_obtenido_vs_esperado = {
    'bajo': "La parte 4 queda por debajo de lo esperable según las partes previas.",
    'normal': "La parte 4 se ajusta a lo esperable según las partes previas.",
    'alto': "La parte 4 queda por encima de lo esperable según las partes previas.",
}

PARRAFO_DigitsMemorization = {
    'bajo': "La memoria operativa medida con dígitos resulta baja.",
    'normal': "La memoria operativa medida con dígitos resulta adecuada.",
    'alto': "La memoria operativa medida con dígitos resulta alta.",
}

PARRAFO_DUALTASK_General_PSV_y_A = {
    'Estable y positivo': "El rendimiento general en Dual Task es positivo y estable entre tareas.",
    'Estable y normal': "El rendimiento general en Dual Task es estable y adecuado.",
    'Estable y negativo': "El rendimiento general en Dual Task es estable, pero limitado.",
    'Inestable y positivo': "El rendimiento general es bueno, aunque desequilibrado entre ambas tareas.",
    'Muy inestable': "El rendimiento general es muy desigual entre tareas.",
}

PARRAFO_DUALTASK_si_inestable = {
    'T1_mas_T2': "La tarea de seguimiento visomotor resulta relativamente más sólida que la tarea de respuesta.",
    'T2_mas_T1': "La tarea de respuesta rápida resulta relativamente más sólida que la de seguimiento visomotor.",
}

PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia = {
    'bajo': "Cuando ambas tareas concurren, el rendimiento conjunto es bajo.",
    'normal': "Cuando ambas tareas concurren, el rendimiento conjunto es adecuado.",
    'alto': "Cuando ambas tareas concurren, el rendimiento conjunto es alto.",
}

PARRAFO_DUALTASK_PSV_cuando_concurrencia = {
    'deterioro y buen T2': "Durante la concurrencia, la T1 empeora mientras la T2 se mantiene adecuada.",
    'deterioro y mal T2 P': "Durante la concurrencia, empeora T1 y también cae la precisión de T2.",
    'deterioro y mal T2 TR': "Durante la concurrencia, empeora T1 y también se ralentiza T2.",
    'deterioro y mal T2 P y TR': "Durante la concurrencia, empeoran T1 y T2 en precisión y velocidad.",
    'no deterioro y buen T2': "Durante la concurrencia, el seguimiento visomotor se mantiene y T2 también.",
    'no deterioro y mal T2 P': "Durante la concurrencia, T1 se mantiene, pero cae la precisión de T2.",
    'no deterioro y mal T2 TR': "Durante la concurrencia, T1 se mantiene, pero se ralentiza T2.",
    'no deterioro y mal T2 P y TR': "Durante la concurrencia, T1 se mantiene, pero T2 empeora en precisión y velocidad.",
}

PARRAFO_DUALTASK_PSV = {
    'bajo': "La precisión de seguimiento visomotor es baja.",
    'normal': "La precisión de seguimiento visomotor es adecuada.",
    'alto': "La precisión de seguimiento visomotor es alta.",
}

PARRAFO_DUALTASK_A = {
    'bajo': "La precisión de la tarea de respuesta es baja.",
    'normal': "La precisión de la tarea de respuesta es adecuada.",
    'alto': "La precisión de la tarea de respuesta es alta.",
}

PARRAFO_DUALTASK_C = {
    'bajo': "Las comisiones en la tarea 2 son escasas.",
    'normal': "Las comisiones en la tarea 2 son esperables.",
    'alto': "Las comisiones en la tarea 2 son elevadas.",
}

PARRAFO_DUALTASK_TR_A_vs_C = {
    'C normal y TR_A_vs_C positivo': "Las comisiones aparecen más rápido que los aciertos, compatible con impulsividad.",
    'C normal y TR_A_vs_C negativo': "Las comisiones no parecen debidas a impulsividad, sino a dificultades de procesamiento.",
    'C alto y TR_A_vs_C positivo': "Las comisiones elevadas parecen estar ligadas a impulsividad.",
    'C alto y TR_A_vs_C negativo': "Las comisiones elevadas parecen ligadas a dificultades de discriminación.",
}

PARRAFO_DUALTASK_O = {
    'bajo': "Las omisiones en la tarea 2 son bajas.",
    'normal': "Las omisiones en la tarea 2 se mantienen en rango esperable.",
    'alto': "Las omisiones en la tarea 2 son altas.",
}

PARRAFO_DUALTASK_TR = {
    'TR bajo y C bajo': "La velocidad de respuesta en la tarea 2 es alta y precisa.",
    'TR bajo y C normal o alto': "La velocidad de respuesta en la tarea 2 es alta, aunque puede acompañarse de impulsividad.",
    'TR normal': "La velocidad de respuesta en la tarea 2 es adecuada.",
    'TR alto y C alto': "La velocidad de respuesta en la tarea 2 es lenta y además aparecen muchas comisiones.",
    'TR alto y C normal': "La velocidad de respuesta en la tarea 2 es lenta.",
    'TR alto y C bajo': "La velocidad de respuesta en la tarea 2 es lenta, con un estilo cuidadoso.",
}

PARRAFO_DUALTASK_Fatiga = {
    'no F': "No se aprecian indicios claros de fatiga durante Dual Task.",
    'F_PSV': "Aparecen indicios de fatiga en el seguimiento visomotor.",
    'F_A': "Aparecen indicios de fatiga en la precisión de la tarea 2.",
    'F_TR': "Aparecen indicios de fatiga en la velocidad de la tarea 2.",
    'F_PSV y F_A': "Aparecen indicios de fatiga tanto en T1 como en la precisión de T2.",
    'F_PSV y F_TR': "Aparecen indicios de fatiga en T1 y en la velocidad de T2.",
    'F_A y F_TR': "Aparecen indicios de fatiga en precisión y velocidad de T2.",
    'F_PSV y F_A y F_TR': "Aparecen indicios de fatiga en todas las medidas principales de Dual Task.",
}

PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK = {
    'intro': "Finalmente, se indican algunas recomendaciones derivadas de la interacción entre tareas.",
    'PARRAFO_DUALTASK_final_inestable_negativo_o_muy_inestable': "El desequilibrio entre tareas aconseja entrenar la gestión simultánea de recursos atencionales.",
    'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_positivo': "Se observa una mejor aptitud relativa para tareas sostenidas y estables.",
    'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_negativo': "La tarea 1 funciona como fortaleza relativa desde la que apoyar el entrenamiento del resto de componentes.",
    'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_positivo': "Se observa una mejor aptitud relativa para tareas rápidas y reactivas.",
    'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_negativo': "La tarea 2 funciona como fortaleza relativa, pero conviene reforzar el control sostenido.",
    'PARRAFO_DUALTASK_final_concurrencia_peorT1_malT2': "La simultaneidad de tareas parece generar sobrecarga y conviene estructurar el trabajo paso a paso.",
    'PARRAFO_DUALTASK_final_PSV_bajo': "Conviene revisar con más detalle las habilidades visomotoras finas si este patrón se mantiene.",
    'PARRAFO_DUALTASK_final_fatiga': "La aparición de fatiga sugiere trabajar también la resistencia cognitiva.",
}
