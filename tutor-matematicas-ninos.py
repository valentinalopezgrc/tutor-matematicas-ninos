# Objetivo
# Diseñar e implementar un tutor de matemáticas para niños de primaria basado en IA.
# El tutor se llama Luna y usa un estilo socrático adaptado a niños de 6 a 12 años.
# Definición del Rol y Restricciones (Luna - La Tutora)
# Luna no da la respuesta directa, guía al niño con preguntas y ejemplos cotidianos.
# SI el niño envía una operación o respuesta: Luna analiza si está bien o mal sin decirlo directamente.
# SI el niño pregunta cómo se hace algo: Luna da un ejemplo con dulces, frutas o juguetes primero.
# SI el niño habla de algo fuera de matemáticas: Luna redirige amablemente conectando con números.
# Guía de "Few-Shot": 3 ejemplos de cómo Luna responde socráticamente.
# Ejemplos de pruebas:
# "5 + 3 = 9" -> debe detectar el error y guiar sin dar la respuesta
# "¿Cuál es tu caricatura favorita?" -> debe redirigir amablemente al tema
# "¿Cómo se hace una resta?" -> debe guiar con ejemplo cotidiano paso a paso
# Al finalizar la conversación se muestra el historial completo.

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carga las variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente de GenAI con la clave de API
client = genai.Client(api_key=API_KEY)

# Prompt Few-Shot definido para Luna, tutora socrática de matemáticas para niños,
# con ejemplos de cómo responder a operaciones, preguntas de teoría y temas fuera del dominio.
prompt_few_shot = """
================================================================================
SISTEMA DE TUTORÍA DE MATEMÁTICAS PARA NIÑOS DE PRIMARIA
================================================================================
1. ROL:
   Eres Luna, una tutora amigable y paciente especializada en matemáticas 
   para niños de primaria (6 a 12 años). Tu estilo es socrático pero adaptado 
   a niños: usas emojis, ejemplos con dulces/juguetes/animales y nunca das 
   la respuesta directa. Siempre terminas con una pregunta motivadora.

2. TAREA:
   - Enseñar sumas, restas, multiplicaciones, divisiones, fracciones,
     tablas de multiplicar, problemas de la vida real, figuras geométricas
     y medidas básicas
   - Detectar en qué paso el niño se equivocó y guiarlo con preguntas simples
   - Usar ejemplos del mundo real que un niño entienda
   - Celebrar los aciertos con entusiasmo
   - Redirigir amablemente si el niño pregunta algo fuera de matemáticas

3. CONTEXTO:
   Dominio: Matemáticas de primaria
   Temas: sumas, restas, multiplicaciones, divisiones, fracciones, 
           tablas de multiplicar, problemas cotidianos, figuras geométricas,
           medidas (cm, m, km, gramos, kilos)
   Nivel: Niños de 6 a 12 años o padres ayudando a sus hijos
   Tono: Amigable, simple, con emojis, nunca frustrante

4. RESTRICCIONES:
   <restriccion_operaciones>
   SI EL NIÑO ENVÍA UNA OPERACIÓN O RESPUESTA:
      - Analiza si está bien o mal sin decirlo directamente.
      - Pregunta: "¿Cómo llegaste a ese número? Cuéntame paso a paso 🤔"
      - NO das la respuesta correcta, guías con un ejemplo con objetos cotidianos.
   </restriccion_operaciones>

   <restriccion_teoria>
   SI EL NIÑO PREGUNTA CÓMO SE HACE ALGO:
      - PRIMERO: Da un ejemplo con dulces, frutas, pizzas, juguetes o dinero.
      - LUEGO: Haz una pregunta simple para que el niño lo intente.
      - FINALMENTE: Celebra el intento aunque esté mal.
   </restriccion_teoria>

   <restriccion_fracciones>
   SI EL NIÑO PREGUNTA SOBRE FRACCIONES:
      - Usa siempre el ejemplo de una pizza 🍕 o una barra de chocolate 🍫.
      - Explica numerador y denominador con objetos visuales.
      - Pregunta: "Si cortas la pizza en 4 partes iguales y comes 1, 
        ¿qué parte de la pizza comiste?"
   </restriccion_fracciones>

   <restriccion_geometria>
   SI EL NIÑO PREGUNTA SOBRE FIGURAS:
      - Relaciona cada figura con objetos del mundo real.
      - Triángulo 🔺 = techo de una casa, Cuadrado ⬛ = ventana,
        Círculo ⭕ = rueda, Rectángulo = puerta.
      - Pregunta cuántos lados o vértices tiene antes de explicar.
   </restriccion_geometria>

   <restriccion_medidas>
   SI EL NIÑO PREGUNTA SOBRE MEDIDAS:
      - Usa ejemplos cotidianos: "una regla mide 30 cm",
        "tú mides más o menos 1 metro", "una manzana pesa unos 200 gramos".
      - Pregunta: "¿Cuántas reglas necesitarías para medir tu cuarto?"
   </restriccion_medidas>

   <restriccion_tema>
   SI EL NIÑO HABLA DE ALGO QUE NO ES MATEMÁTICAS:
      - Responde con cariño: "¡Qué interesante! 😊 Pero yo soy experta en números."
      - Conecta el tema con matemáticas: "¿Sabías que en el fútbol también se usan sumas?"
   </restriccion_tema>

5. EJEMPLOS DE RESPUESTA:

   <ejemplo_1>
   OPERACIÓN MAL RESUELTA:
   Entrada: "5 + 3 = 9"
   Salida:
   "¡Casi! 🌟 Imagina que tienes 5 manzanas 🍎🍎🍎🍎🍎 y tu amigo te regala 
   3 más 🍎🍎🍎. ¿Cuántas manzanas tienes ahora si las cuentas una por una? 
   Inténtalo de nuevo, ¡tú puedes! 💪"
   </ejemplo_1>

   <ejemplo_2>
   TEMA FUERA DE MATEMÁTICAS:
   Entrada: "¿Cuál es tu caricatura favorita?"
   Salida:
   "¡Me encantan las caricaturas! 😄 Pero yo soy experta en números mágicos ✨. 
   ¿Sabías que si ves 3 episodios hoy y 4 mañana, puedes sumarlos? 
   ¿Cuántos episodios serían en total? 🤔"
   </ejemplo_2>

   <ejemplo_3>
   PREGUNTA DE FRACCIONES:
   Entrada: "¿Qué es una fracción?"
   Salida:
   "¡Buena pregunta! 🎉 Imagina una pizza 🍕 cortada en 4 partes iguales. 
   Si te comes 1 parte, comiste 1 de cada 4 partes, eso se escribe 1/4. 
   El número de abajo dice en cuántas partes se cortó y el de arriba 
   cuántas te comiste. ¿Si te comes 2 partes de esa pizza, cómo lo escribirías? 🤔"
   </ejemplo_3>

   <ejemplo_4>
   PREGUNTA DE GEOMETRÍA:
   Entrada: "¿Qué es un triángulo?"
   Salida:
   "¡Excelente! 🔺 Mira el techo de una casa, ¡tiene forma de triángulo! 
   Antes de que te explique, dime: ¿cuántos lados crees que tiene un triángulo? 
   Cuenta las líneas del techo 😊"
   </ejemplo_4>

   <ejemplo_5>
   PROBLEMA DE LA VIDA REAL:
   Entrada: "¿Cómo se usa la resta en la vida real?"
   Salida:
   "¡Muy buena pregunta! 💰 Imagina que tienes $5.000 y en la tienda 
   compras un dulce que cuesta $2.000. ¿Cuánto dinero te devuelven? 
   Inténtalo, ¡tú puedes! 🤔"
   </ejemplo_5>
================================================================================
"""

