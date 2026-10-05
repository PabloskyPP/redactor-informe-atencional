"""
Módulo con los textos para generar el informe vocacional.
"""

import re

# Añadir funcion markdown con párrafo a resaltar en docx
def poner_en_negrita(texto, *palabras):
    """Marca en negrita (Markdown) las palabras indicadas."""
    for palabra in palabras:
        texto = re.sub(
            rf"(?<!\w)({re.escape(palabra)})(?!\w)",
            r"**\1**",
            texto,
            flags=re.IGNORECASE,
        )
    return texto

# ============================================================================
# PÁRRAFOS FIJOS (siempre se incluyen)
# ============================================================================

PARRAFOS_FIJOS = {
    'titulo_general_prueba': "1. Objetivo de la batería de pruebas.",

    'objetivo_prueba': (
        "Este informe está compuesto por 1 cuestionario (ACS) y 5 pruebas conductuales: ANT, CPT, FourFigures, DigitsMemorization y Dual-Task. "
        "En conjunto, estas pruebas evaluan la capacidad atencional. Como se explica más adelante en detalle, a través de cada prueba se mide un subcomponente de la atención "
        "diferente: velocidad de procesamiento, memoria operativa, atención sostenida, control ejecutivo, flexibilidad cognitiva, etc."
    ),

    'titulo_procedimiento': "2. Descripción de las tareas.",

    'descripcion_procedimiento0': (
        "La prueba tiene una duración total de 40 minutos aproximadamente. A continuación se describen los procedimientos de cada prueba."
    ),

    'descripcion_procedimiento1.1': (
    poner_en_negrita(
        "1) En primer lugar el cuestionario ACS. Al participante se le pide responder (Nada, Algo, Mucho) a un total de 20 preguntas breves vinculadas a diferentes habilidades o problemas atencionales, p.ej: "
        "'Me cuesta concentrarme cuando estoy muy excitado con algo', o 'Puedo rápidamente cambiar de una tarea a otra'.",
        "cuestionario ACS",
        )
    ),

    'descripcion_procedimiento2.1': (
    poner_en_negrita(
        "2) Seguidamente, se comienza la evaluación conductual con la prueba ANT (Atentional Network Test). Aquí la persona tiene que observar una serie de símbolos. "
        "Entre estos, una flecha central horizontal, ⬅ o ➡, de la cual el evaluado tiene que indicar el sentido hacia el que señala (izquierda o derecha). "
        "Sin embargo, esta flecha central se presenta precedida y continuada por otras 2 líneas a cada lado, que pueden ser: simples líneas rectas o flechas, en el mismo u opuesto sentido a la flecha central objetivo. "
        "Véase un ejemplo de estos posibles estímulos centrales en la siguiente imagen:",
        "prueba ANT",
        )
    ),

    'descripcion_procedimiento2.2': (
        "Finalmente, estas flechas aparecen de "
        "forma más o menos impredecible, junto con otros estímulos contextuales (unos asteriscos), que bien pueden ser: pistas, distractores o señales irrelevantes. "
        "Véase un ejemplo de estos posibles estímulos contextuales en la siguiente imagen:"
    ),

        'descripcion_procedimiento3.1': (
        poner_en_negrita(
            "3) En la siguiente prueba CPT (Continuous Performance Test) la persona tiene que, en un tiempo límite, señalar el mayor número de elementos objetivo posible: letras 9 con dos puntos, ni uno más ni uno menos (bien arriba, abajo, o 1 arriba y 1 abajo). "
            "Estos elementos se muestran en fila intercalados por estímulos similares pero distractores que se tienen que ignorar. A continuación un ejemplo de fila en el que detectar estos estimulos objetivo entre otros engañosos o distractores:",
            "prueba CPT",       
        )    
    ),

        'descripcion_procedimiento4.1.1': (
        poner_en_negrita(
            "4) Le sigue la prueba FourFigures. Aquí se presentan 4 series de estímulos uno por uno. "
            "Cada estímulo se compone de una figura externa y una interna, las cuales pueden compartir o discrepar en su forma (cuadrado, círculo, triángulo y cruz). En algunas partes de la tarea se pregunta por la forma de la figura externa "
            "y en otras por la de la figura interna. El participante tiene con la mayor rapidez y precisión posible señalar la forma de la figura por la que se está a preguntar en cada momento. Véase a continuación algunos ejemplos de estímulos:",
            "prueba FourFigures",
        )
    ),

        'descripcion_procedimiento4.1.2': (
        poner_en_negrita(    
            "4) Le sigue la prueba NamingNumbers. Aquí se presentan 4 series de estímulos uno por uno. "
            "En la primera serie el estímulo consiste en un cuadrado entre 1 y 9 puntos dentro, los cuales hay que contar. En las siguientes partes, estos puntos cambian por cifras (1-9). La cifra a mostrar y el número de veces que se muestra difiere. En algunas partes se tiene que indicar la identidad de la cifra y en otras la cantidad de cifras mostradas."
            " Véase a continuación algunos ejemplos de estímulos:",
            "prueba NamingNumbers",
        )
    ),

        'descripcion_procedimiento5.1': (
        poner_en_negrita(
            "5) La quinta prueba DigitsMemorization consiste en memorizar y repetir listas de dígitos de longitud creciente (de 2 a 9 cifras) en un orden diferente en cada parte: directo, inverso o creciente.",
            "prueba DigitsMemorization",
        )
    ),

        'descripcion_procedimiento6.1': (
        poner_en_negrita(
            "6) Por último, la prueba DualTask demanda realizar dos tareas simultáneamente. Por un lado, una tarea constante de seguimiento de un punto en movimiento con el cursor del ratón. "
            "Por otro lado, una tarea intermitente de detección de estímulos objetivo frente distractores. Esto es, que en la pantalla ocasionalmente aparecen otros dos estímulos: un cuadrado rojo o azul. "
            "Además de mover el ratón para seguir el punto la persona debe de hacer clic izquierdo cada vez que en pantalla aparece el cuadrado rojo, y evitar pulsarlo cuando el cuadrado es azul.",
            "prueba DualTask",
        )
    ),



    'titulo_indices': "3. Índices que se obtienen.",

    'descripcion_indices': (
        " El desempeño conjunto en todas las tareas permite evaluar con gran consistencia todas las diferentes dimensiones de la atención.\n"
        "   • **Arousal (grado de activación)**. Nesario para mantener un estado despierto y capacidad de atención consciente. "
        "Mide el estado de vigilia o de activación/atención en general. \n"
        "   • **Atención sostenida**. Necesaria para mantener el rendimiento durante toda la duración de la "
        "prueba. Mide la capacidad de la personar para mantenerse concentrado en una misma tarea a lo "
        "largo del tiempo. \n"
        "   • **Atención selectiva**. Requerida para distinguir estímulos señal de "
        "distractores. Mide la capacidad de la persona para discriminar y atender a la "
        "información relevante para la tarea."
        "distractora y engañosa. \n"
        "   • **Control ejecutivo**. Relacionado con el control voluntario y dirigido de la atención y la "
        "conducta. Mide la capacidad de la persona para inhibir la información irrelevante y "
        "engañosa, y la emisión de respuestas controladas frente a la impulsividad. \n"
        "   • **Flexibilidad cognitiva**. Relacionada con el cambio dinámico del foco atencional "
        "entre tareas. Mide la rapidez y eficacia con la que una persona es capaz de " 
        "adaptarse a cambios en las reglas que definen la tarea y conducta a desempeñar. \n"
        "   • **Memoria operativa**. Necesario para procesar y responder adecuadamente ante momentos "
        "de gran cantidad de información y demanda cognitiva. Mide la cantidad de información que se puede "
        "mantener consciente y analizar simultáneamente. \n"
        "   • **Velocidad de procesamiento**. Necesario para entender una tarea y dar respuesta con la mayor rapidez posible. "
        " Se refiere al tiempo que se necesita para percibir, procesar y responder a la información. \n"
        "   • Ante contextos de multitarea, la preferencia o tendencia por un **estilo atencional** de distribución de la atención paralela o de "
        "cambio focal (switching atencional): \n"
        "1. "
        "Un estilo de distribución paralela de la atención. "
        "En este patrón, el participante mantiene entre las dos tareas simultáneas un reparto equilibrado y constante de los recursos "
        "atencionales. \n"
        "2. "
        "Estilo de cambio focal (switching atencional). "
        "En este patrón, cuando dos tareas concurren la atención se desplaza de forma asimétrica hacia el estímulo más saliente o urgente en cada momento, "
        "y retorna a la tarea más constante cuando la carga de trabajo y demanda cognitiva decrece. \n"       
    ),

    'titulo_resultados': "Resumen del rendimiento y perfil atencional de {nombre_completo}",

    'texto_resultados': (
        "A continuación se muestran los resultados de {nombre} mediante tablas, gráficos y "
        "párrafos explicativos que integran y sintetizan los hallazgos obtenidos:"
    ),

    'titulo_resultados_generales': "En términos generales",
    'texto_resultados_generales': " ",

    'titulo_resultados_específicos': "Profundizando en cada prueba atencional",

    'titulo_ACS': "ACS - cuestionario de control atencional",

    'titulo_ANT': "ANT - prueba de eficiencia de redes neuronales atencionales",

    'titulo_CPT': "CPT - prueba de rendimiento continuo",

    'titulo_FourFigures': "Four Figures - prueba de control y flexibilidad cognitiva",

    'titulo_NamingNumbers': "Naming Numbers - prueba de control y flexibilidad cognitiva",

    'titulo_DigitsMemorization': "Memorización de dígitos - prueba de memoria operativa",

    'titulo_DualTask': "Dual Task - prueba multitarea de atención dividida",

    'introduccion_analisis_tareas_DualTask': "A continuación, nos centramos en el rendimiento pormenorizado de cada tarea por separado.",

    'titulo_sintesis_final': "Síntesis final y recomendaciones",

    'introduccion_sintesis_final': "Finalmente, a modo de síntensis revisamos el desempeño global y dimensional de las capacidades atencionales de {nombre}. A fin de señalar las posibles debilidades, fortalezas y áreas en las que prestar más atención futura." 

 }



# ============================================================================
# ACS — PÁRRAFOS CONDICIONALES
# ============================================================================
# Se podría añadir un índice de fiabilidad basado en desviación típica


PARRAFO_ACS_atenciongeneral = {
    'bajo':"""Empezamos mostrando la percepción autodeclarada sobre las capacidades atencionales propias. A través del cuestionario ACS, {nombre} afirma tener, en general, una capacidad atencional baja, con dificultades para aislarse de distracciones y atender la tarea deseada.""",

    'normal':"""Empezamos mostrando la percepción autodeclarada sobre las capacidades atencionales propias. A través del cuestionario ACS, {nombre} afirma tener, en general, una capacidad atencional adecuada. A excepción de algunas dificultades puntuales, se tiene capacidad suficiente para aislarse de distracciones y atender a una tarea deseada.""",

    'alto':"""Empezamos mostrando la percepción autodeclarada sobre las capacidades atencionales propias. A través del cuestionario ACS, {nombre} afirma tener, en general, una capacidad atencional excelente. No se percibe ningún problema o dificultad para aislarse de las distracciones y atender una tarea o varias tareas al máximo.""",
 }

