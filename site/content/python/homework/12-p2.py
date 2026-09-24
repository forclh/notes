class PluginMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != "Plugin":
            mcs.registry[name] = cls
        return cls


class Plugin(metaclass=PluginMeta):
    pass


class ImagePlugin(Plugin):
    pass


class TextPlugin(Plugin):
    pass


class VideoPlugin(Plugin):
    pass


print(PluginMeta.registry)
# 应该输出类似：{'ImagePlugin': <class '__main__.ImagePlugin'>, 'TextPlugin': <class '__main__.TextPlugin'>}
