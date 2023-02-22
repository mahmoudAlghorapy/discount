from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    sum_discount = fields.Float(string='Discount', compute="_compute_total_discount")

    @api.depends('order_line')
    def _compute_total_discount(self):
        for order in self:
            order.sum_discount = sum(l.disc_amount for l in self.order_line)

