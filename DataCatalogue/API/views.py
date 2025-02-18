import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import JSONData
from .serializers import JSONDataSerializer

class UploadJSONView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        # Verifica si se proporcionó un archivo
        if 'file' not in request.data:
            return Response({"error": "No se proporcionó un archivo"}, status=status.HTTP_400_BAD_REQUEST)

        file_obj = request.data['file']

        try:
            # Lee y decodifica el archivo JSON
            json_data = json.loads(file_obj.read().decode('utf-8'))

            # Valida el JSON usando el serializador
            serializer = JSONDataSerializer(data=json_data)
            if not serializer.is_valid():
                return Response(
                    {"error": "Datos inválidos", "details": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Si todo está bien, guarda el archivo en la base de datos
            json_instance = JSONData(file=file_obj)
            json_instance.save()

            return Response({"message": "Archivo cargado exitosamente"}, status=status.HTTP_201_CREATED)

        except json.JSONDecodeError:
            return Response({"error": "El archivo no es un JSON válido"}, status=status.HTTP_400_BAD_REQUEST)