from haystack import indexes

from .models import Resource


class PersonIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    intro_text = indexes.CharField(model_attr='intro_text')
    full_text = indexes.CharField(model_attr='full_text')
    suggestions = indexes.FacetCharField()
    content_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Resource

    def prepare(self, obj):
        prepared_data = super().prepare(obj)
        prepared_data['suggestions'] = prepared_data['text']
        return prepared_data