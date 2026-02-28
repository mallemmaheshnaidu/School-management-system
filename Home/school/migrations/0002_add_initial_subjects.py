from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('school', 'Subject')
    names = ['Python', 'Maths', 'Science', 'Social', 'Economy', 'Polity']
    for name in names:
        Subject.objects.get_or_create(name=name)


def remove_subjects(apps, schema_editor):
    Subject = apps.get_model('school', 'Subject')
    names = ['Python', 'Maths', 'Science', 'Social', 'Economy', 'Polity']
    Subject.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects, remove_subjects),
    ]
