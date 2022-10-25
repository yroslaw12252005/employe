from django.contrib import admin
from .models import Articles,Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

#Изменить цвет в админки и убрать надпись django
class ArticlesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Articles
        fields = '__all__'

class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ("id", "title","author","created_at","is_published",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
