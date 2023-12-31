# Generated by Django 4.2.5 on 2023-10-03 18:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter date of birth of the Author', null=True, verbose_name='Birthday')),
                ('date_of_death', models.DateField(blank=True, help_text='Enter date of death of the Author', null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['-date_of_birth'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ISBN', models.CharField(help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('summary', models.TextField(help_text='Write a brief description of the book', max_length=1000)),
                ('author', models.ForeignKey(default='Unknown', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre(e.g. Sci-fi)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('bid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book in library', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('A', 'Available'), ('B', 'Borrowed'), ('D', 'Delayed'), ('R', 'Reserved'), ('M', 'Maintenance')], default='A', help_text='Set book availability', max_length=10)),
                ('imprint', models.CharField(max_length=200)),
                ('due_date', models.DateField(blank=True, help_text='date to book be returned', null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.genre'),
        ),
    ]
