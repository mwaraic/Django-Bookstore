# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.


class YrbBook(models.Model):
    title = models.CharField(primary_key=True, max_length=25)
    year = models.SmallIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    cat = models.ForeignKey('YrbCategory', models.DO_NOTHING, db_column='cat')
    weight = models.SmallIntegerField()

    class Meta:
        
        db_table = 'yrb_book'
        unique_together = (('title', 'year'),)
    


class YrbCategory(models.Model):
    cat = models.CharField(primary_key=True, max_length=10)

    class Meta:
        
        db_table = 'yrb_category'


class YrbClub(models.Model):
    club = models.CharField(primary_key=True, max_length=15)
    desp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'yrb_club'


class YrbCustomer(models.Model):
    cid = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        
        db_table = 'yrb_customer'


class YrbMember(models.Model):
    club = models.OneToOneField(YrbClub, models.DO_NOTHING, db_column='club', primary_key=True)
    cid = models.ForeignKey(YrbCustomer, models.DO_NOTHING, db_column='cid')

    class Meta:
        
        db_table = 'yrb_member'
        unique_together = (('club', 'cid'),)


class YrbOffer(models.Model):
    club = models.OneToOneField(YrbClub, models.DO_NOTHING, db_column='club', primary_key=True)
    title = models.ForeignKey(YrbBook, models.DO_NOTHING, db_column='title')
    year = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        
        db_table = 'yrb_offer'
        unique_together = (('club', 'title', 'year'),)


class YrbPurchase(models.Model):
    cid = models.SmallIntegerField(primary_key=True)
    club = models.ForeignKey(YrbMember, models.DO_NOTHING, db_column='club')
    title = models.CharField(max_length=25)
    year = models.SmallIntegerField()
    whenp = models.DateTimeField()
    qnty = models.SmallIntegerField()

    class Meta:
        
        db_table = 'yrb_purchase'
        unique_together = (('cid', 'club', 'title', 'year', 'whenp'),)


class YrbShipping(models.Model):
    weight = models.SmallIntegerField(primary_key=True)
    cost = models.DecimalField(unique=True, max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'yrb_shipping'
        
class YrbUser(models.Model):
    cid = models.OneToOneField(YrbCustomer, models.DO_NOTHING, db_column='cid', primary_key=True)
    email = models.CharField(max_length=25)
    password_hash = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'yrb_user'
        unique_together = (('cid', 'email', 'password_hash'),)