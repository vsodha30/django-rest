from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    #snippets = serializers.RelatedField(queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
#Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.