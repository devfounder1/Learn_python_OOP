class Thread_data:
    __shared_attrrs = {
        'name' : 'thread_1 ',
        'data' : {},
        'id' : 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrrs

th = Thread_data()

th_1 = Thread_data()

th_1.id = 3 ## единое для всех th

th.attr_new = 'new attr' ## добавится и в th_1
