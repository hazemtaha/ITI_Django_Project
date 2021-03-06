from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
# from accounts.models import UserProfile
from model_utils.models import TimeStampedModel
# This abstract base class just provides self-updating created and
# modified fields on any model that inherits from it.and you have to
# install it's package too from pip
from geoposition.fields import GeopositionField
from cities_light.models import City, Region
# Create your models here.
from accounts.models import upload_location

PROPERTIES_TYPES = (
    ('Appartment', 'Appartment'),
    ('Building', 'Building'),
    ('Land', 'Land'),
    ('Villa', 'Villa'),
    ('Store', 'Store'),
    ('Office', 'Office'),
)
PROPERTIES_CATEGORIES = (
    ('s', 'For Sale'),
    ('r', 'For Rent'),
)
STATUS = (
    (True, 'Active'),
    (False, 'InActive'),
)


class Properties(TimeStampedModel):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    prop_type = models.CharField(max_length=20, choices=PROPERTIES_TYPES)
    city = models.ForeignKey(Region)
    neighborhood = models.ForeignKey(City)
    category = models.CharField(max_length=1, choices=PROPERTIES_CATEGORIES)
    description = models.TextField()
    price = models.IntegerField()
    size = models.IntegerField()
    yt_url = models.URLField(blank=True, null=True)
    position = GeopositionField()
    owner = models.ForeignKey('accounts.UserProfile')
    #p = Properties(title="Alrehab",status="true",prop_type='l',city="sharkia",neighborhood="belbies",category='s',description="new and unique yeah",price="1000000",size="200",lat="140000.4545",lon="200000.2200",yt_url="https://www.youtube.com/watch?v=FoAqHxm5dpo")
    # save() for testing only

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class PropertiesPhotos(models.Model):
    prop_photo = models.ImageField(
        null=True, blank=True, width_field="img_width", height_field="img_height")
    img_height = models.IntegerField(default=0)
    img_width = models.IntegerField(default=0)
    prop = models.ForeignKey('Properties', on_delete=models.CASCADE)
    # pp=p.propertiesphotos_set.create(prop_photo="image_path")
    # another test to link the foreign keys with each other

    def __str__(self):
        return str(self.prop_photo)
        # this for admin readability
