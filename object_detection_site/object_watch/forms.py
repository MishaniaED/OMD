from django import forms


class ObjectRecognitionForm(forms.Form):
    camera = forms.ChoiceField(label='Выберите камеру:', choices=[('camera1', 'Камера 1')], required=False,
                               widget=forms.Select(attrs={'class': 'form-control', 'id': 'camera-selector'}))
    frames = forms.BooleanField(label='Рамки вокруг распознаных объектов', required=False,
                                widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'defaultCheck1'}))

