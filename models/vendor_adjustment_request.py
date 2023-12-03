from odoo import models, fields, api


class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor adjustment requests'

    order_id = fields.Many2one('sale.order',
                               string='Sale Order',
                               required=True
                               )
    adjustment_detail = fields.Text(string='Adjustment Detail', required=True)
    comment = fields.Text(string='Comment')
