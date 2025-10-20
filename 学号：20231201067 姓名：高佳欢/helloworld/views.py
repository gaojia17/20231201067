from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    """简单的helloworld视图函数"""
    return HttpResponse("<h1>Hello, World! </h1><p>这是高佳欢(学号:20231201067)</p>")



def index(request):
    """首页视图"""
    return HttpResponse("""
    <html>
    <head>
        <title>Django Helloworld 测试</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            a { color: #007bff; text-decoration: none; margin: 10px; display: inline-block; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Django Helloworld 视图测试</h1>
        <p>这是高佳欢(学号:20231201067)创建的Django视图测试应用。</p>
        <div>
            <a href="/hello/">Hello World</a>
            <a href="/hello/高佳欢/">Hello 高佳欢</a>
            <a href="/hello/Django/">Hello Django</a>
        </div>
    </body>
    </html>
    """)