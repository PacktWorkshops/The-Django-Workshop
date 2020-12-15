from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TitledUser(User):

    class Meta:
        verbose_name = 'titled user'
        verbose_name_plural = 'titled users'

    class TitleChoices(models.TextChoices):
        PROF = "PROF", "Prof"
        DR = "DR", "Dr"

    class HonorificChoices(models.TextChoices):
        MR = "MR", "Mr"
        MISS = "MISS", "Miss"
        MRS = "MRS", "Mrs"
        MS = "MS", "MS"

    title = models.CharField(verbose_name="Title", blank=True,
                            choices=TitleChoices.choices,
                            max_length=10)
    honorific = models.CharField(verbose_name="Honorific", blank=True,
                            choices=HonorificChoices.choices,
                            max_length=10)

    def get_full_name(self):
        """
        Return any title or honorific, the first_name plus the last_name,
        with spaces in between .
        """
        if self.title:
            full_name = '{} {} {}'.format(self.title, 
                                          self.first_name,
                                          self.last_name)
        elif self.honorific:
            full_name = '{} {} {}'.format(self.honorific, 
                                          self.first_name,
                                          self.last_name)
        else:
            full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


"""
class ReviewerProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    favourite_book = models.ForeignKey(Book, null=True,
                                       on_delete=models.SET_NULL,
                                       help_text="Your favourite book (if it is "
                                       "present in Bookr)") 
    profile_photo = models.ImageField(null=True, blank=True,
                                      upload_to="profile_photos/")
"""
