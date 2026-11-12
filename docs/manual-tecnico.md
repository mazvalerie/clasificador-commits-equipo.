# Manual Técnico - Clasificador de Commits

## 1. Arquitectura
El sistema implementa una arquitectura cliente-servidor orientada a microservicios locales:
- **Cliente:** Envía peticiones HTTP POST/GET mediante la interfaz interactiva de FastAPI (Swagger UI) o clientes externos como `curl`.
- **API (FastAPI):** Recibe las solicitudes en el puerto `8000`, procesa el texto usando el motor seleccionado (`eco` por reglas o `ollama` con el modelo local) y gestiona la lógica de negocio.
- **Motores de Inferencia:**
  - *Motor Eco:* Análisis mediante expresiones regulares (sin consumo de memoria).
  - *Motor Ollama:* Ejecución local del modelo a través de la API en el puerto `11434`.
- **Base de Datos (PostgreSQL):** Contenedor Docker (`db-ia`) escuchando en el puerto `5432`, encargado de la persistencia de las inferencias.

## 2. Seguridad
- **Exposición de Puertos:** Solo se exponen los puertos estrictamente necesarios localmente (`8000` para la API y `5432` para PostgreSQL).
- **Privilegios Mínimos en Base de Datos:** La aplicación se conecta utilizando el rol `app_ia`, el cual posee únicamente permisos de `CONNECT`, `USAGE`, `SELECT` e `INSERT` sobre la tabla `inferencias`, bloqueando cualquier intento de actualización o borrado (`UPDATE`, `DELETE`, `DROP`).
- **Manejo de Secretos:** Las credenciales y parámetros sensibles se aíslan en el archivo `.env` (el cual está excluido del control de versiones mediante `.gitignore`), proveyendo una plantilla pública `.env.example` sin datos reales.

