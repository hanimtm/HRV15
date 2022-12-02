{
    'name': 'TEST MRP',
    'version': '15.0.1.0.1',
    'author': 'AMLC',
    'category': 'Module for MRP',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mrp',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/mrp_workcenter_view.xml',
        'views/mrp_workorder_view.xml',
    ],
    'application': True,
}
