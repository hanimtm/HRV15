from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = 'hr.employee'

    employee_sequence = fields.Char(string='Employee ID', readonly= True)

    @api.model
    def create(self, vals):
        if self.env.user.company_id.company_code and not vals.get('employee_sequence', False):
            employee_no = self.env['ir.sequence'].next_by_code('employee_seq')
            company_code = self.env.user.company_id.company_code
            employee_id = company_code + employee_no
            vals['employee_sequence'] = employee_id
        else:
            raise ValidationError('Please enter your Company code.')
        return super().create(vals)
        
