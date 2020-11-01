# -*- encoding: utf-8 -*-
from django.test import TestCase
from app.templatetags import trend

"""
Test case for functionality of simple information on covidly dashboard. Show sample statistics.
"""
class TestTrendTemplateTags(TestCase):
    def test_color_tag(self):
        self.assertEqual("text-danger", trend.color("deaths", 20))
        self.assertEqual("text-success", trend.color("deaths", -20))

        self.assertEqual("text-danger", trend.color("confirmed", 20))
        self.assertEqual("text-success", trend.color("confirmed", -20))

        self.assertEqual("text-danger", trend.color("recovered", -20))
        self.assertEqual("text-success", trend.color("recovered", 20))

        self.assertEqual("text-danger", trend.color("death_rate", 20))
        self.assertEqual("text-success", trend.color("death_rate", -20))

    def test_arrow_tag(self):
        self.assertEqual("fa fa-angle-up", trend.arrow("deaths", 20))
        self.assertEqual("fa fa-angle-down", trend.arrow("deaths", -20))

        self.assertEqual("fa fa-angle-up", trend.arrow("confirmed", 20))
        self.assertEqual("fa fa-angle-down", trend.arrow("confirmed", -20))

        self.assertEqual("fa fa-angle-down", trend.arrow("recovered", -20))
        self.assertEqual("fa fa-angle-up", trend.arrow("recovered", 20))

        self.assertEqual("fa fa-angle-up", trend.arrow("death_rate", 20))
        self.assertEqual("fa fa-angle-down", trend.arrow("death_rate", -20))
