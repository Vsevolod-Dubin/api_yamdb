from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .constants import NAME_MAX_LENGTH
from .validators import validate_year

User = get_user_model()


class GroupBaseModel(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        verbose_name="Название",
        help_text="Название элемента",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        help_text="Уникальный фрагмент URL-адреса",
    )

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Category(GroupBaseModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(GroupBaseModel):
    class Meta:
        verbose_name = ("Жанр",)
        verbose_name_plural = "Жанры"


class Title(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Произведение",
        help_text="Название произведения",
    )
    year = models.SmallIntegerField(
        validators=[validate_year],
        verbose_name="Год",
        help_text="Используйте формат для года <YYYY>",
        db_index=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Краткое содержание произведения",
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        "Genre",
        related_name="titles",
        through="GenreTitle",
        verbose_name="Жанр",
        help_text="Название жанра, к которому относится произведение",
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        help_text="Название категории, к которому относится произведение",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class CreatedModel(models.Model):
    pub_date = models.DateTimeField("дата создания", auto_now_add=True)

    class Meta:
        abstract = True


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="titles",
        verbose_name="Произведение",
    )
    genre = models.ForeignKey(
        Genre,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="genres",
        verbose_name="Жанр",
    )

    class Meta:
        ordering = ("title", "genre")
        verbose_name = "Произведение и жанр"
        verbose_name_plural = "Произведения и жанры"


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Название произведения",
    )
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор отзыва",
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, "Оценка не может быть меньше 1"),
            MaxValueValidator(10, "Оценка не может быть больше 10"),
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_review"
            )
        ]

    def __str__(self):
        return f"Отзыв {self.author} на {self.title}"


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Отзыв",
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий {self.author} к отзыву {self.review}"
