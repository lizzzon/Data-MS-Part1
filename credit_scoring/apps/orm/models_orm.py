from django.db import models

class User(models.Model):
    STAFF = 'staff'
    CLIENT = 'client'
    COMPANY = 'company'
    ROLES = [
        (STAFF, 'staff'),
        (CLIENT, 'client'),
        (COMPANY, 'company'),
    ]
    
    email = models.EmailField(max_length=64, unique=True, null=False)
    username = models.CharField(max_length=16, unique=True, null=False)
    user_password = models.CharField(max_length=128, null=False)
    user_role = models.CharField(max_length=7, null=True, choices=ROLES)
    is_active = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)


# class StaffRole(models.Model):
#     staff_role_name = models.CharField(max_length=16, null=False)
#
#
# class Staff(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     staff_role = models.ForeignKey('StaffRole', on_delete=models.CASCADE)
#
#
# class Log(models.Model):
#     ERROR = 'error'
#     WARNING = 'warning'
#     INFO = 'info'
#     LOG_TYPE = [
#         (ERROR, 'error'),
#         (WARNING, 'warning'),
#         (INFO, 'info')
#     ]
#
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     staff_role = models.ForeignKey('StaffRole', on_delete=models.CASCADE)
#     log_type = models.CharField(max_length=7, null=False, choices=LOG_TYPE, default=INFO)
#     log_message = models.CharField(max_length=64, null=False)
#     time_stamp = models.DateTimeField(null=False)
#
#
# class Country(models.Model):
#     country_name = models.CharField(max_length=32, null=False)
#
#
# class City(models.Model):
#     city_name = models.CharField(max_length=32, null=False)
#
#
# class Citizenship(models.Model):
#     citizenship_name = models.CharField(max_length=4, null=False)
#
#
# class Document(models.Model):
#     PASSPORT = 'passport'
#     RESIDENCE = 'residence'
#     PERMIT = 'permit'
#     TYPES = [
#         (PASSPORT, 'passport'),
#         (RESIDENCE, 'residence'),
#         (PERMIT, 'permit')
#     ]
#
#     citizenship = models.ForeignKey('Citizenship', on_delete=models.CASCADE)
#     current_type = models.CharField(max_length=9, null=False, choices=TYPES, default=PASSPORT)
#     documents_number = models.CharField(max_length=16, null=False, unique=True)
#     issue_date = models.DateField(null=False)
#     expiration_date = models.DateField(null=False)
#
#
# class Client(models.Model):
#     MALE = 'male'
#     FEMALE = 'female'
#     SEX = [
#         (MALE, 'male'),
#         (FEMALE, 'female')
#     ]
#
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     country = models.ForeignKey('Country', on_delete=models.CASCADE)
#     city = models.ForeignKey('City', on_delete=models.CASCADE)
#     document = models.ForeignKey('Document', on_delete=models.CASCADE)
#     last_name = models.CharField(max_length=32, null=False)
#     first_name = models.CharField(max_length=32, null=False)
#     middle_name = models.CharField(max_length=32, null=False)
#     sex = models.CharField(max_length=6, null=False, choices=SEX, default=MALE)
#     birth_date = models.DateField(null=False)
#     phone = models.CharField(max_length=16, null=False, unique=True)
#     address = models.CharField(max_length=64, null=False)
#
#
# class Company(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=32, null=False)
#     short_name = models.CharField(max_length=32, null=False)
#
#
# class ProductType(models.Model):
#     product_type_name = models.CharField(max_length=32, null=False)
#
#
# class Product(models.Model):
#     company = models.ForeignKey('Company', on_delete=models.CASCADE)
#     product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=32, null=False)
#     product_cost = models.DecimalField(null=False)
#     product_amount = models.IntegerField(null=False)
#
#
# class Loan(models.Model):
#     CREATED = 'created'
#     CONFIRMED = 'confirmed'
#     ISSUED = 'issued'
#     REDEEMED = 'redeemed'
#     OVERDUE = 'overdue'
#     LOAN_STATUS = [
#         (CREATED, 'created'),
#         (CONFIRMED, 'confirmed'),
#         (ISSUED, 'issued'),
#         (REDEEMED, 'redeemed'),
#         (OVERDUE, 'overdue')
#     ]
#
#     INSTALLMENT = 'installment'
#     CREDIT = 'credit'
#     LOAN_TYPE = [
#         (INSTALLMENT, 'installment'),
#         (CREDIT, 'credit')
#     ]
#
#     client = models.ForeignKey('Client', on_delete=models.CASCADE)
#     company = models.ForeignKey('Company', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     loan_status = models.CharField(max_length=9, null=False, choices=LOAN_STATUS, default=CREATED)
#     loan_type = models.CharField(max_length=11, null=False, choices=LOAN_TYPE, default=CREDIT)
#     order_amount = models.IntegerField(null=False)
#     credit_period = models.IntegerField(null=False)
#     credit_rate = models.DecimalField(null=False)
#     outstanding_loan_amount = models.DecimalField(null=False)
#     credit_datetime = models.DateTimeField(null=False)
#     last_change_datetime = models.DateTimeField(null=False)