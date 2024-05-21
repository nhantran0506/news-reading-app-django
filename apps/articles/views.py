from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

class SummarizeView(APIView):
    def post(self, request):
        text = request.data.get('text')

        if not text:
            return JsonResponse({'error': 'Text is required.'}, status=status.HTTP_400_BAD_REQUEST)

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 5)  

        summarized_text = " ".join([str(sentence) for sentence in summary])
        return JsonResponse({'summary': summarized_text}, status=status.HTTP_200_OK)
