import datetime
from django.utils import timezone
from django.test import TestCase
from .models import CustomerReview
from suppliers.models import Supplier

# Create your tests here.
class CustomerReviewTests(TestCase):

    def test_trivial(self):
        """
        Should always pass this test
        """
        self.assertEqual(True, True)

    def test_isPublished_for_published_review(self):
        """
        Verifies published reviews return true
        """
        cr = CustomerReview(published=timezone.now() - datetime.timedelta(days=1))
        self.assertEqual(cr.isPublished(), True)

    def test_isPublished_for_unpublished_review(self):
        """
        Verifies unpublished review returns false
        """
        cr = CustomerReview()
        self.assertEqual(cr.isPublished(), False)

    def test_isPublished_for_scheduled_future_reviews(self):
        """
        Verifies that reviews with publish dates scheduled in the future return false
        """
        cr = CustomerReview()
        cr.published = timezone.now() + datetime.timedelta(days=1)
        self.assertEqual(cr.isPublished(), False)