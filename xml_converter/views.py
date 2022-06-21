from typing import Dict

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.utils import xml_parser


def upload_page(request):
    if request.method == "POST":
        xml_file = request.FILES["file"]
        # check if the file is XML
        # when we call this function from browser, content type is text/xml
        # and when we call this function from tests, content type is application/xml
        if xml_file.content_type not in {"text/xml", "application/xml"}:
            raise ValidationError("File is not XML")

        to_json: Dict = xml_parser(xml_file)
        return JsonResponse(to_json)

    return render(request, "upload_page.html")
