# Generated by Django 2.2 on 2020-03-28 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=255)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Compra')),
            ],
        ),
    ]