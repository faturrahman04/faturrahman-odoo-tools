from odoo import models, fields

class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  generate_note = fields.Boolean(string="Generate Note")