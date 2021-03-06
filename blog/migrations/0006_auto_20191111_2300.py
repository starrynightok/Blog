# Generated by Django 2.1.4 on 2019-11-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191016_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleOtherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
            ],
            options={
                'verbose_name': '阅读量',
                'verbose_name_plural': '阅读量',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tui',
        ),
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.DeleteModel(
            name='Tui',
        ),
        migrations.AddField(
            model_name='articleotherinfo',
            name='article_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]