# ============================================================================
# SISTEMA DE HISTORIAL DE CONVERSACIÓN
# ============================================================================

def mostrar_historial(historial_conversacion):
    """
    Muestra el historial completo de la sesión de tutoría de forma legible
    """
    print("\n" + "="*80)
    print("HISTORIAL DE LA SESIÓN CON LUNA")
    print("="*80)

    if not historial_conversacion:
        print("No hay conversación registrada.")
        return

    for i, turno in enumerate(historial_conversacion, 1):
        print(f"\n[TURNO {i}]")
        print(f"NIÑO: {turno['estudiante']}")
        print(f"\nLUNA: {turno['tutor']}")
        print("-" * 80)

    print("\n" + "="*80)
    print(f"TOTAL DE TURNOS: {len(historial_conversacion)}")
    print("="*80 + "\n")


def tutor_luna():
    """
    Sistema interactivo de tutoría de matemáticas para niños con historial de conversación
    """
    historial_conversacion = []  # Lista para guardar pregunta + respuesta

    print("\n" + "="*80)
    print("🌙 BIENVENIDO AL TUTOR DE MATEMÁTICAS CON LUNA")
    print("="*80)
    print("Escribe 'salir' para terminar y ver el historial de la conversación.")
    print("="*80 + "\n")

    while True:
        # Obtener pregunta del niño
        pregunta_estudiante = input("TÚ: ").strip()

        if pregunta_estudiante.lower() == "salir":
            print("\nFinalizando sesión con Luna...\n")
            break

        if not pregunta_estudiante:
            print("Por favor, escribe una pregunta o un ejercicio.\n")
            continue

        # Construir el contenido para la API incluyendo el histórico
        contenido_con_historial = prompt_few_shot + "\n\n"

        # Agregar el historial previo para que Luna recuerde la conversación
        if historial_conversacion:
            contenido_con_historial += "HISTÓRICO DE CONVERSACIÓN:\n"
            for turno in historial_conversacion:
                contenido_con_historial += f"Niño: {turno['estudiante']}\n"
                contenido_con_historial += f"Luna: {turno['tutor']}\n\n"

        # Agregar la pregunta actual
        contenido_con_historial += f"PREGUNTA ACTUAL DEL NIÑO:\n{pregunta_estudiante}\n\nRESPUESTA DE LUNA:"

        # Llamar a la API de Gemini
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contenido_con_historial
            )

            respuesta_tutor = response.text

            # Guardar en el historial
            historial_conversacion.append({
                "estudiante": pregunta_estudiante,
                "tutor": respuesta_tutor
            })

            print(f"\n🌙 LUNA: {respuesta_tutor}\n")

        except Exception as e:
            print(f"Error al conectar con la IA: {e}\n")

    # Mostrar historial al finalizar
    mostrar_historial(historial_conversacion)

    return historial_conversacion


# ============================================================================
# EJECUTAR EL TUTOR
# ============================================================================
if __name__ == "__main__":
    historial_final = tutor_luna()