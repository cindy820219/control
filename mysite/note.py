1. create new django project
    $ django-admin.py startproject [project_name]

2. create new app
    $ python3 manage.py startapp [app_name]

    '''
    creat new project then create new app 
    project 和 app 關係：
    一個 project 一般包含 多個 app ，
    一個 app 也可以用在多個 project 中。
    
    djangogirls
    ├── mysite             (project)
    |       __init__.py
    |       settings.py
    |       urls.py
    |       wsgi.py
    ├── manage.py
    └── blog               (app)
            __init__.py
            admin.py
            models.py
            tests.py
            views.py
    '''

3. 同步更改数据库表或字段
    1. 創更改的文件
    $ python3 manage.py makemigrations

    2. 將生成的py文件應用到數據庫
    $ python3 manage.py migrate

4. 使用伺服器
    $ python3 manage.py runserver
    # ^C
    # 當顯示端被佔用時，可用其它端口：
    $ python3 manage.py runserver 8001
    $ python3 manage.py runserver 9999

    # 監聽機器所有可用ip（電腦可能有多個內網ip或多個外網ip）
    $ python3 manage.py runserver 0.0.0.0:8000
    # 如果是外網或者區域網路電腦上可以用其它電腦查看開發服務器
    # 訪問對應的 ip 加端口，比如 http://172.16.20.2:8000

    '''
    ERROR : That port is already in use
    $ sudo fuser -k 8000/tcp
    '''

5. 清空數據庫
    $ python3 manage.py flush

6. create super user
    $ python3 manage.py createsuperuser
    # 按照提示输入用戶名和對應的密碼（郵箱可以留空，用戶名和密碼必填）
    # 修改用戶密碼
    $ python3 manage.py changepassword [username]

7. 導出數據 導入數據
    $ python3 manage.py dumpdata appname > appname.json
    $ python3 manage.py loaddata appname.json

8. Django interactive (!!!!!!!!)
    $ python3 manage.py shell

9. database shell
    $ python3 manage.py dbshell
    
10. More command !
    $ python3 manage.py

11. interactive 
    $ python3 manage.py shell

12. 模板表 (template): (index.html)
    名稱   描述              特徵              範例
    ------------------------------------------------------------
    變量   內容填到模板的位置                    {{ sum }}
    標籤   提供試圖邏輯                         {% if real %}  
    註釋   註釋                                {# this is comment}
    文字   純文字             包含 html 標籤     just text

13. highchart 
    http://www.cnblogs.com/4admin2root/archive/2012/09/06/2673735.html    
    https://www.highcharts.com/demo/dynamic-update

14. template under app
    ### add template/home.html
    ### urls.py ; add new 
    from learn import views as learn_views
    url(r'^$', learn_views.home, name='home'),

    ### template/home.html
    {% for i in TList %}
    {{ i }}
    {% endfor %}
    
    ### view.py
    def home(request):
    TList = ["aaa", "bb", "c"]
    return render(request, 'home.html', {'TList': TList})
    
    # for 
    forloop.counter     索引从 1 开始算
    forloop.counter0    索引从 0 开始算
    forloop.revcounter  索引从最大长度到 1  
    forloop.revcounter0 索引从最大长度到 0
    forloop.first       当遍历的元素为第一项时为真
    forloop.last        当遍历的元素为最后一项时为真
    forloop.parentloop  用在嵌套的 for 循环中，

    # 邏輯判斷
    http://code.ziqiangxuetang.com/django/django-template2.html
    
15. db ---> models ! http://code.ziqiangxuetang.com/django/django-models.html
    create app
    # /settings.py
    INSTALLED_APPS
    # /models.py
    class ():
    # connet to db , cd to project ./manage.py
    python3 manage.py makemigrations
    python3 manage.py migrate
    # complete !
    Running migrations:
    Applying people.0001_initial... OK

    # python3 manage.py shell
    from people.models import Person
    Person.objects.create(name="WeizhongTu", age=24)
        <Person: Person object>
    Person.objects.get(name="WeizhongTu")

16. forms
    
    
