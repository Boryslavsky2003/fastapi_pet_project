# fastapi_pet_project

## 🚀 Запуск без коду

1. Скачайте Docker-образ із [релізів](https://github.com/Boryslavsky2003/fastapi_pet_project/releases/tag/v1.0)
2. Завантажте його в Docker:
   ```bash
   docker load -i fastapi_pet_project.tar
3. Запустіть:
   ```bash
   docker run -p 8000:8000 fastapi_pet_project:v1.0

Tree:
```bash
   📦 fastapi_pet_project/
   ├── 📁 app/                         # 📌 Основний застосунок FastAPI
   │   ├── 📄 __init__.py             # 🔧 Ініціалізує пакет
   │   ├── 📄 main.py                 # 🚀 Запускає FastAPI-додаток
   │   ├── 📄 database.py             # 🗄️ Підключення до SQLite через SQLAlchemy
   │
   │   ├── 📁 repository/             # 📚 Логіка роботи з БД
   │   │   ├── 📄 __init__.py
   │   │   └── 📄 task.py             # ➕➖ CRUD-операції для тасок
   │
   │   ├── 📁 routers/                # 🌐 HTTP-маршрути (ендпоінти)
   │   │   ├── 📄 __init__.py
   │   │   └── 📄 task.py             # 🧭 /tasks: GET, POST
   │
   │   └── 📁 schemas/                # 🧱 Pydantic-схеми для валідації
   │       ├── 📄 __init__.py
   │       └── 📄 task.py             # 📋 Моделі: STaskAdd, STask, STaskId
   │
   ├── 📄 run.py                      # 🧪 Альтернативний запуск (не через `main.py`)
   ├── 🐳 Dockerfile                  # 📦 Інструкції для створення Docker-образу
   ├── 📄 requirements.txt            # 📦 Список залежностей Python
   ├── 📄 README.md                   # 📘 Документація проєкту
   ├── 📄 tasks.db                    # 🗃️ SQLite база даних (створюється автоматично)
   └── 🚫 __pycache__/                # 🧹 Кеш байт-коду Python (ігнорується)
