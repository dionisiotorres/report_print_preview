// #################################################################################
// # Author      : Kelvzxu (<https://kltech-intl.odoo.com/>)
// # Copyright(c): 2015-kltech-intl.
// # All Rights Reserved.
// #
// #
// # This program is copyright property of the author mentioned above.
// # You can`t redistribute it and/or modify it.
// #################################################################################
odoo.define("report_preview_pdf.report_menu", function (require) {
    "use strict";

    var UserMenu = require("web.UserMenu");
    var session = require("web.session");

    UserMenu.include({
        _onMenuPreview: function() {
            var self = this;
            this.trigger_up("clear_uncommitted_changes", {
                callback: function() {
                    self._rpc({
                        route: "/web/action/load", 
                        params: { action_id: "report_preview_pdf.action_short_preview_print" }}).then(function(result) {
                        result.res_id = session.uid;
                        self.do_action(result);
                    });
                },
            });
        },
    });

});
