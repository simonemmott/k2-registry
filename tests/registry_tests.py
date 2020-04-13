from unittest import TestCase
from unittest.mock import patch
import inspect
from k2.registry import Registry
import k2.registry

class RegistryTests(TestCase):
    
    def setUp(self):
        self.registry = Registry()
        
    
    # It should include a registrations list with initial value []
    def test_registry_includes_registrations_list(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'registrations'), 
                'The Registry class does not include the registrations attribute'
            )
        self.assertEqual(
                registry.registrations, 
                [], 
                'The registrations list if not an empty list'
            )
    
    
    # It should include a method to clear the registrations
    def test_registry_includes_clear_registrations(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'clear_registrations'), 
                'The Registry class does not include the clear_registrations attribute'
            )
        self.assertTrue(
                callable(registry.clear_registrations), 
                'The clear_registrations member is not callable'
            )
        registry.registrations = ['XXX']
        registry.clear_registrations()
        self.assertEqual(
                registry.registrations, 
                [], 
                'The registrations list was not cleeared'
            )
        
    
    # It should include a registration decorator method which adds registrations to the registrations field
    def test_registry_includes_registration_decorator(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'registration'), 
                'The Registry class does not include the registration attribute'
            )
        self.assertTrue(
                callable(registry.registration),
                'The registration attribute is not callable'
            )
        registration = registry.registration()
        self.assertTrue(
                callable(registration), 
                'The registration method is not a decorator'
            )
        def test_registration(item):
            item['foo'] = 'bar'
            return item
        
        registration(test_registration)
        
        self.assertTrue(
                test_registration in registry.registrations, 
                'The registration decorator does not add registrations the registrations attribute'
            )
    
    
    # It should include an empty  dictionary named registry
    def test_registry_includes_registry_instance(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'registry'), 
                'The Registry class does not include the registry attribute'
            )
        self.assertEqual(
                {},
                registry.registry,
                'The registry attribute is not an empty dictionary'
            )
        
    
    # It should include a register decorator method which calls the apply registrations 
    # method and adds the registered item to registry dictionary
    def test_registry_includes_register_decorator(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'register'), 
                'The Registry class does not include the register attribute'
            )
        self.assertTrue(
                callable(registry.register),
                'The register attribute is not callable'
            )
        
        with patch.object(Registry, 'apply_registrations') as mock_apply_registrations:
            item = {'foo': 'bar'}
            registry.register('NAME')(item)
            self.assertEqual(
                    item, 
                    self.registry.registry['NAME'], 
                    'The item was not added to the registry attribute'
                )
            mock_apply_registrations.assert_called_once_with(item)
            
            
        with patch.object(Registry, 'apply_registrations') as mock_apply_registrations:
            class NamedClass(object):
                pass
            item = NamedClass()
            registry.register()(item)
            self.assertEqual(
                    item, 
                    self.registry.registry['NamedClass'], 
                    'The item was not added to the registry attribute'
                )
            mock_apply_registrations.assert_called_once_with(item)
                    
    
    # It should include a retrieve method which retrieves items from the registry attribute
    def test_registry_includes_retrieve_method(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'retrieve'), 
                'The Registry class does not include the retrieve attribute'
            )
        self.assertTrue(
                callable(registry.retrieve),
                'The retrieve attribute is not callable'
            )
        
        item = {'foo': 'bar'}
        
        registry.registry['NAME'] = item
        
        self.assertEqual(
                item, 
                registry.retrieve('NAME'), 
                'The named item was not returned from the registry'
            )
        
    # It should include a apply_registrations method which applies all the global registrations and
    # all the local registrations to the given item
    def test_apply_registrations_applies_all_registrations(self):
        registry = self.registry
        self.assertTrue(
                hasattr(registry, 'apply_registrations'), 
                'The Registry class does not include the apply_registrations attribute'
            )
        self.assertTrue(
                callable(registry.apply_registrations),
                'The apply_registrations attribute is not callable'
            )
        
        results = []
        
        def reg_1(item):
            results.append(('reg_1', item))
            
        def reg_2(item):
            results.append(('reg_2', item))
            
        def reg_3(item):
            results.append(('reg_3', item))
            
        def reg_4(item):
            results.append(('reg_4', item))
            
        registry.registrations = [reg_1, reg_2]
        
        item = {'foo': 'bar'}
        
        k2.registry.registration()(reg_3)
        k2.registry.registration()(reg_4)    
        registry.apply_registrations(item)
        
        self.assertEqual(('reg_3', item), results[0], 'The globally registered reg_3 was not called first')
        self.assertEqual(('reg_4', item), results[1], 'The globally registered reg_4 was not called second')
        self.assertEqual(('reg_1', item), results[2], 'The locally registered reg_1 was not called third')
        self.assertEqual(('reg_2', item), results[3], 'The locally registered reg_2 was not called last')
        
        
        
        
            
        
        
        
if __name__ == '__main__':
    unittest.main()
