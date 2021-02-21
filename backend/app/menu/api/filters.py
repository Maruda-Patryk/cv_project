from django_filters.rest_framework import FilterSet, CharFilter, OrderingFilter, \
    IsoDateTimeFilter

from ..models import MenuCard


class MenuCardFilterSet(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    create_date = IsoDateTimeFilter()
    last_update_date = IsoDateTimeFilter()

    order = OrderingFilter(
        choices=(
            ('name', 'name'),
            ('-name', '-name'),
            ('dishes_count', 'dishes_count'),
            ('-dishes_count', '-dishes_count'),
        ),
    )

    class Meta:
        model = MenuCard

        fields = [
            'name',
            'create_date',
            'last_update_date',
        ]
