from rest_framework import serializers
from ..models import MenuCard, Dish


class DishesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class MenuCardSerializerList(serializers.ModelSerializer):
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = MenuCard
        fields = [
            'uuid',
            'name',
            'create_date',
            'last_update_date',
            'dishes_count',
        ]

    @staticmethod
    def get_dishes_count(obj):
        return obj.dishes.all().count()


class MenuCardSerializerDetails(serializers.ModelSerializer):
    dishes = DishesSerializerList(many=True)

    class Meta:
        model = MenuCard
        fields = '__all__'


class MenuCardSerializerUpdateOrCreate(serializers.ModelSerializer):
    class Meta:
        model = MenuCard
        fields = ['name', 'dishes', 'description']