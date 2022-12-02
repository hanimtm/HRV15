from odoo import models, fields


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    user_id = fields.Many2one('res.users', string='Allow User')
