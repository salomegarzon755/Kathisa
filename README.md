# 🎓 Soft Girls — Plataforma de Gestión Académica
## 🤝 Equipo
 -[Salomé Garzón Flórez]
 -[Katherin Daniela Cordoba Chaverra]
 -[Isabela Torres Londoño]
 
**SoftGirls**
 
Plataforma web para la gestión académica de instituciones educativas y organizaciones de formación. Permite administrar cursos, gestionar inscripciones, registrar asistencia y calificaciones, y organizar la información académica según el rol de cada usuario.
 
## 📋 Tabla de contenidos
 
- [Descripción del proyecto](#-descripción-del-proyecto)
- [Objetivo general](#-objetivo-general)
- [Roles de usuario](#-roles-de-usuario)
- [Funcionalidades principales](#-funcionalidades-principales)
- [Tecnologías](#-tecnologías)
- [Modelo de datos](#-modelo-de-datos)
- [Reglas de negocio y validaciones](#-reglas-de-negocio-y-validaciones)
- [Instalación y puesta en marcha](#-instalación-y-puesta-en-marcha)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Equipo](#-equipo)
- [Licencia](#-licencia)
## 📖 Descripción del proyecto
 
El proyecto consiste en desarrollar una plataforma web para la gestión académica de instituciones educativas y organizaciones de formación. Permitirá administrar cursos, gestionar las inscripciones de los estudiantes, registrar la asistencia y las calificaciones, y organizar la información académica.
 
La plataforma cuenta con diferentes roles (organizadores, instructores y estudiantes), cada uno con permisos según sus funciones.
 
## 🎯 Objetivo general
 
Desarrollar una plataforma web para gestionar cursos de formación, facilitando la administración de las inscripciones de los estudiantes, el registro de asistencia, el seguimiento de las calificaciones y la organización de la información académica, de acuerdo con los permisos de cada tipo de usuario.
 
## 👥 Roles de usuario
 
| Rol | Descripción |
|---|---|
| **Administrador (Admin)** | Organiza la información académica, gestiona cursos y grupos, y emite certificados. |
| **Docente (Teacher)** | Dicta los grupos, registra asistencia, crea evaluaciones y califica. |
| **Estudiante (Student)** | Se inscribe en grupos, consulta horarios, entrega trabajos y revisa sus notas. |
 
**Reglas de combinación de roles:**
 
- Un usuario con perfil **Student** no puede ser Admin ni Teacher, y viceversa.
- Un usuario **sí** puede ser Admin y Teacher a la vez.
## ✨ Funcionalidades principales
 
- Gestión de cursos, categorías y grupos.
- Gestión de horarios y sesiones de clase (presencial, virtual o híbrida).
- Inscripción de estudiantes con control de cupos.
- Registro de asistencia por sesión.
- Evaluaciones, calificaciones y entregas de trabajos.
- Emisión de certificados.
- Notificaciones a usuarios.
- Control de acceso según rol.
## 🛠️ Tecnologías
 
> Ajusta esta sección según las herramientas que use el equipo.
 
- **Backend:** Python / Django (el modelo de datos usa `Meta.constraints`, `clean()` y serializers)
- **Base de datos:** _(por definir: PostgreSQL, MySQL, etc.)_
- **Frontend:** _(por definir)_
- **Control de versiones:** Git / GitHub
## 🗄️ Modelo de datos
 
El modelo está compuesto por las siguientes entidades, agrupadas por dominio.
 
### Usuarios y roles
 
| Tabla | Descripción |
|---|---|
| `User` (Django) | Cuenta base: email único, contraseña, nombre, `is_active`. |
| `UserProfile` | Datos personales: tipo y número de documento, fecha de nacimiento, teléfono, género. |
| `Admin`, `Teacher`, `Student` | Perfiles por rol, cada uno vinculado 1 a 1 con `User`. |
| `Gender`, `UserStatus`, `AdminStatus`, `TeacherStatus`, `StudentStatus` | Tablas de catálogo. |
 
### Cursos y grupos
 
| Tabla | Descripción |
|---|---|
| `CourseCategory` | Categorías de cursos. |
| `Course` / `CourseStatus` | Cursos con duración en horas y su estado. |
| `CourseGroup` / `CourseGroupStatus` | Grupos de un curso con docente, fechas y cupo máximo. |
| `Schedule` | Horarios semanales de un grupo. |
| `Modality` | Presencial, virtual o híbrida. |
 
### Inscripciones, sesiones y asistencia
 
| Tabla | Descripción |
|---|---|
| `Enrollment` / `EnrollmentStatus` | Inscripción de un estudiante a un grupo. |
| `ClassSession` / `SessionStatus` | Sesiones de clase concretas, con enlace o aula. |
| `Attendance` / `AttendanceStatus` | Asistencia por sesión e inscripción. |
 
### Evaluación y certificación
 
| Tabla | Descripción |
|---|---|
| `Evaluation` | Evaluaciones de un grupo (examen, taller, proyecto, exposición) con su peso porcentual. |
| `Grade` | Nota (0 a 5) de una inscripción en una evaluación. |
| `AssignmentSubmission` | Entregas de los estudiantes (entregada, tardía, calificada). |
| `Certificate` | Certificado emitido por un administrador para una inscripción. |
 
### Comunicación
 
| Tabla | Descripción |
|---|---|
| `Notification` | Mensajes dirigidos a un usuario, con estado de lectura. |
 
> 💡 Se recomienda añadir aquí el diagrama entidad-relación:
> `![Diagrama ER](docs/diagrama-er.png)`
 
## ✅ Reglas de negocio y validaciones
 
La base de datos solo impone lo declarado en `Meta.constraints`; el resto se valida en `clean()` del modelo, en servicios o en serializers.
 
### A. Restricciones en la base de datos (`CheckConstraint` y `UniqueConstraint`)
 
- Duración mayor a 0; fechas y horas de fin posteriores al inicio.
- Nota entre 0 y 5; pesos entre 0 y 100.
- Día de la semana entre 1 y 7; `max_students` mayor a 0.
- Todos los `UNIQUE` compuestos.
- `departure_time` mayor a `arrival_time` solo cuando ambos tienen valor.
- `AssignmentSubmission`: al menos URL o texto.
- `Notification`: `read_at` coherente con `is_read`.
### B. Usuarios y roles
 
- `Student` es exclusivo respecto a `Admin` y `Teacher`.
- Un usuario puede ser `Admin` y `Teacher` a la vez.
- Convertir `phone` vacío (`""`) en `None` para no violar el `UNIQUE`.
- Si el estado de la cuenta (`UserStatus`) es bloqueada, `is_active` debe ser falso (sincronizar al guardar `UserProfile`).
- Validar el formato de `document` según `document_type`.
### C. Horarios y sesiones
 
- Dos horarios se solapan cuando A empieza antes de que B termine y B empieza antes de que A termine.
- Dentro de un grupo, dos `Schedule` no pueden solaparse.
- Un docente no puede tener dos grupos con `Schedule` solapados (se valida vía `CourseGroup.id_teacher`).
- Un docente no puede tener dos `ClassSession` solapadas el mismo día.
- Un aula (`classroom_location`) no puede tener dos sesiones presenciales solapadas.
- `session_date` debe estar entre `start_date` y `end_date` del grupo.
- Según la modalidad: virtual exige `meet_link`, presencial exige `classroom_location`, híbrida exige ambos.
- El docente de la sesión debe ser el del grupo o un sustituto con habilidad registrada en `TeacherCourse`.
### D. Inscripciones
 
- No inscribir más estudiantes activos que `max_students` (usar `transaction.atomic` con `select_for_update`).
- Un estudiante puede estar en varios grupos, pero sin solapar horarios.
- Solo se inscriben estudiantes activos en grupos cuyo estado admita inscripciones.
### E. Asistencia
 
- El grupo de la inscripción debe ser el mismo que el de la sesión.
- No registrar asistencia a inscripciones retiradas.
- La modalidad de asistencia solo puede ser presencial o virtual, y compatible con la sesión.
- El docente debe ser el del grupo o un sustituto con habilidad registrada.
### F. Evaluaciones, notas y entregas
 
- Los `weight` de las evaluaciones de un grupo deben sumar 100 (se valida al cerrar el grupo).
- En `Grade` y `AssignmentSubmission`, el grupo de la inscripción debe ser el de la evaluación.
- No registrar notas ni entregas a inscripciones retiradas.
- El docente que califica debe ser el del grupo o un sustituto con habilidad registrada.
- El estado `tardia` se calcula comparando `submission_date` con `due_date`; no se asigna a mano.
- Al calificar una entrega, su estado pasa a `calificada`.
## 🚀 Instalación y puesta en marcha
 
> Los comandos son un ejemplo para un proyecto Django. Ajústalos a tu configuración real.
 
```bash
# 1. Clonar el repositorio
git clone https://github.com/<usuario>/<repositorio>.git
cd <repositorio>
 
# 2. Crear y activar el entorno virtual
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
 
# 3. Instalar dependencias
pip install -r requirements.txt
 
# 4. Configurar variables de entorno
cp .env.example .env
 
# 5. Aplicar migraciones
python manage.py migrate
 
# 6. Crear un superusuario
python manage.py createsuperuser
 
# 7. Iniciar el servidor de desarrollo
python manage.py runserver
```
 
La aplicación quedará disponible en `http://127.0.0.1:8000/`.
 
## 📁 Estructura del proyecto
 
> Ejemplo orientativo; reemplázalo por la estructura real.
 
```
.
├── manage.py
├── requirements.txt
├── config/            # Configuración del proyecto
├── users/             # Usuarios, perfiles y roles
├── courses/           # Cursos, grupos y horarios
├── enrollments/       # Inscripciones
├── attendance/        # Sesiones y asistencia
├── evaluations/       # Evaluaciones, notas y entregas
├── certificates/      # Certificados
├── notifications/     # Notificaciones
└── docs/              # Documentación y diagramas
```
 

 
