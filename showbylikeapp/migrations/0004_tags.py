# Generated by Django 3.0.5 on 2020-04-16 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showbylikeapp', '0003_posts_txt_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chr_tag', models.CharField(blank=True, max_length=20, null=True)),
                ('int_weight', models.IntegerField(blank=True, null=True)),
                ('fk_tags', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='showbylikeapp.Tags')),
            ],
        ),
    ]
