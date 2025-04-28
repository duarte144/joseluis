# 🚗 Proyecto Punto Extra: Gestión de Automóviles

## 📚 Descripción
Sistema de administración de automóviles desarrollado con **Django** y **Django REST Framework** para el proyecto de nota extra.

---

## 🔧 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Joseluisduartepachon/PUNTOEXTRA.git
cd PUNTOEXTRA

# 2. Crear y activar entorno virtual
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos
python manage.py migrate

# 5. Ejecutar servidor
python manage.py runserver


📂 Estructura del Proyecto
PUNTOEXTRA/
├── DuarteApp/             # Aplicación principal    
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Lógica de la aplicación
│   └── api/               # API REST (router.py, serializers.py, views.py)
├── manage.py              # Script principal de Django
└── requirements.txt       # Dependencias del proyecto

✨ Funcionalidades Clave
📋 Registro de automóviles con todos sus datos.

🔎 Búsqueda en tiempo real por múltiples campos.

✏️ Edición de registros existentes.

🗑️ Eliminación segura con confirmación.

📱 Interfaz adaptable a dispositivos móviles.

🌐 API REST para gestión de automóviles (GET, POST, PUT, DELETE)

🛠️ Uso de la Aplicación

Acción	Descripción
➕ Agregar	Registrar nuevos automóviles desde el formulario
🔎 Buscar	Buscar vehículos usando el campo de búsqueda
✏️ Editar	Modificar información de automóviles existentes
🗑️ Eliminar	Borrar registros con confirmación de seguridad

🚀 API REST

Método	Endpoint	Acción
GET	/api/automoviles/	Listar todos los automóviles
POST	/api/automoviles/	Crear un nuevo automóvil
GET	/api/automoviles/{id}/	Ver detalles de un automóvil
PUT	/api/automoviles/{id}/	Actualizar un automóvil
DELETE	/api/automoviles/{id}/	Eliminar un automóvil

📧 Contacto
✉️ Email: joseluisduartepachon@gmail.com

🐙 GitHub: Joseluisduartepachon



