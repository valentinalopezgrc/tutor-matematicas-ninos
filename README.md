# 🌙 Luna — Tutora de Matemáticas para Niños
### Tutor Académico Personalizado basado en IA

> Proyecto: **Desarrollo de un Asistente Experto basado en RAG y Agentes**  
> Avance 1 — Diseño de Prompts

---

## ¿Qué es Luna?

Luna es una tutora virtual de matemáticas diseñada para niños de **6 a 12 años**,
implementada con la API de Google Gemini. Usa un **estilo socrático adaptado a niños**:
nunca da la respuesta directa, sino que guía al estudiante con preguntas, ejemplos
cotidianos y celebraciones de sus logros.

---

## 🎯 Enfoque elegido

**Tutor Académico Personalizado** — matemáticas de primaria con pedagogía socrática.

---

## 🧠 Técnicas de Prompting implementadas

### 1. System Prompt estructurado
El prompt define 5 secciones claramente separadas:
- **ROL**: quién es Luna, su estilo y limitaciones
- **TAREA**: qué temas cubre y cómo los enseña
- **CONTEXTO**: dominio, nivel de edad y tono
- **RESTRICCIONES**: comportamiento ante cada tipo de entrada
- **EJEMPLOS**: 5 casos de referencia (Few-Shot)

### 2. Few-Shot Prompting
Se incluyen **5 ejemplos** de pares entrada/respuesta que cubren los casos principales:

| Ejemplo | Situación | Comportamiento esperado |
|---------|-----------|------------------------|
| 1 | Operación mal resuelta (`5 + 3 = 9`) | Guía sin dar la respuesta, usa manzanas |
| 2 | Tema fuera de dominio (`¿tu caricatura favorita?`) | Redirige con cariño hacia números |
| 3 | Pregunta de fracciones | Explica con pizza, pregunta socrática |
| 4 | Pregunta de geometría | Relaciona con objetos reales, pregunta lados |
| 5 | Problema de la vida real | Usa dinero como contexto cotidiano |

### 3. Delimitadores XML
Cada restricción de comportamiento está envuelta en etiquetas XML:
```
<restriccion_operaciones>  → cuando el niño envía una operación o respuesta
<restriccion_teoria>       → cuando pregunta cómo se hace algo
<restriccion_fracciones>   → preguntas sobre fracciones
<restriccion_geometria>    → preguntas sobre figuras geométricas
<restriccion_medidas>      → preguntas sobre unidades de medida
<restriccion_tema>         → cuando habla de algo fuera de matemáticas
```

### 4. Historial de conversación
Al finalizar la sesión se muestra el historial completo con todos los turnos,
permitiendo revisar el proceso de aprendizaje del estudiante.

---

## 🗂️ Estructura del repositorio

```
├── tutor-matematicas-ninos.py   # Código fuente principal
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore                   # Excluye .env y archivos innecesarios
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

---

## ⚙️ Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/valentinalopezgrc/tutor-matematicas-ninos.git
cd tutor-matematicas-ninos

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar API Key
cp .env.example .env
# Editar .env y agregar: GENAI_API_KEY=tu_clave_aqui

# 5. Ejecutar
python tutor-matematicas-ninos.py
```

---

## 💬 Ejemplos de interacción

```
TÚ: 5 + 3 = 9
🌙 LUNA: ¡Casi! 🌟 Imagina que tienes 5 manzanas 🍎🍎🍎🍎🍎 y tu amigo
te regala 3 más 🍎🍎🍎. ¿Cuántas manzanas tienes ahora si las cuentas
una por una? ¡Inténtalo de nuevo, tú puedes! 💪
```

```
TÚ: ¿Cuál es tu caricatura favorita?
🌙 LUNA: ¡Me encantan las caricaturas! 😄 Pero yo soy experta en números
mágicos ✨. ¿Sabías que si ves 3 episodios hoy y 4 mañana, puedes sumarlos?
¿Cuántos episodios serían en total? 🤔
```

```
TÚ: ¿Qué es una fracción?
🌙 LUNA: ¡Buena pregunta! 🎉 Imagina una pizza 🍕 cortada en 4 partes
iguales. Si te comes 1 parte, comiste 1/4. ¿Si te comes 2 partes, cómo
lo escribirías? 🤔
```

---

## 📦 Dependencias

```
google-genai
python-dotenv
```

---

## 🔮 Próximos avances

- **Avance 2**: Integración de RAG con material didáctico real (libros de primaria)
- **Avance 3**: Agente con herramientas para generar ejercicios personalizados
  según el nivel del estudiante

---

## 🛠️ Tecnologías usadas

- **Python 3.10+**
- **Google Gemini 2.5 Flash** via `google-genai`
- **Prompt Engineering**: System Prompt + Few-Shot + Delimitadores XML
