import unittest
from django.test import TestCase as DjangoTest
from menu.models import Tea

# Create your tests here.

class TeaManagerTest(DjangoTest):
    def setUp(self):
        Tea.objects.bulk_create([
            Tea(name="ダージリン", kind="english"),
            Tea(name="ウーロン茶", kind="chinese"),
            Tea(name="プーアル茶", kind="japanese"),
        ])

    def test_count_each_kind(self):
        result = Tea.objects.count_eachkind()
        self.assertEqual(result, dict(english=1, chinese=2))
