# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'deal_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal(u'deal', ['Category'])

        # Adding model 'Subcategory'
        db.create_table(u'deal_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category_pk', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subcategories', to=orm['deal.Category'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal(u'deal', ['Subcategory'])

        # Adding model 'Tag'
        db.create_table(u'deal_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'deal', ['Tag'])

        # Adding model 'Deal'
        db.create_table(u'deal_deal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_started', self.gf('django.db.models.fields.DateField')()),
            ('date_ended', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('promo_thumbnail', self.gf('django.db.models.fields.URLField')(default='media/deal/2013/08/17/f5cd7f84-7e94-4cf6-acb3-9df3d0470421.jpeg', max_length=250, null=True, blank=True)),
            ('promo_image', self.gf('django.db.models.fields.files.ImageField')(max_length=250, blank=True)),
            ('promo_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('total_vote', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('member_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Profile'], blank=True)),
            ('category_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deal.Category'])),
            ('subcategory_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deal.Subcategory'], null=True, blank=True)),
        ))
        db.send_create_signal(u'deal', ['Deal'])

        # Adding M2M table for field tag_pk on 'Deal'
        m2m_table_name = db.shorten_name(u'deal_deal_tag_pk')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('deal', models.ForeignKey(orm[u'deal.deal'], null=False)),
            ('tag', models.ForeignKey(orm[u'deal.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['deal_id', 'tag_id'])

        # Adding model 'DealRating'
        db.create_table(u'deal_dealrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vote', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('deal_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deal.Deal'])),
            ('member_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Profile'])),
        ))
        db.send_create_signal(u'deal', ['DealRating'])

        # Adding model 'FacebookFeed'
        db.create_table(u'deal_facebookfeed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('page_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('recent_feed', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('category_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deal.Category'])),
            ('member_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Profile'], null=True, blank=True)),
        ))
        db.send_create_signal(u'deal', ['FacebookFeed'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'deal_category')

        # Deleting model 'Subcategory'
        db.delete_table(u'deal_subcategory')

        # Deleting model 'Tag'
        db.delete_table(u'deal_tag')

        # Deleting model 'Deal'
        db.delete_table(u'deal_deal')

        # Removing M2M table for field tag_pk on 'Deal'
        db.delete_table(db.shorten_name(u'deal_deal_tag_pk'))

        # Deleting model 'DealRating'
        db.delete_table(u'deal_dealrating')

        # Deleting model 'FacebookFeed'
        db.delete_table(u'deal_facebookfeed')


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
        u'deal.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'deal.deal': {
            'Meta': {'object_name': 'Deal'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ended': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']", 'blank': 'True'}),
            'promo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'promo_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'blank': 'True'}),
            'promo_thumbnail': ('django.db.models.fields.URLField', [], {'default': "'media/deal/2013/08/17/f5cd7f84-7e94-4cf6-acb3-9df3d0470421.jpeg'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'subcategory_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Subcategory']", 'null': 'True', 'blank': 'True'}),
            'tag_pk': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['deal.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'})
        },
        u'deal.dealrating': {
            'Meta': {'object_name': 'DealRating'},
            'deal_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Deal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'deal.facebookfeed': {
            'Meta': {'object_name': 'FacebookFeed'},
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']", 'null': 'True', 'blank': 'True'}),
            'page_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recent_feed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'deal.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': u"orm['deal.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'deal.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'member.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deal_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['deal.Deal']", 'null': 'True', 'through': u"orm['deal.DealRating']", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline_1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'landline_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'store_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['store.Store']", 'null': 'True', 'through': u"orm['store.StoreRating']", 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'store.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'store.store': {
            'Meta': {'object_name': 'Store'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Area']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'landline_1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'landline_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'store.storerating': {
            'Meta': {'object_name': 'StoreRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'store_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Store']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['deal']