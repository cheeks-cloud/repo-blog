# Generated by Django 4.0.5 on 2022-06-13 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Not Good', 'Not Good')], max_length=30)),
                ('usability', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Not Good', 'Not Good')], max_length=30)),
                ('content', models.TextField()),
                ('project_on_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.projects')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
