# Generated by Django 2.2 on 2019-12-18 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=320)),
                ('shoe_size', models.FloatField(null=True)),
                ('password', models.CharField(max_length=60)),
                ('shipping_address', models.CharField(max_length=255, null=True)),
                ('shipping_city', models.CharField(max_length=255, null=True)),
                ('shipping_zip', models.IntegerField(null=True)),
                ('billing_address', models.CharField(max_length=255, null=True)),
                ('billing_city', models.CharField(max_length=255, null=True)),
                ('billing_zip', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_brand', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
                ('item_primary_color', models.CharField(max_length=255)),
                ('item_secondary_color', models.CharField(max_length=255, null=True)),
                ('item_price', models.FloatField(default='50')),
                ('front_img', models.ImageField(null=True, upload_to='images/')),
                ('back_img', models.ImageField(null=True, upload_to='images/')),
                ('top_img', models.ImageField(null=True, upload_to='images/')),
                ('bottom_img', models.ImageField(null=True, upload_to='images/')),
                ('left_img', models.ImageField(null=True, upload_to='images/')),
                ('right_img', models.ImageField(null=True, upload_to='images/')),
                ('condition', models.CharField(max_length=255)),
                ('item_size', models.FloatField()),
                ('item_sex', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('availability', models.BooleanField()),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bought', to='login_register_app.User')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold', to='login_register_app.User')),
            ],
        ),
    ]
