import random
from django.db import transaction
from django.db.models import Q
from .models import Vocabulary, Exercise
from openai_api.services import generate_fill_in_blank


def get_or_create_exercises(word: str, level: str = "N5", display_mode: str = "kanji", count: int = 15):
    """
    Lấy câu ôn tập theo từ + display_mode.
    Nếu chưa có trong DB → gọi Folder A để sinh và lưu.
    Trả về danh sách Exercise.
    """

    # --- Tìm Vocabulary theo hiragana hoặc kanji ---
    vocab = Vocabulary.objects.filter(Q(word_hira=word) | Q(word_kanji=word)).first()

    # Nếu không tìm thấy → tạo mới
    if not vocab:
        vocab = Vocabulary.objects.create(
            word_hira=word,
            word_kanji=word,
            level=level
        )

    # --- Kiểm tra Exercise đã tồn tại theo display_mode ---
    exercises_qs = Exercise.objects.filter(
        vocabulary=vocab,
        display_mode=display_mode
    )

    if exercises_qs.exists():
        return list(exercises_qs)

    # --- Nếu chưa có, gọi Folder A ---
    generated = generate_fill_in_blank(word=word, level=level, display_mode=display_mode, count=count)

    exercises = []
    with transaction.atomic():
        for item in generated:
            ex = Exercise.objects.create(
                vocabulary=vocab,
                display_mode=display_mode,
                sentence=item.get('sentence', ''),
                options=item.get('options', []),
                answer=item.get('answer', ''),
                explanation=item.get('explanation', {}),
            )
            exercises.append(ex)

    return exercises


def get_random_exercises(word: str, level: str = "N5", display_mode: str = "kanji", count: int = 15):
    """
    Lấy 1 câu random duy nhất (trả về object Exercise).
    """
    exercises = get_or_create_exercises(word, level, display_mode, count)
    if not exercises:
        return None
    return random.choice(exercises)
