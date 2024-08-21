from django.db import models

# Create your models here.
class Electionadmin(models.Model):
          a_id = models.AutoField(db_column='a_ID', primary_key=True)  # Field name made lowercase.
          a_username = models.CharField(db_column='a_Username', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
          a_password = models.CharField(db_column='a_Password', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
          a_confirmpassword = models.CharField(db_column='a_ConfirmPassword', max_length=50, blank=True,
                                               null=True)  # Field name made lowercase.
          a_typeadmin = models.IntegerField(db_column='a_typeAdmin', blank=True,
                                            null=True)  # Field name made lowercase.
          a_typesuperadmin = models.IntegerField(db_column='a_typeSuperadmin', blank=True,
                                                 null=True)  # Field name made lowercase.
          a_name = models.CharField(db_column='a_Name', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
          a_contactno = models.CharField(db_column='a_ContactNo', max_length=30, blank=True,
                                         null=True)  # Field name made lowercase.
          a_message = models.CharField(db_column='a_Message', max_length=500, blank=True,
                                       null=True)  # Field name made lowercase.
          a_image = models.ImageField(upload_to='Admin_Images', db_column='a_Image', max_length=500, blank=True,
                                      null=True)  # Field name made lowercase.

          class Meta:
                    db_table = 'electionadmin'
