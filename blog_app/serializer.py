# *****  Learning  *****

# from rest_framework import serializers
# from .models import Blog, Category


# this method is used in the validators below
# def blog_title_valid(value):
#     if len(value) < 4:
#         raise serializers.ValidationError(
#             "Blog title must contain atleast 4 characters.")
#     else:
#         return value

#  *** simple SERIALIZER ***

# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     post_date = serializers.DateField()
#     is_public = serializers.BooleanField()
#     slug = serializers.CharField()

#     # When we use Serializer we need to crete the create and update function in order to post new data and update existing data. Get function and delete function need not be created.

#     def create(self, validated_data):  # this is created so that we can post new data from our views
#         return Blog.objects.create(**validated_data)

#     def update(self, instance, validated_data):  # this is created to perform update operation
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get(
#             "description", instance.description)
#         instance.post_date = validated_data.get(
#             "post_date", instance.post_date)
#         instance.is_public = validated_data.get(
#             "is_public", instance.is_public)
#         instance.slug = validated_data.get("slug", instance.slug)
#         instance.save()
#         return instance

# ***  ***


# *** MODEL SERIALIZER ***
# class BlogSerializer(serializers.ModelSerializer):
# this is for making the validation. We pass the field like this on which we want to use validator
# blog_title = serializers.CharField(validators=[blog_title_valid])

# SerializerMethodField() is used to pass some extra things that are derived for model but are not present in model
# len_blog_title = serializers.SerializerMethodField()

# doing this so that author cannot be changed
# author = serializers.StringRelatedField(read_only=True)

# class Meta:
# model = Blog
# fields = ["blog_title", "blog_description"]
# fields = "__all__"
# exclude = ["slug"]

# we create this method as get_<name_of_thevariable_that_strores_SerializerMethodField>
# def get_len_blog_title(self, object):
#     # it calulates the length of the blog title
#     return len(object.blog_title)

# Validation is triggered when we call the self.validate() method in our views

# Field Level Validation
# def validate_blog_title(self, value):
# if len(value) < 4:
#     raise serializers.ValidationError(
#         "Blog title must contain atleast 4 characters.")
# else:
#     return value

# Object level validation
# def validate(self, data):
#     if data["blog_title"] == data["blog_description"]:
#         raise serializers.ValidationError(
#             "Blog title and Blog description cannot be same.")
#     else:
#         return data


# class CategorySerializer(serializers.ModelSerializer):

# *** NESTED SERIALIZER ***
# we provide the same name of the field as we used in category model

# category_name = serializers.CharField()

# now we use the name of the field category which must have the same name as foreign key field in the Blog Model and we pass the Blog Serializer. This will give us the all the blogs in each category.
# this will give all the information of the data and will contain all the fields

# category = BlogSerializer(many=True, read_only=True)

# category = serializers.StringRelatedField(
#     many=True)  # this will only return the blog title as we mentioned in __str__ method in BlogModel

# category = serializers.PrimaryKeyRelatedField(
#     many=True, read_only=True)  # it will only give the primary keys each blog in the category

# category = serializers.HyperlinkedRelatedField(
#     many=True,
#     read_only=True,
#     view_name="blog_detail")  # it will give the links of each blog in the category and view_name must be the same as the name provided in the url

# category = serializers.SlugRelatedField(
#     many=True, read_only=True, slug_field="slug")  # it will give the slug of each blog in the category

# ***  ***

# class Meta:
#     model = Category
#     exclude = ["id"]
#     fields = "__all__"


# ***  ***


# *** HyperLinkModel Serializer ***

# The primary key will be replaced by the url of the category

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     category = BlogSerializer(many=True, read_only=True)  # nested serializer

#     class Meta:
#         model = Category
#         fields = "__all__"

# *****  *****

from rest_framework import serializers
from .models import Blog, Category, BlogComment
from django.urls import reverse


class BlogCommentSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source="author.username")
    # author = serializers.StringRelatedField(read_only=True)
    blog = serializers.StringRelatedField(read_only=True)
    # blog = BlogSerializer(read_only=True) #nested serializer

    class Meta:
        model = BlogComment
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    # field to get the comments of each blogs. This will use the get_comments() method below.
    comments = serializers.SerializerMethodField()
    
    category = serializers.CharField()

    class Meta:
        model = Blog
        fields = "__all__"

    def validate_blog_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError(
                "Blog title must contain atleast 4 characters.")
        else:
            return value

    def validate(self, data):
        if data["blog_title"] == data["blog_description"]:
            raise serializers.ValidationError(
                "Blog title and Blog description cannot be same.")
        else:
            return data

    def get_comments(self, obj):  # this method is used the serializer method field above
        comments = BlogComment.objects.filter(blog=obj)[:3]  # 3 comments
        request = self.context.get("request")  # get the request

        # using the BlogCommentSerializer and nesting it
        # request.build_absolute_uri(reverse("blog_comment_list", kwargs={"blog_id": obj.id})) is used to create the link that will take to all the blog comments and point to the url with name as blog_comment_list
        return {
            "comments": BlogCommentSerializer(comments, many=True).data,
            "all_comments_link": request.build_absolute_uri(reverse("blog_comment_list", kwargs={"blog_id": obj.id}))
        }


class CategorySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField()

    # nested serializer to give blogs belonging to a particular category.
    category = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        # exclude = ["id"]
        fields = "__all__"
