# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    province_id = models.BigIntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'



class Collect(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    charset = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    favorites_id = models.BigIntegerField()
    is_delete = models.CharField(max_length=255)
    last_modify_time = models.BigIntegerField()
    logo_url = models.CharField(max_length=300, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=600)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'collect'


class CollectorView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    counts = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_view'


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    collect_id = models.BigIntegerField()
    content = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    reply_user_id = models.BigIntegerField(db_column='reply_user_Id')  # Field name made lowercase.
    create_time = models.BigIntegerField()
    comment_time = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    reply_user_name = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comment'


class Config(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    default_collect_type = models.CharField(max_length=255)
    default_model = models.CharField(max_length=255)
    create_time = models.BigIntegerField()
    last_modify_time = models.BigIntegerField()
    default_favorties = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'config'


class Favorites(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    count = models.BigIntegerField()
    create_time = models.BigIntegerField()
    last_modify_time = models.BigIntegerField()
    public_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'favorites'


class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.BigIntegerField()
    feedback_advice = models.CharField(max_length=255)
    feedback_name = models.CharField(max_length=255, blank=True, null=True)
    last_modify_time = models.BigIntegerField()
    phone = models.CharField(max_length=255)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Follow(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    follow_id = models.BigIntegerField()
    follow_status = models.CharField(max_length=255)
    create_time = models.BigIntegerField()
    last_modify_time = models.BigIntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'follow'


class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_sequence'


class Letter(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_time = models.BigIntegerField()
    pid = models.BigIntegerField(blank=True, null=True)
    receive_user_id = models.BigIntegerField()
    send_user_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letter'


class Like(models.Model):
    user_id = models.IntegerField(primary_key=True)
    like_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'like'
        unique_together = (('user_id', 'like_id'),)


class LookRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    collect_id = models.BigIntegerField()
    create_time = models.BigIntegerField()
    last_modify_time = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'look_record'


class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    collect_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    readed = models.CharField(max_length=255)
    create_time = models.BigIntegerField()
    oper_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notice'


class Praise(models.Model):
    id = models.BigAutoField(primary_key=True)
    collect_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'praise'


class Seckill(models.Model):
    seckill_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    number = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seckill'


class Stock(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    sale = models.IntegerField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'


class StockOrder(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_order'


class SuccessKilled(models.Model):
    seckill_id = models.BigIntegerField(primary_key=True)
    user_phone = models.BigIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'success_killed'
        unique_together = (('seckill_id', 'user_phone'),)


class UrlLibrary(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'url_library'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    background_picture = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.BigIntegerField()
    email = models.CharField(unique=True, max_length=255)
    introduction = models.TextField(blank=True, null=True)
    last_modify_time = models.BigIntegerField()
    out_date = models.CharField(max_length=255, blank=True, null=True)
    pass_word = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(unique=True, max_length=255)
    validata_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserIsFollow(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_follow = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_is_follow'
