import uuid

from django.db import models


class MenuMixin(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Dish(MenuMixin):
    """
    Attributes:
        name (string): dish's name
        description (string): dish's description
        price (float): price for dish
        preparation_time (integer): time to preparation dish, stored as a number of seconds
        create_date (datetime): creation datetime
        last_update_date (datetime): date when objects was last update
        is_vegan (bool): True if dish is vegan or False if not
    """

    name = models.CharField(max_length=255)
    prince = models.FloatField()
    preparation_time = models.IntegerField()
    is_vegan = models.BooleanField(db_index=True)


class MenuCard(MenuMixin):
    """
        Attributes:
            name (string): card's name
            description (string): card's description
            create_date (datetime): creation datetime
            last_update_date (datetime): date when objects was last update
        """
    name = models.CharField(max_length=255, unique=True)
    dishes = models.ManyToManyField(Dish)
