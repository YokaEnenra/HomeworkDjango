from rest_framework.pagination import PageNumberPagination


class CustomSubjectPagination(PageNumberPagination):
    page_size = 2
