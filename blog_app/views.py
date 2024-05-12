# ****  For learning  *****


# from .models import Blog, Category
# from .serializer import BlogSerializer, CategorySerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework import generics, mixins
# from rest_framework import viewsets
# from django.shortcuts import get_object_or_404


# *** CLASS BASED VIEWS ***

# class CategoryListView(APIView):
#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         # serializer = CategorySerializer(
#         #     all_categories, many=True, context={'request': request})  # we pass the context when we are using hyperlinkrelatedfield or when we use HyperLinkModelSerialzer in the serializer
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class CategoryDetailView(APIView):
#     def get(self, request, pk):
#         single_category = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(single_category)
#         # serializer = CategorySerializer(
#         #     single_category, context={'request': request})  # we pass the context when we are using hyperlinkrelatedfield or when we use HyperLinkModelSerialzer in the serializer
#         return Response(serializer.data, status=status.HTTP_200_OK)


# GET and POST
# class BlogListView(APIView):
#     def get(self, request):
#         all_blogs = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(all_blogs, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)


# GET, PUT and DELETE
# class BlogListDetailView(APIView):
#     def get(self, request, pk):
#         blog = Blog.objects.get(is_public=True, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         blog = Blog.objects.get(is_public=True, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ***  ***


# *****  GENERIC VIEWS AND MIXINS  *****

# we pass mixins.ListModelMixin and mixins.CreateModelMixin because we want to get all the data and we want to create new data
# we must pass generics.GenericAPIView too

# class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # we must pass queryset which is is used to perform query.
#     queryset = Blog.objects.all()
#     # we pass the seriralizer in the serializer_class
#     serializer_class = BlogSerializer

#     def get(self, request,  *args, **kwargs):  # we use this methid to perform get opertation
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):  # we use this method to perform the post operation
#         return self.create(request, *args, **kwargs)


# mixins.RetrieveModelMixin is used to get single object by id and it provides self.retrieve() method
# mixins.UpdateModelMixin is used to update an object and we can use put() method to update the object by using the self.update() method.
# we must pass generics.GenericAPIView too
# mixins.DestroyModelMixin is used to delete an object and we can use the delete() method to delete the object by using self.destroy() method

# NOTE: Primary key pk is passed it the RetrieveModelMixin and it picks pk from the url. We can change this by using the lookup_field

# class BlogDetailGenericView(mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             generics.GenericAPIView):

#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     # we use the lookup field if want to get an object by some other attribute instead of primary key pk which is by default. In this case we are using slug.
#     lookup_field = "slug"

#     # we use this method to get a single object by it's primary key pk.
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):  # we use this method to update a single object
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# *****   *****

# *** WORKING WITH FUNCTION BASED VIEWS ***

# @api_view(["GET", "POST"])
# def blog_list(request):
#     if request.method == "GET":
#         all_blogs = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(all_blogs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == "POST":
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def blog_detail(request, pk):
#     if request.method == "GET":
#         blog = Blog.objects.get(is_public=True, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == "PUT":
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#  ***  ***


# *****  CONCRETE VIEW CLASS   *****

# NOTE: In concrete view class we pass the generics.<someview> and according to that view we can perform get, post, put and delete operations.

# class BlogCreateConc(generics.CreateAPIView):  # it allows only POST operation
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogListConc(generics.ListAPIView):  # it allows only GET operation
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# it allows only GET for single object by id or by the field mentioned in the lookup_field attribute
# class BlogRetrieveConc(generics.RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

#     # we use the lookup field if want to get an object by some other attribute instead of primary key pk which is by default. In this case we are using slug.
#     lookup_field = "slug"


# # it allows only DELETE operation. It uses primary key pk by default but it can be changed using lookup_field.
# class BlogDeleteConc(generics.DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# this allows both POST and GET operations
# class BlogListConc(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# this allows GET, PUT(update) and DELETE operation by primary key pk or by the attribute mentioned in the lookup_filed. If it is not mentioned in the lookup_field then it used primary key pk by default
# class BlogDetailConc(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# *****  *****

# ***** VIEWSETS  *****

