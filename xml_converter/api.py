from typing import Dict

from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.utils import xml_parser


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        xml_file = request.FILES["file"]
        # check if the file is XML
        # when we call this function from browser, content type is text/xml
        # and when we call this function from tests, content type is application/xml
        if xml_file.content_type not in {"text/xml", "application/xml"}:
            raise ValidationError("File is not XML")
        to_json: Dict = xml_parser(xml_file)
        return Response(to_json)
