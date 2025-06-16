# fastapi_pet_project

## 🚀 Запуск без коду

1. Скачайте Docker-образ із [релізів](https://github.com/Boryslavsky2003/fastapi_pet_project/releases/tag/v1.0)
2. Завантажте його в Docker:
   ```bash
   docker load -i fastapi_pet_project.tar
3. Запустіть:
   ```bash
   docker run -p 8000:8000 fastapi_pet_project:v1.0

Tree -> app/
├── database.py      # ⚙️ Налаштування БД (SQLAlchemy + асинхронний движок)
├── main.py          # 🚀 Точка входу FastAPI: конфігурація, lifespan, підключення роутерів
├── repository/
│   └── task.py      # 📦 Репозиторій: ізоляція доступу до бази даних
└── routers/
    └── task.py      # 🌐 Роутери: HTTP-ендпоінти (POST /tasks, GET /tasks)
└── schemas/
    └── task.py      # 📋 Pydantic-схеми для валідації даних
run.py               # 🧰 Альтернативний скрипт запуску через uvicorn.run()
Dockerfile          # 🐳 Інструкції для створення Docker-образу
requirements.txt    # 📦 Перелік залежностей проєкту
tasks.db            # 🗃️ SQLite file для зберігання даних
README.md           # 📝 Цей файл — документація проєкту
