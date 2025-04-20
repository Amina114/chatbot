from gemma2 import Model

class TextAnalyzer:
    def __init__(self):
        """
        Initialize the Gemma2:2b model.
        """
        # Load the Gemma2:2b model
        self.model = Model("gemma2:2b")

    def analyze(self, user_input: str):
        """
        Use the Gemma2:2b model to analyze user input and extract structured information.
        """
        # Prepare the prompt for the model
        prompt = f"""
        Analyze the following text and extract the following information:
        1. Client: The name of the client mentioned in the text (if any).
        2. Label: The system, product, or feature mentioned in the text (if any).
        3. Severity: Whether the issue is severe or not.

        Text: "{user_input}"

        Return the result as a JSON object with keys: client, label, severity.
        """

        # Query the model
        response = self.model.generate(prompt)

        # Parse the response (assuming it returns a JSON string)
        result = response["text"]  # Modify this based on the actual API response structure
        return result