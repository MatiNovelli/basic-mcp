# 🤖 Basic MCP Agent

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange?logo=google&logoColor=white)
![OpenAI SDK](https://img.shields.io/badge/OpenAI%20SDK-compatible-green?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-purple)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)

Agente CLI en Python que demuestra cómo funcionan internamente los **tool calls** y los **agentes con LLMs**, usando Gemini 2.5 Flash a través de la API compatible con OpenAI.

---

## 📖 ¿Qué es MCP y qué demuestra este proyecto?

**MCP (Model Context Protocol)** es un estándar que define cómo los modelos de lenguaje pueden interactuar con herramientas externas de forma estructurada. En lugar de que el modelo solo genere texto, puede "llamar" funciones reales del sistema.

Este proyecto implementa ese mecanismo de forma manual y minimalista:

1. El usuario escribe un prompt en la terminal.
2. El modelo decide si necesita usar una herramienta o responder directamente.
3. Si usa una herramienta, el código Python la ejecuta localmente.
4. El resultado se muestra en pantalla.

El objetivo no es construir un producto, sino **entender desde adentro** cómo un LLM puede actuar como agente.

---

## ✨ Features principales

- 🗂️ **Listar archivos** de cualquier directorio del sistema
- 📄 **Leer el contenido** de un archivo
- 📝 **Crear archivos** con contenido personalizado
- ⚡ Integración con **Gemini 2.5 Flash** vía endpoint OpenAI-compatible
- 🔁 Bucle interactivo en consola (REPL)

---

## 📁 Estructura del proyecto

```
basic-mcp/
├── main.py          # Bucle principal: input → LLM → tool call → output
├── llm.py           # Definición de herramientas en formato OpenAI (schemas)
├── tools.py         # Implementaciones Python de cada herramienta
├── requirements.txt # Dependencias del proyecto
├── .env.example     # Plantilla de variables de entorno
├── .env             # Variables de entorno reales (NO subir a git)
└── README.md
```

---

## ✅ Requisitos previos

- Python 3.9 o superior
- Una API key válida de Google Gemini (gratuita)
- Git

---

## 🚀 Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/basic-mcp.git
cd basic-mcp
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración del archivo `.env`

Copiá el archivo de ejemplo y completá tu API key:

```bash
cp .env.example .env
```

Luego editá el archivo `.env`:

```env
GEMINI_API_KEY="tu_api_key_aquí"
```

> ⚠️ Nunca subas el archivo `.env` a GitHub. Ya está incluido en `.gitignore`.

---

## 🔑 ¿Cómo obtener una API key de Gemini?

1. Ingresá a [Google AI Studio](https://aistudio.google.com/)
2. Iniciá sesión con tu cuenta de Google
3. Hacé clic en **"Get API key"**
4. Creá una nueva API key y copiala
5. Pegala en tu archivo `.env`

El plan gratuito es suficiente para usar este proyecto.

---

## ▶️ Cómo ejecutar el proyecto

Con el entorno virtual activado:

```bash
python main.py
```

Verás el prompt `>>>` esperando tu input:

```
>>> ¿Qué archivos hay en el directorio actual?
```

Para salir, presioná `Ctrl+C`.

---

## 💬 Ejemplos de prompts para probar

```
>>> ¿Qué archivos hay en el directorio actual?
>>> Leé el archivo main.py y explicame qué hace
>>> Creá un archivo llamado hola.txt con el contenido "Hola, mundo!"
>>> Listá los archivos que hay en la carpeta venv/bin
```

---

## 🔬 ¿Cómo funciona internamente?

El flujo completo de cada interacción es el siguiente:

```
Usuario (input)
      │
      ▼
   main.py
      │  Envía el mensaje + lista de herramientas disponibles
      ▼
  Gemini 2.5 Flash (vía API)
      │
      ├─── Respuesta directa (texto)  ──────────────────────► Imprime respuesta
      │
      └─── Tool call (el modelo quiere usar una herramienta)
                │
                │  Nombre de la herramienta + argumentos (JSON)
                ▼
           tool_map[nombre](**args)
                │
                │  Ejecuta la función Python local
                ▼
           Resultado de la herramienta
                │
                ▼
           Imprime resultado en consola
```

### Detalle por archivo

| Archivo | Rol |
|---|---|
| `llm.py` | Define los **schemas** de las herramientas en formato JSON (qué parámetros acepta cada una). El modelo los lee para saber qué puede usar. |
| `tools.py` | Contiene las **implementaciones reales** de cada herramienta (funciones Python puras). |
| `main.py` | Orquesta el flujo: recibe input, llama al LLM, detecta tool calls y los ejecuta usando el `tool_map`. |

---

## 🛠️ Sistema de tools / Function calling

El **function calling** es el mecanismo por el cual un LLM puede solicitar ejecutar una función externa en lugar de responder con texto.

Funciona así:

1. Al hacer la llamada a la API, se envía una lista de herramientas disponibles (definidas en `llm.py`).
2. El modelo analiza el prompt y decide si necesita una herramienta.
3. Si la necesita, responde con un objeto estructurado: `{ nombre, argumentos }` en lugar de texto.
4. Tu código Python recibe ese objeto, ejecuta la función correspondiente y muestra el resultado.

Para agregar una nueva herramienta al proyecto hay que hacer tres cambios:

- **`llm.py`**: agregar el schema JSON de la nueva función.
- **`tools.py`**: implementar la función Python.
- **`main.py`**: registrar la función en el `tool_map`.

---

## 🧠 ¿Qué aprendés con este proyecto?

- Cómo funciona el **function calling** en la práctica con una API de LLM real
- La diferencia entre el **schema** de una herramienta y su **implementación**
- Cómo un modelo decide cuándo usar una herramienta y cuándo responder con texto
- El patrón básico de un **agente**: percibir → razonar → actuar
- Cómo usar la API de Gemini a través del **SDK compatible con OpenAI**
- La estructura de un **bucle REPL** para agentes conversacionales

---

## 🗺️ Roadmap

- [ ] Historial de conversación entre turnos (memoria de contexto)
- [ ] Loop multi-paso: el agente puede encadenar múltiples tool calls antes de responder
- [ ] Nuevas herramientas: ejecutar comandos de terminal, buscar en internet
- [ ] Interfaz más amigable con colores en la terminal (`rich`)
- [ ] Soporte para múltiples modelos (OpenAI, Ollama local)
- [ ] Tests unitarios para cada herramienta

---

## 🐛 Troubleshooting

**Error: `GEMINI_API_KEY not found`**
> Asegurate de haber creado el archivo `.env` y de que la variable esté correctamente escrita.

**Error: `ModuleNotFoundError`**
> Verificá que el entorno virtual esté activado (`source venv/bin/activate`) y que hayas instalado las dependencias (`pip install -r requirements.txt`).

**El modelo no usa ninguna herramienta**
> Reformulá el prompt de forma más directa, por ejemplo: *"Listá los archivos del directorio actual"* en lugar de *"¿Hay archivos acá?"*.

**Error `401 Unauthorized`**
> Tu API key es inválida o expiró. Generá una nueva en [Google AI Studio](https://aistudio.google.com/).

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT). Podés usarlo, modificarlo y distribuirlo libremente.
