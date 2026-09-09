"""
Módulo con los textos para generar el informe vocacional.
"""

# ============================================================================
# PÁRRAFOS FIJOS (siempre se incluyen)
# ============================================================================

PARRAFOS_FIJOS = {
    'titulo_general_prueba': "1. Objetivo de la batería de pruebas.",

    'objetivo_prueba': (
        "Este informe está compuesto por una batería de 1 cuestionario (ACS) y 4 pruebas conductuales: ANT, CPT, FourFigures and Dual-Task. "
        "En conjunto, estas pruebas evaluan la capacidad atencional. Como se explica más adelante en detalle, a través de cada prueba se mide un subcomponente de la atención "
        "diferente: velocidad de procesamiento, memoria operativa, atención sostenida, atención discriminativa, control ejecutivo, flexibilidad cognitiva, etc."
    ),

    'titulo_procedimiento': "2. Descripción de las tareas.",

    'descripcion_procedimiento0': (
        "La prueba tiene una duración total de 20 minutos aproximadamente. Durante este tiempo el participante debe completar un cuestionario y 4 pruebas conductuales. A continuación se describen los procedimientos de cada prueba."
    ),


    'descripcion_procedimiento1.1': (
        "En primer lugar, al participante se le pide responder (Nada, Algo, Mucho) a un total de 20 preguntas breves vinculadas a diferentes habilidades o problemas atencionales, p.ej: "
        "'Me cuesta concentrarme cuando estoy muy excitado con algo.', 'Puedo rápidamente cambiar de una tarea a otra.', etc.\n"
    ),

    'descripcion_procedimiento2.1': (
        "Para la primera prueba ANT (Atentional Network Test) la persona tiene que observar una serie de símbolos. "
        "Entre estos, una flecha central horizontal, ⬅ o ➡, de la cual el evaluado tiene que indicar el sentido hacia el que señala (izquierda o derecha). "
        "Sin embargo, esta flecha central se presenta precedida y continuada por otras 2 líneas a cada lado, que pueden ser: simples líneas rectas o flechas, en el mismo u opuesto sentido a la flecha central objetivo. "
        "Véase un ejemplo de estos posibles estímulos centrales en la siguiente imagen:"
    ),

    'descripcion_procedimiento2.2': (
        "Finalmente, estas flechas aparecen de "
        "forma más o menos impredecible, junto con otros estímulos contextuales (unos asteriscos), que bien pueden ser: pistas, distractores o señales irrelevantes. "
        "Véase un ejemplo de estos posibles estímulos contextuales en la siguiente imagen:"
    ),

        'descripcion_procedimiento3.1': (
        "En la siguiente prueba CPT (Continuous Performance Test) la persona tiene que en un tiempo límite señalar el mayor número de elementos objetivo posible. "
        "Estos elementos se muestran en fila intercalados por estímulos similares pero distractores que se tienen que ignorar. Los estímulos objetivos y distractores son los de la siguiente imagen."
    ),

        'descripcion_procedimiento4.1': (
        "En la cuarta prueba FourFigures se presentan 4 series de estímulos uno por uno. "
        "Cada estímulo se compone de una figura externa y una interna, las cuales pueden compartir o discrepar en su forma (cuadrado, círculo, triángulo y cruz). En algunas partes de la tarea se pregunta por la forma de la figura externa "
        "y en otras por la de la figura interna. El participante tiene con la mayor rapidez y precisión posible señalar la forma de la figura por la que se está a preguntar en cada momento. Véase a continuación algunos ejemplos de estímulos."
    ),

        'descripcion_procedimiento5.1': (
        "Por último, la prueba DUAL-TASK demanda realizar dos tareas simultáneamente. Por un lado, una tarea constante de seguimiento de un punto en movimiento con el cursor del ratón. "
        "Por otro lado, una tarea intermitente de detección de estímulos objetivo frente distractores. Esto es, que además del cursor a seguir, en la pantalla eventualemente aparecen otros dos estímulos: un cuadrado rojo o azul. "
        "Además de mover el ratón para seguir el punto la persona debe de hacer clic izquierdo cada vez que en pantalla aparece el cuadrado rojo, y evitar pulsarlo cuando el cuadrado es azul."
    ),



    'titulo_indices': "3. Índices que se obtienen.",

    'descripcion_indices': (
        " El desempeño conjunto en todas las tareas permite evaluar con gran consistencia todas las diferentes dimensiones de la atención. \n"
        "• Arousal (grado de activación). Nesario para mantener un estado despierto y capacidad de atención consciente. "
        "Mide el estado de vigilia o de activación/atención en general. \n"
        "• Atención sostenida. Necesaria para mantener el rendimiento durante toda la duración de la "
        "prueba. Mide la capacidad de la personar para mantenerse concentrado en una misma tarea a lo "
        "largo del tiempo. \n"
        "• Atención selectiva. Requerida para distinguir estímulos señal de "
        "distractores. Mide la capacidad de la persona para identificar y atender únicamente a la "
        "información relevante para la tarea, e ignorar la información distractora y engañosa. \n"
        "• Control ejecutivo. Relacionado con el control voluntario y dirigido de la atención y la "
        "conducta. Mide la capacidad de la persona para inhibir la información irrelevante y "
        "engañosa, y la emisión de respuestas controlas frente la impulsividad. \n"
        "• Flexibilidad cognitiva. Relacionada con el cambio dinámico del foco atencional"
        "entre tareas. Mide la rapidez y eficacia con la que una persona es capaz de " 
        "adaptarse a cambios en las reglas que definen la tarea y conducta a desempeñar. "
        "• Memoria operativa. Necesario para realizar un procesamiento y respuesta breves ante momentos "
        "de gran cantidad de información y demanda cognitiva. Mide la cantidad de información que se puede "
        "mantener consciente y analizar simultáneamente."
        "• Velocidad de procesamiento. Necesario para entender una tarea y dar respuesta con la mayor rapidez posible. "
        " Se refiere al tiempo que se necesita para percibir, procesar y responder a la información. "
        "•   Preferencia o tendencia por un estilo atencional de distribución paralela de la atención o de "
        "cambio focal (switching atencional): "
        "1. "
        "Un estilo de distribución paralela de la atención. "
        "En este patrón, el participante mantiene un reparto relativamente equilibrado y constante de los recursos "
        "atencionales entre dos tareas simultáneas."
        "2. 
        "Estilo de cambio focal (switching atencional). "
        "En este patrón, cuando dos tareas concurren la atención se desplaza de forma asimétrica hacia el estímulo más saliente o urgente, "
        "y retorna a la tarea más constante cuando la carga de trabajo y demanda cognitiva decrece. \n"
        "• Hiperactividad. Grado de inquietud física y de movimiento innecesario durante la tarea."
       
    ),

    'titulo_resultados': "Presentación de los resultados de {nombre_completo}",

    'texto_resultados': (
        "A continuación se muestran los resultados de {nombre} a partir de un gráfico para "
        "cada prueba y unos párrafos explicativos que integran y sintetizan los hallazgos obtenidos."
    ),

    'titulo_resultados_generales': "En términos generales",
    'texto_resultados_generales': " ",

    'titulo_resultados_específicos': "Profundizando en cada prueba atencional",

    'titulo_ACS': "ACS - cuestionario de control atencional",

    'texto_resultados_ACS': "Empezamos mostrando la percepción autodeclarada sobre las capacidades atencionales propias. A través del cuestionario ACS, {nombre} afirma tener la siguiente capacidad atencional:",

    'titulo_ANT': "ANT - prueba de eficiencia de redes neuronales atencionales",

    'titulo_CPT': "CPT - prueba de rendimiento continuo",

    'titulo_FourFigures': "Four Figures - prueba de control y flexibilidad cognitiva",

    'titulo_DigitsMemorization': "Memorización de dígitos - prueba de memoria operativa",

    'titulo_DualTask': "Dual Task - prueba multitarea de atención dividida",

    'introduccion_analisis_tareas_DualTask': "A continuación, nos centramos en el rendimiento pormenorizado de cada tarea por separado."

    'título_sintesis_final': "Finalmente, a modo de síntensis revisamos el desempeño global y dimensional de las capacidades atencionales de {nombre}. A fin de señalar las posibles debilidades y fortalezas y áreas en las que cabe prestar más atención futura." 
 }



# ============================================================================
# ACS — PÁRRAFOS CONDICIONALES
# ============================================================================
# Se podría añadir un índice de fiabilidad basado en desviación típica


PARRAFO_ACS_atenciongeneral = {
    'bajo':"""En general, una capacidad atencional baja, con dificultades para aislarse de distracciones y atender la tarea deseada.""",

    'normal':"""En general, una capacidad atencional adecuada. A excepción de algunas dificultades puntuales, se tiene capacidad para aislarse de distracciones y atender la tarea deseada.""",

    'alto':"""En general, una capacidad atencional excelente. No se percibe ningún problema o dificultad para aislarse de las distracciones y atender una tarea o varias tareas al máximo.""",
 }

PARRAFO_ACS_foco = {
    'bajo':"""En particular, se detecta dificultad a la hora de concentrarse y desarrollar un estado de atención focalizada prolongado.""",

    'normal':"""En particular, se detecta una adecuada capacidad para concentrarse y desarrollar un estado de atención focalizada prolongado.""",

    'alto':"""En particular, se detecta una muy buena capacidad para concentrarse y desarrollar un estado de atención focalizada prolongado.""",

 }

