# 💼 TestStep

> Навчальна платформа для перевірки знань студентів

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)]()

## 📋 Опис

Данний проект був створений для контролю знань студентів і він слугуе зручним інструментом для перевірки знань студентів надавая змогу вчителям швидко та зручно створювати тести з різними питаннями і назначати тест студентим в группі

### ✨ Основні можливості

- 🔥 **1** - Створення та редагування тестів
- ⚡ **2** - Групи для учнів і вчителів  
- 🎯 **3** - Створення різних типів питань для тестів а такой різні типи відповідей
- 🛡️ **4** - В учнів є можливість змінювати пароль отримуючи лист на email учня 

---

## 🛠️ Стек проекту

### Frontend
- **HTML** - мова для створення розмітки яка буде відображена у браузері
- **CSS** - мова я слугуе для закріплення різних стилів за кожним елементом в HTML
- **JavaScript** - мова програмування яка надае можливість динамічно змінювати елменти в HTML

### Backend
- **Python** `3.11.x - 3.13.x` - мова програмування
- **Django** `5.0.4` -  фреймворк для Python який надає швидко та зручно розробляти проекти
- **Postgresql** `17.x` - PostgreSql база данний 

---

## 📦 Залежності

### Основні залежності (dependencies)

```json
 {
  "web_framework": {
    "Django": "5.0.7",
    "asgiref": "3.8.1",
    "gunicorn": "23.0.0"
  },
  "database": {
    "psycopg": "3.2.4", 
    "psycopg-binary": "3.2.4",
    "dj-database-url": "2.3.0",
    "sqlparse": "0.5.1"
  },
  "django_extensions": {
    "django-appconf": "1.0.6",
    "django-debug-toolbar": "5.0.1", 
    "django-imagekit": "5.0.0",
    "django-ratelimit": "4.1.0",
    "django-storages": "1.14.4",
    "django-unfold": "0.59.0",
    "django_csp": "3.8"
  },
  "aws_integration": {
    "boto3": "1.35.90",
    "botocore": "1.35.90",
    "s3transfer": "0.10.4"
  },
  "data_processing": {
    "pandas": "2.3.0",
    "numpy": "2.3.0",
    "openpyxl": "3.1.5",
    "xlrd": "2.0.1",
    "et_xmlfile": "2.0.0"
  },
  "media_processing": {
    "pillow": "11.0.0",
    "pilkit": "3.0",
    "audioread": "3.0.1",
    "pydub": "0.25.1",
    "ffmpeg-python": "0.2.0"
  },
  "http_requests": {
    "requests": "2.32.3",
    "httpx": "0.27.0",
    "httpcore": "1.0.6",
    "h11": "0.14.0",
    "urllib3": "2.2.3"
  },
  "utilities": {
    "python-decouple": "3.8",
    "python-dotenv": "1.0.1",
    "python-dateutil": "2.9.0.post0",
    "python-magic": "0.4.27",
    "pytz": "2024.2",
    "tzdata": "2024.1"
  },
  "testing_and_development": {
    "factory_boy": "3.3.3",
    "Faker": "36.1.0"
  },
  "monitoring_and_logging": {
    "sentry-sdk": "2.30.0", 
    "logtail-python": "0.3.3"
  },
  "static_files": {
    "whitenoise": "6.8.2"
  },
  "template_engine": {
    "Jinja2": "3.1.3",
    "MarkupSafe": "2.1.5"
  },
  "system_dependencies": {
    "anyio": "4.6.2.post1",
    "certifi": "2024.8.30",
    "charset-normalizer": "3.4.0",
    "idna": "3.10",
    "jmespath": "1.0.1",
    "lxml": "5.4.0",
    "msgpack": "1.1.0",
    "packaging": "24.2",
    "setuptools": "75.3.0",
    "six": "1.17.0",
    "sniffio": "1.3.1",
    "typing_extensions": "4.12.2",
    "future": "1.0.0"
  }
}

```


### Системні вимоги