# NOTE: Viewset allows us to perform the CRUD operations in the same class. list() is used to perform GET operation and get all the items, retrieve() is used to perform GET operation and get a single item by it's primary keys, create() is used to perform POST operation and create new item, update() is used to perform PUT operation and updates the existing item, destroy() is used to delete the item

# class BlogViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Blog.objects.filter(is_public=True)
#         serialiazer = BlogSerializer(queryset, many=True)
#         return Response(serialiazer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Blog.objects.filter(is_public=True)
#         blog_list = get_object_or_404(queryset, pk=pk)
#         serializer = BlogSerializer(blog_list)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors)

#     def destroy(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response({"message": "Blog deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# ****  MODELVIEWSET  *****

# NOTE: Model Viewset allows us to perform CRUD operaton in same class and without us having to use any methods. It performs GET, GET by primary key pk,POST, PUT and DELETE. We can use look_up field if we want tp get item by some other field instead of primary key pk

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.filter(is_public=True)
#     serializer_class = BlogSerializer
#     # lookup_field = "slug"


# *****  *****

from rest_framework import generics
from .models import Blog, Category, BlogComment
from .serializer import BlogSerializer, CategorySerializer, BlogCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# we import this to use the DjangoFilterBackend in our generics views.
from django_filters.rest_framework import DjangoFilterBackend

# we import this to use the search filter and ordering filter in our generic views.
from rest_framework import filters

# this is out custom permission that we created.
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly


