# TaskOps
**Cloud Task Manager — DevOps Project**

Aplicación web de gestión de tareas desplegada en la nube con infraestructura DevOps moderna.

## Demo en vivo
http://18.226.60.224:5000

## Descripción
TaskOps es una aplicación web desarrollada con Flask que permite a los usuarios gestionar sus tareas diarias. Incluye autenticación de usuarios, prioridades y despliegue automatizado en la nube.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python + Flask** | Backend y servidor web |
| **PostgreSQL** | Base de datos |
| **Docker + Docker Compose** | Contenedores |
| **GitHub Actions** | Pipeline CI/CD |
| **AWS EC2** | Infraestructura cloud |

## Funcionalidades
- Registro e inicio de sesión de usuarios
- Crear, editar, eliminar y completar tareas
- Prioridades: Alta, Media, Baja
- Cada usuario ve solo sus propias tareas
- Interfaz dark mode moderna

## Arquitectura

```
Usuario
   │
AWS EC2 (18.226.60.224)
   │
Docker Compose
   ├── taskops-app (Flask:5000)
   └── taskops-db  (PostgreSQL:5432)
```

## Pipeline CI/CD
git push → GitHub Actions → Docker Build → Deploy EC2

Cada vez que se hace push a `main`:
1. GitHub Actions se activa automáticamente
2. Construye la imagen Docker
3. Se conecta a EC2 por SSH
4. Reconstruye y reinicia los contenedores

## Correr localmente
```bash
git clone https://github.com/Samaa290/TaskOps.git
cd TaskOps
docker compose up --build
```
Abrir: http://localhost:5000

## Estructura del proyecto

```
TaskOps/
├── app/
│   ├── app.py              # Lógica principal Flask
│   ├── Dockerfile          # Imagen Docker
│   ├── requirements.txt    # Dependencias Python
│   ├── templates/          # HTML
│   └── static/             # CSS
├── docker-compose.yml      # Orquestación de contenedores
├── .github/
│   └── workflows/
│       └── deploy.yml      # Pipeline CI/CD
└── README.md
```

## Desarrollado por
Samaya Baján — Estudiante de Ingeniería en Sistemas UMG 2026