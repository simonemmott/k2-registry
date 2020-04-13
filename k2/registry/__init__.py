

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
    
    def register(self, name=None):
        pass
    
    def retrieve(self, name):
        pass
    
    def registration(self):
        pass
    

registry = Registry()

def register(name:None):
    return registry.register(name)

def retrieve(name):
    return registry.retrieve(name)

