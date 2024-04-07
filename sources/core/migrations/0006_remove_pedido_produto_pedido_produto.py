# Generated by Django 4.2.11 on 2024-04-07 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_pedido_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='produto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.produto'),
        ),
    ]
