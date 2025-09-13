import os
from pathlib import Path
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Cấu hình cơ bản của Django
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-xxxxxxxxxxxx")
DEBUG = True
ALLOWED_HOSTS = ["*"]  # Chỉ dùng cho môi trường dev

# --- CẤU HÌNH API AI ---
# Sử dụng biến môi trường để chuyển đổi giữa các nhà cung cấp AI
# Mặc định là Gemini
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

# Cấu hình cho OpenAI (giữ lại để tham khảo hoặc chuyển đổi sau này)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_TEMPERATURE = 0.7

# Cấu hình cho Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
# Sử dụng gemini-1.5-flash-001 vì đây là phiên bản ổn định
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash-latest")


# Hoặc bạn có thể dùng biến môi trường để linh hoạt hơn:
# GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-001")

# --- DANH SÁCH CÁC ỨNG DỤNG ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "notes",
    "users",
    "mazii_api",
    "openai_api",
    "ai_content",
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- CẤU HÌNH KHÁC ---
ROOT_URLCONF = "smartnote_backend.urls"
WSGI_APPLICATION = "smartnote_backend.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# --- CƠ SỞ DỮ LIỆU ---
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartnote',         # tên database bạn đã tạo trong MySQL
        'USER': 'appuser',           # user MySQL bạn tạo (hoặc root)
        'PASSWORD': 'App123456!',    # mật khẩu user đó
        'HOST': '127.0.0.1',         # localhost
        'PORT': '3306',
    }
}


# --- BẢO MẬT MẬT KHẨU ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 8}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- QUỐC TẾ HÓA ---
LANGUAGE_CODE = "ja-jp"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# --- CẤU HÌNH REST FRAMEWORK ---
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

STATIC_URL = "/static/"