- **Python**: версія 3.11 або вище
- **pip**: версія 21.x або вище  
- **PostgreSQL**: версія 16.x або вище
- **FFmpeg**: для обробки аудио/видео файлів

---

## ⚙️ Налаштування та запуск

### ❗❗ ВАЖЛИВО ❗❗
>Для роботи проекту необхідно створити файл **.env** та додати такі необхідні данні

### 1️⃣ SMTP (для відправки повідомлень на email)

> Вам необхідно створити аккаунт google и в налаштуваннях додати двухфакторну аутентифікацию після чого перейти в Паролі додатків і додати новий додаток після чого скопіювати та зберегти пароль ствоненного додатку

> [Довідка](https://support.google.com/a/answer/176600?hl=uk)

```env
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT= <465 для HTTP | 587 для HTTPS>
    EMAIL_HOST_USER= <email адресса вашого аккаунту>
    EMAIL_HOST_PASSWORD= <Пароль додатку>
    EMAIL_USE_TLS= <True для HTTPS| False для HTTP>
```

### 2️⃣ Django Secret key необхідний для доступу к проекту
>[Згенерувати ключ можна тут](https://djecrety.ir/)

```env
    DJANGO_SECRET_KEY = orz(0trfms-x^*c4+zjw(s-%rod^*&k6^5aqy@ysmhy8453fv8
```

### 3️⃣ Amazon s3
## 🏁 Крок 1: Створення AWS акаунта

### 1.1 Реєстрація

1. Перейдіть на [aws.amazon.com](https://aws.amazon.com)
2. Натисніть **"Create an AWS Account"**
3. Заповніть реєстраційну форму:
   - Email адреса
   - Пароль
   - Назва акаунта AWS
4. Підтвердьте email

### 1.2 Вибір плану підтримки

1. Виберіть **"Basic support - Free"** для початку
2. Завершіть реєстрацію

> 💡 **Важливо**: Для нових акаунтів AWS надає Free Tier на 12 місяців!

---

## 🪣 Крок 2: Створення S3 Bucket

### 2.1 Перехід до S3 консолі

1. Увійдіть у [AWS Management Console](https://console.aws.amazon.com)
2. У пошуковому рядку введіть **"S3"**
3. Виберіть **"S3"** з результатів пошуку

### 2.2 Створення нового bucket

1. Натисніть **"Create bucket"**
2. Заповніть основні налаштування:
   - **Bucket name**: `your-project-media-files` (має бути унікальним глобально)
   - **AWS Region**: виберіть найближчий регіон (наприклад, `us-east-1`)

### 2.3 Налаштування доступу

1. **Object Ownership**: виберіть **"ACLs enabled"**
2. **Block Public Access settings**: 
   - Зніміть позначку з **"Block all public access"**
   - Поставте позначку у підтвердженні
3. **Bucket Versioning**: можна залишити **"Disable"**
4. **Default encryption**: виберіть **"Amazon S3 managed keys (SSE-S3)"**

### 2.4 Завершення створення

1. Натисніть **"Create bucket"**
2. Bucket буде створено і він з'явиться у списку

---

## 👤 Крок 3: Створення IAM користувача

### 3.1 Перехід до IAM консолі

1. У AWS Console знайдіть **"IAM"** у пошуковому рядку
2. Виберіть **"IAM"**
3. У лівому меню натисніть **"Users"**

### 3.2 Створення нового користувача

1. Натисніть **"Create user"**
2. **User name**: введіть ім'я, наприклад `s3-django-user`
3. **Access type**: виберіть **"Programmatic access"**
4. Натисніть **"Next"**

### 3.3 Налаштування прав доступу

1. **Set permissions**: виберіть **"Attach policies directly"**
2. У пошуку знайдіть і виберіть **"AmazonS3FullAccess"**
3. Натисніть **"Next"**
4. Додайте теги (опціонально)
5. Натисніть **"Create user"**

### 3.4 Збереження ключів доступу

1. Після створення користувача ви побачите:
   - **Access key ID**: `AKIA...` (20 символів)
   - **Secret access key**: `...` (40 символів)
2. **Скопіюйте та збережіть обидва ключі** - секретний ключ більше не буде показано!
3. Можете завантажити .csv файл із ключами

---

## 🔧 Крок 4: Налаштування CORS та Bucket Policy

### 4.1 Налаштування CORS

1. Поверніться до S3 консолі
2. Виберіть ваш bucket
3. Перейдіть у вкладку **"Permissions"**
4. Знайдіть **"Cross-origin resource sharing (CORS)"**
5. Натисніть **"Edit"** і вставте:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```

### 4.2 Налаштування Bucket Policy
У розділі Persmission нашого S3 вам потрібно знайти Bucket policy та натиснути Edit, після чого додати такий код та сберегти

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::teststepbucket/*"
        }
    ]
}
```

### 5.0 Встановлюемо параметри в **.env**
```env
    AWS_ACCESS_KEY_ID=<id вашого bucket>
    AWS_SECRET_ACCESS_KEY=<access key який був отриманний при створенні bucket>
    AWS_STORAGE_BUCKET_NAME=<Назва вашого bucket>
    AWS_S3_REGION_NAME=eu-north-1
```

### 5️⃣ Додавання Sentry(для поніторингу помилок)
1. Створюємо новий аккаунт в [Sentry](https://sentry.io/)
2. Додаемо застосунок та обираемо Django
3. Переходьте в Settings на головній та в пошуку шукаємо Client Keys(DSN)
4. Копіюйте ваш DSN після чого переходьте у .env файл який ви створювали та додайте в нього ваш
```env
    SENTRY_DSN="<Ваш DSN>"
```

### 6️⃣ Запуск проекту
для початку нам потрібно стровити venv(Віртуальне оточення) для нашого проекту щоб не бути залежним від глобального інтерпретатора Python, зробити це можна дуже просто.
1. Клонуйте проект якщо ще цього не зробили(Вам також будет потрібно встановити [Github cli](https://git-scm.com/downloads))
```bash
    git clone https://github.com/SashaAskub2003/Diploma.git
```
2. Перейдіть в папрку проекту після успішного клонування
```bash
    cd Diploma
```
3. Створіть Віртуальне оточення за допомогою комманди
```bash
    python -m venv <Назва оточення>
```
4. Після чого вам потрібно буде переходити в нього кожен раз для правильної взаемодії с проектом
>Активація віртуального оточення
```bash
    <Назва оточення>/Scripts/activate
```
> Якщо необхідно вийти з нього
```bash
    deactivate
```
5. Встановлюємо залежності проекту
```bash
    pip install -r requirements.txt
```
6. Очікуємо завершення встановлення після чого переходимо за таким шляхом
```
    main/
    ├── settings.py 
```
7. Перейдіть на 115 строку коду в settings.py
> в данному відрізку буде такий код
```bash
    DATABASES = {
        "default": dj_database_url.config(
            default="postgres://test:root@localhost:5432/Tests", conn_max_age=600
        )
    }
```
8. Завантажте одну с останніх версій PostgreSql після чого відкрийте pgadmin4(застосунок який був встановлений разом з службами Postgresql):
   8.1. Ствоюйте користувача в Login/Group Roles
       > Установіть свій пароль який буде використовуватися пізніше а також в Previleges
   8.2. Створіть нову Databases
       > в owner оберіть створенного вами користувача

9. Тепер необхідно змінити url вказаний в DATABASES в settings.py який ви можете редагувати
```bash
    default="postgres://<Ім'я створенного користувача>:<Пароль користувача>@localhost:5432/<Назва свореної бази данних>", conn_max_age=600
```

10. Запуск проекту
```bash
    python manage.py runserver
```

## 🔧 Доступные команды

| Команда | Опис |
|---------|----------|
| `python manage.py runserver` | Запуск сервера |
| `python manage.py createsuperuser` | Створення адміна |
| `python manage.py tests` | Запуск тестів проекту |

---