PARRAFO_ACS_foco = {
    'bajo':"""En particular, se detecta dificultad a la hora de concentrarse y desarrollar un estado de atención focalizada prolongado.""",

    'normal':"""En particular, se detecta una capacidad adecuada para concentrarse y desarrollar un estado de atención focalizada prolongado.""",

    'alto':"""En particular, se detecta una muy buena capacidad para concentrarse y desarrollar un estado de atención focalizada prolongado.""",

 }

PARRAFO_ACS_cambio = {
    'bajo':"""Por otro lado, se señala dificultad para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

    'normal':"""Por otro lado, se señala una capacidad adecuada para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

    'alto':"""Por otro lado, se señala una gran facilidad para intercalar y dirigir la atención entre diferentes estímulos o tareas de manera voluntaria y eficiente.""",

 }


# ============================================================================
# ANT — PÁRRAFOS CONDICIONALES
# ============================================================================
# Se podría añadir un índice de fiabilidad basado en desviación típica


PARRAFO_ANT_TR = {

    'TR alto y C bajo':"""En primer lugar, {nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad. Aunque esto pueda parecer una fortaleza a primeras, cuando revisamos la precisión de estas respuestas vemos que muchas son erróneas. Esto significa entonces un elevado grado de impulsividad, donde {nombre} prioriza velocidad antes que precisión.""",

    'TR alto y C alto o normal':"""En primer lugar, {nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",

    'TR normal y C normal o alto':"""En primer lugar, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",

    'TR normal y C bajo':"""En primer lugar, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas: una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado. Y la posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR bajo':"""En primer lugar, {nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Esto puede deberse a dos cosas. Debido a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. Y a la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",
}

PARRAFO_ANT_A = {

    'A bajo':"""Se registra un escaso número de aciertos, lo que indica complicaciones para completar eficientemente la tarea presentada. Según este resultado, la capacidad atencional general parece ser inferior al promedio de su edad.""",

    'A normal':"""Se registra un número normal de aciertos, lo que parece indicar una capacidad atencional general adecuada a la esperada para su edad.""",
    
    'A alto':"""Se registra un alto número de aciertos, lo que ya de primeras nos sugiere una muy buena atención en general.""",
}

PARRAFO_ANT_C = {

    'C alto y TR alto o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C alto y TR bajo':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",
# Álvaro. En estos dos siguientes párrafos se necesita una dif sign? O dif mínima es suficiente asumiendo una H muy intuitiva de que E impulsiva menor TR y E def. discriminatorio mayor TR. Si necesidad sign.
    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. De nuevo, considerando el escepcionalmente rápido tiempo de respuesta vemos que estas comisiones corresponden con respuestas más impulsivas, más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C bajo y TR normal o bajo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. De nuevo considerando el tiempo de respuesta, vemos que estos errores acontecen a una velocidad normal o incluso retardada de la respuesta. Esto sugiere que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",

}

PARRAFO_ANT_O = {
    'O alto':"""Por otro lado, {nombre} presenta un número de errores de omisión bajo, lo que señala que pocas veces no ha respondido cuando debería. Este resultado señala una velocidad de procesamiento de la información y de toma de decisiones bien ajustada a la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad superior al promedio para mantener la atención sostenida a lo largo de toda la tarea, sin distracción o fatiga que dificulte dar respuesta en los momentos oportunos.""",

    'O normal':"""Por otro lado, {nombre} presenta un número de errores de omisión normal, lo que señala que no ha respondido cuando debería un número de veces igual a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones adecuada a la exigencia temporal de la tarea. Este índice también puede señalar una capacidad adecuada para mantener la atención sostenida a lo largo de toda la tarea, sin distracción o fatiga que dificulte dar respuesta en los momentos oportunos.""",
    
    'O bajo':"""Por otro lado, {nombre} presenta un número de errores de omisión alto, lo que señala que no ha respondido cuando debería un número de veces superior a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones demasiado lenta para la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad inferior al promedio para mantener la atención sostenida a lo largo de toda la tarea. Con tendencia a distraerse o fatigarse, lo que le dificulta dar una respuesta en los momentos oportunos.""",
}

PARRAFO_ANT_F = {
    'F_A positivo y F_TR negativo':"""El rendimiento de {nombre} durante la tarea ha ido mejorando con el avance de la misma, mostrando mejor precisión y velocidad de respuesta al final de la prueba que al principio. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""", 

    'F_A positivo y F_TR no sign':"""A lo largo de la tarea {nombre} muestra una velocidad de respuesta que se mantiene constante, y una precisión que incluso mejora según avanza la misma. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""",

    'F_A positivo y F_TR positivo':""""A lo largo de la tarea {nombre} muestra una precisión de respuesta que mejora con el avance de la misma, mientras que la velocidad de respuesta se ralentiza. Esto indica una clara preferencia de {nombre} por un estilo atencional más reflexivo, con la adopción de un procesamiento de la información más lento pero preciso. {nombre} parece ser muy capaz de automatizar eficazmente tareas simples y repetitivas. Aunque, a su vez, la falta de excitación de esta tarea monótona le supone un mayor esfuerzo y cansancio por mantener la atención sostenida. Finalmente, {nombre} presenta un importante enlantecimiento en su velocidad de trabajo, el cual puede deberse en parte a la fatiga. O a la preferencia y adopción de un estilo atencional más reflexivo con el transcurso de la tarea.""",
    
    'F_A no sign y F_TR negativo':"""A lo largo de la tarea {nombre} muestra una precisión de respuesta constante, mientras que la velocidad de respuesta aumenta con el avance de la tarea. Esto indica una excelente capacidad de automatización de la tarea, especialmente ante tareas simples y repetitivas como esta. Esta habilidad es útil para reducir el esfuerzo ante tareas monótonas y poco estimulantes, y reducir así el cansancio generado. O incluso, en este caso, aumentando la velocidad con la que se realiza la tarea, sin perder calidad en la precisión.""",
    
    'F_A no sign y F_TR no sign':"""A lo largo de la tarea {nombre} muestra un rendimiento sumamente constante, sin que su precisión y velocidad de respuesta se vean afectadas. Esto indica una excelente capacidad de atención sostenida y resistencia a la fatiga, incluso, o especialmente, ante tareas simples y monótonas como esta.""",

    'F_A no sign y F_TR positivo':"""A lo largo de la tarea {nombre} muestra una precisión de respuesta constante, mientras que la velocidad de respuesta se ralentiza. Esto indica dos cosas. Por un lado, el enlantecimiento en su velocidad de trabajo sugiere en {nombre} una baja resistencia a la fatiga ante tareas monótonas y poco estimulantes. Por otro lado, este resulta indica la preferencia de {nombre} por un estilo atencional más reflexivo. De esta manera, ante la aparición de cansancio, {nombre} decide tomarse más tiempo en su respuesta, y así poder seguir procesando la información de manera precisa y consciente.""",

    'F_A positivo y F_TR negativo':"""Con el avance de la tarea {nombre} muestra una aceleración de su velocidad de respuesta, aunque de la mano de un empeoramiento de su precisión. Esto indica dos cosas. Primero, la aparición de cansancio con el avance de la tarea, especialmente ante tareas monótonas y poco estimulantes. En segundo lugar, una clara preferencia y adopción de {nombre} por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas. {nombre} parece tener dificultades para reunir una motivación más intrínseca en el desempeño de la tarea. Y así, ante la falta de estimulación, se cansa o aburre más que lo esperado para su edad, afectando negativamente a su esfuerzo, atención sostenida y rendimiento durante la tarea.""",
    
    'F_A negativo y F_TR no sign y TR bajo o normal':"""A lo largo de la tarea {nombre} muestra una velocidad de respuesta constante, aunque con un empeoramiento en la precisión según avanza la tarea. Esto es indicativo de una baja resistencia a la fatiga, especialmente ante tareas monótonas y poco estimulantes como esta. Con la aparición de cansancio, {nombre} podría esforzarse más para mantener una buena precisión y calidad de respuesta, tomándose más tiempo para pensar y responder. Pero en este caso, parece que {nombre}, bien por falta de capacidad o de motivación, no adopta este estilo atencional más reflexivo, eficaz ante la aparición de cansancio y deterioro en la calidad de la ejecución.""",

    'F_A negativo y F_TR no sign':"""A lo largo de la tarea {nombre} muestra una velocidad de respuesta constante, aunque con un empeoramiento en la precisión según avanza la tarea. Esto es indicativo de una baja resistencia a la fatiga, especialmente ante tareas monótonas y poco estimulantes como esta.""",

    'F_A negativo y F_TR positivo':"""Con el avance de la tarea {nombre} muestra un enlantecimiento de su velocidad de respuesta y un empeoramiento de su precisión. Esto indica una muy baja resistencia al cansancio o el aburrimiento, especialmente ante tareas monótonas y poco estimulantes como esta. Según este índice {nombre} tiene grandes dificultades para mantener la atención sostenida lo que le lleva a no responder o responder erratica o aleatoriamente ante una tarea. Parece así que el rendimiento de {nombre} dependerá más de cuán estimulante le resulte una actividad. Y tiene por tanto, dificultades para reunir motivación más intrínseca en el desempeño de una tarea, y así poder realizar también estas actividades más monótonas o aburridas pero igualmente importantes para la vida diaria.""",
    }


PARRAFO_ANT_alerta = {

    'TR_alerta alto':"""La eficiencia de la red de alerta resultó superior a la media para su edad. Esto se traduce en una excelente capacidad para mantener un alto estado de vigilancia y activación. Es decir, que {nombre} ha estado especialmente despierto durante toda la tarea. Esto le permite reconectar y atender rápidamente con la tarea en los momentos que aparece información relevante.""",

    'TR_alerta normal':"""La eficiencia de la red de alerta resultó adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para mantener un estado de vigilancia y activación durante la tarea. Es decir, que {nombre} ha estado suficientemente despierto durante toda la tarea. Esto le permite reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
    
    'TR_alerta bajo':"""La eficiencia de la red de alerta resultó significativamente por debajo del promedio. Esto se traduce en una capacidad limitada por dificultades para mantener un alto estado de vigilancia y activación. Es decir, parece que {nombre} ha estado poco despierto durante la tarea. Esto le dificulta reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
}
PARRAFO_ANT_orientacion = {

    'TR_orientacion alto':"""Respecto a la red de orientación, {nombre} mostró una eficiencia superior a la media para su edad. Esto se traduce en una excelente capacidad para orientar y dirigir la atención hacia los eventos relevantes.""",

    'TR_orientacion normal':"""Respecto a la red de orientación, {nombre} mostró una eficiencia adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para orientar y dirigir la atención hacia los eventos relevantes.""",
    
    'TR_orientacion bajo':"""Respecto a la red de orientación, {nombre} mostró una eficiencia significativamente por debajo del promedio. Esto se traduce en una capacidad limitada por dificultades para orientar y dirigir la atención hacia los eventos relevantes.""",
}
PARRAFO_ANT_ejecutivo = {

    'TR_ejecutivo alto':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo superior a la media para su edad. Esto se traduce en una excelente capacidad para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un alto control para procesar y ejecutar tareas complejas.""",

    'TR_ejecutivo normal':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un control adecuado para procesar y ejecutar tareas complejas.""",
    
    'TR_ejecutivo bajo':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo significativamente por debajo del promedio. Esto se traduce en una capacidad atencional limitada por dificultades para inhibir durante la tarea la información irrelevante y distractora y las respuestas impulsivas. Así, encontrándose con un control limitado para procesar y ejecutar tareas complejas.""",
}


# ============================================================================
# CPT — PÁRRAFOS CONDICIONALES OPCIONALES  . Se usa tanto para la prueba CPT como la D2
# ============================================================================


# TR equivale a CPT_N 'N' = número de elementos procesados
PARRAFO_CPT_TR = {
    'alto y E alto o normal': """El elevado número de elementos procesados indica una excelente velocidad de procesamiento, asociada a escepcional capacidad de exploración visual y rapidez en la toma de decisiones.""",
    
    'alto y E bajo': """El elevado número de elementos procesados indica una muy buena velocidad de procesamiento, asociada a una rápida exploración visual y rapidez en la toma de decisiones. Esto que a primeras parece positivo cambia al revisar la precisión o calidad de esta capacidad exploratoria y decisional. Vemos aquí que {nombre} bien a omitido información relevante o bien a respondido erróneamente ante información irrelevante. Esto señala un procesamiento de la información superficial, rápido pero defectuoso.""",

    'normal': """El número de elementos procesados se sitúa dentro de los valores esperables para su grupo normativo, indicando una velocidad de procesamiento adecuada, con un ritmo de trabajo ajustado a las demandas temporales de la tarea""",
    
    'bajo y E normal o alto': """El bajo volumen de elementos procesados sugiere una velocidad de procesamiento reducida. {nombre} requiere de más tiempo de lo normal para procesar y discriminar la información. Esto puede incapacitar y emperorar el desempeño, especialmente ante tareas con limitación temporal o de desempeño rápido.""",
# Álvaro. Necesidad calcular una PT de E
    'bajo y E bajo': """El bajo volumen de elementos procesados sugiere una velocidad de procesamiento reducida. Un vistazo al reducido número de errores cometidos (omisiones y comisiones en conjunto) señalan la prevalencia de un estilo atencional y de trabajo más reflexivo, ganando mayor precisión a costa de menor velocidad de respuesta. Aunque esto puede ser ventajoso para el desempeño de tareas más precisas, también puede suponer cierta desventaja ante tareas con limitación temporal y de desempeño rápido. No saber regular el estilo atencional más oportuno a las demandas de una tarea puede suponer una deficiencia atencional, y un problema solventable con entrenamiento."""
}

PARRAFO_CPT_TOT = {
    'alto': """Por otro lado, el índice TOT señala un excelente equilibrio entre velocidad y precisión, donde, aún analizando muchos casos, se descuidan pocos estímulos señal y se erra poco con los distractores. Esto refleja un estado muy despierto y una elevada concentración durante esta tarea.""",
    
    'normal': """Por otro lado, el índice TOT se sitúa dentro de valores esperables, indicando un equilibrio adecuado entre velocidad y precisión durante la ejecución de la tarea. Esto refleja un estado de activación y concentración adecuado para las demandas de la tarea.""",
    
    'bajo': """Por otro lado, el bajo índice TOT señala dificultades para integrar rapidez y precisión, bien por exceso de velocidad con descuido, bien por excesiva parsimonia, o bien por ambas, lentitud y descuido. Esto señala que la concentración de {nombre} durante la prueba fue en general pobre, y que seguramente no estuvo lo suficientemente despierto como para realizarla correctamente."""
}

# O - Errores de omisión
PARRAFO_CPT_O = {
    'bajo': """La presencia de un número elevado de errores de omisión indica dificultades en la atención selectiva y la detección de información relevante. Esto se asocia con lapsus atencionales y un seguimiento inconsistente de las reglas de la tarea, lo que deriva en un escaneo visual incompleto y una discriminación y respuesta deficiente de la información objetivo.""",
    
    'normal': """El número de errores de omisión se sitúa dentro de los valores esperables para su grupo normativo, lo que indica una adecuada atención sostenida y capacidad para detectar los estímulos relevantes a lo largo de la tarea. Este resultado sugiere un escaneo visual correcto y un seguimiento apropiado de la consigna, sin evidenciar lapsus atencionales significativos.""",
    
    'alto': """El bajo número de errores de omisión refleja una elevada focalización atencional, con muy buena capacidad para detectar los estímulos relevantes."""
}

# C - Errores de comisión
PARRAFO_CPT_C = {
    'bajo': """Por otro lado, el aumento de errores de comisión sugiere dificultades en el control inhibitorio: una mayor impulsividad en la respuesta o cierta deficiencia perceptiva en la discriminación y omisión de la información irrelevante  y engañosa.""",
    
    'normal': """Por otro lado, la frecuencia de errores de comisión se encuentra dentro de rangos normales, lo que refleja un control inhibitorio adecuado, y una impulsiva en la respuesta igual a lo esperado para su edad. Este patrón sugiere una correcta discriminación y omisión de información irrelevante  y engañosa.""",
    
    'alto': """Por otro lado, la escasa presencia de errores de comisión indica un alto control inhibitorio, con respuestas cuidadosas y precisas que reflejan una buena capacidad de discriminación y omisión de la información irrelevante y engañosa."""
}


PARRAFO_CPT_VAR = {
# Álvaro. Calcular presencia Fatiga o automatismo por prueba t entre el índice TOT del primer y tercer tercio prueba? Necesidad baremar esta dif.?
    ('bajo', 'nada'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series, vinculada a dificultades para mantener la motivación constante y a una mayor facilidad para distraerse. Esto influye a su vez a un declive en la puntuación de {nombre} en los demás aspectos atencionales anteriormente evaluados.""",

# dentro de la condición VAR se tratan las condiciones 'Fatiga' y 'Automatizacion' si dif. sign. negativa o positiva respectivamente entre el primer (primeras 4 series) y tercer tercio (últimas 4 series) de la prueba.
    ('bajo', 'fatiga'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series, vinculada a dificultades para mantener la motivación y a una mayor facilidad para distraerse. En particular, aparece aquí cierto cansancio o fatiga con el transcurso de la tarea, ya que la serie de peor rendimiento se obtuvo más hacia el final de la tarea, en comparación con la de mayor rendimiento. Esto influye a su vez a un declive en la puntuación de {nombre} en los demás aspectos atencionales anteriormente evaluados.""",

# 'automatismo' (positivo) o 'dificultadinicial'(negativo) en f(TOT)
    ('bajo', 'automatismo', 'TOT normal o alto' ): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series. Además se observa que el rendimiento fue en mejora progresiva, con las peores series al principio de la tarea y las de mejor rendimiento hacia el final. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad se trata más bien de una notable capacidad para adaptarse y automatizar la ejecución a largo plazo.""",

    ('bajo', 'dificultadinicial', 'TOT bajo'): """{nombre} mostró un rendimiento muy variable entre su mejor y peor serie. Véase esta variabilidad en la gráfica superior y su curva de trabajo, la línea zigzagueante que une el último elemento procesado de cada serie. Este dato puede indicar una falta de atención sostenida entre diferentes series. Además se observa que el rendimiento fue en mejora progresiva, con las peores series al principio de la tarea y las de mejor rendimiento hacia el final. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad se trata más bien de una dificultad inicial para asimilar y acomodarse rápidamente a la nueva tarea.""",

    ('normal', 'nada'): """ El último aspecto para mencionar es en relación a la variabilidad del rendimiento, trazada en el perfil gráfico adjunto en este informe. Aquí se puede ver que el rendimiento de {nombre} durante la prueba ha resultado estable y consistente entre series. Esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales aquí evaluados resulta típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte o la aparición de cansancio, respectivamente, son menos probables.""",

    ('normal', 'fatiga'): """ El último aspecto para mencionar es en relación a la variabilidad del rendimiento, trazada en el perfil gráfico adjunto en este informe. Aquí se puede ver que el rendimiento de {nombre} durante la prueba ha resultado estable y consistente entre series. Esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales aquí evaluados resulta típico y constante en su persona. Y que por tanto, otras explicaciones aleatorias a su mejor o peor rendimiento son menos probables. Sin embargo, sí que parece que el rendimiento general se ha podido ver perjudicado debido a cierto cansancio o fatiga hacia el final de la tarea.""",

    ('normal','automatismo', 'TOT normal o alto' ): """ El último aspecto para mencionar es en relación a la variabilidad del rendimiento, trazada en el perfil gráfico adjunto en este informe. Aquí se puede ver que el rendimiento de {nombre} durante la prueba ha resultado estable y consistente entre series. Esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales aquí evaluados resulta típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte o la aparición de cansancio, respectivamente, son menos probables. Sin embargo, sí que se encuentra bastante diferencia entre las primeras y las últimas series de la tarea. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilida corresponde con una resaltable capacidad para adaptarse y automatizar la ejecución a largo plazo.""",

    ('normal', 'dificultadinicial', 'TOT bajo'): """ El último aspecto para mencionar es en relación a la variabilidad del rendimiento, trazada en el perfil gráfico adjunto en este informe. Aquí se puede ver que el rendimiento de {nombre} durante la prueba ha resultado estable y consistente entre series. Esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales aquí evaluados resulta típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte o la aparición de cansancio, respectivamente, son menos probables. Sin embargo, sí que se encuentra bastante diferencia entre las primeras y las últimas series de la tarea. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad corresponde con una importante dificultad inicial para asimilar y acomodarse rápidamente a la nueva tarea.""",

    ('alto', 'nada'): """El bajo nivel de variabilidad observado sugiere una alta consistencia y estabilidad en el rendimiento, indicando una buena resistencia al cansancio o fatiga y una buena capacidad para sostener el esfuerzo atencional de forma uniforme durante toda la tarea. Además, esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales anteriormente evaluados resulta aún más típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte, distracciones puntuales o la aparición de cansancio, respectivamente, son menos probables.""",
   
    ('alto','fatiga'): """ El bajo nivel de variabilidad observado sugiere una alta consistencia y estabilidad en el rendimiento, indicando una buena capacidad para sostener el esfuerzo atencional de forma uniforme durante toda la tarea. Además, esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales anteriormente evaluados resulta aún más típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte, distracciones puntuales o la aparición de cansancio, respectivamente, son menos probables. Sin embargo, en esta tarea sí que se ha mostrado un cansancio o fatiga con el transcurso de la tarea, lo que pudo influir en un declive en la puntuación de {nombre} en los demás aspectos atencionales en esta tarea evaluados.""",
   
    ('alto','automatismo', 'TOT normal o alto' ): """ El bajo nivel de variabilidad observado sugiere una alta consistencia y estabilidad en el rendimiento, indicando una buena resistencia al cansancio o fatiga y una buena capacidad para sostener el esfuerzo atencional de forma uniforme durante toda la tarea. Además, esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales anteriormente evaluados resulta aún más típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte, distracciones puntuales o la aparición de cansancio, respectivamente, son menos probables. Sin embargo, sí que se encuentra bastante diferencia entre las primeras y últimas series de la tarea. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad corresponde con una resaltable capacidad para adaptarse y automatizar la ejecución a largo plazo.""",
   
    ('alto', 'dificultadinicial', 'TOT bajo'): """ El bajo nivel de variabilidad observado sugiere una alta consistencia y estabilidad en el rendimiento, indicando una buena resistencia al cansancio o fatiga y una buena capacidad para sostener el esfuerzo atencional de forma uniforme durante toda la tarea. Además, esto es indicativo de que la ejecución de {nombre} en los demás aspectos atencionales anteriormente evaluados resulta aún más típico y constante en su persona. Y que por tanto, otras explicaciones a su mejor o peor rendimiento, como la suerte, distracciones puntuales o la aparición de cansancio, respectivamente, son menos probables. Sin embargo, sí que se encuentra bastante diferencia entre las primeras y las últimas series de la tarea. Teniendo también en cuenta el índice CON promedio, vemos que esta variabilidad corresponde con una importante dificultad inicial para asimilar y acomodarse rápidamente a la nueva tarea.""",

}


# ============================================================================
# 3.3 DUAL-TASK
# ============================================================================


# PD_Total - Según puntuación directa total y correspondiente percentil. Nuevo índice T2 P sale de A - C
PARRAFO_DUALTASK_General_PSV_y_A = {

    'PSV alto y T2 P alto':"""El rendimiento general en la prueba es escepcionalmente bueno, a la vez que estable entre las dos tareas. En la tarea de seguimiento visomotor se registra un rendimiento continuo excelente, mientras que en la segunda tarea más disruptiva y vinculada a los reflejos, también se obtuvo un número de aciertos superior al promedio. Esto ya de primeras nos sugiere una sobresaliente capacidad atencional, y más importante aún, una muy buena capacidad de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo.""",

    'PSV alto y T2 P normal':"""El rendimiento general en la prueba es excelente. En particular, en la tarea de seguimiento visomotor se registra un rendimiento de atención sostenida por encima del promedio. Mientras, en la segunda tarea más disruptiva y vinculada a los reflejos, se mantuvo un rendimiento en cuestión de aciertos, algo peor en comparación con la otra tarea, pero igualmente bueno, adecuado a lo esperable para su edad. Esto corresponde a una buena capacidad de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo, sin desatender ninguna en exceso.""",

    'PSV normal y T2 P alto':"""El rendimiento general en la prueba es positivo y estable entre tareas. En particular, en la tarea 2 de desempeño disruptivo y dependiente de reflejos, donde el número de aciertos registrado está por encima del promedio. Mientras, en la tarea 1, de seguimiento visomotor continuado, se mantuvo un rendimiento algo peor en comparación con la otra tarea, pero igualmente bueno, adecuado a lo esperable para su edad. Esto corresponde a una buena capacidad de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo, sin desatender ninguna en exceso.""",

    'PSV normal y T2 P normal':"""El rendimiento general en la prueba es adecuado y estable entre tareas. Esto índica una capacidad adecuada de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo, sin desatender ninguna tarea en exceso.""",

    'PSV normal y T2 P bajo':"""El rendimiento general en la prueba es algo inestable entre tareas. Esto indica una capacidad limitada de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo. Mientras que el seguimiento visomotor continuado se mantiene adecuadamente, la segunda tarea de desempeño disruptivo y dependiente de reflejos, se desatiende en exceso obteniendo un rendimiento deficiente, por debajo de lo normal.""",

    'PSV bajo y T2 P normal':"""El rendimiento general en la prueba es algo inestable entre tareas. Esto indica una capacidad limitada de gestión de los recursos atencionales para atender y responder a más de una tarea al mismo tiempo. Mientras que el desempeño en la segunda tarea, vinculada a la detección de estímulos disruptivos y respuestas rápidas, resulta adecuado, el seguimiento visomotor asociado a la primera tarea se desatiende, originando un rendimiento deficiente, por debajo de lo normal.""",

    'PSV alto y T2 P bajo':"""El rendimiento general en la prueba resulta sumamente inestable y variable entre tareas. Esto indica que {nombre} tiene importantes dificultades para gestionar sus recursos atencionales y poder atender y responder a más de una tarea al mismo tiempo. Bien por preferencia o por capacidad atencional, toda la atención parece haberse depositado en la tarea de seguimiento visomotor, para la cual el rendimiento ha sido sobresaliente. Por otra parte sin embargo, la segunda tarea de respuesta ocasional y rápida se ha desatendido hasta el punto de obtener un número de aciertos significativamente por debajo del promedio. Las dificultades para gestionar equitativamente los recursos atencionales y cognitivos en función de la demanda de trabajo derivan en un resultado total insuficiente. Para ejemplificar esto, es como si una persona pudiese leer muy rápido pero sólo hablar lentamente, resultando en que sólo pueda leer lentamente en voz alta.""",

    'PSV bajo y T2 P alto':"""El rendimiento general en la prueba resulta sumamente inestable y variable entre tareas. Esto indica que {nombre} tiene importantes dificultades para gestionar sus recursos atencionales y poder atender y responder a más de una tarea al mismo tiempo. Bien por preferencia o por capacidad atencional, toda la atención parece haberse depositado en la tarea de respuesta refleja y ocasional, para la cual el rendimiento ha sido sobresaliente. Por otra parte sin embargo, la tarea de constante seguimiento visomotor parece haberse desatendido casi por completo, resultando en un rendimiento significativamente por debajo del promedio. Las dificultades para gestionar equitativamente los recursos atencionales y cognitivos en función de la demanda de trabajo derivan en un resultado total insuficiente. Para ejemplificar esto, es como si una persona pudiese leer muy rápido pero sólo hablar lentamente, resultando en que sólo pueda leer lentamente en voz alta.""",

    'PSV bajo y T2 P bajo':"""El rendimiento general en la prueba está muy por debajo del promedio. Tanto en la tarea de constante seguimiento visomotor como en la de respuesta refleja ocasional el desempeño ha sido deficiente. Un resultado tan negativo es incluso poco probable y bien puede deberse a una ejecución poco seria, de respuesta aleatoria o ausente, que no es representativa de la capacidad atencional real de la persona. Si por el contrario, la persona ha intentado rendir al máximo durante esta prueba, estos resultados señalan entonces una capacidad atencional general limitada, o inferior a lo normal y esperable para una persona de su edad. También importantes dificultades en la gestión de sus recursos atencionales para atender y responder a más de una tarea al mismo tiempo.""",
}

PARRAFO_DUALTASK_si_inestable = {
    'PSV alto y T2 P normal o bajo':"""La existencia de cierto desbalance en la gestión de la atención dirigida a cada tarea sugiere una preferencia cognitiva por las tareas que demandan una atención sostenida y ejecución constante, frente a las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva. Esta preferencia cognitiva supone una mejor aptitud para actividades donde importa la persistencia, la concentración prolongada y el ritmo estable, tales como: leer, redactar y pintar de forma extendida, meditar, hacer senderismo o natación.""",
    'PSV normal y T2 P bajo':"""La existencia de cierto desbalance en la gestión de la atención dirigida a cada tarea sugiere una preferencia cognitiva por las tareas que demandan una atención sostenida y ejecución constante, frente a las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva. Esta preferencia cognitiva supone una mejor aptitud para actividades donde importa la persistencia, la concentración prolongada y el ritmo estable, tales como: leer, redactar y pintar de forma extendida, meditar, hacer senderismo o natación.""",

    'PSV normal o bajo y T2 P alto':"""La existencia de cierto desbalance en la gestión de la atención dirigida a cada tarea sugiere una preferencia cognitiva por las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva, frente a las tareas atención sostenida y ejecución constante. Esta preferencia cognitiva supone una mejor aptitud para actividades donde predominan los picos de acción intensa, decisiones rápidas y cambios abruptos, tales como: improvisación teatral u oratoria, deportes (fútbol, baloncesto, boxeo) y videojuegos frenéticos.""",
    'PSV bajo y T2 P normal':"""La existencia de cierto desbalance en la gestión de la atención dirigida a cada tarea sugiere una preferencia cognitiva por las tareas basadas en reflejos que demandan una ejecución rápida e intermitente o disruptiva, frente a las tareas atención sostenida y ejecución constante. Esta preferencia cognitiva supone una mejor aptitud para actividades donde predominan los picos de acción intensa, decisiones rápidas y cambios abruptos, tales como: improvisación teatral u oratoria, deportes (fútbol, baloncesto, boxeo) y videojuegos frenéticos.""",
}


# Revisar. Cambiar memoria de trabajo x  operativa si correlación con MemorizationDigits
# Confirmar si este índice realmente correlaciona con memoria de trabajo en DigitsNumbers. Este y el siguiente párrafo se obtienen por la dif. sign y baremada de PSV en evento concurrente o (concurrente + after) frente unrelated. 
# Deterior significa dif. sign. PSV concurrent vs unrelated ¿y también baremada?
PARRAFO_DUALTASK_estilo_atencional_cuando_concurrencia = {
    'deterioro y T2 normal o alto':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se deteriora significativamente en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender a la tarea 1 y 2, información procedente de diversas fuentes. 
    No obstante, en estos momentos de concurrencia de tareas y mayor demanda atencional, mientras que la precisión de seguimiento en la tarea 1 empeora, el desempeño en la tarea 2 se mantiene satisfactorio. Esto sugiere que el problema no se debe a una capacidad de memoria operativa limitada, pero a una importante dificultad en la gestión de la atención en contextos dinámicos y multitarea. Así como la preferencia y prevalencia por un estilo atencional caracterizado por el cambio focal intermitente entre tareas. {nombre} no atiende a ambas tareas simultáneamente, sino que deja completamente de atender la primera tarea de desempeño continuo cuando la segunda tarea de respuesta rápida y ocasional demanda más atención. Y solo volviendo a atender a la primera una vez la demanda atencional de la segunda se reduce o desaparece.""",

    'deterioro y T2 P bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se deteriora significativamente en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender a la tarea 1 y 2, información procedente de diversas fuentes. 
    Además, en estas situaciones de concurrencia de tareas y mayor demanda atencional, también la atención en la segunda tarea resulta insuficiente, particularmente en relación a la precisión de respuesta. El deterioro en el rendimiento repartido por igual entre ambas tareas parece señalar la preferencia y prevalencia por un estilo atencional caracterizado por la distribución paralela de la atención. A fin de atender y responder lo mejor posible a las dos tareas, {nombre} opta por hacer más difuso y amplio su foco atencional. Manteniendo así una atención estable y simultánea para las dos tareas. Sin embargo, 'el que mucho abarca poco aprieta'. Debido a una limitada memoria operativa, {nombre} encuentra dificultades para procesar tanta información, lo que termina repercutiendo negativamente en su rendimiento.""",
    
    'deterioro y T2 TR bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se deteriora significativamente en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender a la tarea 1 y 2, información procedente de diversas fuentes. 
    Además, en estas situaciones de concurrencia de tareas y mayor demanda atencional, también la atención en la segunda tarea resulta insuficiente, particularmente en relación a la velocidad de respuesta. El deterioro en el rendimiento repartido por igual entre ambas tareas parece señalar la preferencia y prevalencia por un estilo atencional caracterizado por la distribución paralela de la atención. A fin de atender y responder lo mejor posible a las dos tareas, {nombre} opta por hacer más difuso y amplio su foco atencional. Manteniendo así una atención estable y simultánea para las dos tareas. Sin embargo, 'el que mucho abarca poco aprieta'. Debido a una limitada memoria operativa, {nombre} encuentra dificultades para procesar tanta información, lo que termina repercutiendo negativamente en su rendimiento.""",
    
    'deterioro y T2 P y TR bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se deteriora significativamente en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender a la tarea 1 y 2, información procedente de diversas fuentes. 
    Además, en estas situaciones de concurrencia de tareas y mayor demanda atencional, también la atención en la segunda tarea resulta muy insuficiente, tanto en velocidad como en precisión de la respuesta. Un deterioro tan grande en el rendimiento señala importantes dificultades en la gestión de los recursos atencionales en contextos dinámicos y multitarea. Así como también una memoria operativa insuficiente, limitada para procesar simultáneamente una cantidad de información mayor y proveniente de distintas fuentes.""",
    
    'no deterioro y T2 P y TR normal o alto':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se mantiene estable en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender simultánemamente a la tarea 1 y 2, información procedente de diversas fuentes. Esto señala una buena memoria operativa, capacidad suficiente para atender y procesar más cantidad de información simultáneamente. 
    Además, el rendimiento también se mantiene estable y positivo en la tarea 2 tanto como en la 1. Este rendimiento estable entre tareas señala una preferencia y prevalencia por un estilo atencional caracterizado por la distribución paralela de la atención. A fin de atender y responder efectivamente a las dos tareas, {nombre} opta por hacer más difuso y amplio su foco atencional. Manteniendo así una atención estable y simultánea para las dos tareas.""",

    'no deterioro y T2 P bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se mantiene estable en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender simultánemamente a la tarea 1 y 2, información procedente de diversas fuentes. Podría esto señalar suficiente memoria operativa para atender y procesar más cantidad de información simultáneamente. 
    No obtanste en estos momentos de concurrencia de tareas y mayor demanda atencional, aunque el rendimiento en la tarea 1 no se ve apenas afectado, la atención en la tarea 2 sí que resulta insuficiente, particularmente en materia de precisión de la respuesta. Esto puede deberse bien a una dificultad perceptiva específica de la segunda tarea, o a una dificultad en la gestión de la atención en contextos dinámicos y multitarea. Y en cualquier caso, una preferencia y tendencia a focalizar asimétricamente más recursos cognitivos en una tarea frente otra.""",

    'no deterioro y T2 TR bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se mantiene estable en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender simultánemamente a la tarea 1 y 2, información procedente de diversas fuentes. Podría esto señalar suficiente memoria operativa para atender y procesar más cantidad de información simultáneamente. 
    No obtanste en estos momentos de concurrencia de tareas y mayor demanda atencional, aunque el rendimiento en la tarea 1 no se ve apenas afectado, la atención en la tarea 2 sí que resulta insuficiente, con relación tanto a la precisión como a la velocidad en la respuesta, ambas inferiores al promedio. Esto sí que sugiere cierta dificultad en la gestión de la atención en contextos dinámicos y de multitarea. Y una preferencia y tendencia a focalizar asimétricamente más recursos cognitivos en una tarea frente otra.""",

    'no deterioro y T2 P y TR bajo':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se mantiene estable en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender simultánemamente a la tarea 1 y 2, información procedente de diversas fuentes. 
    No obtanste en estos momentos de concurrencia de tareas y mayor demanda atencional, aunque el rendimiento en la tarea 1 no se ve apenas afectado, la atención en la tarea 2 sí que resulta insuficiente, particularmente en materia de velocidad de respuesta. Esto señala importantes dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y una preferencia y tendencia a focalizar todos los recursos cognitivos en una única tarea.""",

    'mejora y T2 P y TR normal o alto':"""Respecto a la memoria de trabajo, se ve que el seguimiento visomotor en la tarea 1 se mantiene incluso más estable de lo esperable en los momentos de mayor carga de trabajo y demanda cognitiva. Esto es, en los momentos que hay que atender simultáneamente a la tarea 1 y 2, información procedente de diversas fuentes. Mientras que tampoco se desatiende el desempeño en la segunda tarea. Este resultado señala una excelente memoria operativa. Esto es, una capacidad por encima del promedio para atender y procesar mayor cantidad de información de manera simultánea. 
    Por otro lado, en estos momentos de concurrencia de tareas y mayor demanda atencional, el rendimiento estable entre tareas sugiere una preferencia y prevalencia por un estilo atencional caracterizado por la distribución paralela de la atención. A fin de atender y responder efectivamente a las dos tareas, {nombre} opta por hacer más difuso y amplio su foco atencional. Manteniendo así una atención estable y simultánea para las dos tareas.""",

    'mejora y T2 P bajo':"""Respecto a la memoria de trabajo, se ve que que el rendimiento entre tareas es muy dispar, con el excelente desempeño en la tarea 1 facilitado por la completa desatención de la tarea 2, particularmente en materia de precisión de la respuesta. No siendo así indicativo de una buena memoria operativa. Por el contrario, es de esperar que la cantidad de información que {nombre} es capaz de procesar de manera simultánea sea menor a la del promedio. 
    Este desempeño desigual en los momentos de concurrencia de tareas y mayor demanda atencional sugiere dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, una preferencia y tendencia a focalizar más recursos cognitivos en una única tarea, con preferencia por las tareas de ejecución continua.""",

    'mejora y T2 TR bajo':"""Respecto a la memoria de trabajo, se ve que que el rendimiento entre tareas es muy dispar, con el excelente desempeño en la tarea 1 facilitado por la completa desatención de la tarea 2, particularmente en materia de velocidad de respuesta. No siendo así indicativo de una buena memoria operativa. Por el contrario, es de esperar que la cantidad de información que {nombre} es capaz de procesar de manera simultánea sea menor a la del promedio. 
    Este desempeño desigual en los momentos de concurrencia de tareas y mayor demanda atencional sugiere dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, una preferencia y tendencia a focalizar más recursos cognitivos en una única tarea, con preferencia por las tareas de ejecución continua.""",
    
    'mejora y T2 P y TR bajo':"""Respecto a la memoria de trabajo, se ve que que el rendimiento entre tareas es muy dispar, con el excelente desempeño en la tarea 1 facilitado por la completa desatención de la tarea 2, tanto en precisión como en velocidad de respuesta. No siendo así indicativo de una buena memoria operativa. Por el contrario, es de esperar que la cantidad de información que {nombre} es capaz de procesar de manera simultánea sea menor a la del promedio. 
    Este desempeño desigual en los momentos de concurrencia de tareas y mayor demanda atencional sugiere dificultades en la gestión de la atención y la excesiva carga de trabajo en contextos dinámicos y de multitarea. Y también, una preferencia y tendencia a focalizar todos los recursos cognitivos en una única tarea, con preferencia por las tareas de ejecución continua.""",
}

PARRAFO_DUALTASK_PSV = {
    'bajo':"""En la tarea 1 la precisión del seguimiento visomotor inferior al promedio señala dificultades en las capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir. Dificultades en esta dimensión representa una mayor probabilidad de presentar problemas de disgrafía.""",

    'normal':"""En la tarea 1 la precisión del seguimiento visomotor igual al promedio señala adecuadas capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir.""",

    'alto':"""En la tarea 1 la precisión del seguimiento visomotor superior al promedio señala sobresalientes capacidades visomotoras y de movimiento fino. Esta habilidad es importante para la capacidad de seguir estímulos en movimiento y realizar movimientos coordinados ojo mano, tales como escribir, pintar o construir.""",
}

# Este párrafo no se utiliza actualmente. Los A contabilizan para el párrafo de Rendimiento General 'PARRAFO_DUALTASK_General_PSV_y_A'. Cambiar si tal después de confirmar su ubicación en arousal o at. sostenida tras correlaciones.
PARRAFO_DUALTASK_A = {

    'A bajo':"""Para la tarea 2 encontramos en primer lugar bajo número de aciertos. Esto puede ser indicativo de un estado de vigilancia o de atención sostenida deficiente durante la prueba.""",

    'A normal':"""Para la tarea 2 encontramos en primer lugar un número de aciertos normal. Esto puede ser indicativo de un adecuado estado de vigilancia y de atención sostenida durante la prueba.""",
    
    'A alto':"""Para la tarea 2 encontramos en primer lugar un elevado número de aciertos. Esto puede ser indicativo de un sobresaliente estado de vigilancia o de atención sostenida.""",
}

PARRAFO_DUALTASK_O = {
    'O alto':"""A su vez, el número de errores de omisión resulta bajo. Es decir, que pocas veces no se ha respondido cuando se debería. Este resultado señala una velocidad de procesamiento de la información y de toma de decisiones bien ajustada a la exigencia temporal de la tarea. Otra explicación factible es la de una capacidad superior al promedio para mantener la atención sostenida a lo largo de la tarea, sin distracción o fatiga que dificulte emitir una respuesta en los momentos oportunos.""",

    'O normal':"""A su vez, el número de errores de omisión resulta normal, Es decir, que no se ha respondido cuando se debería un número de veces igual a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones adecuada a la exigencia temporal de la tarea. Este índice también puede señalar una capacidad adecuada para mantener la atención sostenida a lo largo de la tarea, sin distracción o fatiga que dificulte emitir una respuesta en los momentos oportunos.""",
    
    'O bajo':"""A su vez, el número de errores de omisión resulta alto. Es decir, que no se ha respondido cuando se debería un número de veces superior a lo esperado para su edad. Este resultado señala una velocidad de procesamiento de la información y toma de decisiones demasiado lenta para la exigencia temporal de la tarea. Otra explicación factible es la de una capacidad inferior al promedio para mantener la atención sostenida a lo largo de la tarea: con tendencia a distraerse o fatigarse, y dificultad para emitir una respuesta en los momentos oportunos.""",
}

PARRAFO_DUALTASK_C = {

    'C alto':"""Finalmente el número de errores de comisión es bajo. Es decir, que pocas veces {nombre} emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente, y una muy baja impulsividad.""",

    'C normal':"""Finalmente el número de errores de comisión es normal. Es decir, que {nombre} emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",

    'C bajo':"""Finalemnte el número de errores de comisión es alto. Es decir, que {nombre} emite un número de respuestas erróneas superior a lo esperado para su edad. Este resultado puede señalar dos cosas: una capacidad inferior al promedio para discriminar la información de manera eficiente, y/o un nivel de impulsividad superior al esperado para su edad.""",
}

# Añadir este PARRAFO_TR_A_vs_C sólo cuando C es normal o alto
PARRAFO_DUALTASK_TR_A_vs_C = {
    'C normal y TR_A_vs_C positivo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una mayor velocidad de respuesta en comparación con los aciertos. Esto señala que los errores de precisión se deben a respuestas más impulsivas.""",
    'C normal y TR_A_vs_C negativo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto señala que los errores de precisión se deben, no tanto a un problema de impulsividad, pero a dificultades puntuales en la percepción y el procesamiento de la información.""",

    'C alto y TR_A_vs_C positivo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una mayor velocidad de respuesta en comparación con los aciertos. Esto señala que el problema atencional está especialmente vinculado a una elevada impulsividad, con respuestas más rápidas pero menos precisas.""",
    'C alto y TR_A_vs_C negativo':"""Si miramos al tiempo de respuesta de las comisiones frente a los aciertos, vemos que los errores de comisión de {nombre} acontecen a una menor velocidad de respuesta en comparación con los aciertos. Esto señala que el problema atencional no está tan vinculado a la impulsividad, sino a importantes dificultades en la percepción y el procesamiento de la información, que incapacitan a {nombre} para discriminar la información de manera eficiente.""",

}

# Parrafo condicional de C para posibilidad de identificar la prevalencia de un estilo atencional reflexivo o impulsivo
PARRAFO_DUALTASK_TR = {

    'TR alto y C normal o alto':"""Por último, {nombre} muestra un tiempo de respuesta bajo, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad.""",
    'TR alto y C bajo':"""Por último, {nombre} muestra un tiempo de respuesta bajo, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad. Aunque esta mayor velocidad también puede deberse a la evidente preferencia o tendencia de {nombre} por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas.""",

    'TR normal':"""Por último, {nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",
    
    'TR bajo y C bajo':"""Por último, {nombre} muestra un tiempo de respuesta elevado, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Este resultado puede señala que {nombre} requiere de más tiempo para procesar la misma cantidad de información que otros individuos de su edad.""",

    'TR bajo y C normal':"""Por último, {nombre} muestra un tiempo de respuesta elevado, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Este resultado puede señalar dos fenómenos diferentes: la necesidad de {nombre} de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. Y la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'TR bajo y C alto':"""Por último, {nombre} muestra un tiempo de respuesta elevado, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Considerando el reducido número de comisiones parece que prevalece un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",
}

#F_A si fatiga (diferencia significativa) en precisión T1, F_TR en TR T2, TR_PSV si precisión T1
PARRAFO_DUALTASK_Fatiga = {
    
    'no F':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. A lo cual, resulta que no se ha encontrado indicio de cansancio en ninguna de las dimensiones cognitivas y atencionales evaluada, lo que indica una buena resistencia y capacidad de atención cognitiva.""",

    'F PSV':"""Queda comparar el rendimiento de {nombre} hacia el  principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado una rápida aparición de cansancio y fatiga, caracterizado por un progresivo empeoramiento de la precisión de seguimiento visomotor de la tarea 1. Es decir, dificultad para mantener la atención sostenida con el paso del tiempo.""",
    
    'F A':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado una rápida aparición de cansancio y fatiga, caracterizado por un progresivo empeoramiento de la precisión en la tarea 2. Es decir, dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa.""",

    'F TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado una rápida aparición de cansancio y fatiga, caracterizado por un progresivo empeoramiento de la velocidad de procesamiento y respuesta en la tarea 2. Es decir, dificultad para mantener un ritmo acelerado en el despeño de la tarea.""",

    'F PSV y F A':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga. Caracterizado por un progresivo empeoramiento de la precisión de seguimiento visomotor de la tarea 1. Esto indica una aparición rápida de fatiga cognitiva y dificultades para mantener la atención sostenida con el paso del tiempo. La fatiga también ha provocado un deterioro de la precisión en la segunda tarea. Esto es, dificultades para mantener la precisión con la que se discrimina, atiende y responde a la información relevante frente la irrelevante y engañosa.""",

    'F PSV y F TR':""""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga. Caracterizado por un progresivo empeoramiento de la precisión de seguimiento visomotor de la tarea 1. Esto indica una aparición rápida de fatiga cognitiva y dificultades para mantener la atención sostenida con el paso del tiempo. La fatiga también ha provocado un deterioro del tiempo de respuesta la segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",
    
    'F A y F TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga durante la prueba. Caracterizado por un progresivo empeoramiento de la precisión en la tarea 2: dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa. La fatiga también ha provocado un deterioro del tiempo de respuesta en esta segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",

    'F PSV, F A y F TR':"""Queda comparar el rendimiento de {nombre} hacia el principio y el final de la prueba. Esto a fin de estimar posibles efectos de automatización, fatiga o cansancio a lo largo de la prueba. {nombre} ha mostrado un importante cansancio y fatiga durante la prueba, viéndose afectado su rendimiento en todos los índices de la prueba, incluyendo: la precisión de seguimiento visomotor de la tarea 1 o dificultades para mantener la atención sostenida en general. Una reducción de la precisión en la tarea 2, y dificultad para mantener la capacidad de discriminar, atender y responder adecuadamente a la información relevante frente la irrelevante y engañosa. Y, finalmente, un deterioro del tiempo de respuesta en la segunda tarea. Esto es, dificultades para mantener la misma velocidad de procesamiento y respuesta durante el breve tiempo de duración de la prueba.""",
    
    }

# Este Párrafo_automatización puede no añadirse si no hay una diferencia significativa positiva del último tercio de la prueba frente al primero.
PARRAFO_DUALTASK_automatización = {
    'Automatización PSV':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma. Esta facilidad para automatizar tareas sostenidas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización TR':"""Por otro lado, se ha observado una mejora del rendimiento en la velocidad de procesamiento y respuesta en la tarea 2. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma, aumentando la velocidad con la que se ejecuta. Esta facilidad para automatizar una tarea puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de respuesta en la tarea 2. Esto sugiere una rápida adaptación a las reglas y procedimientos de esta tarea y capacidad para automatizar y mejorar el rendimiento en la misma, mejorando la efectividad con la que se ejecuta. Esta facilidad para automatizar una tarea puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización PSV y TR':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1 y velocidad de procesamiento y respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas y procedimientos de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización PSV y P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1, y la precisión de respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas y procedimientos de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización TR y P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión y velocidad de respuesta en la tarea 2. Esto señala una buena capacidad para adaptarse a las reglas de una tarea, y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",

    'Automatización PSV, TR y P':"""Por otro lado, se ha observado una mejora del rendimiento en la precisión de seguimiento y atención sostenida en la tarea 1 y precisión y velocidad de procesamiento y respuesta en la tarea 2. Esto señala una capacidad excelente para adaptarse a las reglas de una tarea y automatizar y mejorar su ejecución. Esta facilidad para automatizar la ejecución de diferentes tareas puede suponer una fortaleza y ventaja para un mejor desempeño en otras actividades del estilo.""",
    }

PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK = {

    'intro':"Se indican algunas recomendaciones para trabajar con {nombre} en las próximas sesiones.",

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
    'PARRAFO_DUALTASK_final_fatiga ':"""Respecto al evidente cansancio o fatiga originado hacia el final de la prueba, hay que destacar que esta es una actividad de 2 minutos de duración. Puede ser conveniente en este aspecto entrenar la resistencia de {nombre} a la fatiga ante tareas de alta demanda cognitiva. Esto le ayudará a poder mantener su concentración y ritmo de trabajo durante más tiempo ante tareas más dinámicas y complejas. Por ejemplo, ante cálculos matemáticos complejos, síntesis de información, razonamiento contrafactual, interacciones sociales, etc.""",

}

# Este PARRAFO es opcional, condicional de si el rendimiento en C en T2 es normal o alto. En este caso elegir la opción impulsividad si TR_C es menor TR_A. Y elegir la opción distraibilidad si TR_C es mayor que TR_A. Si no hay una diferencia significativa entre TR_C y TR_A, no añadir este párrafo.
PARRAFO_DUALTASK_final_dif_TR_A_y_C = {
    'impulsividad':"""La precisión de {nombre} al emitir respuestas acertadas se ha visto perjudicado parece que en gran parte debido a la impulsividad. Esta representa otra área de la atención donde existe margen de mejora. Y donde se recomiendan actividades de control atencional interno o voluntario. Por ejemplo, con ejercicios de mindfulness, o con la adopción mediante retroalimentación o instrucciones verbales de un estilo atencional y de trabajo más reflexivo, lento pero preciso.""",

    'distraibilidad':"""Se ha registrado un deterioro en la precisión de respuesta en la tarea 2, debido a puntuales fallas de distraibilidad, y durante las cuales el procesamiento de la información de la tarea ha sido mínimo. Es importante valorar el grado de deterioro en el rendimiento de la tarea T2. Ya que de ser alto, esto significaría un problema de distraibilidad persistente y de importante interferencia en el adecuado desempeño atencional."""
    }



# ============================================================================
# 3.5.1 FourFigures
# ============================================================================

# TR - Velocidad de procesamiento
PARRAFO_FourFigures_TR = {
   'TR alto':"""{nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media de su edad.""",

    'TR normal y C normal o bajo':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media de su edad.""",

    'TR normal y C alto':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas. Primero una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado. Y segundo, una posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR bajo':"""{nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Esto puede deberse a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. O la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas. Véase a continuación, el apartado de 'Comisiones' para valorar esta segunda posibilidad.""",
}

PARRAFO_FourFigures_A = {
    'alto': """El elevado número de aciertos indica que durante toda la prueba {nombre} ha estado muy despierto. Además presentadno una especial facilidad perceptiva para esta tarea, lo cual puede haber favorecido el desempeño en otras dimensiones atencionales.""",
    
    'normal': """El número de aciertos obtenido es adecuado y dentro de la norma para su edad. Esto señala un adecuado estado de activación o vigilia durante la prueba.""",
    
    'bajo': """El número de aciertos obtenido es limitado, menor a lo normal o esperable para su edad. Este índice se suele asociar al estado de activación o vigilia de la persona. En este caso parece que {nombre} no estuvo lo suficientemente despierto durante la tarea. Otra explicación posible es que {nombre} haya respondido aleatoriamente o que no haya entendido bien las instrucciones. En cualquier caso esta atención general deficiente ha perjudicado el desempeño en el resto de dimensiones atencionales en esta prueba evaluadas.""",
    }


# C - Errores de comisión
PARRAFO_FourFigures_C = {
    'C alto y TR alto o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una muy buena capacidad para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C alto y TR bajo':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una muy buena capacidad para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",

    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Considerando la suma rapidez con la que se responde vemos que estos errores de comisión se deben a una escepcionalmente alta impulsividdad, con respuestas más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C bajo y TR normal o bajo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Considerando el velocidad normal o lenta con el que se responde, vemos que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",
}

# Flexibilidad cognitiva. Diferencia puntuación obtenida en P4 vs puntuación esperada en P4 en base a puntuación obtenida en P2 y P3.
PARRAFO_FourFigures_P4_A_obtenido_vs_esperado = {
# Álvaro. Comparar prueba significación prueba t o PT en comparación con la muestra? Aquí avogo por PT dada la mayor facilidad de P2 y P3 frente la tarea NamingNumbers, en la cual propongo usar sign. prueba t.
    'alto': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento incluso superior al esperado, prueba de una excelente capacidad para adaptarse y dirigir su atención a voluntad.""",

    'normal': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento normal e igual a lo esperable. Esto prueba una adecuada capacidad para adaptarse y dirigir su atención a voluntad.""",
    
    'bajo': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento inferior al esperado. Esto muestra una alta rigidez cognitiva o dificultad para cambiar el foco atencional rápidamente y adaptarse a una nueva forma de procesar y responder a una tarea."""
}


# ============================================================================
# 3.5.2 NamingNumbers
# ============================================================================


# TR - Velocidad de procesamiento
PARRAFO_NamingNumbers_TR = {
   'TR alto':"""{nombre} muestra un tiempo de respuesta rápido, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media de su edad.""",

    'TR normal y C normal o bajo':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media de su edad.""",

    'TR normal y C alto':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad. Además un breve vistazo al número de comisiones durante la tarea nos muestra la excelente precisión de {nombre} durante la tarea. Ambos índices parecen señalar dos cosas. Primero una sobrada capacidad para procesar esta tarea y otras más difíciles en un tiempo de respuesta adecuado. Y segundo, una posible preferencia por un estilo atencional más reflexivo, que prioriza precisión ante velocidad de respuesta.""",
    
    'TR bajo':"""{nombre} muestra un tiempo de respuesta lento, lo que indica una velocidad de procesamiento de la información y toma de decisiones significativamente por debajo del promedio. Esto puede deberse a un déficit en el procesamiento, necesidad de más tiempo para procesar la misma cantidad de información que otros individuos de su edad. O la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas. Véase a continuación, el apartado de 'Comisiones' para valorar esta segunda posibilidad.""",
}

PARRAFO_NamingNumbers_A = {
    'alto': """El elevado número de aciertos indica que durante toda la prueba {nombre} ha estado muy despierto. Además presentadno una especial facilidad perceptiva para esta tarea, lo cual puede haber favorecido el desempeño en otras dimensiones atencionales.""",
    
    'normal': """El número de aciertos obtenido es adecuado y dentro de la norma para su edad. Esto señala un adecuado estado de activación o vigilia durante la prueba.""",
    
    'bajo': """El número de aciertos obtenido es limitado, menor a lo normal o esperable para su edad. Este índice se suele asociar al estado de activación o vigilia de la persona. En este caso parece que {nombre} no estuvo lo suficientemente despierto durante la tarea. Otra explicación posible es que {nombre} haya respondido aleatoriamente o que no haya entendido bien las instrucciones. En cualquier caso esta atención general deficiente ha perjudicado el desempeño en el resto de dimensiones atencionales en esta prueba evaluadas.""",
    }


# C - Errores de comisión
PARRAFO_NamingNumbers_C = {
    'C alto y TR alto o normal':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una muy buena capacidad para discriminar la información de manera eficiente y una muy baja impulsividad.""",

    'C alto y TR bajo':"""Respecto al número de errores de comisión, este fue bajo, lo que señala que pocas veces emite una respuesta errónea. Este resultado señala una muy buena capacidad para discriminar la información de manera eficiente y una muy baja impulsividad. Por otro lado, {nombre} tarda más de lo normal o esperado en emitir sus respuestas. Ambos índices parecen señalar la prevalencia de un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""Respecto al número de errores de comisión, este fue normal, lo que señala que emite un número de respuestas erróneas igual a lo esperado para su edad. Este resultado señala, a la hora de tomar decisiones, una capacidad adecuada para discriminar la información de manera eficiente y un nivel de impulsividad igual al esperado para su edad.""",

    'C bajo y TR alto':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Considerando la suma rapidez con la que se responde vemos que estos errores de comisión se deben a una escepcionalmente alta impulsividdad, con respuestas más rápidas pero menos precisas. Son errores que se pueden reducir si se practica un desempeño tranquilo y concienciado mantenido a lo largo de toda la tarea.""",

    'C bajo y TR normal o bajo':"""Respecto al número de errores de comisión, este fue alto, lo que señala que emite un número de respuestas erróneas superior a lo esperado para su edad. Considerando el velocidad normal o lenta con el que se responde, vemos que el problema no está primariamente vinculado a impulsividad, sino a importantes dificultades perceptivas y en el procesamiento de la información, que incapacitan a {nombre} a discriminar la información de manera eficiente, independientemente de la velocidad con la que intente responder.""",
}

# Flexibilidad cognitiva. Diferencia puntuación obtenida en P4 vs puntuación esperada en P4 en base a puntuación obtenida en P2 y P3.
PARRAFO_NamingNumbers_P4_A_obtenido_vs_esperado = {
# Álvaro. Comparar prueba significación prueba t o PT en comparación con la muestra? Aquí avogo por PT dada la mayor facilidad de P2 y P3 frente la tarea NamingNumbers, en la cual propongo usar sign. prueba t.
    'alto': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento incluso superior al esperado, prueba de una excelente capacidad para adaptarse y dirigir su atención a voluntad.""",

    'normal': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento normal e igual a lo esperable. Esto prueba una adecuada capacidad para adaptarse y dirigir su atención a voluntad.""",
    
    'bajo': """Por último, comparamos el rendimiento real obtenido en la parte 4 de la prueba con el rendimiento esperado en base a la puntuación obtenida en las partes anteriores. Véanse estas en la tabla anterior. La diferencia con la parte 4 es que aquí el objetivo a atender cambia continuamente. De esta manera obtenemos un índice de la flexibilidad cognitiva, o capacidad para adaptarse rápidamente a cambios en las reglas de ejecución de una tarea. En este sentido, {nombre} ha mostrado un rendimiento inferior al esperado. Esto muestra una alta rigidez cognitiva o dificultad para cambiar el foco atencional rápidamente y adaptarse a una nueva forma de procesar y responder a una tarea."""
}

# ============================================================================
# 3.6 Digits Memorization
# ============================================================================

# Calcular este índice en función de la PT promedio de PD_directo y PD_inverso
PARRAFO_DigitsMemorization = {

    'bajo':"""Finalmente está la prueba de memorización de dígitos, la cual informa sobre la capacidad de memoria operativa. En este aspecto el desempeño promedio ha resultado deficiente, por debajo de la norma o lo esperable. Esto significa que {nombre} solo puede mantener consciente por un tiempo una cantidad reducida de información. Véase a continuación, para cada parte de la prueba, el número de series y el número máximo de dígitos recordados correctamente:""",

    'normal':"""Finalmente está la prueba de memorización de dígitos, la cual informa sobre la capacidad de memoria operativa. En este aspecto el desempeño ha resultado normal. {nombre} puede adecuadamente procesar y mantener consciente por un tiempo una creciente cantidad de información. Véase a continuación, para cada parte de la prueba, el número de series y el número máximo de dígitos recordados correctamente:""",

    'alto':"""Finalmente está la prueba de memorización de dígitos, la cual informa sobre la capacidad de memoria operativa. En este aspecto el desempeño ha resultado escepcionalmente bueno. {nombre} tiene una gran capacidad para procesar y mantener consciente por un tiempo una gran cantidad de información. Véase a continuación, para cada parte de la prueba, el número de series y el número máximo de dígitos recordados correctamente:""",
}


# Puntuacion decreciente entre P1 < P2 < P3
PARRAFO_DigitsMemorization_decreciente = {

    'decreciente':"""Adicionalmente, se puede ver en la tabla anterior que se recuerda mejor las primeras partes de la prueba frente las siguientes. Esto es debido a la dificultad creciente de la prueba, lo que normaliza este desempeño decreciente y más aún, da mayor validez y veracidad a la medición obtenida sobre ela capacidad de memoria operativa de {nombre}.""",
}


# Se calcula en función de series erradas antes de las 2 últimas: alto si 0, normal si 1 o 2, bajo si más
PARRAFO_DigitsMemorization_consistencia = {

    'alto':"""Otro aspecto a mencionar es la muy estrecha relación existente entre el número de dígitos a memorizar y el recuerdo exitoso. Esto reduce la posibilidad de errores debido a despistes y aumenta la confianza en una medición representativa de la capacidad de memoria operativa real de {nombre}.""",

    'normal': """Otro aspecto a mencionar es la normal relación existente entre el número de dígitos a memorizar y el recuerdo exitoso. Antes de llegar al tope de su capacidad de memoria operativa {nombre} ya falla alguna serie por alguna comisión puntual debido a un despiste, impulso o desliz. Estos errores puntuales durante la prueba se encuentran sin embargo dentro de la normalidad y no restan credibilidad a la medición final de la capacidad de memoria operativa de {nombre}.""",

    'bajo':"""No obstante resulta importante mencionar la reducida relación existente entre el número de dígitos a memorizar y el recuerdo exitoso. Antes de llegar al tope de su capacidad de memoria operativa {nombre} ya falla varias series debido a despistes, impulsos o deslices. La alta incongruencia entre series de menos dígitos erradas, y la mayor serie en dígitos finalmente alcanzada a recordar, sugiere que la medición final de la capacidad de memoria operativa de {nombre} puede estar limitada. Sesgada a la baja en cambio por la presencia de otros problemas atencionales de diferente índole: arousal, distracción, velocidad de procesamiento, impulsividad, etc.""",

}

PARRAFO_DigitsMemorization_P3 = {

    'P3_inesperado':"""Por otro lado y de último, destaca el significativamente peor resultado de en la parte 3 de la prueba. Este resultado tan deteriorado difiere drásticamente de lo esperable en base al rendimiento en las partes anteriores. Por lo tanto parece que este resultado puede no ser tan representativo de la capacidad de memoria operativa, y en cambio estar sesgado por un problema cognitivo específico de esta parte con cálculo. Esto es, la sospecha de una posible discalculia.""",

}

# ============================================================================
# 4. FINAL
# ============================================================================

# Párrafo de síntesis final con rendimiento PT en el las dimensiones a evaluar.

PARRAFO_sintesis_arousal = {
    # Si solo 1 de los 4 índices es desfavorable
    'poco malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente normal, a excepción de algún caso puntual (tarea {tarea_deficit_arousal}) donde este aspecto ha resultado inferior.""",

    # Si 2 o 3 de 4 desfavorables
    'malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente deficiente, en especial durante las tareas: {tarea_deficit_arousal}. Esto perjudica el rendimiento en el resto de índices atencionales evaluados, y sesga la fiabilidad con la que se pueden medir en detalle estas dimensiones.""",

    # Si 4 de 4 desfavorables
    'muy malo':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completamente deficiente en todas las pruebas: {tarea_deficit_arousal}. Esto puede suponer una falla atencional muy grave, o bien la nulidad de la prueba. Pues un resultado tan negativo también puede deberse a una completa falta de entendimiento o actividad durante el desempeño de la tarea. Esto perjudica enormemente el rendimiento en el resto de índices atencionales evaluados, y sesga la fiabilidad con la que se pueden medir en detalle estas dimensiones.""",

    # Si todo normal
    'normal':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completamente normal en todas las pruebas. Esto señala un adecuado estado de activación durante toda la evaluación, lo que ya sugiere un estado atencional general favorable y una mayor fiabilidad de los resultados obtenidos en el resto de dimensiones evaluadas.""",

    # Si algunos desfavorables y otros, en menor medida, favorables
    'malo y poco bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente desfavorable: {tarea_deficit_arousal}. Aunque este problema parece desaparecer o incluso revertirse en otras pruebas: {tarea_fortaleza_arousal}. Parece que {nombre} ha estado más dormido o despierto según la prueba. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado muy variable, con un estado significativamente más despierto ante la(s) prueba(s): {tarea_fortaleza_arousal}. Y más dormido durante {tarea_deficit_arousal}. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente superior: {tarea_fortaleza_arousal}. Aunque con excepciones puntuales donde esta atención general ha decrecido, incluso hasta el punto de resultar deficiente; {tarea_deficit_arousal}. Parece que {nombre} ha estado excepcionalmente más dormido o despierto según la prueba. Esto podría deberse a diversas causas, tales como: diferente estimulación o interés entre pruebas, demora en adaptarse al procedimiento general de evaluación, o la fatiga acumulada. Independientemente del motivo, este hecho provoca más variabilidad en el resto de dimensiones evaluadas, y con esto, una menor fiabilidad en la señalización de déficits o fortalezas concretos y puntuales.""",

    # Si solo 1 de los 4 índices es favorable
    'poco bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado adecuado, e incluso excepcionalmente favorable en algún caso puntual (tarea {tarea_fortaleza_arousal}). Esto mejora la fiabilidad y el detalle con los que se miden el resto de índices atencionales evaluados.""",

    # Si 2 o 3 de 4 favorables
    'bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado mayormente favorable, e incluso excepcional durante las tareas: {tarea_fortaleza_arousal}. Esto mejora la fiabilidad y el detalle con los que se miden el resto de índices atencionales evaluados.""",

    # Si 4 de 4 favorables
    'muy bueno':"""Primeramente, en cuestión de arousal, o el grado de activación y atención general en el que se encontraba {nombre} durante la prueba. Este ha resultado completa y excepcionalmente favorable durante todas las pruebas. Esto mejora la fiabilidad y el detalle con los que se miden el resto de índices atencionales evaluados.""",
    }


PARRAFO_sintesis_atencionsostenida = {
    # Si solo 1 o 2 de los 6 índices es desfavorable
    'poco malo':"""El siguiente aspecto a revisar es el de atención sostenida. En este sentido el desempeño ha sido mayormente normal y adecuado, pero con algún problema puntual en la parte de: {tarea_deficit_atencionsostenida}. Esto señala una puntual incapacidad para mantener una atención prolongada durante una misma tarea, que debido a sus particularidades resultó especialmente aburrido o agotador""",

    # Si entre 3 y 4 desfavorables
    'malo':"""El siguiente aspecto a revisar es el de la atención sostenida. En este sentido el desempeño ha sido mayormente desfavorable, con especial deterioro en la parte de: {tarea_deficit_atencionsostenida}. Esto señala un patrón de vulnerabilidad a la fatiga, e incapacidad más generalizada para mantener una atención prolongada.""",
    
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
    'malo':"""Con respecto al control ejecutivo (atención selectiva + control inhibitorio). El rendimiento ha sido desfavorable, en particular en las partes de: {tarea_deficit_controlejecutivo}. Frecuentemente {nombre} presenta importantes dificultades para discriminar la información relevante e irrelevante e inhibir las respuestas impulsivas.""",

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
    'malo':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento deficiente. Esto sugiere cierta dificultad para procesar y responder adecuadamente ante tareas complejas que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",

    'normal':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento normal. Esto sugiere una capacidad adecuada para procesar y responder ante tareas complejas que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",

    'bueno':"""Otro aspecto a mencionar es el de la memoria de trabajo o memoria operativa. En este aspecto {nombre} ha mostrado un rendimiento excelente. Esto sugiere una capacidad por encima del promedio para procesar y responder ante tareas complejas que demandan atender y mantener consciente por un tiempo una cantidad creciente de información.""",
}


PARRAFO_sintesis_velocidadprocesamiento = {
    # Si solo 1 de los 5 índices es desfavorable
    'poco malo':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento normal en la mayoría de las pruebas, aunque con ocasional deterioro significativo en la parte de {tarea_deficit_velocidadprocesamiento}. Normalmente {nombre} procesa la información a una velocidad adecuada. Aunque en algún caso puntual debido quizás a la fatiga acumulada o la dificultad de la tarea, puede ralentizarse más de lo esperable.""",

    # Si entre 2 y 3 desfavorables
    'malo':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento deficiente: {tarea_deficit_velocidadprocesamiento}. {nombre} presenta una velocidad de procesamiento y respuesta especialmente lenta, lo que le dificulta o incapacidad dar respuestas precisas rápidas cuando es necesario.""",

    # Si entre 4 y 5 desfavorables
    'muy malo':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento completamente deficiente en todas o casi todas las pruebas. {nombre} presenta una velocidad de procesamiento y respuesta escepcionalmente lenta. Un resultado tan negativo más probable significa la nulidad de la evaluación, debido a la ausencia de participación activa y seria durante las pruebas. De no ser este el caso, esto reflejaría una muy grave dificultad e incapacidad para responder rápidamente cuando es necesario.""",

    # Si todo normal
    'normal':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento completamente normal. {nombre} procesa y responde a la información en un tiempo adecuado o igual a lo esperable.""",

    # Si 1 favorable 2 no
    'malo y poco bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento variable. En la mayoría de casos el rendimiento fue normal, o incluso excepcionalmente bueno en: {tarea_fortaleza_velocidadprocesamiento}. Sin embargo, también hay un par de casos en los que el desempeño resulto deficiente: {tarea_deficit_velocidadprocesamiento}. Parece que, en general, {nombre} presenta una velocidad de procesamiento y respuesta adecuada. Aunque también existen casos puntuales en los que, quizás debido a la fatiga acumulada o la dificultad de la tarea, la respuesta puede ralentizarse notablemente.""",

    # Si 1 o 2 favorable y 3 no, o 4 desfavorable y 1 no
    'muy malo y poco bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy variable. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo, pues puede ser prueba de una ejecución aleatoria de la tarea. En caso contrario y siguiendo la prevalencia mayoritaria, {nombre} parece presentar una deficiente velocidad de procesamiento que le imposibilita dar respuesta rápidas en la mayoría de casos: {tarea_deficit_velocidadprocesamiento}. Aunque este problema parece solventarse o incluso revertirse en algún(os) caso(s), como ante {tarea_fortaleza_velocidadprocesamiento}. Si estos resultados son representativos de una ejecución seria de la prueba, cabe indagar más acerca de esta variabilidad, que puede deberse por ejemplo a una especial dificultad para lidiar con la fatiga acumulada o la creciente dificultad de una tarea.""",

    # Si algunos desfavorables y otros, en igual medida, favorables
    'malo y bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy variable. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. De ser un resultado de una ejecución seria de la tarea, {nombre} presentaría una velocidad sumamente variable entre tareas mostrando en ocasiones un rendimiento normal, con ocasional rendimiento excelente ({tarea_fortaleza_velocidadprocesamiento}) o insuficiente ({tarea_deficit_velocidadprocesamiento}). En tal caso, cabe indagar más acerca de esta variabilidad, que puede verse afectada por otras variables tales como la fatiga acumulada o la dificultad y otras particularidades de cada tarea.""",

    # Si algunos desfavorables y otros, en mayor medida, favorables
    'poco malo y bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento mayormente favorable, e incluso sobresaliente en algunos casos: {tarea_fortaleza_velocidadprocesamiento}. Sin embargo, este rendimiento es variable, y también se ha observado un desempeño insuficiente en alguna(s) parte(s): ({tarea_deficit_velocidadprocesamiento}. Esta variabilidad resulta atípica y reduce la fiabilidad de medición del constructo. Basándonos en la prevalencia mayoritaria, parece que normalmente {nombre} procesa la información a una velocidad adecuada o incluso por encima del promedio. Aunque también existe el caso en que, quizás debido a la fatiga acumulada o la dificultad de la tarea, la respuesta puede ralentizarse drásticamente.""",

    # Si 1 favorable
    'poco bueno':""""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento normal, e incluso escepcionalmente bueno en alguna ocasión ({tarea_fortaleza_velocidadprocesamiento}. {nombre} puede procesar y responder a la información a una velocidad adecuada o incluso superior al promedio.""",

    # Si entre 2 y 3 favorables
    'bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento excelente, en especial en la parte de: {tarea_fortaleza_velocidadprocesamiento}. {nombre} puede procesar y responder a la información a una velocidad escepcionalmente rápida. Esto es indicativo de altas capacidades""",

    # Si entre 4 y 5 favorables
    'muy bueno':"""Por último, en relación a la velocidad de procesamiento o tiempo de respuesta. Aquí se ha mostrado un rendimiento muy por encima del promedio durante todas las pruebas. {nombre} procesa y responde a la información a una velocidad escepcionalmente rápida. Esto es indicativo de altas capacidades""",

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
    'normal':"""Finalmente, {nombre} ha mostrado un desempeño adecuado, sin deficiencia atencional alguna en cualquiera de las áreas evaluadas. Por lo tanto, no hay motivos para extender este cribado de habilidades neuropsicológicas a una evaluación o intervención más profunda. No existe necesidad de refuerzo especial, dado que las habilidades de {nombre} se ajustan a lo normal y esperable para una persona de su edad.""",

# Caso Bueno: 5 o más PTs altas y no 1 o ninguna PT baja
    'bueno':"""Finalmente, {nombre} ha mostrado desempeño adecuado, incluso por encima del promedio. El funcionamiento y capacidad atencional de {nombre} es sobresaliente. Un resultado tan positivo incluso puede ser señal de altas capacidades. Más evaluación al respecto es recomendable ya ante una condición de altas capacidades puede traer también problemas a futuro, tales como desinterés, desapetencia y falta de disciplina. Aunque detectado a tiempo puede ser una fortaleza a aprovechar.""",

# Caso Muy Bueno: 10 o más PTs altas y no PTs baja
    'muy bueno':"""Finalmente, el desempeño ha resultado muy por encima del promedio. El funcionamiento y capacidad atencional de {nombre} es escepcionalmente bueno. Este resultado señala que {nombre} tiene altas capacidades. Una evaluación y consideración especial de esta condición es recomendable, ya que en casos como este se avoga por un reacondicionamiento de la enseñanza recibida a la altura de sus capacidades. Esto a fin de aprovechar este potencial al máximo y evitar la aparición de factores perjudiciales en el aprendizaje, tales como desinterés, desapetencia y falta de disciplina.""",

}