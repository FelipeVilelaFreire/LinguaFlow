from django.db import migrations


def column_names(schema_editor, table_name):
    with schema_editor.connection.cursor() as cursor:
        return {column.name for column in schema_editor.connection.introspection.get_table_description(cursor, table_name)}


def ensure_completion_goal_column(apps, schema_editor):
    columns = column_names(schema_editor, "content_studydaycompletion")
    if "goal_id" not in columns:
        schema_editor.execute("ALTER TABLE content_studydaycompletion ADD COLUMN goal_id bigint NULL")


class Migration(migrations.Migration):
    dependencies = [
        ("progress", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(ensure_completion_goal_column, migrations.RunPython.noop),
    ]