PARRAFO_ACS_cambio = {
    'bajo':"""Y por otro lado, se señala dificultad para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

    'normal':"""Y por otro lado, se señala una adecuada capacidad para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

    'alto':"""Y por otro lado, se señala una gran facilidad para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

 }


# ============================================================================
# ANT — PÁRRAFOS CONDICIONALES
# ============================================================================
# Se podría añadir un índice de fiabilidad basado en desviación típica


PARRAFO_ANT_TR = {

    'TR bajo':"""En primer lugar, {nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",

    'TR normal y C normal o alto':"""En primer lugar, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",

    'TR normal y bajo':"""En primer lugar, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas: una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado, y la posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR alto':"""En primer lugar, {nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Esto puede deberse a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. O la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas. Véase a continuación, el apartado de 'Comisiones' para valorar esta segunda posibilidad.""",
}

PARRAFO_ANT_A = {

    'A bajo':"""{nombre} muestra un porcentaje de aciertos bajo, lo que indica complicaciones para completar eficientemente la tarea presentada. Según este resultado, la capacidad atencional general resulta inferior a la media para su edad.""",

    'A normal':"""{nombre} muestra un porcentaje de aciertos normal, lo que indica una capacidad atencional general adecuada a la esperada para su edad.""",
    
    'A alto':"""{nombre} muestra un porcentaje de aciertos alto, lo que indica una capacidad atencional general superior a la media para su edad.""",
}

PARRAFO_ANT_C = {

    'C bajo y TR bajo o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",
# Álvaro. En estos dos siguientes párrafos se necesita una dif sign? O dif mínima es suficiente asumiendo una H muy intuitiva de que E impulsiva menor TR y E def. discriminatorio mayor TR. Si necesidad sign.
    'C alto y TR_A_vs_C positivo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Comparando el tiempo de respuesta entre errores y aciertos vemos que estas comisiones corresponden con respuestas más impulsivas, más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C alto y TR_A_vs_C negativo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Estos errores acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto sugiere que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",
}

PARRAFO_ANT_O = {
    'O bajo':"""{nombre} presenta un número de errores de omisión bajo, lo que señala que pocas veces no ha respondido cuando debería. Este resultado señala una velocidad de procesamiento de la información y de toma de decisiones bien ajustada a la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad superior al promedio para mantener la atención sostenida a lo largo de toda la tarea, sin distraerse o fatigarse, de manera que se dificulte dar una respuesta en los momentos oportunos.""",

    'O normal':"""{nombre} presenta un número de errores de omisión normal, lo que señala que no ha respondido cuando debería un número de veces igual a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones adecuada a la exigencia temporal de la tarea. Este índice también puede señalar una capacidad adecuada para mantener la atención sostenida a lo largo de toda la tarea, sin distraerse o fatigarse demasiado, de manera que se dificulte dar una respuesta en los momentos oportunos.""",
    
    'O alto':"""{nombre} presenta un número de errores de omisión alto, lo que señala que no ha respondido cuando debería un número de veces superior a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones demasiado lenta para la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad inferior al promedio para mantener la atención sostenida a lo largo de toda la tarea. Con tendencia a distraerse o fatigarse, lo que le dificulta dar una respuesta en los momentos oportunos.""",
}

PARRAFO_ANT_F = {
    'F_A bajo y F_TR bajo':"""El rendimiento de {nombre} durante la tarea ha ido mejorando con el avance de la misma, mostrando mejor precisión y velocidad de respuesta al final de la prueba que al principio. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""", 

    'F_A bajo y F_TR normal':"""A lo largo de la tarea {nombre} muestra una velocidad de respuesta que se mantiene constante, y una precisión que incluso mejora según avanza la misma. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""",

    'F_A bajo y F_TR alto':""""A lo largo de la tarea {nombre} muestra una precisión de respuesta que mejora con el avance de la misma, mientras que la velocidad de respuesta se ralentiza. Esto indica una clara preferencia de {nombre} por un estilo atencional más reflexivo, con la adopción de un procesamiento de la información más lento pero preciso. {nombre} parece ser muy capaz de automatizar eficazmente tareas simples y repetitivas. Aunque, a su vez, la falta de excitación de esta tarea monótona le supone un mayor esfuerzo y cansancio por mantener la atención sostenida. Finalmente, {nombre} presenta un importante enlantecimiento en su velocidad de trabajo, el cual puede deberse en parte a la fatiga. O a la preferencia y adopción de un estilo atencional más reflexivo con el transcurso de la tarea.""",
    
    'F_A normal y F_TR bajo':"""A lo largo de la tarea {nombre} muestra una precisión de respuesta constante, mientras que la velocidad de respuesta aumenta con el avance de la tarea. Esto indica una excelente capacidad de automatización de la tarea, especialmente ante tareas simples y repetitivas como esta. Esta habilidad es útil para reducir el esfuerzo ante tareas monótonas y poco estimulantes, y reducir así el cansancio generado. O incluso, en este caso, aumentando la velocidad con la que se realiza la tarea, sin perder calidad en la precisión.""",
    
    'F_A normal y F_TR normal':"""A lo largo de la tarea {nombre} muestra un rendimiento sumamente constante, sin que su precisión y velocidad de respuesta se vean afectadas. Esto indica una excelente capacidad de atención sostenida y resistencia a la fatiga, incluso, o especialmente, ante tareas simples y monótonas como esta.""",

    'F_A normal y F_TR alto':"""A lo largo de la tarea {nombre} muestra una precisión de respuesta constante, mientras que la velocidad de respuesta se ralentiza. Esto indica dos cosas. Por un lado, el enlantecimiento en su velocidad de trabajo sugiere en {nombre} una baja resistencia a la fatiga ante tareas monótonas y poco estimulantes. Por otro lado, este resulta indica la preferencia de {nombre} por un estilo atencional más reflexivo. De esta manera, ante la aparición de cansancio, {nombre} decide tomarse más tiempo en su respuesta, y así poder seguir procesando la información de manera precisa y consciente.""",

    'F_A alto y F_TR bajo':"""Con el avance de la tarea {nombre} muestra una aceleración de su velocidad de respuesta, aunque de la mano de un empeoramiento de su precisión. Esto indica dos cosas. Primero, la aparición de cansancio con el avance de la tarea, especialmente ante tareas monótonas y poco estimulantes. En segundo lugar, una clara preferencia y adopción de {nombre} por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas. {nombre} parece tener dificultades para reunir una motivación más intrínseca en el desempeño de la tarea. Y así, ante la falta de estimulación, se cansa o aburre más que lo esperado para su edad, afectando negativamente a su esfuerzo, atención sostenida y rendimiento durante la tarea.""",
    
    'F_A alto y F_TR normal':"""A lo largo de la tarea {nombre} muestra una velocidad de respuesta constante, aunque con un empeoramiento en la precisión según avanza la tarea. Esto es indicativo de una baja resistencia a la fatiga, especialmente ante tareas monótonas y poco estimulantes como esta. Con la aparición de cansancio, {nombre} podría esforzarse más para mantener una buena precisión y calidad de respuesta, a costa de tomarse más tiempo para pensar y responder. Pero en este caso, parece que {nombre}, bien por falta de capacidad o de motivación, no adopta este estilo atencional más reflexivo, eficaz ante la aparición de cansancio y deterioro en la calidad de la ejecución.""",

    'F_A alto y F_TR alto':"""Con el avance de la tarea {nombre} muestra un enlantecimiento de su velocidad de respuesta y un empeoramiento de su precisión. Esto indica una muy baja resistencia al cansancio o el aburrimiento, especialmente ante tareas monótonas y poco estimulantes como esta. Según este índice {nombre} tiene grandes dificultades para mantener la atención sostenida lo que le lleva a no responder o responder erratica o aleatoriamente ante una tarea. Parece así que el rendimiento de {nombre} dependerá más de cuán estimulante le resulte una actividad. Y tiene por tanto, dificultades para reunir motivación más intrínseca en el desempeño de una tarea, y así poder realizar también estas actividades más monótonas o aburridas pero igualmente importantes para la vida diaria.""",
    }


PARRAFO_ANT_alerta = {

    'TR_alerta bajo':"""La eficiencia de la red de alerta resultó superior a la media para su edad. Esto se traduce en una excelente capacidad para mantener un alto estado de vigilancia y activación. Es decir, que {nombre} ha estado especialmente despierto durante la tarea. Esto le permite reconectar y atender rápidamente con la tarea en los momentos que aparece información relevante.""",

    'TR_alerta normal':"""La eficiencia de la red de alerta resultó adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para mantener un estado de vigilancia y activación durante la tarea. Es decir, que {nombre} ha estado suficientemente despierto durante la tarea. Esto le permite reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
    
    'TR_alerta alto':"""La eficiencia de la red de alerta resultó inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para mantener un alto estado de vigilancia y activación. Es decir, parece que {nombre} ha estado poco despierto durante la tarea. Esto le dificulta reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
}
PARRAFO_ANT_orientacion = {

    'TR_orientacion bajo':"""Respecto a la red de orientación, {nombre} mostró una eficiencia superior a la media para su edad. Esto se traduce en una excelente capacidad para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",

    'TR_orientacion normal':"""Respecto a la red de orientación, {nombre} mostró una eficiencia adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",
    
    'TR_orientacion alto':"""Respecto a la red de orientación, {nombre} mostró una eficiencia inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",
}
PARRAFO_ANT_ejecutivo = {

    'TR_ejecutivo bajo':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo superior a la media para su edad. Esto se traduce en una excelente capacidad para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un alto control para procesar y ejecutar tareas complejas.""",

    'TR_ejecutivo normal':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un control adecuado para procesar y ejecutar tareas complejas.""",
    
    'TR_ejecutivo alto':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un control limitado para procesar y ejecutar tareas complejas.""",
}


# ============================================================================
# CPT — PÁRRAFOS CONDICIONALES OPCIONALES  . Se usa tanto para la prueba CPT como la D2
# ============================================================================

# TR - Velocidad de procesamiento
PARRAFO_CPT_TR = {
    'alto': """El elevado número de elementos procesados indica una alta velocidad de procesamiento, asociada a buena capacidad de exploración visual y rapidez en la toma de decisiones.""",
    
    'normal': """El número de elementos procesados se sitúa dentro de los valores esperables para su grupo normativo, indicando una velocidad de procesamiento adecuada, con un ritmo de trabajo ajustado a las demandas temporales de la tarea""",
    
    'bajo y E normal o alto': """El bajo volumen de elementos procesados sugiere una velocidad de procesamiento reducida. {nombre} requiere de más tiempo de lo normal para procesar y discriminar la información. Esto puede incapacitar y emperorar el desempeño, especialmente ante tareas con limitación temporal o de desempeño rápido."""
# Álvaro. Necesidad calcular una PT de E
    'bajo y E bajo': """El bajo volumen de elementos procesados sugiere una velocidad de procesamiento reducida. Un vistazo al reducido número de errores cometidos (omisiones y comisiones en conjunto) señalan la prevalencia de un estilo atencional y de trabajo más reflexivo, ganando mayor precisión a costa de menor velocidad de respuesta. Aunque esto puede ser ventajoso para el desempeño de tareas más precisas, también puede suponer cierta desventaja ante tareas con limitación temporal y de desempeño rápido. No saber regular el estilo atencional más oportuno a las demandas de una tarea puede suponer una deficiencia atencional, y un problema solventable con entrenamiento."""
}

# O - Errores de omisión
PARRAFO_CPT_O = {
    'alto': """La presencia de un número elevado de errores de omisión indica dificultades en la atención selectiva y la detección de información relevante. Esto se asocia a lapsus atencionales y un seguimiento inconsistente de la consigna o reglas de la tarea, lo que deriva en un escaneo visual incompleto y una discriminación y respuesta deficiente de la información relevante procesada.""",
    
    'normal': """El número de errores de omisión se sitúa dentro de los valores esperables para su grupo normativo, lo que indica una adecuada atención sostenida y capacidad para detectar los estímulos relevantes a lo largo de la tarea. Este resultado sugiere un escaneo visual correcto y un seguimiento apropiado de la consigna, sin evidenciar lapsus atencionales significativos.""",
    
    'bajo': """El bajo número de errores de omisión refleja una elevada focalización atencional, con muy buena capacidad para detectar los estímulos relevantes."""
}

# C - Errores de comisión
PARRAFO_CPT_C = {
    'alto': """El aumento de errores de comisión sugiere dificultades en el control inhibitorio: una mayor impulsividad en la respuesta o cierta deficiencia perceptiva en la discriminación y omisión de la información irrelevante  y engañosa.""",
    
    'normal': """La frecuencia de errores de comisión se encuentra dentro de rangos normales, lo que refleja un control inhibitorio adecuado, y una impulsiva en la respuesta igual a lo esperado para su edad. Este patrón sugiere una correcta discriminación y omisión de la información irrelevante  y engañosa.""",
    
    'bajo': """La escasa presencia de errores de comisión indica un alto control inhibitorio, con respuestas cuidadosas y precisas que reflejan una buena capacidad de discriminación y omisión de la información irrelevante y engañosa."""
}

# CON - Concentración
PARRAFO_CPT_CON = {
    'alto': """El índice de concentración elevado evidencia un excelente equilibrio entre velocidad y precisión, reflejando una elevada concentración y control atencional durante la tarea. Esto sugiere que {nombre} estuvo muy despierto durante la realización de la prueba.""",
    
    'normal': """El índice de concentración se sitúa dentro de valores esperables, indicando un equilibrio adecuado entre rapidez y exactitud en la ejecución de la tarea. Este resultado refleja una capacidad de concentración acorde a las demandas de la tarea, sin que se observen dificultades importantes en la regulación del esfuerzo atencional. Según esto, {nombre} estuvo lo suficientemente despierto para realizar adecuadamente la tarea.""",
    
    'bajo': """Un nivel bajo en el índice de concentración sugiere dificultades para integrar rapidez y precisión, bien por exceso de velocidad con descuido, bien por lentitud sin compensación en precisión, o bien por ambas, lentitud y descuido. Esto señala que la concentración de {nombre} durante la prueba fue en general pobre, y que seguramente no estuvo lo suficientemente despierto como para realizarla correctamente."""
}


PARRAFO_CPT_VAR = {
# Álvaro. Calcular presencia Fatiga o automatismo por prueba t entre el índice CON del primer y tercer tercio prueba? Necesidad baremar esta dif.?
    ('alto', 'nada'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series, vinculada a dificultades para mantener la motivación constante y a una mayor facilidad para distraerse. Esto influye a su vez a un declive en la puntuación de {nombre} en los demás aspectos atencionales anteriormente evaluados."""

# dentro de la condición VAR se tratan las condiciones 'Fatiga' y 'Automatizacion' si dif. sign. negativa o positiva respectivamente entre el primer (primeras 4 series) y tercer tercio (últimas 4 series) de la prueba.
    ('alto', 'fatiga'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series, vinculada a dificultades para mantener la motivación y a una mayor facilidad para distraerse. En particular, aparece aquí cierto cansancio o fatiga con el transcurso de la tarea, ya que la serie de peor rendimiento se obtuvo más hacia el final de la tarea, en comparación con la de mayor rendimiento. Esto influye a su vez a un declive en la puntuación de {nombre} en los demás aspectos atencionales anteriormente evaluados."""

# Si promedio CON 4 primeras series es 5 puntos mayor que promedio 4 últimas
    ('alto', 'automatismo'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series. Además se observa que el rendimiento fue en mejora progresiva, con las peores series al principio de la tarea y las de mejor rendimiento hacia el final. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad se trata más bien de una notable capacidad para adaptarse y automatizar la ejecución a largo plazo."""

# Si promedio CON 4 primeras series es 5 puntos menos que promedio 4 últimas
    ('alto', 'dificultadinicial'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series. Además se observa que el rendimiento fue en mejora progresiva, con las peores series al principio de la tarea y las de mejor rendimiento hacia el final. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad se trata más bien de una dificultad inicial para asimilar y acomodarse rápidamente a la nueva tarea."""

    'normal': """ El último aspecto para mencionar es en relación a la curva de trabajo trazada en el perfil gráfico adjunto en este informe. Aquí se puede ver que el rendimiento de {nombre} durante la prueba ha resultado estable y consistente entre series. Esto es indicativo de que la ejecución de {nombre} en los aspectos atencionales aquí evaluados resulta típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte o la aparición de cansancio, respectivamente, son menos probables.""",

    'bajo': """El bajo nivel de variabilidad observado sugiere una alta consistencia y estabilidad en el rendimiento, indicando una buena resistencia al cansancio o fatiga y una buena capacidad para sostener el esfuerzo atencional de forma uniforme durante toda la tarea. Además, esto es indicativo de que la ejecución de {nombre} en los aspectos atencionales anteriormente evaluados resulta aún más típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte, distracciones puntuales o la aparición de cansancio, respectivamente, son menos probables."""
}

# ============================================================================
# 3.3.1 FourFigures
# ============================================================================

# TR - Velocidad de procesamiento
PARRAFO_FourFigures_TR = {
   'TR bajo':"""{nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",

    'TR normal y C normal o alto':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",

    'TR normal y C bajo':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas. Primero una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado. Y segundo, una posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR alto':"""{nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Esto puede deberse a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. O la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas. Véase a continuación, el apartado de 'Comisiones' para valorar esta segunda posibilidad.""",
}

PARRAFO_FourFigures_A = {
    'alto': """El elevado número de aciertos indica una atención general excelente, asociada a un estado de activación o vigilia excepcional. {nombre} estuvo completamente despierto a lo largo de toda esta tarea, lo que también debería haber favorecido el desempeño en otras dimensiones atencionales.""",
    
    'normal': """El número de aciertos obtenido es adecuado y dentro de la norma para su edad. Esto señala un adecuado estado de activación o vigilia durante la prueba.""",
    
    'bajo': """El número de aciertos obtenido es limitado, menor a lo normal o esperable para su edad. Este índice se suele asociar al estado de activación o vigilia de la persona. En este caso parece que {nombre} no estuvo lo suficientemente despierto durante la tarea. Otra explicación posible es que {nombre} haya respondido aleatoriamente o que no haya entendido bien las instrucciones. En cualquier caso esta atención general deficiente ha perjudicado el desempeño en el resto de dimensiones atencionales en esta prueba evaluadas.""",
    }


# C - Errores de comisión
PARRAFO_FourFigures_C = {
    'C bajo y TR bajo o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",
# Álvaro. En estos dos siguientes párrafos se necesita una dif sign? O dif mínima es suficiente asumiendo una H muy intuitiva de que E impulsiva menor TR y E def. discriminatorio mayor TR. Si necesidad sign.
    'C alto y TR_A_vs_C positivo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Comparando el tiempo de respuesta entre errores y aciertos vemos que estas comisiones corresponden con respuestas más impulsivas, más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C alto y TR_A_vs_C negativo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Estos errores acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto sugiere que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",
}

# Flexibilidad cognitiva. Diferencia puntuación obtenida en P4 vs puntuación esperada en P4 en base a puntuación obtenida en P2 y P3.
PARRAFO_FourFigures_P4_A_obtenido_vs_esperado = {
# Álvaro. Comparar prueba significación prueba t o PT en comparación con la muestra? Aquí avogo por PT dada la mayor facilidad de P2 y P3 frente la tarea FiveDigits, en la cual propongo usar sign. prueba t.
    'alto': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento incluso superior al esperado, prueba de una excelente capacidad para adaptarse y dirigir su atención a voluntad.""",

    'normal': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento normal e igual a lo esperable. Esto prueba una adecuada capacidad para adaptarse y dirigir su atención a voluntad.""",
    
    'bajo': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento inferior al esperado. Esto muestra una alta rigidez cognitiva o dificultad para cambiar el foco atencional rápidamente y adaptarse a una nueva forma de procesar y responder a una tarea."""
}


# ============================================================================
# 3.3.2 FiveDigits
# ============================================================================

# TR - Velocidad de procesamiento
PARRAFO_FiveDigits_TR = {
   'TR bajo':"""{nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",

    'TR normal y C normal o alto':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",

    'TR normal y C bajo':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas. Primero una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado. Y segundo, una posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR alto':"""{nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Esto puede deberse a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. O la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas. Véase a continuación, el apartado de 'Comisiones' para valorar esta segunda posibilidad.""",
}

PARRAFO_FiveDigits_A = {
    'alto': """El elevado número de aciertos indica una atención general excelente, asociada a un estado de activación o vigilia excepcional. {nombre} estuvo completamente despierto a lo largo de toda esta tarea, lo que también debería haber favorecido el desempeño en otras dimensiones atencionales.""",
    
    'normal': """El número de aciertos obtenido es adecuado y dentro de la norma para su edad. Esto señala un adecuado estado de activación o vigilia durante la prueba.""",
    
    'bajo': """El número de aciertos obtenido es limitado, menor a lo normal o esperable para su edad. Este índice se suele asociar al estado de activación o vigilia de la persona. En este caso parece que {nombre} no estuvo lo suficientemente despierto durante la tarea. Otra explicación posible es que {nombre} haya respondido aleatoriamente o que no haya entendido bien las instrucciones. En cualquier caso esta atención general deficiente ha perjudicado el desempeño en el resto de dimensiones atencionales en esta prueba evaluadas.""",
    }


# C - Errores de comisión
PARRAFO_FourFigures_C = {
    'C bajo y TR bajo o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",
# Álvaro. En estos dos siguientes párrafos se necesita una dif sign? O dif mínima es suficiente asumiendo una H muy intuitiva de que E impulsiva menor TR y E def. discriminatorio mayor TR. Si necesidad sign.
    'C alto y TR_A_vs_C positivo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Comparando el tiempo de respuesta entre errores y aciertos vemos que estas comisiones corresponden con respuestas más impulsivas, más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C alto y TR_A_vs_C negativo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Estos errores acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto sugiere que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",
}

# Flexibilidad cognitiva. Diferencia puntuación obtenida en P4 vs puntuación esperada en P4 en base a puntuación obtenida en P2 y P3.
PARRAFO_FourFigures_P4 = {
# Álvaro. Comparar prueba significación prueba t o PT en comparación con la muestra? Aquí avogo por usar sign. prueba t.
    'alto': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento superior al esperable. Esto destaca positivamente su capacidad para adaptarse y dirigir la atención a voluntad.""",

# Quitar distinción en f(A) si al final se usa una PT.
    'normal y A normal o alto': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento igual a lo esperable en la línea de su rendimiento general. Esto evidencia una adecuada flexibilidad cognitiva, capacidad para adaptarse y dirigir la atención a voluntad..""",

    'normal y A bajo': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento igual a lo esperable en la línea de su rendimiento general. Esto disminuye la posibilidad de una deficiencia atencional particularmente ligada a problemas de flexibilidad cognitiva, o la capacidad para cambiar el foco atencional rápidamente y a voluntad.""",
    
    'bajo': """Por último, comparamos el rendimiento real en la parte 4 de la prueba, con el rendimiento esperado en base al rendimiento en las partes anteriores. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva o capacidad de adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento inferior al esperado. Esto muestra una alta rigidez cognitiva o dificultad para cambiar el foco atencional rápidamente y adaptarse a una nueva forma de procesar y responder a una tarea."""
}

# ============================================================================
# 3.5 Digits Memorization
# ============================================================================

# Calcular este índice en función de la PT promedio de PD_directo y PD_inverso
PARRAFO_DigitsMemorization = {

    'bajo':"""En relación a la prueba de memorización de dígitos, esta nos indica la capacidad de memoria operativa. En este aspecto el desempeño ha resultado deficiente, por debajo de lo normal o esperable. {nombre} parece presentar dificultades para procesar y mantener consciente por un tiempo mayores cantidades de información.""",

    'normal':"""En relación a la prueba de memorización de dígitos, esta nos indica la capacidad de memoria operativa. En este aspecto el desempeño ha resultado normal. {nombre} puede adecuadamente procesar y mantener consciente por un tiempo mayores cantidades de información.""",

    'alto':"""En relación a la prueba de memorización de dígitos, esta nos indica la capacidad de memoria operativa. En este aspecto el desempeño ha resultado escepcionalmente bueno. {nombre} tiene una gran capacidad para procesar y mantener consciente por un tiempo mayores cantidades de información.""",
}

# ============================================================================
# 3.5 DUAL-TASK
# ============================================================================


# PD_Total - Según puntuación directa total y correspondiente percentil
PARRAFO_DUALTASK_General_PSV_y_A = {

    'Estable y positivo':"""El rendimiento general en la prueba es positivo y estable entre tareas. Esto índica una muy buena capacidad de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo.""",

    'Estable y normal':"""El rendimiento general en la prueba es adecuado y estable entre tareas. Esto índica una capacidad adecuada de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo.""",

    'Estable y negativo':"""El rendimiento general en la prueba es estable entre tareas, pero mayormente negativo. Esto indica una capacidad limitada de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo.""",

    'Inestable y positivo':"""El rendimiento general en la prueba es inestable entre tareas, aunque mayormente positivo. Esto indica que {nombre} dispone de buenos recursos atencionales para atender y responder a más de una tarea al mismo tiempo. Se observa un mejor rendimiento en la """,

    'Inestable y negativo':"""El rendimiento general en la prueba es inestable entre tareas y mayormente negativo. Esto indica que {nombre} tiene una capacidad limitada y dificultades en la gestión de sus recursos atencionales para atender y responder a más de una tarea al mismo tiempo. Se observa un mejor rendimiento en la """,

    'Muy inestable':"""El rendimiento general en la prueba resulta muy inestable y variable entre tareas. Esto indica que {nombre} tiene muchas dificultades para gestionar sus recursos atencionales y poder atender y responder a más de una tarea al mismo tiempo. El rendimiento ha resultado máximo y sobresaliente para una parte de la prueba, en la que ha depositado todos sus recursos atencionales. Pero ha desatendido completamente la otra tarea, obteniendo un rendimiento inferior al promedio y esperado para su edad. Las dificultades para gestionar adecuadamente sus recursos atencionales y cognitivos en función de la demanda de trabajo derivan en un resultado insuficiente para el cómputo total. Para ejemplificar esto, es como si una persona pudiese leer muy rápido pero sólo hablar lentamente, resultando en que sólo pueda leer lentamente en voz alta. El rendimiento se ha observado mejor en la """,
}

PARRAFO_DUALTASK_si_inestable = {
    'T1_mas_T2':"""tarea 1 frente la 2, señalando un desbalance en la gestión de la atención dirigida a cada tarea. Esto parece señalar una preferencia cognitiva por las tareas que demandan una atención sostenida y ejecución constante, frente a las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva. Esta preferencia cognitiva supone una mejor aptitud para actividades donde importa la persistencia, la concentración prolongada y el ritmo estable, tales como: leer, redactar y pintar de forma extendida, meditar, hacer senderismo o natación.""",

    'T2_mas_T1':"""tarea 2 frente la 1, señalando un desbalance en la gestión de la atención dirigida a cada tarea. Esto parece señalar una preferencia cognitiva por las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva, frente a las tareas atención sostenida y ejecución constante. Esta preferencia cognitiva supone una mejor aptitud para actividades donde predominan los picos de acción intensa, decisiones rápidas y cambios abruptos, tales como: improvisación teatral o en oratoria, deportes (fútbol, baloncesto, boxeo) y videojuegos frenéticos.""",
}

PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia = {
    'bajo':"""Respecto a la memoria de trabajo, esta se estima a partir del rendimiento promedio de las dos tareas de la prueba cuando ambas tareas concurrieron y la carga de trabajo y demanda cognitiva era mayor. La puntuación obtenida señala una memoria de trabajo por debajo del promedio. Esto significa que {nombre} tiene dificultades para procesar de manera simultánea información procedente de diversas fuentes. Es decir, una capacidad limitada para procesar más información.""",

    'normal':"""Respecto a la memoria de trabajo, esta se estima a partir del rendimiento promedio de las dos tareas de la prueba cuando ambas tareas concurrieron y la carga de trabajo y demanda cognitiva era mayor. La puntuación obtenida señala una memoria de trabajo adecuada o promedio. Esto significa que {nombre} tiene una capacidad normal o promedio para procesar de manera simultánea información procedente de diversas fuentes. Es decir, una capacidad adecuada para procesar mucha información.""",

    'alto':"""Respecto a la memoria de trabajo, esta se estima a partir del rendimiento promedio de las dos tareas de la prueba cuando ambas tareas concurrieron y la carga de trabajo y demanda cognitiva era mayor. La puntuación obtenida señala una memoria de trabajo por encima del promedio. Esto significa que {nombre} tiene una capacidad sobresaliente para procesar de manera simultánea información procedente de diversas fuentes. Es decir, una buena capacidad para procesar más información.""",
}

PARRAFO_DUALTASK_PSV_cuando_concurrencia = {
    'deterioro y buen T2':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 ha deteriorado significativamente, mientras que sí se ha respondido bien a tarea 2. Esto sugiere una preferencia y prevalencia de un estilo atencional caracterizado por el cambio focal intermitente entre tareas. {nombre} no atiende a ambas tareas simultáneamente, sino que deja de atender la primera para atender la segunda cuando esta demanda más atención, y vuelve rápidamente a atender a la primera cuando la demanda atencional de la segunda se reduce o desaparece.""",

    'deterioro y mal T2 P':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 ha deteriorado significativamente, mientras que la respuesta a la tarea 2 también a resultado insuficiente, en particular, con relación a una precisión de la respuesta inferior a lo esperado. Esto sugiere una preferencia y prevalencia de un estilo atencional caracterizado por el cambio focal intermitente entre tareas. {nombre} no atiende a ambas tareas simultáneamente, sino que deja de atender la primera para atender la segunda cuando esta demanda más atención, y vuelve rápidamente a atender a la primera cuando la demanda atencional de la segunda se reduce o desaparece. Sin embargo, {nombre} presenta dificultades para dirigir adecuadamente su atención y para procesar tanta información, repercutiendo negativamente en su rendimiento durante la prueba.""",

    'deterioro y mal T2 TR':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 ha deteriorado significativamente, mientras que la respuesta a la tarea 2 también a resultado insuficiente, en particular con relación a una lentitud en la respuesta mayor a lo esperado. Esto sugiere una preferencia y prevalencia de un estilo atencional caracterizado por el cambio focal intermitente entre tareas. {nombre} no atiende a ambas tareas simultáneamente, sino que deja de atender la primera para atender la segunda cuando esta demanda más atención, y vuelve rápidamente a atender a la primera cuando la demanda atencional de la segunda se reduce o desaparece. Sin embargo, {nombre} presenta dificultades para dirigir adecuadamente su atención y para procesar tanta información, repercutiendo negativamente en su rendimiento durante la prueba.""",

    'deterioro y mal T2 P y TR':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 ha deteriorado significativamente, mientras que la respuesta a la tarea 2 también a resultado insuficiente, con relación tanto a la baja precisión como a la lentitud de la respuesta. El estilo atencional aquí presente está caracterizado por el cambio focal intermitente entre tareas. Sin embargo, {nombre} presenta dificultades para dirigir adecuadamente su atención y para procesar tanta información. El tener que procesar una segunda tarea simultáneamente únicamente le provoca una gran distracción y perjuicio durante la prueba.""",

    'no deterioro y buen T2':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 no se ha visto apenas afectada, a la vez que se mantuvo un buen rendimiento en la segunda tarea. Esto sugiere una preferencia y prevalencia de un estilo atencional caracterizado por una distribución paralela de la atención. A fin de atender y responder efectivamente a las dos tareas, {nombre} opta por hacer más difuso y amplio su foco atencional. Manteniendo así una atención estable y simultánea para las dos tareas.""",

    'no deterioro y mal T2 P':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 no se ha visto apenas afectada, aunque la respuesta a la tarea 2 ha resultado insuficiente, en particular con relación a una precisión de la respuesta inferior a lo esperado. Esto puede señalar dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, sugiere una preferencia y tendencia a focalizar todos los recursos cognitivos en una única tarea.""",

    'no deterioro y mal T2 TR':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 no se ha visto apenas afectada, aunque la respuesta a la tarea 2 ha resultado insuficiente, en particular con relación a una lentitud en la respuesta mayor a lo esperado. Esto puede señalar dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, sugiere una preferencia y tendencia a focalizar todos los recursos cognitivos en una única tarea.""",

    'no deterioro y mal T2 P y TR':"""Por otro lado, en los momentos en que hubo concurrencia entre tareas y mayor demanda atencional, la precisión de seguimiento en la tarea 1 no se ha visto apenas afectada, aunque la respuesta a la tarea 2 ha resultado insuficiente, con relación tanto a la baja precisión como a la lentitud de la respuesta. Esto puede señalar dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, sugiere una preferencia y tendencia a focalizar todos los recursos cognitivos en una única tarea.""",
}


PARRAFO_DUALTASK_PSV = {
    'bajo':"""
En la tarea 1 la precisión del seguimiento visomotor ha sido inferior al promedio; señalando así dificultades en las capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir. Dificultades en esta dimensión representa una mayor probabilidad de presentar problemas de disgrafía.""",

    'normal':""" 
En la tarea 1 la precisión del seguimiento visomotor ha resultado normal, y tanto así las adecuadas capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir.""",

    'alto':"""
En la tarea 1 la precisión del seguimiento visomotor ha sido superior al promedio, y tanto así las sobresalientes capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir.""",
}


PARRAFO_DUALTASK_A = {

    'A bajo':"""Avanzamos entonces a los resultados de la tarea 2. En primer lugar, {nombre} muestra un porcentaje de aciertos bajo, lo que indica complicaciones para completar eficientemente la tarea presentada. Esto señala que la capacidad atencional en general resulta inferior a la media para su edad.""",

    'A normal':"""Avanzamos entonces a los resultados de la tarea 2. En primer lugar, {nombre} muestra un porcentaje de aciertos normal, lo que indica una capacidad atencional en general adecuada a la esperada para su edad.""",
    
    'A alto':"""Avanzamos entonces a los resultados de la tarea 2. En primer lugar, {nombre} muestra un porcentaje de aciertos alto, lo que indica una capacidad atencional en general superior a la media para su edad.""",
}


PARRAFO_DUALTASK_C = {

    'C bajo':"""Respecto al número de errores de comisión, este fue bajo. Es decir, que pocas veces {nombre} emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente, y una muy baja impulsividad.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal. Es decir, que {nombre} emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",

    'C alto':"""Respecto al número de errores de comisión, este fue alto. Es decir, que {nombre} emite un número de respuestas erróneas superior a lo esperado para su edad. Este resultado puede señalar dos cosas: una capacidad inferior al promedio para discriminar la información de manera eficiente, y/o un nivel de impulsividad superior al esperado para su edad.""",
}

# Añadir este PARRAFO_TR_A_vs_C sólo cuando C es normal o alto
PARRAFO_DUALTASK_TR_A_vs_C = {
'C normal y TR_A_vs_C positivo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una mayor velocidad de respuesta en comparación con los aciertos. Esto señala que los errores de precisión se deben a respuestas más impulsivas.""",
'C normal y TR_A_vs_C negativo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto señala que los errores de precisión se deben, no tanto a un problema de impulsividad, pero a dificultades puntuales en la percepción y el procesamiento de la información.""",

'C alto y TR_A_vs_C positivo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una mayor velocidad de respuesta en comparación con los aciertos. Esto señala que el problema atencional está especialmente vinculado a una elevada impulsividad, con respuestas más rápidas pero menos precisas.""",
'C alto y TR_A_vs_C negativo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto señala que el problema atencional no está tan vinculado a la impulsividad, sino a importantes dificultades en la percepción y el procesamiento de la información, que incapacitan a {nombre} para discriminar la información de manera eficiente.""",

}

PARRAFO_DUALTASK_O = {
    'O bajo':"""En relación al número de errores de omisión, este resulta bajo. Esto significa que pocas veces no se ha respondido cuando se debería. Este resultado señala una velocidad de procesamiento de la información y de toma de decisiones bien ajustada a la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad superior al promedio para mantener la atención sostenida a lo largo de la tarea, sin distraerse o fatigarse, de manera que se dificulte emitir una respuesta en los momentos oportunos.""",

    'O normal':"""En relación al número de errores de omisión, este resulta normal, Esto significa que no se ha respondido cuando se debería un número de veces igual a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones adecuada a la exigencia temporal de la tarea. Este índice también puede señalar una capacidad adecuada para mantener la atención sostenida a lo largo de la tarea, sin distraerse o fatigarse demasiado, de manera que se dificulte emitir una respuesta en los momentos oportunos.""",
    
    'O alto':"""En relación al número de errores de omisión, este resulta alto. Esto significa que no se ha respondido cuando se debería un número de veces superior a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones demasiado lenta para la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad inferior al promedio para mantener la atención sostenida a lo largo de la tarea: con tendencia a distraerse o fatigarse, lo que le dificulta emitir una respuesta en los momentos oportunos.""",
}

# Parrafo condicional de C para posibilidad de identificar la prevalencia de un estilo atencional reflexivo o impulsivo
PARRAFO_DUALTASK_TR = {

    'TR bajo y rendimiento C igual':"""Por último, {nombre} muestra un tiempo de respuesta bajo, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",
    'TR bajo y rendimiento C menor':"""Por último, {nombre} muestra un tiempo de respuesta bajo, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad. Aunque esta mayor velocidad también puede deberse a la evidente preferencia o tendencia de {nombre} por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas.""",

    'TR normal':"""Por último, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",
    
    'TR alto y rendimiento C igual':"""Por último, {nombre} muestra un tiempo de respuesta elevado, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Este resultado puede señala que {nombre} requiere de más tiempo para procesar la misma cantidad de información que otros individuos de su edad.""",
    'TR alto y rendimiento C mayor':"""Por último, {nombre} muestra un tiempo de respuesta elevado, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Este resultado puede señalar dos fenómenos diferentes: la necesidad de {nombre} de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. Y la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",


}

#F_A si fatiga (diferencia significativa) en precisión T1, F_TR en TR T2, TR_PSV si precisión T1
PARRAFO_DUALTASK_Fatiga = {
    
    'no F':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. A lo cual, resulta que no se ha encontrado indicio de cansancio en ninguna de las dimensiones cognitivas y atencionales evaluada, lo que indica una buena resistencia y capacidad de atención cognitiva.""",

    'F_PSV':"""Queda comparar el rendimiento de {nombre} hacia el  principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado indicios una rápida aparición cansancio y fatiga, consistente en un progresivo peor rendimiento en la precisión de seguimiento visomotor de la tarea 1. Es decir, dificultad para mantener la atención sostenida con el paso del tiempo.
       """,
    
    'F_A':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado indicios una rápida aparición de cansancio y fatiga, consistente en un progresivo peor rendimiento en la precisión en la tarea 2. Es decir, dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa.""",

    'F_TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado indicios una rápida aparición de cansancio y fatiga, consistente en un progresivo peor rendimiento en la velocidad de procesamiento y respuesta en la tarea 2. Es decir, dificultad para mantener un ritmo acelerado en el despeño de la tarea.""",

    'F_PSV y F_A':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga. Consistente en un progresivo peor rendimiento en la precisión de seguimiento visomotor de la tarea 1. Esto indica una aparición rápida de fatiga cognitiva y dificultades para mantener la atención sostenida con el paso del tiempo. La fatiga también ha provocado un deterioro de la precisión en la segunda tarea. Esto es, dificultades para mantener la precisión con la que se discrimina, atiende y responde a la información relevante frente la irrelevante y engañosa.""",

    'F_PSV y F_TR':""""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga. Consistente en un progresivo peor rendimiento en la precisión de seguimiento visomotor de la tarea 1. Esto indica una aparición rápida de fatiga cognitiva y dificultades para mantener la atención sostenida con el paso del tiempo. La fatiga también ha provocado un deterioro del tiempo de respuesta la segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",
    
    'F_A y F_TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga durante la prueba. Consistente en un progresivo peor rendimiento en la precisión en la tarea 2, y dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa. La fatiga también ha provocado un deterioro del tiempo de respuesta en esta segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",

    'F_PSV, F_A y F_TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga durante la prueba, viéndose afectado su rendimiento en todos los índices de la prueba, incluyendo: la precisión de seguimiento visomotor de la tarea 1 o dificultades para mantener la atención sostenida en general. Una reducción de la precisión en la tarea 2, y dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa. Y, finalmente, un deterioro del tiempo de respuesta en la segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",
    }

# Este Párrafo_automatización puede no añadirse si no hay una diferencia significativa positiva del último tercio de la prueba frente al primero.
PARRAFO_DUALTASK_automatización = {
    'Automatización_PSV':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma. Esta facilidad para automatizar tareas sostenidas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_TR':"""Por otro lado, se ha observado una mejora del rendimiento en la velocidad de procesamiento y respuesta en la tarea 2. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma, aumentando la velocidad con la que se ejecuta. Esta facilidad para automatizar una tarea puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de respuesta en la tarea 2. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma, mejorando la efectividad con la que se ejecuta. Esta facilidad para automatizar una tarea puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_PSV_y_TR':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1 y velocidad de procesamiento y respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas y procedimientos de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_PSV_y_P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1, y la precisión de respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas y procedimientos de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_TR_y_P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión y velocidad de respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización_PSV, TR_y_P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1 y precisión y velocidad de procesamiento y respuesta en la tarea 2. Esto señala una capacidad excelente para adaptarse a las reglas de una tarea y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",
    }

PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK = {

    'intro':"Finalmente, se indican algunas recomendaciones para trabajar con {nombre} en las próximas sesiones.",

# Este PARRAFO es opcional, condicional de si el rendimiento es muy diferente entre T1 (PSV) y T2 (A-E y TR), uno bajo y otro alto, o uno normal y otro bajo.
    'PARRAFO_DUALTASK_final_inestable_negativo_o_muy_inestable':"Dado el rendimiento variable entre tareas, cabe hacer más evaluación y entrenamiento en torno a la capacidad de {nombre} para dirigir su atención ante tareas dinámicas, y aumentar su capacidad de memoria de trabajo para poder manejar más cantidad y diversidad de información en un mismo momento.",

# Este PARRAFO es opcional, condicional de si el rendimiento es diferente entre T1 (PSV) y T2 (A-E y TR) y T1 alto y T2 normal.
    'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_positivo':"Se ha observado una preferencia o mejor aptitud para las actividades que demandan una atención sostenida y de concentración prolongada y estable.",

# Este PARRAFO es opcional, condicional de si el rendimiento es diferente entre T1 (PSV) y T2 (A-E y TR) y T1 normal o alto y T2 bajo
    'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_negativo':"En este contexto, se ha encontrado una clara preferencia o mejor aptitud para el desempeño de la tarea más relacionada con la atención sostenida y concentración prolongada y estable. Esto supone una fortaleza desde la que trabajar y mejorar la atención y cognición. {nombre} parece poder implicarse y mantenerse bien concentrado en una misma tarea por suficiente tiempo. Es recomendable aprovechar esta capacidad para implicar a {nombre] en la ejecución de actividades de entrenamiento de las habilidades atencionales que se han visto más deficientes: la memoria de trabajo, el control voluntario de la atención, y la atención discriminativa, o capacidad para distinguir rápidamente que nueva información es relevante o irrelevante para la tarea u objetivo a desempeñar.""",

# Este PARRAFO es opcional, condicional de si el rendimiento es diferente entre T1 (PSV) y T2 (A-E y TR) y T2 alto y T1 normal.
    'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_positivo':"Se ha observado una preferencia o mejor aptitud para las actividades que demandan una atención responsiva basada en reflejos y respuestas rápidas a estímulos disruptivos.",

# Este PARRAFO es opcional, condicional de si el rendimiento es diferente entre T1 (PSV) y T2 (A-E y TR) y T2 normal o alto y T1 bajo.
    'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_negativo':"En este contexto, se ha encontrado una clara preferencia o mejor aptitud para el desempeño de la tarea más relacionada con la atención disruptiva basada en reflejos. Esto es, acciones que demandan un procesamiento y respuesta rápida a información novedosa o inesperada. Esto supone una fortaleza desde la que trabajar y mejorar la atención y cognición. {nombre} parece poder realizar análisis rápidos y efectivos de la información, distinguiendo la información relevante de la irrelevante o engañosa. Esto supone una buena aptitud para actividades estimulantes y reactivas, incluso frenéticas. Sin embargo, otras áreas atencionales parecen presentar dificultades, tales como:  la memoria de trabajo, el control voluntario de la atención, y la atención sostenida, o capacidad para mantenerse concentrado en una misma tarea menos estimulante por el tiempo suficiente. En este sentido, resulta necesario explicar a {nombre} la importancia de tener un control intrínseco y voluntario de la atención propia, y ser capaz de mantenerse concentrado por un tiempo en actividades menos estimulante. Para esto conviene implicar a {nombre} en actividades tranquilas que demanden una atención constante e intencional o guiada por la persona, tales como: puzle, juegos de mesa, pintar, leer, natación y caminar.",

# Este PARRAFO es opcional, condicional de si el rendimiento en T1 (promedio PSV) es significativamente peor en eventos de concurrencia (mediciones 0.2 y 0.4 después de estímulo T2) frente eventos independientes. Y además el rendimiento en T2 (en A-E o TR) es bajo.
    'PARRAFO_DUALTASK_final_concurrencia_peorT1_malT2':"Otro aspecto es que la distribución de recursos atencionales al tener que procesar dos tareas simultáneamente ha resultado deficiente, provocando distracción, confusión y mal desempeño. Por lo que es recomendable para {nombre} instaurar un método de trabajo ordenado y focalizado. Atendiendo y realizando una única tarea en cada momento, y maximizando así los recursos cognitivos que a esta se le dedica.",

# Este PARRAFO es opcional, condicional de si el rendimiento en T1 (promedio PSV) es bajo
    'PARRAFO_DUALTASK_final_PSV_bajo':"De nuevo, remarcar la importancia de realizar una evaluación más exhaustiva de las habilidades de movimiento fino y coordinación ojo mano, que en esta prueba se han visto insuficientes para lo normal o esperado para su edad, y que pueden indicar un problema de disgrafía. De confirmarse esto en próximas evaluaciones, se recomienda entrenar dicha habilidad con actividades tales como: caligrafía, construcción con piezas Lego, o videojuegos con movimiento preciso (plataforma, acción, aventura…).",

# Este PARRAFO es opcional, condicional de si algún índice de fatiga resulta significativo. Esto es, una diferencia significativa entre el rendimiento del primer tercio de la prueba y el último tercio de la prueba, en alguna de las dimensiones evaluadas: precisión de seguimiento visomotor, precisión de respuesta en la tarea 2, o tiempo de respuesta en la tarea 2.
    'PARRAFO_DUALTASK_final_fatiga ':"""Respecto al evidente cansancio o fatiga originado hacia el final de la prueba, hay que destacar que esta es una actividad de 2 minutos de duración. Puede ser conveniente en este aspecto entrenar la resistencia de {nombre} a la fatiga cognitiva ante tareas de alta demanda cognitiva. Esto le ayudará a poder mantener su concentración y ritmo de trabajo durante más tiempo ante tareas más dinámicas y complejas. Por ejemplo, ante cálculos matemáticos complejos, síntesis de información, razonamiento contrafactual, interacciones sociales, etc.""",

}

# Este PARRAFO es opcional, condicional de si el rendimiento en C en T2 es normal o alto. En este caso elegir la opción impulsividad si TR_C es menor TR_A. Y elegir la opción distraibilidad si TR_C es mayor que TR_A. Si no hay una diferencia significativa entre TR_C y TR_A, no añadir este párrafo.
PARRAFO_DUALTASK_final_dif_TR_A_y_C = {
    'impulsividad':"""La precisión de {nombre} al emitir respuestas acertadas se ha visto perjudicado parece que en gran parte debido a la impulsividad. Esta representa otra área de la atención donde existe margen de mejora.  Y donde se recomiendan actividades de control atencional interno o voluntario. Por ejemplo, con ejercicios de mindfulness, o con la adopción mediante retroalimentación o instrucciones verbales de un estilo atencional y de trabajo más reflexivo, lento pero preciso.""",

    'distraibilidad':"""Se ha registrado un deterioro en la precisión de respuesta en la tarea 2, debido a puntuales fallas de distraibilidad, y durante las cuales el procesamiento de la información de la tarea ha sido mínimo. Es importante valorar el grado de deterioro en el rendimiento de la tarea T2. Ya que de ser alto, esto significaría un problema de distraibilidad persistente y de importante interferencia en el adecuado desempeño atencional."""
    }



# ============================================================================
# 4. FINAL
# ============================================================================

# Párrafo de síntesis final con rendimiento PT en el las dimensiones a evaluar.

PARRAFO_sintesis_arousal = {
    # Si solo 1 de los 4 índices es desfavorable
    'poco malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente normal, a excepción de algún caso puntual (tarea {tarea_deficit_arousal}) donde este aspecto ha resultado inferior.""",

    # Si 2 o 3 de 4 desfavorables
    'malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente deficiente, en especial durante las tareas {tarea_deficit_arousal}. Esto perjudica el rendimiento en el resto de índices atencionales evaluados, y sesga la fiabilidad con la que se pueden medir en detalle estas dimensiones.""",

    # Si 4 de 4 desfavorables
    'muy malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completamente deficiente en todas las pruebas: {tarea_deficit_arousal}. Esto puede suponer una falla atencional muy grave, o bien la nulidad de la prueba. Pues un resultado tan negativo también puede deberse a una completa falta de entendimiento o actividad durante el desempeño de la tarea. Esto perjudica enormemente el rendimiento en el resto de índices atencionales evaluados, y sesga la fiabilidad con la que se pueden medir en detalle estas dimensiones.""",

    # Si todo normal
    'normal':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completamente normal en todas las pruebas. Esto señala un adecuado estado de activación durante toda la evaluación, lo que ya sugiere un estado atencional general favorable y una mayor fiabilidad de los resultados obtenidos en el resto de dimensiones evaluadas.""",

    # Si algunos desfavorables y otros, en menor medida, favorables
    'malo y poco bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente desfavorable: {tarea_deficit_arousal}. Aunque este problema parece desaparecer o incluso revertirse en otras pruebas: {tarea_fortaleza_arousal}. Parece que {nombre} ha estado más dormido o despierto según la prueba. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado muy variable, con un estado significativamente más despierto ante la(s) prueba(s) {tarea_fortaleza_arousal}, y más dormido durante {tarea_deficit_arousal}. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente superior: {tarea_fortaleza_arousal}. Aunque con excepciones puntuales donde esta atención general ha decrecido, incluso hasta el punto de resultar deficiente; {tarea_deficit_arousal}. Parece que {nombre} ha estado excepcionalmente más dormido o despierto según la prueba. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si solo 1 de los 4 índices es favorable
    'poco bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado adecuado, e incluso excepcionalmente favorable en algún caso puntual (tarea {tarea_fortaleza_arousal}). Esto favorece el rendimiento en el resto de índices atencionales evaluados, así como la fiabilidad en la medición en detalle de estas dimensiones.""",

    # Si 2 o 3 de 4 favorables
    'bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha mayormente favorable, e incluso excepcional durante las tareas {tarea_fortaleza_arousal}. Esto favorece el rendimiento en el resto de índices atencionales evaluados, así como la fiabilidad en la medición en detalle de estas dimensiones.""",

    # Si 4 de 4 favorables
    'muy bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completa y excepcionalmente favorable durante todas las pruebas. Esto favorece enormemente el rendimiento en el resto de índices atencionales evaluados, así como la fiabilidad en la medición en detalle de estas dimensiones.""",
    }


PARRAFO_sintesis_atencionsostenida = {
    # Si solo 1 o 2 de los 6 índices es desfavorable
    'poco malo':"""El siguiente aspecto a revisar es el de atención sostenida. En este sentido el desempeño ha sido mayormente normal y adecuado, pero con algún problema puntual en la parte de {tarea_deficit_atencionsostenida}. Esto señala una puntual incapacidad para mantener una atención prolongada durante una misma tarea, que debido a sus particularidades resultó especialmente aburrido o agotador""",

    # Si entre 3 y 4 desfavorables
    'malo':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido mayormente desfavorable, con especial deterioro en la parte de {tarea_deficit_atencionsostenida}. Esto señala un patrón de vulnerabilidad a la fatiga, e incapacidad más generalizada para mantener una atención prolongada.""",
    
    # Si entre 5 y 6 desfavorables
    'muy malo':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido completamente desfavorable en todas las pruebas. Esto señala una clara e importante vulnerabilidad a la fatiga, y significativa incapacidad generalizada para mantener una atención prolongada.""",

    # Si todo normal
    'normal':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido completamente normal en todas las pruebas. Esto señala una resistencia normal a la fatiga, y capacidad para mantener una atención prolongada en una misma tarea, independientemente de cuán estimulante o aburrida sea esta.""",

    # Si entre 2 y 3 desfavorables y otros, en menor medida, favorables
    'poco malo y poco bueno':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido mayormente desfavorable: {tarea_deficit_atencionsostenida}. Aunque este problema parece desaparecer o incluso revertirse en otras partes: {tarea_fortaleza_atencionsostenida}. Esto sugiere que {nombre} puede mantener su atención y resistir la fatiga mejor o peor dependiendo de lo estimulante o aburrida/saturante que le resulte una tarea.""",

    # Si entre 4 y 5 desfavorables y otros, en menor medida, favorables
    'muy malo y poco bueno':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido mayormente desfavorable: {tarea_deficit_atencionsostenida}. Aunque este problema parece desaparecer o incluso revertirse en otras partes: {tarea_fortaleza_atencionsostenida}. Esto sugiere que {nombre} solo puede mantener su atención y resistir la fatiga ante unas pocas tareas específicas que no le aburren o saturan.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido muy variable, con un rendimiento deficiente el alguna(s) parte(s): {tarea_deficit_atencionsostenida}, y excepcionalmente bueno en otra(s): {tarea_fortaleza_atencionsostenida}. Esto sugiere que la capacidad de {nombre} para mantener su atención y resistir la fatiga es altamente dependiente de las particularidades de la tarea. Pudiendo tanto mantener un hiperfoco en aquellas tareas que le estimulan o interesan, como descuidar drásticamente su desempeño ante tareas que le aburren o saturan.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido variable, mayormente favorable ({tarea_fortaleza_atencionsostenida}) pero con puntual desempeño deficiente en otra(s) parte(s): {tarea_fortaleza_atencionsostenida}. Esto sugiere que {nombre} puede, en su mayoría, mantener una atención prolongada y resistir la fatiga. Aunque en ocasiones puntuales, quizás ante un cansancio acumulado o falta de estimulación excesiva también puede llegar a descuidar en exceso su desempeño.""",
 
    # Si entre 1 y 2 favorables
    'poco bueno':""""El siguiente aspecto a revisar es el de atención sostenida. En este sentido el desempeño ha sido adecuado, e incluso sobresaliente en alguna parte puntual: {tarea_fortaleza_atencionsostenida}. Esto señala una capacidad muy buena para mantener una atención prolongada durante una misma tarea.""",


    # Si entre 3 y 4 favorables
    'bueno':"""El siguiente aspecto a revisar es el de atención sostenida. En este sentido el desempeño ha sido sobresaliente, en especial en las partes de: {tarea_fortaleza_atencionsostenida}. Esto señala una capacidad especialmente sobresaliente para mantener una atención prolongada durante una misma tarea. Esto es indicativo de altas capacidades.""",

    # Si entre 5 y 6 favorables
    'muy bueno':"""El siguiente aspecto a revisar es el de atención sostenida. En este sentido el desempeño ha sido completamente excelente y superior a lo normal o esperado. Esto señala una capacidad excepcional para mantener una atención prolongada durante una misma tarea. Esto es indicativo de altas capacidades.""",

}


PARRAFO_sintesis_controlejecutivo = {
    # Si solo 1 o 2 de los 8 índices es desfavorable
    'poco malo':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido normal en su mayoría, a excepción de algún caso puntual de rendimiento defiente: {tarea_deficit_controlejecutivo}. En general, {nombre} puede discriminar la información relevante e irrelevante e inhibir respuestas impulsivas de manera adecuada. Aunque debido bien al cansancio/saturación acumulado, o la dificultad de la tarea, puede eventualmente presentar dificultades para mantener una atención selectiva y control inhibitorio adecuado.""",
    
    # Si entre 3 y 4 desfavorables
    'malo':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido desfavorable, en particular en las partes de: {tarea_deficit_controlejecutivo}. No siempre pero frecuentemente {nombre} presenta importantes dificultades para discriminar la información relevante e irrelevante e inhibir las respuestas impulsivas.""",

    # Si entre 5 y 6 y 8 desfavorables
    'muy malo':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido completamente deficiente en todas las partes de la evaluación. Un resultado tan negativo suele significar la nulidad de la prueba, que más probablemente ha sido contestada de manera aleatoria y sin intención de acertar. Aunque menos probable, si ciertamente {nombre} ha intentado responder correctamente, este resultado significaría una completa discapacidad para discriminar la información relevante e irrelevante y/o inhibir las respuestas impulsivas.""",

    # Si todo normal
    'normal':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha completamente normal. {nombre} puede discriminar la información relevante e irrelevante e inhibir respuestas impulsivas de manera adecuada.""",
    
    # Si entre 2 y 3 desfavorables y otros, en menor medida, favorables
    'malo y poco bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido variable. Aunque mayormente el rendimiento fue adecuado o incluso excelente: {tarea_fortaleza_controlejecutivo}, también existe algún caso puntual de rendimiento deficiente: {tarea_deficit_controlejecutivo}. En general, {nombre} discrimina bien la información relevante e irrelevante e inhibe sus respuestas impulsivas de manera adecuada. Aunque eventualmente ante la acumulación de cansancio/saturación acumulado, o una mayor dificultad de tarea, también puede llegar a presentar dificultades significativas para mantener una atención selectiva y control inhibitorio adecuado.""",

    # Si entre 4 y 7 desfavorables y otros, en menor medida, favorables
    'muy malo y poco bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento es mayoritariamente deficiente: {tarea_deficit_controlejecutivo}. Aunque también existe algún caso de rendimiento adecuado o incluso excelente: {tarea_fortaleza_controlejecutivo}. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. Aunque siguiendo la tendencia mayoritaria {nombre} parece presentar una importante dificultad para discriminar la información relevante e irrelevante e inhibir respuestas impulsivas de manera adecuada. Sin embargo, esta discapacidad puede verse solventada o incluso revertida ante tareas de mayor sencillez perceptiva que otorgan un mayor tiempo de reflexión y autocontrol antes de la emisión de la respuesta.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). Aquí el rendimiento ha sido muy variable, con un rendimiento deficiente el alguna(s) parte(s): {tarea_deficit_controlejecutivo}, y excepcionalmente bueno en otra(s): {tarea_fortaleza_controlejecutivo}. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. Sin embargo, podemos decir que, en general, {nombre} presenta una capacidad adecuada para discriminar la información relevante e irrelevante e inhibir respuestas impulsivas. Aunque esta capacidad varia significativamente entre tareas, llegando a ser inferior y deficiente ante tareas de mayor complejidad perceptiva o con menor tiempo para la reflexión y el autocontrol antes de la emisión de la respuesta.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). Aquí el rendimiento ha sido en su mayoría favorable o incluso excelente en las partes de {tarea_fortaleza_controlejecutivo}. Sin embargo, también existe alguna(s) parte(s) donde contrariamente el control ejecutivo ha resultado deficiente ({tarea_fortaleza_controlejecutivo}). Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. Siguiendo la tendencia mayoritaria, parece que {nombre} presenta una capacidad excelente para discriminar la información relevante e irrelevante e inhibir respuestas impulsivas. Aunque esta capacidad también puede variar puntual pero drásticamente ante tareas particulares, en función de la complejidad perceptiva o la velocidad de respuesta requerida.""",

    # Si entre 1 y 2 favorables
    'poco bueno':""""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido adecuado en su mayoría, e incluso excelente en algún caso ({tarea_fortaleza_controlejecutivo}). {nombre} tiene muy buena capacidad para discriminar la información relevante e irrelevante e inhibir respuestas impulsivas.""",
    
    # Si entre 3 y 4 favorables
    'bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido favorable e incluso excelente en varias partes: {tarea_fortaleza_controlejecutivo}. {nombre} tiene una capacidad excepcional para discriminar la información relevante e irrelevante e inhibir las respuestas impulsivas. Esto es indicativo de altas capacidades.""",

    # Si entre 5 y 6 y 7 favorables
    'muy bueno':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido excepcional. {nombre} tiene una capacidad muy por encima del promedio para discriminar la información relevante e irrelevante e inhibir las respuestas impulsivas. Esto es indicativo de altas capacidades.""",

}


PARRAFO_sintesis_flexibilidadcognitiva = {
# Tono menos contundente (parece) porque esta dimensión se mide con un único índice.
    'malo':"""Seguidamente está el aspecto de la flexibilidad cognitiva, o capacidad para cambiar rápidamente el foco atencional y adaptarse a nuevas reglas de ejecución de la tarea. La atención en este sentido ha resultado desfavorable. La capacidad de concentración de {nombre} está caracterizada por una excesiva rigidez cognitiva, dificultad para cambiar rápidamente la forma en la que atiende, procesa y responde a la información.""",

    'normal':"""Seguidamente está el aspecto de la flexibilidad cognitiva, o capacidad para cambiar rápidamente el foco atencional y adaptarse a nuevas reglas de ejecución de la tarea. La atención en este sentido ha resultado normal. {nombre} tiene una capacidad adecuada a lo esperable para cambiar rápidamente la forma en la que atiende, procesa y responde a la información.""",

    'bueno':"""Seguidamente está el aspecto de la flexibilidad cognitiva, o capacidad para cambiar rápidamente el foco atencional y adaptarse a nuevas reglas de ejecución de la tarea. La atención en este sentido ha resultado sobresaliente. La capacidad de concentración de {nombre} está caracterizada por una flexibilidad cognitiva mayor a lo esperado, con notable facilidad para cambiar rápidamente la forma en la que atiende, procesa y responde a la información.""",
}

PARRAFO_sintesis_memoriatrabajo = {
# Tono menos contundente (parece) porque esta dimensión se mide con un único índice.
    'malo':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento deficiente. Esto sugiere cierta dificultad para procesar y responder adecuadamente ante tareas complejs que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",

    'normal':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento normal. Esto sugiere una capacidad adecuada para procesar y responder ante tareas complejas que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",

    'bueno':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento excelente. Esto sugiere una capacidad por encima del promedio para procesar y responder ante tareas complejas que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",
}


PARRAFO_sintesis_velocidadprocesamiento = {
    # Si solo 1 de los 5 índices es desfavorable
    'poco malo':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento normal en la mayoría de las pruebas, aunque con ocasional deterioro significativo en la parte de {tarea_deficit_velocidadprocesamiento}. Normalmente {nombre} procesa la información a una velocidad adecuada. Aunque en algún caso puntual debido quizás a la fatiga acumulada o la dificultad de la tarea, puede ralentizarse más de lo esperable.""",

    # Si entre 2 y 3 desfavorables
    'malo':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento deficiente: {tarea_deficit_velocidadprocesamiento}. {nombre} presenta una velocidad de procesamiento y respuesta especialmente lenta, lo que le dificulta o incapacidad dar respuestas precisas rápidas cuando es necesario.""",

    # Si entre 4 y 5 desfavorables
    'muy malo':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento completamente deficiente en todas o casi todas las pruebas. {nombre} presenta una velocidad de procesamiento y respuesta escepcionalmente lenta. Un resultado tan negativo más probable significa la nulidad de la evaluación, debido a la ausencia de participación activa y seria durante las pruebas. De no ser este el caso, esto reflejaría una muy grave dificultad e incapacidad para responder rápidamente cuando es necesario.""",

    # Si todo normal
    'normal':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento completamente normal. {nombre} procesa y responde a la información en un tiempo adecuado o igual a lo esperable.""",

    # Si 1 favorable 2 no
    'malo y poco bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento variable. En la mayoría de casos el rendimiento fue normal, o incluso excepcionalmente bueno en {tarea_fortaleza_velocidadprocesamiento}. Sin embargo, también hay un par de casos en los que el desempeño resulto deficiente: {tarea_deficit_velocidadprocesamiento}. Parece que, en general, {nombre} presenta una velocidad de procesamiento y respuesta adecuada. Aunque también existen casos puntuales en los que, quizás debido a la fatiga acumulada o la dificultad de la tarea, la respuesta puede ralentizarse notablemente.""",

    # Si 1 o 2 favorable y 3 no, o 4 desfavorable y 1 no
    'muy malo y poco bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy variable. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo, pues puede ser prueba de una ejecución aleatoria de la tarea. En caso contrario y siguiendo la prevalencia mayoritaria, {nombre} parece presentar una deficiente velocidad de procesamiento que le imposibilita dar respuesta rápidas en la mayoría de casos: {tarea_deficit_velocidadprocesamiento}. Aunque este problema parece solventarse o incluso revertirse en algún(os) caso(s), como ante {tarea_fortaleza_velocidadprocesamiento}. Si estos resultados son representativos de una ejecución seria de la prueba, cabe indagar más acerca de esta variabilidad, que puede deberse por ejemplo a una especial dificultad para lidiar con la fatiga acumulada o la creciente dificultad de una tarea.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy variable. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. De ser un resultado de una ejecución seria de la tarea, {nombre} presentaría una velocidad sumamente variable entre tareas mostrando en ocasiones un rendimiento normal, con ocasional rendimiento excelente ({tarea_fortaleza_velocidadprocesamiento}) o insuficiente ({tarea_deficit_velocidadprocesamiento}). En tal caso, cabe indagar más acerca de esta variabilidad, que puede verse afectada por otras variables tales como la fatiga acumulada o la dificultad y otras particularidades de cada tarea.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento mayormente favorable, e incluso sobresaliente en algunos casos: {tarea_fortaleza_velocidadprocesamiento}. Sin embargo, este rendimiento es variable, y también se ha observado un desempeño insuficiente en alguna(s) parte(s): ({tarea_deficit_velocidadprocesamiento}. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. Basándonos en la prevalencia mayoritaria, parece que normalmente {nombre} procesa la información a una velocidad adecuada o incluso por encima del promedio. Aunque también existe el caso en que, quizás debido a la fatiga acumulada o la dificultad de la tarea, la respuesta puede ralentizarse drásticamente.""",

    # Si 1 favorable
    'poco bueno':""""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento normal, e incluso escepcionalmente bueno en alguna ocasión ({tarea_fortaleza_velocidadprocesamiento}. {nombre} puede procesar y responder a la información a una velocidad adecuada o incluso superior al promedio.""",

    # Si entre 2 y 3 favorables
    'bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento excelente, en especial en la parte de {tarea_fortaleza_velocidadprocesamiento}. {nombre} puede procesar y responder a la información a una velocidad escepcionalmente rápida. Esto es indicativo de altas capacidades""",

    # Si entre 4 y 5 favorables
    'muy bueno':"""Finalmente, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy por encima del promedio durante todas las pruebas. {nombre} procesa y responde a la información a una velocidad escepcionalmente rápida. Esto es indicativo de altas capacidades""",

}



PARRAFO_sintesis_final = {
# Álvaro. Revisar distribución (frecuencia típica) de PTs fuera de la norma. Después decidir si añadir más párrafos con distinción entre deficiencias puntuales o más constantes dentro de una misma dimensión.
    
# Muy malo: 10 o más    Disperso
    'muy malo disperso':"""Finalmente, {nombre} con más o menos excepción, ha mostrado un rendimiento muy deficiente en gran parte de la evaluación.
    Además se puede ver que estas dificultades atencionales se presentaron dispersas entre las diferentes dimensiones y pruebas atencionales evaluadas.
    Un resultado tan negativo puede ser señal de nulidad de la prueba. Esto es, que la ejecución de la prueba no haya sido seria, y por tanto tampoco los resultados
    serían representativos de la capacidad atencional real de {nombre}. En caso contrario, si se intento rendir al máximo durante la evaluación, este resultado señala
    una importante discapacidad atencional, y con gran probabilidad la presencia de un trastorno del neurodesarrollo. Una mayor evaluación e intervención al respecto
    es necesaria para mejorar las competencias cognitivas de {nombre} y su autonomía.""",
       
#Muy malo: 10 o más    Foco en una misma dimensión atencional
    'muy malo focalizado area atencional':"""Finalmente, {nombre} con más o menos excepción, ha mostrado un rendimiento muy deficiente en gran parte de la evaluación.
    Un resultado tan negativo puede ser señal de nulidad de la prueba. Esto es, que la ejecución de la prueba no haya sido seria, y por tanto tampoco los resultados
    serían representativos de la capacidad atencional real de {nombre}. La otra explicación factible es que exista
    una importante discapacidad atencional, y con gran probabilidad la presencia de un trastorno del neurodesarrollo.
    En este caso además se puede ver que estas dificultades se encuentran más localizadas en torno a una dimensión atencional concreta, en particular, {dimension_afectada}, por lo que esta segunda explicación es más viable.
    Dado el alto nivel de interferencia e incapacitación que estas dificultades atencionales provocan, es necesaria una mayor evaluación e intervención futura específica de estas áreas afectadas. Esto a fin de
    mejorar las competencias cognitivas de {nombre} y su autonomía.""",
     
# Muy malo: 10 o más    Foco en una misma tarea
    'muy malo focalizado tarea':"""Finalmente, {nombre} con más o menos excepción, ha mostrado un rendimiento muy deficiente en gran parte de la evaluación.
    Un resultado tan negativo puede ser señal de nulidad de la prueba. Esto es, que la ejecución de la prueba no haya sido seria, y por tanto tampoco los resultados
    serían representativos de la capacidad atencional real de {nombre}. En este caso además se puede ver que estas dificultades se encuentran más localizadas en torno a unas pocas pruebas {prueba_afectada},
    por lo que es más factible la explicación de que este resultado se deba más a una falta de rigor en el entendimiento o ejecución de alguna(s) prueba(s) en específico.
    Igualmente, este resultado salta las alarmas sobre la posible presencia de un trastorno del neurodesarrollo. Por lo tanto, una mayor evaluación e intervención al respecto
    es necesaria para mejorar las competencias cognitivas de {nombre}.""",
    
# Malo: Entre 5 y 9 bajas y no altas    Disperso
    'malo':"""Finalmente, {nombre} con ha mostrado un rendimiento normal o favorable en algunas partes, pero también defiente en otras.
    Esto señala un rendimiento por debajo del promedio con dificultades importantes en ocasiones concretas. Y puede incluso ser síntoma de 
    la presencia de un trastorno del neurodesarrollo.
    Sin embargo, en este caso actual las dificultades están dispersas entre las distintas dimensiones y pruebas atencionales evaluadas.
    Esto sugiere una afección más generalizada. Así mismo, sería recomendable ahondar en este problema a futuro con más evaluación e intervención. Entrenar la dificultad atencional de {nombre} puede con el tiempo reducir el problema actual 
    mejorando sus competencias cognitivas y autonomía.""",

    # Malo: Entre 5 y 9 bajas y no altas    Foco en una misma dimensión atencional
    'malo':"""Finalmente, {nombre} con ha mostrado un rendimiento normal o favorable en algunas partes, pero también defiente en otras.
    Esto señala un rendimiento por debajo del promedio con dificultades importantes en ocasiones concretas. Y puede incluso ser síntoma de 
    la presencia de un trastorno del neurodesarrollo.
    En este caso además se puede ver que estas dificultades se encuentran más localizadas en torno a una dimensión atencional concreta, en particular, {dimension_afectada}.
    De esta manera a futuro es recomendable continuar con más evaluación e intervención específica de estas áreas afectadas. Entrenar estas áreas afectadas puede con el tiempo reducir la actual interferencia y, en general, 
    mejorar las competencias cognitivas de {nombre} y su autonomía.""",

    # Malo: Entre 5 y 9 bajas y no altas    Foco en una misma tarea
    'malo':"""Finalmente, {nombre} con ha mostrado un rendimiento normal o favorable en algunas partes, pero también defiente en otras.
    En este caso además se puede ver que estas dificultades se encuentran más localizadas en torno a la ejecución en algunas pocas pruebas: {dimension_afectada}.
    Dado esto, cabe primero revisar que este mal desempeño no se debe a ningún otro problema no representativo de la capacidad atencional ocurrido durante la ejecución de estas tareas, por ejemplo: un cansancio excesivo o ejecución pasiva o aleatoria de la prueba.
    De no ser este el caso, este resultado significaría un rendimiento por debajo del promedio con dificultades importantes en ocasiones concretas. Y puede incluso ser síntoma de 
    la presencia de un trastorno del neurodesarrollo. De esta manera a futuro es recomendable realizar más evaluación al respecto, junto con una posible intervención. Entrenar estas áreas afectadas puede con el tiempo reducir la actual interferencia y, en general, 
    mejorar las competencias cognitivas de {nombre} y su autonomía.""",

# Variable mal: 5 o más PTs bajas y algunas menos PTs altas
    'variable mal':"""Finalmente, {nombre} ha mostrado desempeño sumamente variable. Este es un resultado atípico, por lo que se considera que los resultados podrían estar sesgados por otros factores no relacionados con la capacidad atencional de {nombre}, por ejemplo: respuestas aleatorias o ausentes, la presencia de elevada fatiga, entre otras explicaciones. 
    Así pues, se recomienda ahondar más en la evaluación a fin de obtener una representación fiable del rendimiento atencional típico de {nombre}. De ser este el caso actual, los resultados señalan en general un rendimiento atencional desfavorable. Aún existiendo ciertas fortalezas puntuales, también 
    se registraron importantes dificultades, un mayor número de casos en los que la capacidad atencional ha resultado significativamente por debajo del promedio.""",

# Variable bien: 5 o más PTs altas y algunas menos PTs bajas
    'variable bien':"""Finalmente, {nombre} ha mostrado desempeño sumamente variable. Este es un resultado atípico, por lo que se considera que los resultados podrían estar sesgados por otros factores no relacionados con la capacidad atencional de {nombre}, por ejemplo: respuestas aleatorias o ausentes, la presencia de elevada fatiga, entre otras explicaciones. 
    Así pues, se recomienda ahondar más en la evaluación a fin de obtener una representación fiable del rendimiento atencional típico de {nombre}. De ser este el caso actual, los resultados señalan en general un rendimiento atencional favorable. Aún existiendo ciertas dificultades puntuales, también 
    se registraron incluso más potencialidades, o casos de desempeño atencional donde se rindió significativamente por encima del promedio.""",


# Caso Normal: Máx 4 PT baja y/o otras 4 PTs altas de las 23 PTs
    'normal':"""Finalmente, {nombre} ha mostrado un desempeño adecuado, sin deficiencia atencional alguna en cualquiera de las áreas evaluadas. 
    Por lo tanto, no hay motivos para indagar más en estas habilidades neuropsicológicas de la atención y el procesamiento de información. 
    Además queda obsoleta la necesidad de invertir en un refuerzo adicional de estas habilidades que de por si se ajustan a lo normal y esperable para una persona de su edad.""",

# Caso Bueno: 5 o más PTs altas y no 1 o ninguna PT baja
    'bueno':"""Finalmente, {nombre} ha mostrado desempeño adecuado, incluso por encima del promedio. El funcionamiento y capacidad atencional de {nombre} es sobresaliente. 
     Un resultado tan positivo incluso puede ser señal de altas capacidades. Más evaluación al respecto es recomendable ya ante una condición de altas capacidades puede traer también 
     problemas a futuro, tales como desinterés, desapetencia y falta de disciplina. Aunque detectado a tiempo puede ser una fortaleza a aprovechar.""",

# Caso Muy Bueno: 10 o más PTs altas y no PTs baja
    'muy bueno':"""Finalmente, el desempeño ha resultado muy por encima del promedio. El funcionamiento y capacidad atencional de {nombre} es escepcionalmente bueno. 
     Este resultado señala que {nombre} tiene altas capacidades. Una evaluación y consideración especial de esta condición es recomendable, ya que en casos como este se avoga por un reacondicionamiento de 
     la enseñanza recibida a la altura de sus capacidades. Esto a fin de aprovechar este potencial al máximo y evitar la aparición de factores perjudiciales en el aprendizaje, tales como desinterés, desapetencia y falta de disciplina.""",

}