from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "description",
    )
    list_editable = (
        "year",
        "description",
    )
    search_fields = (
        "name",
        "year",
        "genre",
        "category",
    )
    list_filter = ("name",)
    list_display_links = ("name",)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    list_editable = ("slug",)
    search_fields = ("name",)
    list_filter = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    list_editable = ("slug",)
    search_fields = ("name",)
    list_filter = ("name",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "author",
        "score",
        "pub_date",
    )
    list_editable = (
        "title",
        "text",
    )
    search_fields = (
        "title",
        "text",
    )
    list_filter = ("author",)
    list_display_links = ("author",)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "author",
        "pub_date",
        "review",
    )
    list_editable = ("text",)
    search_fields = (
        "text",
        "review",
    )
    list_filter = (
        "text",
        "review",
        "author",
    )
    list_display_links = (
        "review",
        "author",
    )


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
