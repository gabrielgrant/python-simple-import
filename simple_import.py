def import_item(x):
    """ Imports and returns the object specified by a given dotted path """
    mod_name, cls_name = x.rsplit('.', 1)
    return from_x_import_y(mod_name, cls_name)

def from_x_import_y(x, y):
    """ from mod_name import object_name"""
    module = __import__(x, fromlist=x.rsplit('.', 1)[0])
    return getattr(module, y)
