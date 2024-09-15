from odoo import models, fields


class Ticket(models.Model):
    _name = "todo.ticket"
    _description = "Todo Ticket"

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    file = fields.Binary()
    description = fields.Text()
