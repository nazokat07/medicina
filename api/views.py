from rest_framework import generics, mixins, response, status, permissions
from rest_framework.response import Response
from app.models import *
from .serializers import *


'''class CafeList(generics.ListAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetail(generics.RetrieveAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafePost(generics.CreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafePut(generics.UpdateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDelete(generics.DestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer'''

'''class CafeAPIView(generics.ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class MenuAPIView(generics.ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = MenuSerializer

class MenuDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = MenuSerializer'''



'''class CafeViewSet(viewsets.ModelViewSet):

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class MenuViewSet(viewsets.ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

'''


class ClientAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []

    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ClientDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






class BlogAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []

    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class BlogDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return []
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







class SponsorAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []

    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class SponsorDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return []
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


