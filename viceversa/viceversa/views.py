from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    orginal_text = request.GET['usertext']
    reverse_text = orginal_text[::-1]
    words = orginal_text.split()
    number_words = str(len(words))
    return render(request, 'reverse.html', {'new_text':reverse_text,'number': number_words})
