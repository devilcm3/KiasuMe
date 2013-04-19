# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'promotion_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'promotion', ['Category'])

        # Adding model 'Subcategory'
        db.create_table(u'promotion_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotion.Category'])),
        ))
        db.send_create_signal(u'promotion', ['Subcategory'])

        # Adding model 'Tag'
        db.create_table(u'promotion_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'promotion', ['Tag'])

        # Adding model 'Promotion'
        db.create_table(u'promotion_promotion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_started', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 3, 0, 0))),
            ('date_ended', self.gf('django.db.models.fields.DateTimeField')()),
            ('promo_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('promo_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('total_vote', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('member_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Profile'])),
            ('category_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotion.Category'])),
            ('subcategory_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotion.Subcategory'])),
        ))
        db.send_create_signal(u'promotion', ['Promotion'])

        # Adding M2M table for field tag_pk on 'Promotion'
        db.create_table(u'promotion_promotion_tag_pk', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotion', models.ForeignKey(orm[u'promotion.promotion'], null=False)),
            ('tag', models.ForeignKey(orm[u'promotion.tag'], null=False))
        ))
        db.create_unique(u'promotion_promotion_tag_pk', ['promotion_id', 'tag_id'])

        # Adding model 'PromotionRating'
        db.create_table(u'promotion_promotionrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vote', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('promotion_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotion.Promotion'])),
            ('member_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Profile'])),
        ))
        db.send_create_signal(u'promotion', ['PromotionRating'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'promotion_category')

        # Deleting model 'Subcategory'
        db.delete_table(u'promotion_subcategory')

        # Deleting model 'Tag'
        db.delete_table(u'promotion_tag')

        # Deleting model 'Promotion'
        db.delete_table(u'promotion_promotion')

        # Removing M2M table for field tag_pk on 'Promotion'
        db.delete_table('promotion_promotion_tag_pk')

        # Deleting model 'PromotionRating'
        db.delete_table(u'promotion_promotionrating')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'member.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'promotion_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotion.Promotion']", 'through': u"orm['promotion.PromotionRating']", 'symmetrical': 'False'}),
            'store_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['store.Store']", 'through': u"orm['store.StoreRating']", 'symmetrical': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'promotion.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'promotion.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotion.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ended': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 3, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'promo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'promo_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'subcategory_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotion.Subcategory']"}),
            'tag_pk': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotion.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'promotion.promotionrating': {
            'Meta': {'object_name': 'PromotionRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'promotion_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotion.Promotion']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'promotion.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotion.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'promotion.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'store.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'province_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Province']"})
        },
        u'store.province': {
            'Meta': {'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'store.store': {
            'Meta': {'object_name': 'Store'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Area']"}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'province_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Province']"}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'store.storerating': {
            'Meta': {'object_name': 'StoreRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'store_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Store']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['promotion']