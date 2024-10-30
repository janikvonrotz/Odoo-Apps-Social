import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    def render_message(self, res_ids):
        template_values = super(MailComposer, self).render_message(res_ids)

        for value in template_values:
            _logger.warning(value)

            # record = self.env[self.model].browse(res_id)
            # model = self.env['ir.model']._get(record._name)
            # template_ctx = {
            #     'message': self.env['mail.message'].sudo().new(dict(body=bodies[res_id], record_name=record.display_name)),
            #     'subtype': self.env['mail.message.subtype'].sudo(),
            #     'model_description': model.display_name,
            #     'record': record,
            #     'record_name': False,
            #     'subtitles': False,
            #     'company': 'company_id' in record and record['company_id'] or self.env.company,
            #     'email_add_signature': False,
            #     'signature': '',
            #     'website_url': '',
            # }
            # body =  self.env['ir.qweb']._render('mail.mail_notification_light', template_ctx, minimal_qcontext=True, raise_if_not_found=False)
            # bodies[res_id] = body

        return template_values
