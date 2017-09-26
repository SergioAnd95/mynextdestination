from haystack import indexes

from .models import Resource


class PersonIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    intro_text = indexes.CharField(model_attr='intro_text')
    full_text = indexes.CharField(model_attr='full_text')

    def get_model(self):
        return Resource