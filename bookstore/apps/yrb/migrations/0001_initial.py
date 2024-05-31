# Generated by Django 3.1.8 on 2024-05-30 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YrbBook',
            fields=[
                ('title', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('year', models.SmallIntegerField()),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'yrb_book',
            },
        ),
        migrations.CreateModel(
            name='YrbCategory',
            fields=[
                ('cat', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'yrb_category',
            },
        ),
        migrations.CreateModel(
            name='YrbClub',
            fields=[
                ('club', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('desp', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'yrb_club',
            },
        ),
        migrations.CreateModel(
            name='YrbCustomer',
            fields=[
                ('cid', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'yrb_customer',
            },
        ),
        migrations.CreateModel(
            name='YrbOffer',
            fields=[
                ('year', models.SmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('offerid', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('club', models.ForeignKey(db_column='club', on_delete=django.db.models.deletion.DO_NOTHING, to='yrb.yrbclub')),
                ('title', models.ForeignKey(db_column='title', on_delete=django.db.models.deletion.DO_NOTHING, to='yrb.yrbbook')),
            ],
            options={
                'db_table': 'yrb_offer',
                'unique_together': {('club', 'title', 'year', 'offerid')},
            },
        ),
        migrations.CreateModel(
            name='YrbShipping',
            fields=[
                ('weight', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, unique=True)),
            ],
            options={
                'db_table': 'yrb_shipping',
                'unique_together': {('weight', 'cost')},
            },
        ),
        migrations.AddField(
            model_name='yrbbook',
            name='cat',
            field=models.ForeignKey(db_column='cat', on_delete=django.db.models.deletion.DO_NOTHING, to='yrb.yrbcategory'),
        ),
        migrations.CreateModel(
            name='YrbPurchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.SmallIntegerField()),
                ('club', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=25)),
                ('year', models.SmallIntegerField()),
                ('whenp', models.DateTimeField()),
                ('qnty', models.SmallIntegerField()),
                ('offerid', models.ForeignKey(db_column='offerid', on_delete=django.db.models.deletion.DO_NOTHING, to='yrb.yrboffer')),
            ],
            options={
                'db_table': 'yrb_purchase',
                'unique_together': {('id', 'club', 'title', 'year', 'whenp', 'offerid', 'cid')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='yrbbook',
            unique_together={('title', 'year')},
        ),
        migrations.CreateModel(
            name='YrbMember',
            fields=[
                ('club', models.OneToOneField(db_column='club', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='yrb.yrbclub')),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, to='yrb.yrbcustomer')),
            ],
            options={
                'db_table': 'yrb_member',
                'unique_together': {('club', 'cid')},
            },
        ),
    ]
