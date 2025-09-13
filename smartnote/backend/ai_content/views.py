from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_random_exercises
from .serializers import ExerciseSerializer
import traceback

class ExerciseView(APIView):
    """
    Endpoint: /api/ai/exercise/?word=勉強&display_mode=kanji
    Trả về 1 câu ngẫu nhiên duy nhất
    """
    def get(self, request):
        word = request.query_params.get("word")
        if not word:
            return Response({"error": "Thiếu tham số 'word'"}, status=status.HTTP_400_BAD_REQUEST)

        level = request.query_params.get("level", "N5")
        display_mode = request.query_params.get("display_mode", "kanji")
        count = int(request.query_params.get("count", 15))

        try:
            exercise = get_random_exercises(word, level, display_mode, count)
            if not exercise:
                return Response({"error": "Không tìm thấy hoặc sinh câu thất bại"}, status=status.HTTP_404_NOT_FOUND)

            serializer = ExerciseSerializer(exercise)  # không dùng many=True nữa
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": traceback.format_exc()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
