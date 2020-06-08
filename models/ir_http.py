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

from odoo import models
from odoo.http import request

class Http(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super(Http, self).session_info()

        user = request.env.user

        result.update({
            "preview_print": user.preview_print,
            "automatic_printing": user.automatic_printing,
            "report_layout": bool(user.company_id.external_report_layout_id),
            "exist_logo": bool(user.company_id.logo)
        })

        return result
