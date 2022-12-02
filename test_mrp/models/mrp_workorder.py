from odoo import models, fields, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    workorder_line = fields.One2many('mrp.workorder.line','workorder_id')
    qty_balance = fields.Float(compute='_compute_qty_balance', store=True)
    total_qty_finished = fields.Float(compute='_compute_sum_qty_finished', store=True)
    qty_order = fields.Float(related="production_id.product_qty", store=True)
    user_ids = fields.Many2many(related="workcenter_id.user_ids")

    @api.depends('workorder_line')
    def _compute_sum_qty_finished(self):
        for res in self:
            if res.workorder_line:
                res.total_qty_finished = sum(res.workorder_line.mapped('qty_finished'))

    @api.depends('workorder_line')
    def _compute_qty_balance(self):
        for res in self:
            res.qty_balance = res.qty_order - res.total_qty_finished
