import sys
import os



## 冻结路径

def app_path():
    ## """Returns the base application path."""
    if hasattr(sys, 'frozen'):
    # Handles PyInstaller
        return os.path.dirname(sys.executable)      #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)    #没打包前的py目录



## 其中的app_path()函数返回一个程序的执行路径，为了方便我们将此文件放在项目文件的根目录，通过这种方式建立了相对路径的关系。
# 源代码中使用路径时，以app_path()的返回值作为基准路径，其它路径都是其相对路径。


# print(app_path())