from django.shortcuts import render,get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .models import post
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .serializers import ProductSerializer
product=[
    {
        'name': 'Product 1',
        'content': 'Description of Product 1',
        'id': 1,
        'price': 99.99
    },
    {
        'name': 'Product 2',
        'content': 'Description of Product 2',
        'id': 2,
        'price': 49.99
    },
    {
        'name': 'Product 3',
        'content': 'Description of Product 3',
        'id': 3,
        'price': 79.99
    },
    {
        'name': 'Product 4',
        'content': 'Description of Product 4',
        'id': 4,
        'price': 59.99
    },
    {
        'name': 'Product 5',
        'content': 'Description of Product 5',
        'id': 5,
        'price': 89.99
    }
]


@api_view(["GET"])
def api(request):
    Post=post.objects.all()
    serializer=ProductSerializer(instance=Post,many=True)
    response={'message':'hello world',
              "data":serializer.data}
    return Response(data=response)

@api_view(['GET',"POST","PUT"])
def Post(request):
    posts=post.objects.all()
    if request.method=="POST":
        data=request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res={
                "mess":"post is creted",
                "post":serializer.data
            }
            return Response(data=res)
    else:
        
        serializer=ProductSerializer(instance=posts,many=True)
        res={
                    "mess":"post showed",
                    "post":serializer.data
                }
        return Response(data=res)

@api_view(['GET',"POST"])
def Postindex(request,index):
    Post=post.objects.get_or_create(id=index)
    serializer=ProductSerializer(data=Post)
    return Response(data=product[index])
@api_view(['PUT'])
def update_post(request:Request, post_id:int):
   
    Post = get_object_or_404(post,id=post_id)  

    data = request.data
    serializer = ProductSerializer(instance=Post, data=data)
    
    if serializer.is_valid():
        serializer.save()
        response = {
            "msg": "Post updated",
            "data": serializer.data
        }
        return Response(data=response)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request,index):
    Post=get_object_or_404(post,id=index)
    Post.delete()
    p=post.objects.all()
    serializer=ProductSerializer(instance=p,many=True)
    
    response = {
            "msg": "your data id dleted",
            "data": serializer.data
        }
    return Response(response)


#class based view
class Apipost(APIView):
    serializer=ProductSerializer

    def get(self,request):
        Post=post.objects.all()
        
        serializer=ProductSerializer(instance=Post,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data

        serializer=ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

class PostViewDeleteView(APIView):
    serializer=ProductSerializer
    def put(self,request,index):
        posts=get_object_or_404(post,id=index)
        data=request.data

        serializer=ProductSerializer(posts,data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,index):
        posts=get_object_or_404(post,id=index)
        posts.delete()
        return Response(data={"is delete":"g"},status=status.HTTP_202_ACCEPTED)


#mixins

class postmixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=post.objects.all()
    serializer_class=ProductSerializer

    def get(self,request):
        return self.list(request)
  
    def post(self,request):
        return self.create(request)
   
    
class reterview(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=post.objects.all()
    serializer_class=ProductSerializer

    def put(self,request,pk):
        return self.update(request, pk=pk)

    def delete(self,request,pk):
        return self.destroy(request, pk=pk)
    
    def get(self,request,pk):
        return self.retrieve(request, pk=pk)
    
#viewset

class Postviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=post.objects.all()
        serilaizer=ProductSerializer(instance=queryset,many=True)
        return Response(data=serilaizer.data)
    
    def retrieve(self,request,pk=None):
        Post=get_object_or_404(post,pk=pk)
        serializer=ProductSerializer(instance=post)
        return Response(data=serializer.data)
    
#viewset.modleviewset

class modleviewset(viewsets.ModelViewSet):
    queryset=post.objects.all()
    serializer_class=ProductSerializer
    