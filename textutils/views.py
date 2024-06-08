from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "indexv2.html")


def text_analyzer(request):

    try:
        text = request.POST.get("input_text", "Input Text Is None")
        remove_punctuation = request.POST.get("remove_punctuation", "off")
        capitalize_first = request.POST.get("capitalize_first", "off")
        upper_case = request.POST.get("upper_case", "off")
        new_line_remover = request.POST.get("new_line_remover", "off")

        analyzed_text = ""
        final_response = list()
        if remove_punctuation == "on":
            default_punctuation = '''!()-[];:'"/,.<>|?!@#$%^&*_`~'''
            for letter in text:
                if letter not in default_punctuation:
                    analyzed_text += letter

            args = {"option": "Remove Punctuation", "final_text": analyzed_text}
            final_response.append(args)

        if capitalize_first == "on":
            analyzed_text = text.capitalize()
            args = {"option": "Capitalize First", "final_text": analyzed_text}
            final_response.append(args)

        if upper_case == "on":
            analyzed_text = text.upper()
            args = {"option": "Convert Text to UPPER CASE", "final_text": analyzed_text}
            final_response.append(args)

        if new_line_remover == "on":
            analyzed_text = ''.join(text.splitlines())
            args = {"option": "Remove New Line", "final_text": analyzed_text}
            final_response.append(args)

        if not final_response:
            args = {"option": "You have not choose any option", "final_text": text}
            final_response.append(args)

        response = {"final_response": final_response}
        return render(request, "analyzedv2.html", response)

    except Exception as e:
        return e
