import unittest
from app.utils.text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.clients = ["SBC Bank", "ABC Corp", "XYZ Inc"]
        self.labels = ["Agile Reporter", "Payment Gateway", "Login System"]
        self.analyzer = TextAnalyzer(self.clients, self.labels)

    def test_analyze(self):
        user_input = "The client SBC Bank has a problem when they try to submit a return using Agile Reporter."
        result = self.analyzer.analyze(user_input)
        self.assertIn("SBC Bank", result)
        self.assertIn("Agile Reporter", result)
        self.assertIn("Non mentionnée", result)

if __name__ == "__main__":
    unittest.main()