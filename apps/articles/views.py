from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Define a view for summarizing text using an API endpoint
class SummarizeView(APIView):

    # Define the method to handle POST requests
    def post(self, request):
        # Extract the 'text' parameter from the request data
        text = request.data.get('text')

        # Check if 'text' is provided in the request
        if not text:
            # Return an error response if 'text' is not provided
            return JsonResponse({'error': 'Text is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Parse the input text using PlaintextParser and a tokenizer for the English language
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        
        # Initialize the LSA (Latent Semantic Analysis) summarizer
        summarizer = LsaSummarizer()
        
        # Generate the summary with a fixed number of sentences (e.g., 5 sentences)
        summary = summarizer(parser.document, 5)

        # Join the summary sentences into a single string
        summarized_text = " ".join([str(sentence) for sentence in summary])
        
        # Return the summarized text as a JSON response with a 200 OK status
        return JsonResponse({'summary': summarized_text}, status=status.HTTP_200_OK)
