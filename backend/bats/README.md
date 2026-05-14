# Backend BATs

Esta pasta concentra os scripts manuais do backend. Evite criar `.bat` solto na raiz do `backend`; coloque aqui.

## Setup completo por idioma

Use estes quando quiser preparar um idioma inteiro, incluindo migrations e seed:

```bat
backend\bats\idiomas\es.bat
backend\bats\idiomas\it.bat
backend\bats\idiomas\de.bat
```

Cada arquivo roda:

```text
conda activate linguaflow
python manage.py makemigrations
python manage.py migrate
python manage.py seed_languages
python manage.py seed_<idioma>
python manage.py seed_<idioma>_sections --reset
```

## Migrations apenas

Use este quando quiser somente atualizar o banco, sem rodar seeds:

```bat
backend\bats\migrations.bat
```

## Seeds apenas

Use estes quando o banco ja esta migrado e voce quer apenas recriar o conteudo:

```bat
backend\bats\seeds\es.bat
backend\bats\seeds\it.bat
backend\bats\seeds\de.bat
```

## Estrutura

```text
backend\bats\
  migrations.bat
  idiomas\
    es.bat
    it.bat
    de.bat
  seeds\
    es.bat
    it.bat
    de.bat
```
