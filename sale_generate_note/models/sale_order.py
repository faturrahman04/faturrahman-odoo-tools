from odoo import models, fields, api

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  note = fields.Html(compute="_compute_note", store=False)

  @api.depends('partner_id', 'payment_term_id')
  def _compute_note(self):
    is_generated_note_enabled = self.env['ir.config_parameter'].sudo().get_param(
      'sale_generate_note.generate_note'
     ) == 'True'
    if is_generated_note_enabled:
      for rec in self:
        print(rec.name)
        if rec.partner_id and rec.payment_term_id:
          rec.note = f"""
<strong>{rec.name} Details</strong><br />
Customer : {rec.partner_id.display_name}<br />
Payment Term : {rec.payment_term_id.display_name}<br />
Total : {self.env.company.currency_id.symbol} {rec.amount_total:,.2f}
"""
        
  @api.model
  def _get_generate_note_config(self):
    is_generate_note_enabled = self.env['res.config.settings'].search([('')])
        
class SaleOrderLine(models.Model):
  _inherit = 'sale.order.line'

  def write(self, vals):
    is_generated_note_enabled = self.env['ir.config_parameter'].sudo().get_param('sale_generate_note.generate_note', True) 

    if is_generated_note_enabled:
      for so in self:
        old_product_uom_qty = so.product_uom_qty
      res = super().write(vals)
      
      for line in self:
        if 'product_uom_qty' in vals:
          self.order_id.message_post_with_source(
            "sale_generate_note.sale_order_mail_template",
            render_values={
              'product':line.product_id.display_name, 
              'quantity': line.product_uom_qty, 
              'old_quantity' : old_product_uom_qty}
          )
      
    return super().write(vals)
 


