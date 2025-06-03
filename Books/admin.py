from django.contrib import admin

from .models import Book,BookLoan

admin.site.register(Book)
admin.site.register(BookLoan)

