import os.path
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from card.views import CardFileProcessor
from card.serializers import FileSerializer
from django.conf import settings


class FileSerializerTestCase(TestCase):

    def test_file_serializer(self):
        """ Test the FileSerializer """
        upload_file = open(os.path.join(settings.BASE_DIR, 'Modelo.txt'), 'rb')
        test_file = SimpleUploadedFile(upload_file.name, upload_file.read())
        serializer = FileSerializer(data={'file': test_file})

        self.assertTrue(serializer.is_valid())
        self.assertIn('file', serializer.validated_data)


class CardFileProcessorTestCase(TestCase):

    def test_process_card_file(self):
        """Test the process_card_file method of CardFileProcessor"""
        upload_file = open(os.path.join(settings.BASE_DIR, 'Modelo.txt'), 'rb')
        test_file = SimpleUploadedFile(upload_file.name, upload_file.read())

        result = CardFileProcessor.process_card_file(test_file.file)
        self.assertIsNotNone(result)

    def test_include_cards(self):
        """Test the include_cards method of CardFileProcessor"""
        upload_file = open(os.path.join(settings.BASE_DIR, 'Modelo.txt'), 'rb')
        test_file = SimpleUploadedFile(upload_file.name, upload_file.read())
        df_cards = CardFileProcessor.process_card_file(test_file.file)

        result = CardFileProcessor.include_cards(df_cards)
        self.assertIsNone(result)
