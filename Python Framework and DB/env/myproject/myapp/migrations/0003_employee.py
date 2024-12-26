# Generated by Django 5.1.4 on 2024-12-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_product_name_productmst_pname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pin', models.IntegerField(max_length=10)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Product Manager', 'Product Manager')], max_length=40)),
            ],
        ),
    ]
