from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "slug")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    genre = GenreSerializer(many=True, required=True)
    rating = serializers.IntegerField(read_only=True, default=None)

    class Meta:
        fields = "__all__"
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field="slug",
        many=True,
        queryset=Genre.objects.all(),
        allow_null=False,
        allow_empty=False,
    )
    rating = serializers.IntegerField(default=None, read_only=True)

    class Meta:
        fields = "__all__"
        model = Title

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context["view"].action
        if action not in ["list", "retrieve"]:
            representation.pop("rating")
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Review
        fields = ["id", "text", "author", "score", "pub_date"]
        read_only_fields = ("title", "pub_date")

    def validate(self, data):
        request = self.context["request"]
        title_id = self.context["view"].kwargs.get("title_id")
        author = request.user

        if (
            request.method == "POST"
            and Review.objects.filter(
                title_id=title_id, author=author
            ).exists()
        ):
            raise serializers.ValidationError(
                "Вы уже оставили отзыв на это произведение."
            )

        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Comment
        fields = ["id", "text", "author", "pub_date"]
        read_only_fields = ("review",)
