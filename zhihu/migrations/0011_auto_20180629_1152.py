# Generated by Django 2.0.3 on 2018-06-29 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhihu', '0010_auto_20180626_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answercomment',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Answer', verbose_name='回答'),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='usercollectanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Answer', verbose_name='回答'),
        ),
        migrations.AlterField(
            model_name='usercollectanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userfollowanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Answer', verbose_name='回答'),
        ),
        migrations.AlterField(
            model_name='userfollowanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userfollowquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhihu.Question', verbose_name='问题'),
        ),
        migrations.AlterField(
            model_name='userfollowquestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]