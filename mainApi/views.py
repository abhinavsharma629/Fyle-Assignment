from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from .customClasses import CustomLimitAndOffset
from .serializers import BankDetailsSerializer
from rest_framework.generics import ListAPIView
from .models import BankDetails
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status


#GET API to fetch a bank details, given branch IFSC code
@api_view(['GET'])
@cache_page(60*2)
def bankDetail(request):
    permission_classes = [IsAuthenticated]
    try:
        bankObj=BankDetails.objects.get(ifsc=request.GET.get('ifsc_code'))
        serializer=BankDetailsSerializer(bankObj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'message': "No Such record present/ Wrong query parameter given"
        }, status=status.HTTP_404_NOT_FOUND)


#GET API to fetch all details of branches, given bank name and a city 
@permission_classes([IsAuthenticated])
class bankDetails(ListAPIView):
    
    queryset=BankDetails.objects.all()
    serializer_class = BankDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bank_name', 'city']
    pagination_class = CustomLimitAndOffset
    
    ''' NOTE:- 
    We can also return the queryset manually rather than using filter backends'''

    # def get_queryset(self):
    #     """
    #     This view should return a list of details of all the branches
    #     for the given city and bank name.
    #     """
    #     bank_name = self.request.GET.get('bank_name')
    #     city=self.request.GET.get('city')
        
    #     return BankDetails.objects.filter(bank_name=bank_name, city=city)
    
    #Caching Results
    @method_decorator(cache_page(60*2))
    def dispatch(self, *args, **kwargs):
        return super(bankDetails, self).dispatch(*args, **kwargs)

