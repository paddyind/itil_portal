from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('knowledge_base', 'Category')
    categories = [
        'Cloud Infrastructure',
        'On-Prem Infrastructure',
        'Overall Infrastructure and Network Layout',
        'Best Practices',
        'How To Section',
    ]
    for category_name in categories:
        Category.objects.create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
