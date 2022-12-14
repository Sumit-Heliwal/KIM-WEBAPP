# Generated by Django 4.0.6 on 2022-11-16 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Data',
            fields=[
                ('Emp_Code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Employee_Name', models.CharField(max_length=100, unique=True)),
                ('Designation', models.CharField(max_length=25)),
                ('Address_1', models.CharField(max_length=300)),
                ('Address_2', models.CharField(max_length=300)),
                ('Contact_no1', models.BigIntegerField()),
                ('Contact_no2', models.BigIntegerField()),
                ('Personal_Email_ID', models.EmailField(max_length=254)),
                ('Official_Email_ID', models.EmailField(max_length=254)),
                ('Date_of_Birth', models.DateField()),
                ('Date_of_Joining', models.DateField()),
                ('Date_of_Confirmation', models.DateField()),
                ('Group', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Leave_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_Type', models.CharField(max_length=25)),
                ('From_Date', models.DateField()),
                ('To_Date', models.DateField()),
                ('Recommended_Authority', models.CharField(max_length=25)),
                ('Approved_By', models.CharField(max_length=25)),
                ('Reason_for_Leave', models.CharField(max_length=300)),
                ('Emp_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_Department.employee_data')),
            ],
        ),
    ]
