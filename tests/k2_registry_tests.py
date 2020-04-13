from unittest import TestCase
from unittest.mock import patch
import inspect
from k2 import registry

class K2RegistryTests(TestCase):
    
    # It should include a method to clear the global registrations
    def test_registry_includes_clear_registrations(self):
        self.assertTrue(
                hasattr(registry, 'clear_registrations'), 
                'The registry package does not include the clear_registrations attribute'
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
    
    # It should include a registrations list with initial value []
    def test_registry_includes_registrations_list(self):
        self.assertTrue(
                hasattr(registry, 'registrations'), 
                'The registry package does not include the registrations attribute'
            )
        self.assertEqual(
                registry.registrations, 
                [], 
                'The registrations list if not an empty list'
            )
    
    # It should include a registration decorator method which adds registrations to the list of global registrations
    def test_registry_includes_registration_decorator(self):
        self.assertTrue(
                hasattr(registry, 'registration'), 
                'The registry package does not include the registration attribute'
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
                'The registration decorator does not add registrations the global registrations'
            )
        registry.clear_registrations()
    
    
    # It should define the Registry class
    def test_registry_defines_Registry(self):
        self.assertTrue(
                hasattr(registry, 'Registry'), 
                'The registry package does not include the Registry attribute'
            )
        self.assertTrue(
                callable(registry.Registry),
                'The Registry attribute is not callable'
            )
        self.assertTrue(
                inspect.isclass(registry.Registry), 
                'The Registry attribute is not a Class'
            )
        
        
    
    # It should include a Registry instance named registry
    def test_registry_includes_registry_instance(self):
        self.assertTrue(
                hasattr(registry, 'registry'), 
                'The registry package does not include the registry attribute'
            )
        self.assertTrue(
                isinstance(registry.registry, registry.Registry),
                'The registry attribute is not an instance of Registry'
            )
        
    
    # It should include a register decorator method which registers an item with the global Registry
    def test_registry_includes_register_decorator(self):
        self.assertTrue(
                hasattr(registry, 'register'), 
                'The registry package does not include the register attribute'
            )
        self.assertTrue(
                callable(registry.register),
                'The register attribute is not callable'
            )
        
        def mock_func(item):
            return item
        
        with patch.object(registry.Registry, 'register', return_value=mock_func) as mock_register:
            name_register = registry.register('NAME')
            self.assertEqual(
                    mock_func, 
                    name_register, 
                    'The register method does not return the decorator function'
                )
            mock_register.assert_called_once_with('NAME')
            
    
    # It should include a retrieve method which retrieves items from the global registry
    def test_registry_includes_retrieve_method(self):
        self.assertTrue(
                hasattr(registry, 'retrieve'), 
                'The registry package does not include the retrieve attribute'
            )
        self.assertTrue(
                callable(registry.retrieve),
                'The retrieve attribute is not callable'
            )
        
        item = {'foo': 'bar'}
        
        
        with patch.object(registry.Registry, 'retrieve', return_value=item) as mock_retrieve:
            self.assertEqual(
                    item, 
                    registry.retrieve('NAME'), 
                    'The retrieve method does not return the value from the retrieve method of the Registry'
                )
            mock_retrieve.assert_called_once_with('NAME')
    
        
        
if __name__ == '__main__':
    unittest.main()
