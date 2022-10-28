# Generated by Django 4.1.1 on 2022-09-14 18:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=15, null=True)),
                ('account_type', models.CharField(max_length=15, null=True)),
                ('account_number', models.CharField(max_length=15, null=True)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=25, null=True)),
                ('nationality', models.CharField(max_length=15, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('recipient', models.CharField(max_length=15, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=15, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('balance', models.IntegerField()),
                ('pin', models.TextField(max_length=4, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_Customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_Amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('transcation_ID', models.CharField(max_length=10, null=True)),
                ('transaction_type', models.CharField(max_length=15, null=True)),
                ('transaction_charge', models.IntegerField()),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account')),
                ('transaction_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_transaction_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_Wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_Account', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customerId', models.CharField(max_length=8, null=True)),
                ('reward_points', models.CharField(max_length=15, null=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_Reward', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept_type', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('account_number', models.IntegerField(default=0)),
                ('reciept_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reciept_Transcation', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.IntegerField()),
                ('loan_type', models.CharField(max_length=15, null=True)),
                ('loan_balance', models.CharField(max_length=15, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gauranter', models.CharField(max_length=15, null=True)),
                ('loan_term', models.IntegerField()),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=15, null=True)),
                ('card_type', models.CharField(max_length=15, null=True)),
                ('card_number', models.IntegerField()),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_Account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_Wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
