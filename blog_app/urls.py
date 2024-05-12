# *****  For learning  *****

# from django.urls import path, include
# from . import views

# importing router when we use viewset
# from rest_framework import routers

# NOTE: We must use routers when we are using Viewset or Model Viewset

# router = routers.DefaultRouter()

# router.register(r"blogs", views.BlogViewSet, basename="blogs")

# urlpatterns = [
# FUNCTION BASED VIEWS
# path("blog_list/", views.blog_list, name="blog_list"),
# path("blog_detail/<int:pk>/", views.blog_detail, name="blog_detail")

# CLASS BASED VIEWS

# Blogs urls
#     path("blog_list/", views.BlogListView.as_view(), name="blog_list"),
# path("blog_detail/<int:pk>/",
#      views.BlogListDetailView.as_view(), name="blog_detail"),

# category urls
#     path("category_list/", views.CategoryListView.as_view(), name="category_list"),
#     path("category_detail/<int:pk>/", views.CategoryDetailView.as_view(),
#          name="category-detail"),

# GENERIC VIEW URL

#   path("blog_list_generic/", views.BlogListGenericView.as_view(), name="blog_list"),
#     #     path("blog_detail/<int:pk>/",
#     #          views.BlogDetailGenericView.as_view(), name="blog_detail"), # path to get update and delete a blog by primary key pk
#     path("blog_detail/<str:slug>/",
#          views.BlogDetailGenericView.as_view(), name="blog_detail")  # this is the path to get update and delete a blog by the slug

# CONCRETE VIEW CLASS URLs

#     path("blog_list_create/", views.BlogCreateConc.as_view(), name="blog_list"),
#     path("blog_list_all/", views.BlogListConc.as_view(), name="blog_list_all"),
#     path("blog_retrieve/<str:slug>",
#          views.BlogRetrieveConc.as_view(), name="blog_retrieve"),  # get single blog by the slug
#     path("blog_delete/<int:pk>", views.BlogDeleteConc.as_view(), name="blog_delete")
# path("blog_list/", views.BlogListConc.as_view(), name="blog_list"),
# path("blog_detail/<int:pk>/", views.BlogDetailConc.as_view(), name="blog_detail")

# url for viewset
# path("", include(router.urls))

# ]

# *****  *****

from django.urls import path
from . import views

urlpatterns = [
        path("blog_list/", views.BlogListCreateView.as_view(), name="blog_list"),
    #     path("blog_list/<str:username>/",
    #          views.BlogListCreateView.as_view(), name="blog_list"),  # this path is used for filter against the url
    # this path is used for filter against the query
    # example: http://localhost:8000/api/blog/blog_list/?username=admin
#     path("blog_list/", views.BlogListCreateView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),

    path("category_list/", views.CategoryListCreateView.as_view(),
         name="category_list"),
    path("category_detail/<int:pk>/",
         views.CategoryDetailView.as_view(), name="category_detail"),

    path("blog_comment_list/blog/<int:blog_id>/",
         views.BlogCommentListCreate.as_view(), name="blog_comment_list"),

    path("blog_comment_detail/blog/<int:blog_id>/comment/<int:comment_id>/",
         views.BlogCommentDetailView.as_view(), name="blog_detail"),
]
