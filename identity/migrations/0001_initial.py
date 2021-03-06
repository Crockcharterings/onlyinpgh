# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Identity'
        db.create_table('identity_identity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('avatar', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('identity', ['Identity'])

        # Adding M2M table for field account on 'Identity'
        db.create_table('identity_identity_account', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('identity', models.ForeignKey(orm['identity.identity'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('identity_identity_account', ['identity_id', 'user_id'])

        # Adding model 'Organization'
        db.create_table('identity_organization', (
            ('identity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['identity.Identity'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, blank=True)),
        ))
        db.send_create_signal('identity', ['Organization'])

        # Adding model 'Individual'
        db.create_table('identity_individual', (
            ('identity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['identity.Identity'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('identity', ['Individual'])


    def backwards(self, orm):
        
        # Deleting model 'Identity'
        db.delete_table('identity_identity')

        # Removing M2M table for field account on 'Identity'
        db.delete_table('identity_identity_account')

        # Deleting model 'Organization'
        db.delete_table('identity_organization')

        # Deleting model 'Individual'
        db.delete_table('identity_individual')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'identity.identity': {
            'Meta': {'ordering': "['name']", 'object_name': 'Identity'},
            'account': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'identity.individual': {
            'Meta': {'ordering': "['name']", 'object_name': 'Individual', '_ormbases': ['identity.Identity']},
            'identity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['identity.Identity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'identity.organization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Organization', '_ormbases': ['identity.Identity']},
            'identity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['identity.Identity']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['identity']
