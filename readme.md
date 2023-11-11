# 值班管理系统

### 思路

```  text
值班安排分类 带班班员相互关系起来 一个科室不能一起值班 人员数不等 两合一（白晚班） 导出（counter + 1）              
白班班员：        
晚班班员：
晚班班员：
晚班带班：

```

| 安排分类 | 带班班员相互关系 | 一个科室不能一起值班 | 人员数不等 | 两表合一 | 导出和计数器 |
|------|----------|------------|-------|------|--------|
| 白班班员 |          |            |       |      |        |
| 白班带班 |          |            |       |      |        |
| 晚班班员 |          |            |       |      |        |
| 晚班带班 |          |            |       |      |        |

### 环境

- Mac
- Pycharm 2022.3.1
- Python 3.9.13
- Django 4.1.5
- Sqlite3
- Bootstrap 5.3.0
- Bootstrap-Icons 1.10.3

### 安装依赖

```shell
# 离线安装
pip install --no-index --find-links=PIPDIR -r requirements.txt

# 线上安装
pip install -r requirements.txt
```

### 创建超级管理员

```shell
# 创建超级管理员
python manage.py createsuperuser


```

### 其他

#### 支持一下数据库：

* MySQL
* Orcale
* PostgreSQL
* MariaDB
* SQLite

查看相关文档地址：https://docs.djangoproject.com/zh-hans/4.1/ref/databases/

### 演示图
![](./演示图/截屏2023-02-03%2017.14.18.png)
![](./演示图/截屏2023-02-03%2017.15.37.png)
![](./演示图/截屏2023-02-03%2017.16.01.png)
![](./演示图/截屏2023-02-03%2017.16.36.png)
![](./演示图/截屏2023-02-03%2017.42.50.png)

### 赞赏

#### Gitee链接：https://gitee.com/hayratjan

#### Github链接 https://github.com/hayratjan

<img height="320" src="https://img-blog.csdnimg.cn/40cc4e962df540d38729cdad5870788a.png" width="320"/>