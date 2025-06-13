# YaMDb

**YaMDb** is a backend service for collecting reviews on works of art. Users can leave reviews, rate items, and discuss opinions with others.

## Description

The YaMDb project collects user reviews on works from various categories: movies, books, music, and more. The works themselves are not stored. Users can leave reviews, comments, and assign ratings from 1 to 10. Based on the ratings, each work receives an overall score.

## Key Features

- User registration and authentication via email and JWT tokens.
- Access levels:
  - Anonymous users — read-only access.
  - Authenticated users — create/edit their own reviews and comments.
  - Moderator — manage others' reviews and comments.
  - Administrator — full access to all data and users.
- API endpoints:
  - **Titles** — works of art
  - **Categories** — categories of works
  - **Genres** — genres
  - **Reviews** — user reviews for works
  - **Comments** — comments on reviews
  - **Users** — user management
  - **Auth** — registration and token issuance

## Technologies

- Python 3.10+
- Django 3.2.25
- Django REST Framework
- JWT (djangorestframework-simplejwt)
- SQLite / PostgreSQL
- CSV data import via management command

## Installation and Launch

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/api_yamdb.git
   cd api_yamdb
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. (Optional) Load test data:
   ```bash
   python manage.py import_csv
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. API documentation will be available at:
   ```
   http://127.0.0.1:8000/redoc/
   ```

## Project Team

- **Timofey** — authentication, registration, token system.
https://github.com/pahomdze

- **Nikita** — models and API for titles, categories, genres, data import.
https://github.com/NikitaUkhalov

- **Vsevolod** — team lead, developed reviews, comments, and rating system.
https://github.com/Vsevolod-Dubin/

<details>
<summary>🇷🇺 Нажмите, чтобы раскрыть описание на русском</summary>

# YaMDb

**YaMDb** — это бэкенд-сервис для сбора отзывов на произведения искусства. Здесь можно оставлять рецензии, ставить оценки и обсуждать мнения других пользователей.

## Описание

Проект YaMDb собирает отзывы пользователей на произведения из различных категорий: фильмы, книги, музыка и др. Сами произведения не хранятся. Пользователи могут оставлять отзывы, комментарии и выставлять оценки от 1 до 10. На основе оценок формируется рейтинг произведения.

## Основной функционал

- Регистрация пользователей и аутентификация через e-mail и JWT-токены.
- Разделение прав доступа:
  - Анонимный пользователь — только чтение.
  - Аутентифицированный пользователь — создание/редактирование своих отзывов и комментариев.
  - Модератор — управление чужими отзывами и комментариями.
  - Администратор — полный доступ к данным и пользователям.
- Работа с ресурсами API:
  - **Titles** — произведения
  - **Categories** — категории произведений
  - **Genres** — жанры
  - **Reviews** — отзывы на произведения
  - **Comments** — комментарии к отзывам
  - **Users** — управление пользователями
  - **Auth** — регистрация и выдача токенов

## Технологии

- Python 3.10+
- Django 3.2.25
- Django REST Framework
- JWT (djangorestframework-simplejwt)
- SQLite / PostgreSQL
- CSV-загрузка данных через management-команду

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/api_yamdb.git
   cd api_yamdb
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции:
   ```bash
   python manage.py migrate
   ```

5. (По желанию) Загрузите тестовые данные:
   ```bash
   python manage.py import_csv
   ```

6. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

7. Документация API будет доступна по адресу:
   ```
   http://127.0.0.1:8000/redoc/
   ```

## Команда проекта

- **Тимофей** — разработка системы аутентификации, регистрации, токенов.
https://github.com/pahomdze

- **Никита** — модели и API для произведений, категорий, жанров, импорт данных.
https://github.com/NikitaUkhalov

- **Всеволод** — тимлид, разработка отзывов, комментариев и рейтингов.
https://github.com/Vsevolod-Dubin/

</details>