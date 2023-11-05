from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)