def import_class(name):
    module = name.split('.')[:-1]
    klass = name.split('.')[-1:].pop()
    module = __import__('.'.join(module), fromlist=[klass])
    klass = getattr(module, klass)
    return klass
