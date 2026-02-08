# 🎮 PlayHub - Plataforma de Juegos y Reseñas

PlayHub es una plataforma web desarrollada con Django donde los usuarios pueden gestionar un catálogo de juegos y publicar reseñas. Cuenta con un diseño minimalista y moderno.

## 📋 Características (Fase A)

### ✅ Funcionalidades Implementadas

- **Gestión de Juegos (CRUD completo)**
  - Crear, leer, actualizar y eliminar juegos
  - Campos: título, plataforma (PC, PlayStation, Xbox, Switch), precio, fecha de lanzamiento
  - Validación: precio debe ser mayor que 0

- **Sistema de Reseñas (CRUD completo)**
  - Crear, leer, actualizar y eliminar reseñas
  - Campos: título del juego, usuario, puntuación (1-10), comentario
  - Validaciones:
    - Puntuación entre 1 y 10
    - Comentario mínimo de 50 caracteres
  - Solo usuarios autenticados pueden crear/editar/eliminar reseñas
  - El nombre de usuario se asigna automáticamente

- **Autenticación**
  - Sistema de login/logout de Django
  - Protección de vistas con `LoginRequiredMixin`

- **Middleware Personalizado**
  - Registra información de cada petición:
    - Ruta
    - Método HTTP
    - Usuario autenticado
    - Tiempo de ejecución en milisegundos

- **Panel de Administración**
  - Modelos registrados con configuraciones personalizadas
  - `list_display`, `search_fields`, `list_filter`
  - Búsqueda y filtrado avanzado

- **Diseño Minimalista y Moderno**
  - Interfaz limpia con fondo blanco
  - Colores profesionales (azul primario)
  - Sombras sutiles y bordes limpios
  - Tipografía moderna
  - Diseño responsive con Bootstrap 5

## 🎨 Sistema de Diseño

### Paleta de Colores
- **Primario**: `#2563eb` (azul vibrante)
- **Secundario**: `#64748b` (gris)
- **Fondo**: `#f8fafc` (blanco suave)
- **Superficie**: `#ffffff` (blanco)
- **Texto**: `#0f172a` (negro suave)
- **Bordes**: `#e2e8f0` (gris claro)

### Características del Diseño
- Variables CSS para consistencia
- Transiciones suaves
- Efectos hover sutiles
- Sombras profesionales
- Bordes redondeados
- Tipografía del sistema


## 📁 Estructura del Proyecto

```
PlayHub/
├── playhub/              # Configuración del proyecto
│   ├── settings.py       # Configuración principal
│   ├── urls.py          # URLs principales
│   └── wsgi.py
├── games/               # App de juegos
│   ├── models.py        # Modelo Juego
│   ├── views.py         # Vistas CRUD
│   ├── forms.py         # Formulario JuegoForm
│   ├── admin.py         # Configuración admin
│   └── urls.py          # URLs de juegos
├── reviews/             # App de reseñas
│   ├── models.py        # Modelo Reseña
│   ├── views.py         # Vistas CRUD (con LoginRequiredMixin)
│   ├── forms.py         # Formulario ReseñaForm
│   ├── admin.py         # Configuración admin
│   └── urls.py          # URLs de reseñas
├── middleware/          # Middleware personalizado
│   └── request_logger.py
├── templates/           # Plantillas HTML
│   ├── base.html        # Template base (usa CSS externo)
│   ├── registration/
│   │   └── login.html
│   ├── games/
│   │   ├── juego_list.html
│   │   ├── juego_detail.html
│   │   ├── juego_form.html
│   │   └── juego_confirm_delete.html
│   └── reviews/
│       ├── reseña_list.html
│       ├── reseña_form.html
│       └── reseña_confirm_delete.html
├── static/              # Archivos estáticos
│   └── css/
│       └── estilos.css  # Estilos minimalistas
├── venv/                # Entorno virtual
├── db.sqlite3           # Base de datos
└── manage.py
```

## 🎯 Uso de la Aplicación

### Gestión de Juegos

1. **Ver catálogo**: Navega a "Juegos" en el menú
2. **Agregar juego**: Click en "Agregar Juego"
3. **Ver detalles**: Click en "Ver" en cualquier juego
4. **Editar**: Click en "Editar" en cualquier juego
5. **Eliminar**: Click en "Eliminar" y confirma

### Gestión de Reseñas

1. **Ver reseñas**: Navega a "Reseñas" en el menú
2. **Crear reseña**: 
   - Debes iniciar sesión primero
   - Click en "Escribir Reseña"
   - Completa el formulario (mínimo 50 caracteres en comentario)
3. **Editar/Eliminar**: Solo puedes editar/eliminar tus propias reseñas

### Panel de Administración

1. Accede a http://127.0.0.1:8000/admin/
2. Inicia sesión con: `admin` / `admin123`
3. Gestiona juegos y reseñas con funciones avanzadas

## 🔍 Validaciones Implementadas

### Modelo Juego
- **precio**: Debe ser mayor que 0 (validación en modelo y formulario)

### Modelo Reseña
- **puntuacion**: Debe estar entre 1 y 10 (validación en modelo y formulario)
- **comentario**: Mínimo 50 caracteres (validación en modelo y formulario)

## 🛡️ Seguridad

- Las vistas de creación, edición y eliminación de reseñas están protegidas con `LoginRequiredMixin`
- Los usuarios no autenticados son redirigidos al login
- El campo `usuario_username` se asigna automáticamente desde `request.user.username`

## 📊 Middleware de Logging

El middleware personalizado registra en consola:
```
[GET] /juegos/ - User: admin - Time: 45.23ms
[POST] /reseñas/crear/ - User: usuario1 - Time: 123.45ms
```

## 🎨 Arquitectura CSS

### Archivo de Estilos: `static/css/estilos.css`

**Características**:
- Variables CSS para colores y espaciados
- Estilos modulares por componente
- Diseño responsive
- Transiciones suaves
- Estados de focus para accesibilidad
- Scrollbar personalizado

**Ventajas**:
- ✅ Separación de responsabilidades
- ✅ Fácil mantenimiento
- ✅ Reutilización de estilos
- ✅ Mejor rendimiento (cacheable)
- ✅ Código más limpio en templates

## 📝 Notas de la Fase A

En la **Fase A** del proyecto:
- Los modelos **NO** usan relaciones ForeignKey
- `Reseña` almacena `juego_titulo` y `usuario_username` como texto plano
- En la Fase B se refactoriza para usar relaciones FK

## 🔧 Comandos Útiles

```bash
# Iniciar servidor
venv/bin/python manage.py runserver

# Crear superusuario
venv/bin/python manage.py createsuperuser

# Crear migraciones
venv/bin/python manage.py makemigrations

# Aplicar migraciones
venv/bin/python manage.py migrate

# Acceder a shell de Django
venv/bin/python manage.py shell

# Recolectar archivos estáticos (producción)
venv/bin/python manage.py collectstatic
```

## 👨‍💻 Desarrollo

Desarrollado con Django 6.0.1:
- Class-based views
- ModelForms
- Template inheritance
- Middleware personalizado
- Admin customization
- Separación de estilos (CSS externo)
