import unittest
from hash_generator import generate_hash
from math_calc import calculate_linear

class TestFunctions(unittest.TestCase):
    """Teste para verificar se a hash considera todos os caracteres"""
    
    def test_hash_generator(self):
        test_string = "Python"
        expected_hash = sum(ord(char) for char in test_string)
        actual_hash = generate_hash(test_string)
        
        self.assertEqual(
            expected_hash, 
            actual_hash, 
            f"Bug encontrado: A hash gerada ({actual_hash}) não considera todos os caracteres. Valor esperado: {expected_hash}."
        )

    def test_calculate_linear(self):
        x = 5
        a = 2
        b = 3
        expected_result = a * x + b  
        actual_result = calculate_linear(x)
        
        self.assertEqual(
            expected_result,
            actual_result, 
            f"Bug encontrado: O resultado da função linear ({actual_result}) não corresponde ao esperado ({expected_result})."
        )
        
if __name__ == '__main__':
    unittest.main()