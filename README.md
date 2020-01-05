# 数据库大作业
- src 文件夹包含所有源码
- doc 文件夹包含所有报告，包括小组报告和个人报告
- sub_videos 文件夹包含所有功能的视频展示片段以及展示引导PPT
- total_video 文件夹包含演示网站系统功能的视频
- 实现成果  
    在命令行中cd到RAILWAY_TICKET_BOOKSYSTEM目录下，运行  
    > python3 manage.py runserver  

    (前提是python3中已配置好了Django1.10.6，pytz等环境)  
    然后打开浏览器访问[http://127.0.0.1:8000/](http://127.0.0.1:8000/)将会来到预订系统的欢迎界面！  
    如图：  
    ![](doc/9.png)   
    在输入框输入出发城市，到达城市以及日期  
    <img src="doc/11.png" style="zoom: 50%;" />  
    <img src="doc/10.png" style="zoom: 50%;" />  
    点击let's go按钮，即会跳转到查询结果页面。  
    若没有往返两地的列车，将显示以下页面  

    ![](doc/22.png) 
    若有往返两地的列车，则显示以下页面  
    默认的车票信息按照价格升序排列，在价格旁边还有满座率等信息。  

    ![](doc/13.png)   
    用鼠标点击绿色按钮出发时间，红色按钮到达时间，或者橙色按钮价格将会按照该列属性从小到大进行排序。  
    如图按照出发时间排序。  
    ![](doc/12.png)   
    
    可以看到右上角显示欢迎 先生/女士，没有用户名，说明尚未登录。  
    所以点击订票会直接跳转到登录页面。  
    ![](doc/14.png)   
    若还没有账号，点击下方的click here进行注册。   
    ![](doc/15.png)    
    输入username等信息点击submit即可进行注册。  
    注册成功后即会直接跳转回刚刚的查询车票界面。  
    ![](doc/16.png)   
    再次点击订票，  
    ![](doc/17.png)   
    点击确认即可进行订票，并弹出订票成功信息。  
    ![](doc/18.png)   
    此时，点击右上角的个人中心可以查看自己的订票信息。  
    ![](doc/19.png)   
    点击退票  
    ![](doc/20.png)    
    点击确定  
    该条订票记录将直接消失  
    ![](doc/21.png)     
    点击右上角的购票将跳转回查询页面  
    ![](doc/22.png)    
    若预订已经预订过的车次，将会跳转至以下页面  
    ![](doc/24.png)   
    点击右上角的退出可退出登录  
    ![](doc/23.png)    
    修改网页地址栏在booksystem后加上admin，将进入本预订系统的后台  
    ![](doc/25.png)   
    输入admin的账号密码即可登录后台  
    ![](doc/26.png)   
    点击users或者railways旁边的add，change可直接跳转到添加，修改的页面  
    点击users可以查看本系统的用户以及管理员  
    点击Railways即可查看所有火车的信息，并可进行增改删查的操作  
    右边的Recent actions可查看管理员的近期操作日志。  
    ![管理员表](doc/27.png)   
    如上为管理员表，点击右侧窗口按钮可进行切换为用户表或者查看用户以及管理员状态(是否active)    
    ![用户表](doc/28.png)  
    如上为用户表   
    ![](doc/35.png)    
    选择actions栏选择用户或管理员点击go即可进行删除操作   
    点击add user即可添加管理员  
    ![](doc/36.png)    
    点击右上角的change password还可以跳转至修改密码界面  
    ![](doc/37.png)    
    

    点击左边的home回到首页
    点击Railways查看所有车次信息表  
    点击右上角按钮可添加车次  
    ![](doc/29.png)   
    点击add railway后跳转至以下页面，填入信息点击下面save可进行保存    
    ![](doc/34.png)   
    选择delete点击go可直接删除该车次  
    ![](doc/30.png)   
    点击左边车次name即可直接跳转至修改车次信息页面  
    ![](doc/31.png)   
    可在左侧修改后点击下面的save保存   
    ![](doc/32.png)   
    也可点击右上角的history查看历史修改记录    
    ![](doc/33.png)   
    点击log out即可退出管理员登录  
    ![](doc/38.png)  
    点击右上角的view site可回到[http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
    重新查询后，点击个人中心  
    ![](doc/39.png)   
    可看到此时用户为admin管理员身份  
    点击个人中心，即可查看本系统的年，月，星期利润以及所有的订单列表  
    ![](doc/40.png)   