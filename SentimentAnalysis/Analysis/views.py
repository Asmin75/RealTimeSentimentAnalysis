from django.shortcuts import render
from nltk import accuracy
from .forms import UserInput
from .classifier import get_classifier
from .preprocess import process
from .preprocess import create_word_features


def index(request):
    user_input = UserInput()
    return render(request, "Analysis/index.html", {'Enter_Input': user_input})


def analyse(request):
    user_input = UserInput(request.GET or None)
    if request.GET and user_input.is_valid():
        Enter_Input = user_input.cleaned_data['Message']
        print(Enter_Input)
        demo = process(Enter_Input)
        demo1 = create_word_features(demo)
        data, data_accuracy = get_classifier()
        demo2 = ('The sentiment is ' + data.classify(demo1))
        return render(request, "Analysis/index.html", {'msg': demo2, 'accuracy': data_accuracy, 'Enter_input': Enter_Input})
    return render(request, "Analysis/index.html", {'Enter_Input': user_input})



