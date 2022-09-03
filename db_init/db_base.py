import pymysql
import yaml
import os


class DbMySql:
    def db_connect(self, key):
        '''
        传入数据库配置文件的文件名，带后缀
        :param FileName:
        :return: dict
        '''
        # 获取当前脚本所在的文件夹路径
        curPath = os.path.dirname(os.path.realpath(__file__))
        # 获取yanml文件路径
        yamlPath = os.path.join(curPath, 'db_conn.yaml')
        # with open方法打开文件，读取内容
        with open(yamlPath, 'r', encoding='utf-8') as f:
            file = f.read()
            data = yaml.safe_load(file)
            db_data = data[key]
            print("数据库联接配置为:", db_data)
        # 数据库联接操作
        conn = pymysql.connect(user=db_data.get('user'), password=db_data['password'], host=db_data['host'],
                               port=db_data['port'], database=db_data['database'])
        # 创建游标对象
        cur = conn.cursor()
        try:
            cur.execute("show databases")
        except Exception as e:
            print("数据库联接失败：", e)
        else:
            print("数据库联接成功！")
        # 关闭游标、联接
        cur.close()
        conn.close()


DbMySql().db_connect('Mysql_Database')
