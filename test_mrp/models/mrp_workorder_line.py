from odoo import models, fields


class MrpWorkOrderLine(models.Model):
    _name = "mrp.workorder.line"
    _description = "mrp workorder Line"


    workorder_id = fields.Many2one('mrp.workorder', 'Work Order', index=True)
    date_start = fields.Datetime('Date')
    qty_finished = fields.Float()
    name_machine = fields.Char()
