import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_env_file(BASE_DIR / ".env")


def resolve_env_path(name: str, default: str = "") -> str:
    value = os.environ.get(name, default).strip()
    if not value:
        return ""
    path = Path(value)
    if path.is_absolute():
        return str(path)
    return str(BASE_DIR / path)

SECRET_KEY = "dev-only-linguaflow-secret"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "apps.accounts.apps.AccountsConfig",
    "apps.learning.apps.LearningConfig",
    "apps.goals.apps.GoalsConfig",
    "apps.progress.apps.ProgressConfig",
    "apps.adventure.apps.AdventureConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "linguaflow.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "linguaflow.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


def env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


ADVENTURE_TTS_ENABLED = env_bool("ADVENTURE_TTS_ENABLED", False)
ADVENTURE_TTS_PROVIDER = os.environ.get("ADVENTURE_TTS_PROVIDER", "browser").strip().lower()
ADVENTURE_TTS_PIPER_EXE = resolve_env_path("ADVENTURE_TTS_PIPER_EXE", "piper")
ADVENTURE_TTS_PIPER_DEFAULT_MODEL = resolve_env_path("ADVENTURE_TTS_PIPER_DEFAULT_MODEL", "")
# Optional per-character Piper model env vars:
# ADVENTURE_TTS_PIPER_MODEL_DON_MIGUEL, ADVENTURE_TTS_PIPER_MODEL_MIGUEL,
# ADVENTURE_TTS_PIPER_MODEL_ROSA, ADVENTURE_TTS_PIPER_MODEL_CARMEN,
# ADVENTURE_TTS_PIPER_MODEL_SOFIA, ADVENTURE_TTS_PIPER_MODEL_MARIA,
# ADVENTURE_TTS_PIPER_MODEL_ALCALDE, ADVENTURE_TTS_PIPER_MODEL_VIGILANTE,
# ADVENTURE_TTS_PIPER_MODEL_INSPECTOR.

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5178",
    "http://127.0.0.1:5178",
]
CORS_ALLOW_ALL_ORIGINS = DEBUG

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}
