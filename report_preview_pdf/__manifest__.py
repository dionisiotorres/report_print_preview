# -*- coding: utf-8 -*-
#################################################################################
# Author      : Kelvzxu (<https://kltech-intl.odoo.com/>)
# Copyright(c): 2015-kltech-intl.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#################################################################################

{
    "name": "Report Pdf Preview",
    "summary": "Preview and Print PDF report in your current browser",
    "category": "Report",
    "version": "1.0.1",
    "sequence": 0,
    "author": "kelvzxu",
    "license": "Other proprietary",
    "website": "https://kltech-intl.odoo.com",
    "description": """
        Previw Report,
        Preview PDF,
        Pdf direct preview,
        Direct Preview,
        Printer,
        Report,
        Sale,
        Purchase,
    """,
    "live_test_url": "http://zhiyitechnology.me/web",
    "depends": ['web'],
    "data": [
        "views/assets.xml",
        "views/res_users.xml"
    ],
    "qweb": [
        "static/src/xml/content.xml",
        "static/src/xml/dialog.xml",
        "static/src/xml/user_menu.xml"
    ],
    "demo": [],
    "images": ['static/description/Banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 17.70,
    "currency": "EUR",
}