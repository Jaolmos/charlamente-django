# CharlaMente 🧠

CharlaMente es una aplicación web desarrollada con Django que permite transcribir y resumir automáticamente charlas, conferencias y reuniones utilizando inteligencia artificial.

## 🚀 Características

- Transcripción automática de audio/video usando Whisper
- Generación de resúmenes con GPT-3.5
- Actualización en tiempo real del estado de procesamiento con HTMX
- Sistema de cola asíncrona con Celery y RabbitMQ
- Interfaz moderna y responsive con Bootstrap
- Tema oscuro personalizado con CSS
- Autenticación y gestión de usuarios

## 🔧 Tecnologías

### Backend
- Django
- Celery
- RabbitMQ
- MySQL

### Frontend
- HTML5
- CSS3 (diseño personalizado)
- Bootstrap 5
- HTMX
- Google Fonts (Inter & Poppins)
- Font Awesome (iconos)

### IA y Procesamiento
- OpenAI GPT-3.5
- Whisper

## 🎨 Características de Diseño

- Tema oscuro moderno
- Diseño responsive
- Animaciones y transiciones suaves
- Badges de estado dinámicos
- Iconografía consistente
- Tipografía personalizada

## 📂 Estructura del Proyecto

```
charlamente/
│── apps/
│   ├── core/ # App principal, templates base
│   ├── talks/ # Gestión de charlas y procesamiento
│   ├── users/ # Autenticación y gestión de usuarios
│
│── charlamente/ # Configuración del proyecto
│   ├── settings/ # Configuraciones separadas por entorno
│   ├── urls.py
│   ├── wsgi.py
│
│── docs/ # Documentación
│── media/ # Archivos subidos por usuarios
│── static/ # Archivos estáticos
│   ├── css/
│   ├── img/
│   ├── js/
│
│── venv/ # Entorno virtual (no versionado)
│── .env # Variables de entorno (no versionado)
│── .env.example # Ejemplo de variables de entorno
│── .gitignore 
│── manage.py 
│── requirements.txt # Dependencias del proyecto
```

## ⚙️ Instalación

### 1. Clonar el repositorio
```markdown
git clone https://github.com/tuusuario/charlamente.git
cd charlamente
```

### 2. Crear entorno virtual e instalar dependencias
```markdown
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```markdown
cp .env.example .env
```
Editar `.env` con tus configuraciones:
```markdown
OPENAI_API_KEY=tu_api_key
DATABASE_URL=mysql://user:password@localhost:3306/charlamente
```

### 4. Ejecutar migraciones
```markdown
python manage.py migrate
```

### 5. Iniciar servicios
```markdown
# Terminal 1: Django
python manage.py runserver

# Terminal 2: Celery
celery -A charlamente worker -l info
```

## 🔄 Flujo de Trabajo

1. El usuario sube un archivo de audio/video
2. El sistema lo coloca en una cola de procesamiento
3. Celery procesa el archivo:
   - Transcribe el audio con Whisper
   - Genera un resumen con GPT-3.5
4. HTMX actualiza el estado en tiempo real
5. El usuario puede ver la transcripción y el resumen

## 🌟 Características Principales

### Procesamiento de Audio/Video
- Soporte para múltiples formatos (mp3, wav, mp4, avi, mov)
- Transcripción automática con Whisper
- Generación de resúmenes con GPT-3.5

### Interfaz de Usuario
- Diseño responsive y moderno
- Tema oscuro personalizado
- Actualizaciones en tiempo real con HTMX
- Indicadores de estado dinámicos

### Sistema de Usuarios
- Registro y autenticación
- Gestión de charlas personales
- Historial de transcripciones

## 🛠️ Requisitos del Sistema

- Python 3.8+
- MySQL
- RabbitMQ
- FFmpeg (para procesamiento de audio)

## Capturas de Pantalla

### Página Principal
![Página Principal](docs/images/home.png)

### Lista de Charlas
![Mis Charlas](docs/images/talks_list.png)

### Subir Nueva Charla
![Subir Charla](docs/images/upload_talk.png)

### Detalle de Charla
![Detalle de Charla](docs/images/talk_detail.png)

---

