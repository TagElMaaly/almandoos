# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    sales_channel = fields.Many2one(comodel_name='sales.channel', string="Sales Channel")

    def unlink(self):
        return models.Model.unlink(self)



class SalesChannel(models.Model):
    _name = "sales.channel"
    _description = "Sales Channel"

    name = fields.Char(string="Name")
