# Generated by Django 4.1.1 on 2023-04-27 05:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexIIdoc',
            fields=[
                ('Doc_ID', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fileIn', models.CharField(blank=True, max_length=200)),
                ('serialNo', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('vilagename', models.CharField(blank=True, max_length=200)),
                ('subdistrict', models.CharField(blank=True, max_length=200)),
                ('district', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, choices=[('maharashtra', 'maharashtra'), ('andhra pradesh', 'andhra pradesh'), ('arunachal pradesh ', 'arunachal pradesh '), ('assam', 'assam'), ('bihar', 'bihar'), ('chhattisgarh', 'chhattisgarh'), ('goa', 'goa'), ('gujarat', 'gujarat'), ('haryana', 'haryana'), ('himachal pradesh', 'himachal pradesh'), ('jammu and kashmir', 'jammu and kashmir'), ('jharkhand', 'jharkhand'), ('karnataka', 'karnataka'), ('kerala', 'kerala'), ('madhya pradesh', 'madhya pradesh'), ('manipur', 'manipur'), ('meghalaya', 'meghalaya'), ('mizoram', 'mizoram'), ('nagaland', 'nagaland'), ('odisha', 'odisha'), ('punjab', 'punjab'), ('rajasthan', 'rajasthan'), ('sikkim', 'sikkim'), ('tamil nadu', 'tamil nadu'), ('telangana', 'telangana'), ('tripura', 'tripura'), ('uttar pradesh', 'uttar pradesh'), ('uttarakhand', 'uttarakhand'), ('west bengal', 'west bengal'), ('andaman and nicobar islands', 'andaman and nicobar islands'), ('chandigarh', 'chandigarh'), ('dadra and nagar haveli', 'dadra and nagar haveli'), ('daman and diu', 'daman and diu'), ('lakshadweep', 'lakshadweep'), ('national capital territory of delhi', 'national capital territory of delhi'), ('puducherry', 'puducherry')], default='maharashtra', max_length=200)),
                ('language', models.CharField(choices=[('English', 'eng')], default=('English', 'eng'), max_length=100)),
            ],
        ),
    ]