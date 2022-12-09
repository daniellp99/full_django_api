from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Product Instance
    post -> create -> New Instance
    patch -> update -> Update Instance
    put -> partial update -> Partial Update Instance
    delete -> destroy -> Delete Instance
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Product Instance
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