# use generics.ListAPIView when we want filter against the url
class BlogListCreateView(generics.ListCreateAPIView):
    # we modify the queryset by def get_queryset() when we are using url filtering or search filtering
    # queryset = Blog.objects.filter(is_public=True)

    # we use this query set instead of filtering by is_public because we are using filtering it using DjangoFilterBackend and we are using the is_public field to filter.
    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    # applying the DjangoFilterBackend in this generic view.
    # we can use multiple filters.
    # we need to mention the filters.SearchFilter in the filter_backend fields.
    # we need to mention the filters.OrderingFilter in the filter_backend fields.
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    # we need to mention the fields we want to search in the search_fields.
    search_fields = ['blog_title',
                     'blog_description', 'author__username', 'category__category_name']

    # we need to mention the fields on which we want to apply the filters.
    filterset_fields = ['category__category_name', 'is_public']

    # we need to mention the fields on which we want to order by. If we don't mention it then we can order by all the fields.
    ordering_fields = ['id', 'post_date']

    # NOTE: we are inheriting this from ListCreateAPIView which inherits list() method from mixins

    # REASON: If there are blogs then I want to show the blogs, if there are no blogs I want to show custom message

    # REMEMBER: We can inherit the methods we need to make custom changes. It is important to know what these Concrete classes use internally and what mixins are used.

    # method to get all the blogs. We inherit for custom changes.

    # FILTERING
    # applying filter against the url and filtering against query parameters
    # when we filter by url we override the get_queryset() method and we also use the generics.ListAPIView instead of generics.ListCreateAPIView
    # def get_queryset(self):  # we will take the username from the url
    #     # username = self.kwargs.get("username") #we take the username from the url
    #     # we take the username from the query in the url
    #     username = self.request.query_params.get("username")
    #     # get the username from author__username which will point to the author foreign key in the Blog model
    #     return Blog.objects.filter(author__username=username)

    # def list(self, request, *args, **kwargs): # when we use the DjangoFilterBackend we need remove ths def list()
    #     queryset = self.get_queryset()  # get all the objects from Blog model.
    #     serializer = BlogSerializer(
    #         queryset, many=True, context={"request": request})
    #     if queryset.exists():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"message": "No blogs found"}, status=status.HTTP_204_NO_CONTENT)

    # NOTE: We are inheriting the create() method from ListCreateAPIView which inherits it from mixins

    # REASON: When user creates a new blog he/she has to logged in and author field should be taken from logged in user.

    # method to create new blog. We inherit for custom changes.
    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(
            data=request.data, context={"request": request})

        # if we have error it will raise exception
        serializer.is_valid(raise_exception=True)

        # self.request.user will fetch the current logged in user and we set that user to the author field
        serializer.save(author=self.request.user)

        # this is used to set the success header
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAdminUserOrReadOnly]
    # lookup_field = "id"

    # NOTE: We want to get single object by the primary and retrieve() method is used to get single object. This is inherited in RetrieveUpdateDestroyAPIView by mixins.

    # REASON: We want custom logic to check item and it item is not found we want custom message.

    # this method is used to get single item by id(primary key)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # this will get the allocated serializer of this class which is Blog Serializer
        serializer = self.get_serializer(instance)

        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No blog found"}, status=status.HTTP_404_NOT_FOUND)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # using custom permission: if user is admin we will have permission to perform post CRUD operations else allow only ReadOnly
    permission_classes = [IsAdminUserOrReadOnly]
    # permission_classes = [IsAdminUser]

    # NOTE: We use the permission_classes field to handle the permission and IsAunthenticated allows only the loggedIn user to access this view.
    # permission_classes = [IsAuthenticated]

    # NOTE: We use the permission_classes field to handle the permission and IsAdminUser allows only the loggedIn user who is admin to access this view.
    # permission_classes = [IsAdminUser]

    # NOTE: We use the permission_classes field to handle the permission and IsAuthenticatedOrReadOnly allows only the loggedIn user to perform post, put and delte operation and not logged in users can only perform the get operation
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # this will give the queryset of this class
        serializer = CategorySerializer(
            queryset, many=True, context={"request": request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No categories found"}, status=status.HTTP_204_NO_CONTENT)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # using custom permission: if user is admin we will have permission to perform post CRUD operations else allow only ReadOnly
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


class BlogCommentListCreate(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]

    # NOTE: this  get_queryset() is inherited from GenericAPIView which is inherited in ListCreateAPIView
    # REASON: We want the particular blog by it's id and we want to add comment to that blog that is why we modify the get_queryset() method for our custom change.

    def get_queryset(self):  # get the blog object by id
        blog_id = self.kwargs.get("blog_id")
        return BlogComment.objects.filter(blog_id=blog_id)

    # NOTE: perform_create() is inherited from CreateModelMixin which is inherited in ListCreateAPIView
    # REASON: We want to check if a user has already commented on a blog, if it has commented then it will not be allowed to comment again and if it has not commented then it can comment and logged in user's details will be stored in the author field

    def perform_create(self, serializer):
        blog_id = self.kwargs.get("blog_id")
        blog = get_object_or_404(Blog, id=blog_id)  # get the blog object by id

        # check if logged in user has already commented or not.
        if BlogComment.objects.filter(blog=blog, author=self.request.user).exists():
            raise serializers.ValidationError(
                {"message": "You have already commented on this blog."})
        serializer.save(author=self.request.user, blog=blog)


class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):

        # get comment id from comment_id in url
        comment_id = self.kwargs.get("comment_id")

        # get the comment object by using the comment_id. comment contains the attributes of the model BlogComment
        comment = get_object_or_404(BlogComment, id=comment_id)
        # print(comment.comment_date)
        # print(comment.description)
        # print(comment.blog)
        # print(comment.blog.blog_description)
        # print(comment.blog.author)

        blog_id = self.kwargs.get("blog_id")  # get the blog id from the url
        if comment.blog.id != blog_id:  # check if the blog id inside the comment is same as the blog id
            raise serializers.ValidationError(
                {"message": "This comment is not related to the requested blog"})
        return comment

    def put(self, request, *args, **kwargs):  # allow only the owner to edit the blog

        # get the comment object that contains the attributes of BlogComment model.
        comment = self.get_object()
        if comment.author != request.user:
            raise serializers.ValidationError(
                {"message": "You are not authroized to perform this action."})
        return super().put(request, *args, **kwargs)

    # allow only the owner to delete the blog.
    def delete(self, request, *args, **kwargs):

        # get the comment object that contains the attributes of BlogComment model.
        comment = self.get_object()
        if comment.author != request.user:  # check to see the comment.author is same as logged in user or not
            raise serializers.ValidationError(
                {"message": "You are not authorized to perform this action."})
        return super().delete(request, *args, **kwargs)
