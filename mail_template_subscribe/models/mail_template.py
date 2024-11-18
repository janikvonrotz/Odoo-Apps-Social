import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MailTemplate(models.Model):
    _inherit = "mail.template"

    subscriber_domain = fields.Char(
        required=True,
        default="[('id', '=', user.partner_id.id)]",
        help="Contacts machting this domain will be subscribed to the mail document.",
    )
