import  os
from configparser import ConfigParser
#使用相对目录确定文件位置
conf_dir=os.path.dirname(__file__)
conf_file=os.path.join(conf_dir,'config.ini')
print(conf_file)
#继承ConfigParser，将结果转为dict
class MyParser(ConfigParser):
    def as_dict(self):
        d=dict(self._sections)
        for k in d:
            d[k]=dict(d[k])
            return d

#读取所有配置，以字典方式输出
def get_all_conf():
    config=MyParser()
    result={}
    if os.path.isfile(conf_file):
        try:
            config.read(conf_file,encoding='utf-8')
            result=config.as_dict()
        except OSError:
            raise ValueError("Read config file failed: %s" % OSError)
        return  result

#将各项配置读取出来，放到变量中，后续其它文件直接引用这些变量
config_all=get_all_conf()
sys_config=config_all['sys']
smtp_config=config_all['smtp']
print(sys_config)
print(smtp_config)
print(smtp_config['host'])
log_config=config_all['log']
print(log_config)
