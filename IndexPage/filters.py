import django_filters
from Books.models import Book

class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Search Book'
    )

    class Meta:
        model = Book
        fields = ['name']