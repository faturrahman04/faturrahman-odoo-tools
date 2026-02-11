from odoo import models, fields, api

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  note = fields.Html(compute="_compute_note", store=False)

  @api.depends('partner_id', 'payment_term_id')
  def _compute_note(self):
    for rec in self:
      print(rec.name)
      if rec.partner_id and rec.payment_term_id:
        rec.note = f"""
<strong>{rec.name} Details</strong><br />
Customer : {rec.partner_id.display_name}<br />
Payment Term : {rec.payment_term_id.display_name}<br />
Total : {self.env.company.currency_id.symbol} {rec.amount_total:,.2f}
"""
        
class SaleOrderLine(models.Model):
  _inherit = 'sale.order.line'

  def write(self, vals):
    res = super().write(vals)
    if 'product_uom_qty' in vals:
      self.order_id.message_post_with_source(
        "sale_generate_note.",
        render_values={
          
        }
      )
      

    return res
 


