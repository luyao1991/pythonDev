# coding:utf-8


class Singleton(object):
    # 如果类中未创建实例，则为该类创建一个实例并返回，否则直接返回已存在的实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


#  使用修饰器实现单例模式
def singleton(cls, *args, **kw):
    _instance = {}

    def get_instance():
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return get_instance


@singleton
class Person(object):
    pass


if __name__ == '__main__':
    # s1 = Singleton()
    # s2 = Singleton()
    # print(id(s1))
    # print(id(s2))
    s1 = Person()
    s2 = Person()
    print(id(s1))
    print(id(s2))
