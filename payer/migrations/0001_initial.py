# Generated by Django 3.0.14 on 2021-10-07 09:55

import core.fields
import core.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0014_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now)),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('id', models.AutoField(db_column='PayerID', primary_key=True, serialize=False)),
                ('uuid', models.CharField(db_column='PayerUUID', default=uuid.uuid4, max_length=36, unique=True)),
                ('type', models.CharField(choices=[('C', 'Co-operative'), ('D', 'Donor'), ('G', 'Government'), ('L', 'Local Authority'), ('O', 'Other'), ('P', 'Private Organization')], db_column='PayerType', max_length=1)),
                ('name', models.CharField(db_column='PayerName', max_length=100)),
                ('address', models.CharField(blank=True, db_column='PayerAddress', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=50, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_column='eMail', max_length=50, null=True)),
                ('audit_user_id', models.IntegerField(db_column='AuditUserID')),
            ],
            options={
                'db_table': 'tblPayer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayerType',
            fields=[
                ('code', models.CharField(db_column='Code', max_length=1, primary_key=True, serialize=False)),
                ('payer_type', models.CharField(db_column='PayerType', max_length=50)),
                ('alt_language', models.CharField(blank=True, db_column='AltLanguage', max_length=50, null=True)),
                ('sort_order', models.IntegerField(blank=True, db_column='SortOrder', null=True)),
            ],
            options={
                'db_table': 'tblPayerType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayerMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payers', to='core.MutationLog')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payer.Payer')),
            ],
            options={
                'db_table': 'payer_PayerMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
    ]
