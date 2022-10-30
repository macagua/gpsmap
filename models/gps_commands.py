from odoo import fields, models
import pytz


class gps_commands(models.Model):
    _name = "gps_commands"
    _description = 'GPS Commands'
    _order = "name DESC"

    name = fields.Char(string = "", 'Name', size = 50)
    protocol_id = fields.Many2one('gps_protocol', ondelete = 'set null', string = "GPS Port")
    command = fields.Char(string = "Command", size = 50)
    sample = fields.Char(string = "Sample", size = 50)
    optional = fields.Boolean(string = "Optional")
    priority = fields.Integer(string = "Priority")
