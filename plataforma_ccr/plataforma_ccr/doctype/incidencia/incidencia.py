# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.website.website_generator import WebsiteGenerator

class Incidencia(WebsiteGenerator):

	def before_save(self):
		
		self.fecha_incidencia = datetime.date.today().strftime("%Y-%m-%d")
		if self.estado_incidencia == "Borrador":
			self.estado_incidencia = "Enviado"