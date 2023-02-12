from django.shortcuts import render
from django.http import JsonResponse
from .config import secret_key
import openai

openai.api_key = secret_key

def index(request):
    return render(request, 'index.html', {})    

def chapter_reflect(request):

    # start_sequence = "\nAI:"
    # restart_sequence = "\nHuman: "

    if request.method == 'POST':

        chapter_input = request.POST.get('chapter_input', None)

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="\n\nHello, the following text will ask you a question" + chapter_input,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        # stop=[" Human:", " AI:"]
        )
        
        server_response = JsonResponse({"response": response.choices[0].text})

        server_response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        server_response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization'


        return server_response