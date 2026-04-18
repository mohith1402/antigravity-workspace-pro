import unittest
import os

# Mock the environment variable so the test doesn't fail missing the key
os.environ["GEMINI_API_KEY"] = "mock_key_for_testing_only"

class TestAIEngine(unittest.TestCase):
    """Unit tests for the AI Engine to ensure code quality and stability."""
    
    def test_environment(self) -> None:
        """Test that the testing framework runs correctly."""
        self.assertEqual(1 + 1, 2)
        
    def test_empty_input_handling(self) -> None:
        """Test that empty inputs are handled safely without crashing the app."""
        from ai_engine import evaluate_text
        result = evaluate_text("   ")
        self.assertIn("Error", result)

if __name__ == '__main__':
    unittest.main()