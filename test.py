import unittest
from ht import HashTable

class instantiationTestCase(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
    def testSize(self):
        """ Hash table should have initial size of 0"""
        assert self.ht.size == 0

    def testCapacity(self):
        """ Should default to capacity of 101"""
        assert self.ht.capacity == 100

    def testCustomCapacity(self):
        """ Should override default capacity"""
        self.ht = HashTable(200)
        assert self.ht.capacity == 200
    
class insertionTestCase(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
        self.ht.set('foo', 'bar')
        self.ht.set(('foo', 'bar'), 'bam')
    
    def testInsertSingle(self):
        """ Insertion should increase size """
        assert self.ht.size == 2

    def testOverrideInsert(self):
        """ Given an key, override existing value """
        self.ht.set('foo', 'kung')
        assert self.ht.get('foo') == 'kung'

    def testLookup(self):
        """ Should be able to get what was inserted """
        assert self.ht.get('foo') == 'bar'
        assert self.ht.get(('foo', 'bar')) == 'bam'
    
    def testErrorLookup(self):
        """ Error should be thrown if no key in table """
        self.assertRaises(KeyError, self.ht.get, 'blah')

class collisionTestCase(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
        self.ht.set(14, 'fourteen')
        self.ht.set(114, 'oneFourteen')
        self.ht.set(214, 'twoFourteen')
    
    def testHash(self):
        """ All three keys should hash to the same idx in table """
        assert self.ht.get_idx(14) == 14
        assert self.ht.get_idx(114) == 14
        assert self.ht.get_idx(214) == 14
    
    def testSeperateChaining(self):
        """ Should be able to properly look up all keys, even with collision """
        assert self.ht.get(14) == 'fourteen'
        assert self.ht.get(114) == 'oneFourteen'
        assert self.ht.get(214) == 'twoFourteen'

class resizeTestCase(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
        for i in range(0, 40):
            self.ht.set(i, i)
    
    def testLoadFactor(self):
        """ Should properly calculate the load factor, 0.4 (size / capacity) """
        assert self.ht.get_load_factor() == 0.4
    
    def testResize(self):
        """ Capacity should double once the load factor is >= 0.5"""
        for i in range(40, 50):
            self.ht.set(i, i)
        assert self.ht.capacity == 200
        assert self.ht.size == 50

    def testElementsStillInTable(self):
        """ After resizing, all elements should still be in table """
        for i in range(40, 50):
            self.ht.set(i, i)
        for i in range(0,50):
            assert self.ht.get(i) == i
class deleteTestCase(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
        self.ht.set(14, 'fourteen')
        self.ht.set(114, 'oneFourteen')
        self.ht.set(214, 'twoFourteen')
        self.ht.set(314, 'threeFourteen')
        self.ht.set('foo', 'bar')
    
    def testDeleteNonLinkedEntry(self):
        """ Delete a single entry that is not connected to other entries"""
        self.ht.delete('foo')
        self.assertRaises(KeyError, self.ht.get, 'foo')
    
    def testDeleteFirstLinkedEntry(self):
        """ Delete the first connected entry, but still have access to other connected entries"""
        self.ht.delete(14)
        self.assertRaises(KeyError, self.ht.get, 14)
        assert self.ht.get(114) == 'oneFourteen'
        assert self.ht.get(214) == 'twoFourteen'

    def testDeleteIntermediateLinkedEntry(self):
        """ Delete an intermediate connected entry, but still have access to other connected entries"""
        self.ht.delete(214)
        self.assertRaises(KeyError, self.ht.get, 214)
        assert self.ht.get(14) == 'fourteen'
        assert self.ht.get(114) == 'oneFourteen'
        assert self.ht.get(314) == 'threeFourteen'
    
    def testDeleteFinalLinkedEntry(self):
        """ Delete the last connected entry, but still have access to other connected entries"""
        self.ht.delete(314)
        self.assertRaises(KeyError, self.ht.get, 314)
        assert self.ht.get(14) == 'fourteen'
        assert self.ht.get(214) == 'twoFourteen'
        assert self.ht.get(114) == 'oneFourteen'
    def testDeleteNonExistantKey(self):
        self.assertRaises(KeyError, self.ht.delete, 'George Costanza')

if __name__ == "__main__":
    unittest.main() 