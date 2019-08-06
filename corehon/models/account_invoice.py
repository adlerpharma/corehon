# Copyright 2019 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    warehouse_id = fields.Many2one(
        'stock.warehouse',
        help="The warehouse related with delivery of products in customer"
             " invoices")

    @api.model
    def split_amount_text(self, amount_text, length):
        """ Split an amount in text in two strings where the length of the
        first string must be less than the length parameter
        """
        sum_wordf = ''
        sum_wordl = ''
        words = amount_text.split()
        for word in words:
            if sum_wordl == '' and (len(sum_wordf) + len(word)) < length:
                sum_wordf += ' %s' % word
            else:
                sum_wordl += ' %s' % word
        return [sum_wordf, sum_wordl]

    @api.multi
    def split_date_invoice(self):
        """" Split date invoice to obtain day, month and year separated in
        report
        """
        self.ensure_one()
        return [self.date_invoice.day, self.date_invoice.month,
                self.date_invoice.year]
