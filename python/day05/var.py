# coding:utf-8

class Phone(object):
    info = 1

    def send_short_message(self, message):
        """
        :param message:
        :return:
        """
        print(self.info)
        self.info += 1
        print(self.info)
        print(message)

    @classmethod
    def information(cls, message):
        print(id(cls.info))
        print(cls.info)
        cls.info += 1
        print(cls.info)
        print(message)


if __name__ == '__main__':
    # Phone.information()
    phone1 = Phone()
    # phone1.send_short_message("我是第一个手机！")
    phone1.information("我是第一个手机！")
    print('########')
    phone2 = Phone()
    # phone2.send_short_message("我是第二个手机！")
    phone2.information("我是第二个手机！")
