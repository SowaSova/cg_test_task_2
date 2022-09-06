### cg_test_task_2

# Выполнены пункты: 3, 4, 5, 6, 7, 8

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SowaSova/cg_test_task_2.git
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
. venv/bin/activate
```

Обновить pip
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Перейти в каталог
```
cd cg_test_task/
```
Создать базу данных и выполнить миграции:
```
python3 manage.py migrate
```

Импортировать данные:
```
python3 manage.py insert_data
```

Запустить проект:
```
python3 manage.py runserver
```

Так же функционал API проекта доступен по ссылке
http://127.0.0.1:8000/swagger/
