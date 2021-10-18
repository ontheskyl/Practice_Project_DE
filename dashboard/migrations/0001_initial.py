# Generated by Django 3.2.7 on 2021-10-18 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information_Book_Detail',
            fields=[
                ('Book_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_Title', models.CharField(max_length=50)),
                ('Author_Name', models.CharField(max_length=50)),
                ('Author_Url', models.CharField(max_length=50, null=True)),
                ('Description', models.CharField(max_length=1000, null=True)),
                ('Rating_Avg', models.FloatField(null=True)),
                ('Rating_Count', models.IntegerField(null=True)),
                ('Reviews_Count', models.IntegerField(null=True)),
                ('Num_Pages', models.IntegerField(null=True)),
                ('Book_Format', models.CharField(max_length=50, null=True)),
                ('Time_publish', models.CharField(max_length=50, null=True)),
                ('Publisher', models.CharField(max_length=50, null=True)),
                ('ISBN', models.CharField(max_length=50, null=True)),
                ('Language', models.CharField(max_length=50, null=True)),
                ('Genres', models.JSONField(null=True)),
                ('Book_Url', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Book Detail',
                'verbose_name_plural': 'Book Details',
                'db_table': 'Book_Details',
                'ordering': ['Author_Name', 'Book_Title'],
            },
        ),
        migrations.CreateModel(
            name='Information_User_Detail',
            fields=[
                ('User_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50)),
                ('User_Url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Rating_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_url', models.CharField(max_length=100)),
                ('user_rating', models.FloatField()),
                ('Book_Info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='User_to_Book', to='dashboard.information_book_detail')),
                ('User_Info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='User_to_User', to='dashboard.information_book_detail')),
            ],
            options={
                'verbose_name': 'User Rating',
                'verbose_name_plural': 'User_Ratings',
                'db_table': 'User_Rating',
            },
        ),
    ]
