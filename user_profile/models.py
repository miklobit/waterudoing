from django.db import models
from django.conf import settings
from django.urls import reverse


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    weekly_laundry_loads = models.IntegerField(null=False)
    daily_bathroom_trips = models.IntegerField(null=False)
    weekly_showers = models.IntegerField(null=False)
    shower_times = models.IntegerField(null=False)
    weekly_baths = models.IntegerField(null=False)
    weekly_dishes = models.IntegerField(null=False)
    weekly_sprinkler = models.IntegerField(null=False)
    swimming_pool = models.BooleanField(null=False, default=False)
    score = models.IntegerField(null=False)

    shower_head_choices = [
        ("Normal Shower Head", "Normal Shower Head"),
        ("Efficient Shower Head", "Efficient Shower Head"),
    ]

    shower_head_choices = models.CharField (
        max_length = 30,
        null=False,
        choices = shower_head_choices,
    )

    washer_type_choices = [
        ("Top Load Washer", "Top Load Washer"),
        ("Front Load Washer", "Front Load Washer"),
    ]

    washer_type_choices = models.CharField (
        max_length = 30,
        null=False,
        choices = washer_type_choices,
    )

    swimming_pool_choices = [
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
        ("I Don't Have A Pool", "I Don't Have A Pool"),
    ]

    swimming_pool_choices = models.CharField (
        max_length = 30,
        null=False,
        choices = swimming_pool_choices
    )

    def profile_url(self):
        return reverse('view_profile', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        self.score = self.weekly_laundry_loads * settings.TOP_LOAD_WASHER_LOAD
        self.score += self.daily_bathroom_trips * settings.TOILET_FLUSH 
        self.score += self.weekly_showers * self.shower_times * settings.NORMAL_SHOWER_MINUTE 
        self.score += self.weekly_baths * settings.BATHTUB_FILL 
        self.score += self.weekly_dishes * settings.DISHWASHER_CYCLE 
        self.score += self.weekly_sprinkler * settings.SPRINKLER_MINUTE
        if self.swimming_pool :
            self.score = self.score + settings.SWIMMING_POOL_FILL
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
