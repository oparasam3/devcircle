# Generated by Django 4.0.6 on 2022-08-15 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_contact_alter_phone_best_selling_alter_phone_latest'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('paid', models.BooleanField()),
                ('amount', models.IntegerField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.phone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
                'db_table': 'cart',
                'managed': True,
            },
        ),
    ]
