# Куда пойти — Москва глазами Артёма

Проект сайта о самых интересных местах Москвы.

![](https://i.ibb.co/tLTvzv1/site.png)

## Установка

Python 3 должен быть установлен. Установите зависимости:

```
pip install -r requirements.txt
```

## Переменные окружения

Создайте в каталоге проекта `.env` файл со седующими переменными и замените их значения на свои:

```
SECRET_KEY='YOU_SECRET_KEY'
DEBUG='True'
ALLOWED_HOSTS='*'
STATICFILES_DIRS=''
STATIC_ROOT=''
STATIC_URL='/static/'
MEDIA_ROOT=''
MEDIA_URL='/media/'
DATABASE='db.sqlite3'
DATABASE_ENGINE='django.db.backends.sqlite3'
```

## Локальный запуск

В консоли выполните команду, чтобы создать базу данных:

```
python manage.py migrate
```

Затем создайте суперпользователя командой:

```
python manage.py createsuperuser
```

И запустите сайт командой:

```
python manage.py runserver
```

После запуска перейдите в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы увидеть сайт.
Панель администратора доступна по адресу http://127.0.0.1:8000/admin/.

## Используемые библиотеки

* [Django](https://www.djangoproject.com/) — сервер для разработки, панель администратора, шаблонизация
* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).
Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).