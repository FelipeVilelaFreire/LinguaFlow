from django.db import migrations


def column_names(schema_editor, table_name):
    with schema_editor.connection.cursor() as cursor:
        return {column.name for column in schema_editor.connection.introspection.get_table_description(cursor, table_name)}


def ensure_goal_columns(apps, schema_editor):
    columns = column_names(schema_editor, "content_goal")
    if "study_weekdays" not in columns:
        schema_editor.execute("ALTER TABLE content_goal ADD COLUMN study_weekdays text NOT NULL DEFAULT '[]'")
    if "session_minutes" not in columns:
        schema_editor.execute("ALTER TABLE content_goal ADD COLUMN session_minutes integer NOT NULL DEFAULT 30")


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(ensure_goal_columns, migrations.RunPython.noop),
    ]
