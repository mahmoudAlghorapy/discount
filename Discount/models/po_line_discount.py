from odoo import models, fields, api


class POLineDiscount(models.Model):
    _inherit = 'purchase.order.line'

    discount = fields.Float(string='Discount')
    disc_amount = fields.Float()

    # @api.depends('discount')
    # def _compute_amount_with_discount(self):
    #     for line in self:
    #         compute_disc = line.price_unit * line.discount
    #         price_disc = line.price_unit - compute_disc
    #         line.price_unit = price_disc

    @api.depends('product_qty', 'price_unit', 'taxes_id', 'discount')
    def _compute_amount(self):
        for line in self:
            taxes = line.taxes_id.compute_all(**line._prepare_compute_all_values())
            dis_val = (line.discount) * taxes['total_excluded']
            total_val = taxes['total_excluded'] - dis_val
            print("TEST1", taxes, dis_val, total_val)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': total_val,
                'disc_amount': dis_val,
            })

    def _prepare_account_move_line(self, move=False):
        res = super(POLineDiscount)._prepare_account_move_line(move)
        res.update({'discount': self.discount})
        return res
