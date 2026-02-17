from odoo import models, fields

class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  generate_note = fields.Boolean(string="Generate Note", config_parameter="sale_generate_note.generate_note", default=False)