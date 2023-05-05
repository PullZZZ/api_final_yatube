## API для YaTube
### Описание
 Проект представляет собой сервис, предоставляющий доступ к YaTube через REST API.
С его помощью можно:
- Создавать, просматривать, редактировать и удалять посты
- Создавать, просматривать, редактировать и удалять комментарии к постам
- Просматривать группы
- Подписываться на авторов
### Локальная установка
Для установки нужно:
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/PullZZZ/api_final_yatube.git

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Для авторизации сервис использует JWT-токен, который, после запуска, можно получить выполнив POST запрос по адресу:
```
/api/v1/jwt/create/
```
передав в body данные пользователя
```
{
"username": "string",
"password": "string"
}
```

## Примеры работы с API
- Получение списка постов:
```
GET /api/v1/posts/
```
Также доступна пагинация:
```
GET /api/v1/posts/?limit=5&offset=0
```
- Создание поста
```
POST /api/v1/posts/
{
"text": "string",
"image": "string",
"group": 0
}
```
- Удаления поста:
```
DEL /api/v1/posts/{id}/
```
- Добавление комментария
```
POST /api/v1/posts/{post_id}/comments/
{
"text": "string"
}
```
## Документация
Полный список запросов доступен в файле [redoc.yaml](https://github.com/PullZZZ/api_final_yatube/blob/master/yatube_api/static/redoc.yaml).
Или, после запуска, по адресу: /redoc/
