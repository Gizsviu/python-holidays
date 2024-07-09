#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.MG import MgHolidays
from tests.common import CommonCountryTests


class TestMgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MgHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-03-08", "Жіночий день"),
            ("2022-03-29", "День мучеників"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-05-29", "День матері"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-19", "День батька"),
            ("2022-06-26", "День незалежності"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-11", "День республіки"),
            ("2022-12-25", "Різдво Христове"),
        )
