from rest_framework.response import Response
from product.models import Category,Product,Review
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer



    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10:
            return Response('product with stock more than 10 could not be deleted')
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
            # sob viewset a eka kwargs thake seta Dict. akare thake.
            #context akare product_id ta k pathailam viewset a thaka product_pk name er value ta
            # jate serializer ta product_id ta pai jetai ami review debo