from odoo import models, fields


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    user_ids = fields.Many2many('res.users','rel_workcenter_users', string='Allow User')
