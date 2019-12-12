from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest
from unittest import skip

class FunctionalTest(StaticLiveServerTestCase):

    def test(self):
        print(self.browser.title)
        self.assertIn(self.browser.title, 'Django')

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()
