from pathlib import Path

from django.test import TestCase, Client


TEST_DIR = Path(__file__).parent / Path("test_files")


class XMLConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_connected_convert_empty_document(self):
        """
        Test that an empty document is converted to an empty dictionary with root tag as key.
        """
        with (TEST_DIR / Path("empty.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/connected/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {
                    "Root": "",
                },
            )

    def test_api_convert_empty_document(self):
        """
        Test that an empty document is converted to an empty dictionary with root tag as key.
        """
        with (TEST_DIR / Path("empty.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/api/converter/convert/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {
                    "Root": "",
                },
            )

    def test_connected_convert_addresses(self):
        """
        Test that xml file with addresses is converted to a dictionary with root tag as key.
        """
        with (TEST_DIR / Path("addresses.xml")).open() as fp:
            # GIVE/WHEN
            response = self.client.post(
                "/connected/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {
                    "Root": [
                        {
                            "Address": [
                                {"StreetLine1": "123 Main St."},
                                {"StreetLine2": "Suite 400"},
                                {"City": "San Francisco"},
                                {"State": "CA"},
                                {"PostCode": "94103"},
                            ]
                        },
                        {
                            "Address": [
                                {"StreetLine1": "400 Market St."},
                                {"City": "San Francisco"},
                                {"State": "CA"},
                                {"PostCode": "94108"},
                            ]
                        },
                    ],
                },
            )

    def test_api_convert_addresses(self):
        """
        Test that xml file with addresses is converted to a dictionary with root tag as key.
        """
        with (TEST_DIR / Path("addresses.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/api/converter/convert/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {
                    "Root": [
                        {
                            "Address": [
                                {"StreetLine1": "123 Main St."},
                                {"StreetLine2": "Suite 400"},
                                {"City": "San Francisco"},
                                {"State": "CA"},
                                {"PostCode": "94103"},
                            ]
                        },
                        {
                            "Address": [
                                {"StreetLine1": "400 Market St."},
                                {"City": "San Francisco"},
                                {"State": "CA"},
                                {"PostCode": "94108"},
                            ]
                        },
                    ],
                },
            )

    def test_connected_convert_example_1_from_readme(self):
        """
        Test that example from readme is converted to a dictionary with root tag as key.
        """
        with (TEST_DIR / Path("example1_from_readme.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/connected/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Foo": "Bar"},
            )

    def test_api_convert_example_1_from_readme(self):
        """
        Test that example from readme is converted to a dictionary with root tag as key.
        """
        with (TEST_DIR / Path("example1_from_readme.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/api/converter/convert/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Foo": "Bar"},
            )

    def test_connected_convert_example_2_from_readme(self):
        """
        Test that example from readme is converted to a dictionary with root tag as key.
        """
        with (TEST_DIR / Path("example2_from_readme.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/connected/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Foo": [{"Bar": "Baz"}]},
            )

    def test_api_convert_example_2_from_readme(self):
        with (TEST_DIR / Path("example2_from_readme.xml")).open() as fp:
            # GIVEN/WHEN
            response = self.client.post(
                "/api/converter/convert/",
                {
                    "file": fp,
                },
            )

            # THEN
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Foo": [{"Bar": "Baz"}]},
            )
