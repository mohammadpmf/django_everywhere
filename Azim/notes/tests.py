from django.test import TestCase
from django.urls import reverse
from django.shortcuts import reverse # حاجی حسینی این رو نوشته بود. ولی من زدم خودش یو آر الز رو اتو ایمپورت کرد و زدم کار هم میکرد و خروجی شون رو پرینت هم کردم هر دو تا یکی بود. (البته فقط روی یک حالت تست کردم. اما به هر حال چیزی که حاجی حسینی هم گفته بود رو نوشتم.)
# البته تو خود شورتکاتس که رفتم، دیدم تابع ریورس رو خودشون از توی یو آر الز امیپورت کردن. پس جفتش اوکی هست.
from .models import Note

class NotesListViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(author='Mohammad', text="Something.")

    def test_notes_list_view_url(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)
    def test_notes_list_view_url_by_name(self):
        print('\n\n\n',reverse("notes_list"),"\n\n\n")
        response = self.client.get(reverse("notes_list"))
        self.assertEqual(response.status_code, 200)
    
    def test_notes_list_page(self):
        # note = Note.objects.create(author='Mohammad', text="Something.")
        # خط بالا اول اینجا بود. بعد منتقلش کردیم به تابع ستاپ و چون داخل کلاس بود و خواستیم همه جا بهش دسترسی داشته باشیم،یه سلف هم زدیم تنگش.
        response = self.client.get(reverse("notes_list"))
        self.assertContains(response, 'Some')
        self.assertContains(response, self.note.text)
