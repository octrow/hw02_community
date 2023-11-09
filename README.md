# hw02_community

### Сообщество Яндекс.Практикум.

Что реализовано в сообществе. Создано и зарегистрировано приложение Posts. Подключена база данных. Десять последних записей выводятся на главную страницу. В админ-зоне доступно управление объектами модели Post: 
можно публиковать новые записи или редактировать/удалять существующие. 

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Настройка и запуск

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw02_community.git
```

Переходим в папку с проектом:

```bash
cd hw02_community
```

Устанавливаем виртуальное окружение:

```bash
python3 -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Устанавливаем зависимости:

```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
```
```bash
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

Делаем коллекцию статики (опционально):

```bash
python yatube/manage.py collectstatic
```

Предварительно сняв комментарий с:
```bash
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

И закомментировав: 
```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Добавить в .gitingore файлы:

```bash
.env
.venv
```

Запускаем проект:

```bash
python yatube/manage.py runserver
```

После чего проект будет доступен по адресу http://localhost:8080/

Заходим в http://localhost:8080/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Запускаем тестов:

```bash
pytest
```

Автор: [Daniil Petrov](https://github.com/octrow) :+1:
