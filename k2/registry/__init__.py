
registrations = []

def clear_registrations():
    global registrations
    registrations = []

def registration():
    
    def decorator(func):
        registrations.append(func)
        return func
        
    return decorator

class Registry(object):
    def __init__(self):
        self.registrations = []
        self.registry = {}
        
    def clear_registrations(self):
        self.registrations.clear()
        
    def apply_registrations(self, item):
        
        for registration in registrations:
            registration(item)
            
        for registration in self.registrations:
            registration(item)
        
    
    def register(self, name=None):
        
        def decorator(item):
            self.apply_registrations(item)
            if name:
                self.registry[name] = item
            else:
                if hasattr(item, '__name__'):
                    self.registry[item.__name__] = item
                elif hasattr(item, '__class__'):
                    self.registry[item.__class__.__name__] = item
                elif hasattr(item, '__getitem__'):
                    if '__name__' in item:
                        self.registry[item['__name__']] = item
                    elif 'name' in item:
                        self.registry[item['name']] = item
                    elif 'id' in item:
                        self.registry[item['id']] = item
                    elif 'ref' in item:
                        self.registry[item['ref']] = item
            return item
        
        return decorator
    
    
    def retrieve(self, name):
        return self.registry.get(name, None)
    
    
    def registration(self):
        
        def decorator(func):
            self.registrations.append(func)
            return func
        
        return decorator
    
    def __setitem__(self, key, item):
        self.registry[key] = item

    def __getitem__(self, key):
        return self.registry[key]

    def __repr__(self):
        return repr(self.registry)

    def __len__(self):
        return len(self.registry)

    def __delitem__(self, key):
        del self.registry[key]

    def clear(self):
        return self.registry.clear()

    def copy(self):
        reg = Registry()
        reg.registrations.extend(self.registrations)
        reg.registry = self.registry.copy()
        return reg

    def has_key(self, k):
        return k in self.registry

    def keys(self):
        return self.registry.keys()

    def values(self):
        return self.registry.values()

    def items(self):
        return self.registry.items()

    def __contains__(self, item):
        return item in self.registry

    def __iter__(self):
        return iter(self.registry)

    def __unicode__(self):
        return unicode(repr(self.registry))
    

registry = Registry()

def register(name:None):
    return registry.register(name)

def retrieve(name):
    return registry.retrieve(name)

