from odoo import fields, models, _


class vehicle(models.Model):
    _inherit = "fleet.vehicle"
    
    image_vehicle = fields.Selection([
        ('01', _('Gray Vehicle')),
        ('02', _('Red Vehicle')),
        ('03', _('Gray van')),
        ('04', _('Gray van')),
        ('05', _('White truck')),
        ('06', _('White van')),
        ('07', _('Blue van')),
        ('30', _('Moto')),
        ('90', _('Black Phone')),
        ('91', _('Blue  Phone')),
        ('92', _('Green Phone')),
        ('93', _('Red  Phone'))
        ], string = "Img GPS", default = '01', help = 'Image of GPS Vehicle', required = True)
    temporal_id = fields.Many2one('res.partner', string = "temporal")
    economic_number = fields.Char(string = "Economic Number", size = 50)
    speed = fields.Char(string = "Speed", default = 100, size = 3)
    motor = fields.Boolean(string = "Motor", default = True, tracking = True)
    gps1_id = fields.Many2one('gps_devices', ondelete = 'set null', string = "GPS", index = True)
    positionid = fields.Many2one('gps_positions', ondelete = 'set null', string = "GPS Position", index = True)

    def get_last_vehicle_position(self):
        positions_arg = [('positionid', '!=', False)]
        vehicles = self.search(positions_arg)
        positions = {}
        for vehicle in vehicles:
            pos = vehicle["positionid"]

            totalDistance = int(pos.totalDistance/1000)

            position = {
                "idv": vehicle["id"],
                "nam": vehicle["name"],
                "lic": vehicle["license_plate"],
                "ima": vehicle["image_vehicle"],
                "vsp": vehicle["speed"],
                "oun": vehicle["odometer_unit"],
                "idp": pos.id,
                "lat": pos.latitude,
                "lon": pos.longitude,
                "alt": pos.altitude,
                "psp": pos.speed,
                "tde": pos.devicetime,
                "dat": pos.devicetime.strftime("%Y-%m-%d"),
                "tim": pos.devicetime.strftime("%H:%M"),
                "tse": pos.servertime,
                "tfi": pos.fixtime,
                "sta": pos.status,
                "eve": pos.event,
                "gas": pos.gas,
                "dis": pos.distance,
                "dto": totalDistance,
                "cou": pos.course,
                "bat": pos.batery,
            }
            positions[vehicle["id"]] = {0: position}
        return positions
