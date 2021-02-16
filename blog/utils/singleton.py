class Singleton(type):
    _class_instance_mapper = dict()

    def __call__(cls, *args, **kwds):
        if cls not in cls._class_instance_mapper:
            new_instance = super().__call__(*args, *kwds)
            cls._class_instance_mapper[cls] = new_instance

        return cls._class_instance_mapper[cls]
