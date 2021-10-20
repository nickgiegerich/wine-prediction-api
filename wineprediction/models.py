from django.db import models

# Create your models here.

class Wine (models.Model):

    MODEL_CHOICES = (
        ('RF', 'Random Forest'),
        ('KNN', 'K Nearest Neighbor'),
    )
    

    id = models.AutoField(primary_key=True, unique=True)
    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    ph = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    # model_to_run = models.CharField(choices=MODEL_CHOICES, max_length=3, default='RF')
    model_to_run = models.BooleanField(default=True)