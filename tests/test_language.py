import unittest

from omnilingual.language import Language, LanguageCode, IetfComponents


class TestLanguage(unittest.TestCase):
    def test_requires_valid_code(self):
        with self.assertRaises(ValueError):
            Language.where(tag="a")

    def test_russian_equivalents(self):
        iso_1 = "ru"
        iso_3 = "rus"

        self.assertEqual(Language.where(iso_1=iso_1), iso_1)
        self.assertEqual(Language.where(iso_3=iso_3), iso_3)
        self.assertEqual(Language.where(iso_1=iso_1), iso_3)
        self.assertEqual(Language.where(iso_3=iso_3), iso_1)

        self.assertEqual(Language.where(iso_1=iso_1), Language.where(iso_3=iso_3))

    def test_supports_un_languages(self):
        self.assertEqual(Language.where(iso_3="ara"), LanguageCode.Arabic)
        self.assertEqual(Language.where(iso_3="zho"), LanguageCode.Chinese)
        self.assertEqual(Language.where(iso_3="fra"), LanguageCode.French)
        self.assertEqual(Language.where(iso_3="rus"), LanguageCode.Russian)
        self.assertEqual(Language.where(iso_3="spa"), LanguageCode.Spanish)

    def test_should_convert_non_iso_639_3_codes(self):
        self.assertEqual(Language.where(iso_2="fre").code, LanguageCode.French)
        self.assertEqual(Language.where(iso_2="ger").code, LanguageCode.German)

        self.assertEqual(Language.where(tag="fre").code, LanguageCode.French)
        self.assertEqual(Language.where(tag="ger").code, LanguageCode.German)

    def test_ietf_code_without_region(self):
        self.assertEqual(Language.where(tag="zh-Hant").ietf_tag(alpha_3=False), "zh")

    def test_ietf_code_with_region(self):
        self.assertEqual(
            Language.where(tag="zh-Hant").ietf_tag(
                IetfComponents(script=True), alpha_3=False
            ),
            "zh-Hant",
        )

    def test_ietf_regionless_code_with_region(self):
        self.assertEqual(Language.where(tag="eng").ietf_tag(), "eng")


if __name__ == "__main__":
    unittest.main()
