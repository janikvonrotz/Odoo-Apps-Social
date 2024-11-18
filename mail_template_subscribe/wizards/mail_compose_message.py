import logging

from odoo import fields, models
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    subscriber_ids = fields.Many2many("res.partner", compute="_compute_subscriber_ids")

    def _compute_subscriber_ids(self):
        for mail in self:
            if mail.template_id.subscriber_domain:
                eval_context = {
                    "user": self.env.user,
                }
                mail.subscriber_ids = self.env["res.partner"].search(
                    safe_eval(mail.template_id.subscriber_domain, eval_context)
                )
            else:
                mail.subscriber_ids = []

    def _action_send_mail(self, auto_commit=False):
        """Add subscribers as followers to mail object."""
        for mail in self:
            record = self.env[mail.model].browse(mail.res_id)
            _logger.warning([record])
            record._message_subscribe(partner_ids=mail.subscriber_ids.ids)
        return super()._action_send_mail(auto_commit)
