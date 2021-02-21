from django.db.models import Count

from rest_framework import viewsets, permissions

from .serializers import MenuCardSerializerList, MenuCardSerializerUpdateOrCreate, MenuCardSerializerDetails, \
    DishesSerializerList
from .filters import MenuCardFilterSet
from ..models import MenuCard, Dish


class MenuCardViewSet(viewsets.ModelViewSet):
    queryset = MenuCard.objects.exclude(dishes=None).prefetch_related('dishes')
    filterset_class = MenuCardFilterSet

    def create(self, request, *args, **kwargs):
        """ Create Menu

        :param:

            data:
            {
                "name": " (str) New name for Menu"
                "description": "(str) Menu's description"
                "dishes": "(list of uuids) List of uuids"
            }

            example:
            {
                "name": "menu's name",
                "dishes": [
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                ],
                "description": "menu's description"
            }
        :return: Updated Menu body
        """

        self.serializer_class = MenuCardSerializerUpdateOrCreate
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """ Get Menu's List

        :param name: (str) Filter by name
        :param create_date: (datetime) Filter by create datetime (example: 2021-02-18T12:39:37.813554Z)
        :param last_update_date:(datetime) Filter by update datetime (example: 2021-02-18T12:39:37.813554Z)
        :param order: (str) Order by Field, Allowed fields: 'name', 'dishes_count'

        """
        self.serializer_class = MenuCardSerializerList
        self.queryset = self.queryset.annotate(dishes_count=Count('dishes'))
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """ Update Menu (PUT method)

        :param:

            data:
            {
                "name": " (str) New name for Menu"
                "description": "(str) Menu's description"
                "dishes": "(list of uuids) List of uuids"
            }

            example:
            {
                "name": "menu's name",
                "dishes": [
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                ],
                "description": "menu's description"
            }

        :return: Updated Menu body
        """
        self.serializer_class = MenuCardSerializerUpdateOrCreate
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """ Update Menu (PATCH method)

        :param:

            data:
            {
                "name": " (str) New name for Menu"
                "description": "(str) Menu's description"
                "dishes": "(list of uuids) List of uuids"
            }

            example:
            {
                "name": "menu's name",
                "dishes": [
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                ],
                "description": "menu's description"
            }

        :return: Updated Menu body
        """
        self.serializer_class = MenuCardSerializerUpdateOrCreate
        return super().partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ Get Menu's Details

        :return: Menu data, with list of dishes
        """
        self.serializer_class = MenuCardSerializerDetails
        return super().retrieve(request, *args, **kwargs)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishesSerializerList
    permission_classes = (permissions.DjangoModelPermissions,)
