import hashlib
import os


def get_file_md5(file_name):
    # 计算文件的md5
    m = hashlib.md5()  # 创建md5对象
    if os.path.isfile(file_name):
        with open(file_name, 'rb') as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                m.update(data)  # 更新md5对象
        return m.hexdigest()  # 返回md5对象
    else:
        return False


def get_str_md5(content):
    # 计算字符串md5
    m = hashlib.md5(content.encode())  # 创建md5对象
    return m.hexdigest()


if __name__ == '__main__':
    ch = input('请输入需要计算摘要的原文本内容：')
    print(get_str_md5(ch))
    # file = input('请输入文件地址：')
    # print(get_file_md5(file))
