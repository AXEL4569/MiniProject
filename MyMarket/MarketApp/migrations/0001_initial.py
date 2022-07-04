# Generated by Django 3.2.13 on 2022-06-26 14:34

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
            name='Gigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('category', models.CharField(choices=[('PC', 'Pest Control'), ('HC', 'Home Cleaners'), ('GL', 'Gardening and Landscaping'), ('MA', 'Music and Audio'), ('LS', 'LockSmith'), ('EL', 'Electricians'), ('PL', 'Plumbing'), ('MO', 'Moving'), ('CO', 'Contractors'), ('OT', 'Others')], max_length=2)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='gigPics/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('phoneNumber', models.TextField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Average'), ('4', 'Good'), ('5', 'Excellent')], max_length=1)),
                ('content', models.TextField()),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketApp.gigs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
