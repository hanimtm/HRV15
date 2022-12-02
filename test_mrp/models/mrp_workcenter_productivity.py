from odoo import models, fields


class MrpWorkorderProductivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'

    employee = fields.Many2one('hr.employee', string='Employee')
