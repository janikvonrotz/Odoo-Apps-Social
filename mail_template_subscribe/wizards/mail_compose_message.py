import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    def _action_send_mail(self, auto_commit=False):
        """Add subscribers as followers to mail object."""
        for mail in self:
            if mail.template_id:
                record = self.env[mail.model].browse(mail.res_id)
                subscriber_ids = mail.template_id.get_subscriber_ids()
                if subscriber_ids:
                    record._message_subscribe(partner_ids=subscriber_ids.ids)
        return super()._action_send_mail(auto_commit)
