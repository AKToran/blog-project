from django.shortcuts import render
from post.models import Post

def home(request):
    data = Post.objects.all()
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    return render(request, 'index.html', {'data': data})
