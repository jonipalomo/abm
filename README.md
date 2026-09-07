# ABM de Alumnos (Django)

Proyecto educativo con:

- **Landing page** (`/`) con presentación del sistema.
- **ABM de Alumnos** (`/alumnos/`): Alta, Baja y Modificación de registros.
- Panel de administración de Django (`/admin/`).

Pensado para que trabajen **dos desarrolladores en paralelo**: uno de **backend** y uno de
**frontend**, sobre el mismo repositorio. Ver la sección [Roles](#roles) más abajo.

No se usa entorno virtual (`venv`) para simplificar el setup: las dependencias se instalan
directo con `pip` en el Python del sistema.

**Última actualización a cargo de:** _(completar)_

---

## Requisitos previos

- **Python 3.10+** (se probó con 3.12) — https://www.python.org/downloads/
- **pip** (viene incluido con Python)
- **Git** — https://git-scm.com/downloads

Verificá las versiones instaladas:

```bash
python --version
pip --version
git --version
```

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPO>
   cd abm-alumnos
   ```

2. Instalar las dependencias (sin virtualenv, directo en el Python del sistema):

   ```bash
   pip install -r requirements.txt
   ```

3. Aplicar las migraciones para crear la base de datos (SQLite, ya viene configurada):

   ```bash
   python manage.py migrate
   ```

4. Crear un usuario administrador (para entrar a `/admin/`):

   ```bash
   python manage.py createsuperuser
   ```

5. Levantar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

6. Abrir en el navegador:

   - Landing page: http://127.0.0.1:8000/
   - Listado de alumnos: http://127.0.0.1:8000/alumnos/
   - Admin: http://127.0.0.1:8000/admin/

## Comandos esenciales

| Comando | Para qué sirve |
|---|---|
| `pip install -r requirements.txt` | Instalar/actualizar dependencias del proyecto |
| `python manage.py runserver` | Levantar el servidor de desarrollo |
| `python manage.py makemigrations` | Generar migraciones a partir de cambios en `models.py` |
| `python manage.py migrate` | Aplicar las migraciones a la base de datos |
| `python manage.py createsuperuser` | Crear un usuario para el panel de administración |
| `python manage.py shell` | Abrir una consola interactiva con el proyecto cargado |
| `python manage.py test` | Correr los tests del proyecto |
| `python manage.py startapp <nombre>` | Crear una nueva app de Django |

Flujo típico después de modificar `models.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Estructura del proyecto

```
abm-alumnos/
├── manage.py
├── requirements.txt
├── config/              # Configuración del proyecto (settings, urls raíz)
├── alumnos/             # App del ABM: modelos, vistas, urls, admin
│   └── templates/alumnos/
├── templates/           # Templates globales (base.html, landing page)
│   ├── base.html
│   └── home.html
└── static/css/          # CSS del sitio
    └── style.css
```

## Roles

### Backend (Alta/Baja/Modificación, datos, lógica)

Archivos principales: `alumnos/models.py`, `alumnos/views.py`, `alumnos/forms.py`,
`alumnos/urls.py`, `alumnos/admin.py`, `config/settings.py`.

Responsabilidades:

- Definir y evolucionar el modelo `Alumno` (campos, validaciones, migraciones).
- Escribir la lógica de las vistas (filtros, búsquedas, paginación, permisos).
- Configurar el panel de `/admin/`.
- Escribir tests.

### Frontend (landing page, templates, estilos, UX)

Archivos principales: `templates/base.html`, `templates/home.html`,
`alumnos/templates/alumnos/*.html`, `static/css/style.css`.

Responsabilidades:

- Diseñar y mejorar la landing page.
- Mejorar los templates del ABM (listado, formulario, confirmación de borrado).
- Estilos (CSS), responsividad, mensajes de éxito/error, interactividad (JS opcional).
- Cuidar la experiencia de usuario en general.

**Punto de contacto entre ambos roles:** los nombres de contexto que las vistas le pasan a
los templates (`alumnos`, `form`, `object`, `messages`, etc.) y las `url`/`name` definidas en
`alumnos/urls.py`. Si backend cambia algo ahí, avisar al compañero de frontend (y viceversa).

## Ejercicios para practicar

### Backend

1. Agregar un campo nuevo al modelo `Alumno` (por ejemplo `telefono`) y generar/aplicar la
   migración correspondiente.
2. Agregar validación: que el DNI solo acepte números y tenga entre 7 y 8 dígitos.
3. Agregar un filtro por `curso` en el listado (además de la búsqueda por nombre/apellido que
   ya existe).
4. Escribir tests (`alumnos/tests.py`) para el modelo y para las vistas de alta y baja.
5. Restringir el acceso al ABM solo a usuarios logueados (`LoginRequiredMixin`).
6. (Bonus) Agregar una vista que devuelva el listado de alumnos en JSON.

### Frontend

1. Mejorar la landing page: agregar una sección "sobre el instituto" y un footer con enlaces.
2. Mejorar la tabla de alumnos: resaltar la fila al pasar el mouse, ordenar por columna.
3. Agregar confirmación antes de eliminar usando un modal (JS), en vez de una página aparte.
4. Mostrar los errores de validación del formulario con mejor estilo visual.
5. Hacer el sitio responsive (que se vea bien en celular).
6. (Bonus) Agregar un contador de alumnos activos/inactivos en la landing page usando datos
   reales del backend.

### En conjunto

1. Ponerse de acuerdo en el nombre de las variables de contexto antes de que backend cambie
   una vista que frontend ya está usando en un template.
2. Trabajar en ramas (`git checkout -b nombre-rama`) y abrir Pull Requests para revisar el
   código del otro antes de mergear a `main`.
3. Resolver al menos un conflicto de merge entre los dos.
