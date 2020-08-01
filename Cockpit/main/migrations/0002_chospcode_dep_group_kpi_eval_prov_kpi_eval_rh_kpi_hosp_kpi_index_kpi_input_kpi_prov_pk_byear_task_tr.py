# Generated by Django 3.0.8 on 2020-07-29 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chospcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospcode', models.CharField(max_length=5)),
                ('hosname', models.CharField(max_length=255)),
                ('mu', models.CharField(max_length=2)),
                ('subdistcode', models.CharField(max_length=2)),
                ('ampcode', models.CharField(max_length=2)),
                ('provcode', models.CharField(max_length=2)),
                ('cupcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('DEPTID', models.IntegerField(primary_key=True, serialize=False)),
                ('DEPTNAME', models.CharField(max_length=150)),
                ('DepJob', models.CharField(max_length=3)),
                ('DEPTNAMEnew', models.CharField(max_length=150)),
                ('fstaus', models.CharField(max_length=1)),
                ('fstatustime', models.CharField(max_length=1)),
                ('DepJob_old', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.IntegerField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_eval_prov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi_year', models.DateField(blank=True, null=True)),
                ('hospcode', models.CharField(max_length=5)),
                ('kpi_id', models.CharField(max_length=5)),
                ('ex', models.CharField(max_length=55)),
                ('kpi_eval', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_eval_rh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi_year', models.DateField(blank=True, null=True)),
                ('kpi_id', models.CharField(max_length=5)),
                ('ex', models.CharField(max_length=55)),
                ('kpi_eval', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_hosp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospcode', models.CharField(max_length=5)),
                ('kpi_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi', models.CharField(max_length=5)),
                ('kpi_name', models.TextField()),
                ('ex', models.CharField(max_length=15)),
                ('goal', models.CharField(max_length=15)),
                ('cri_type', models.CharField(max_length=55)),
                ('hdc', models.CharField(max_length=15)),
                ('respon', models.CharField(max_length=255)),
                ('etc', models.TextField()),
                ('kpi_year', models.DateField(blank=True, null=True)),
                ('success_type', models.CharField(max_length=1)),
                ('main_kpi_id', models.CharField(max_length=15)),
                ('unit', models.CharField(max_length=100)),
                ('static_target', models.CharField(max_length=1)),
                ('kpi_formular', models.CharField(max_length=255)),
                ('kpi_formular_script', models.TextField()),
                ('a', models.TextField()),
                ('b', models.TextField()),
                ('c', models.TextField()),
                ('d', models.TextField()),
                ('e', models.TextField()),
                ('f', models.TextField()),
                ('pa', models.CharField(max_length=1)),
                ('h_kpi', models.CharField(max_length=1)),
                ('active', models.CharField(max_length=1)),
                ('note', models.TextField()),
                ('target', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pk_byear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearprocess', models.DateField(choices=[('2020', '2563')], default='2020', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Trole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=155)),
                ('type_group', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpi_id', models.TextField()),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_hospcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chospcode')),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_prov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.CharField(max_length=15)),
                ('kpi_year', models.DateField(blank=True, null=True)),
                ('hospcode', models.CharField(max_length=5)),
                ('hosname', models.CharField(max_length=255)),
                ('b1', models.DecimalField(decimal_places=2, max_digits=19)),
                ('a1', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p1', models.DecimalField(decimal_places=2, max_digits=19)),
                ('b2', models.DecimalField(decimal_places=2, max_digits=19)),
                ('a2', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p2', models.DecimalField(decimal_places=2, max_digits=19)),
                ('b3', models.DecimalField(decimal_places=2, max_digits=19)),
                ('a3', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p3', models.DecimalField(decimal_places=2, max_digits=19)),
                ('b4', models.DecimalField(decimal_places=2, max_digits=19)),
                ('a4', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p4', models.DecimalField(decimal_places=2, max_digits=19)),
                ('bt', models.DecimalField(decimal_places=2, max_digits=19)),
                ('at', models.DecimalField(decimal_places=2, max_digits=19)),
                ('pt', models.DecimalField(decimal_places=2, max_digits=19)),
                ('goal', models.CharField(max_length=15)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('kpi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Kpi_index')),
            ],
        ),
        migrations.CreateModel(
            name='Kpi_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospcode', models.CharField(max_length=5)),
                ('kpi_month', models.DateField()),
                ('kpi_year', models.DateField(blank=True, null=True)),
                ('a1', models.CharField(max_length=155)),
                ('b1', models.CharField(max_length=155)),
                ('a2', models.CharField(max_length=155)),
                ('b2', models.CharField(max_length=155)),
                ('a3', models.CharField(max_length=155)),
                ('b3', models.CharField(max_length=155)),
                ('a4', models.CharField(max_length=155)),
                ('b4', models.CharField(max_length=155)),
                ('a5', models.CharField(max_length=155)),
                ('b5', models.CharField(max_length=155)),
                ('a6', models.CharField(max_length=155)),
                ('b6', models.CharField(max_length=155)),
                ('a7', models.CharField(max_length=155)),
                ('b7', models.CharField(max_length=155)),
                ('a8', models.CharField(max_length=155)),
                ('b8', models.CharField(max_length=155)),
                ('a9', models.CharField(max_length=155)),
                ('b9', models.CharField(max_length=155)),
                ('a10', models.CharField(max_length=155)),
                ('b10', models.CharField(max_length=155)),
                ('a11', models.CharField(max_length=155)),
                ('b11', models.CharField(max_length=155)),
                ('a12', models.CharField(max_length=155)),
                ('b12', models.CharField(max_length=155)),
                ('etc', models.TextField()),
                ('kpi_value', models.CharField(max_length=15)),
                ('d_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('input_date', models.DateTimeField()),
                ('kpi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Kpi_index')),
            ],
        ),
    ]