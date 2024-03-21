# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Incidencia(WebsiteGenerator):

	def Validate(self):
		
		self.fecha_incidencia = frappe.utils.now_datetime()
		if self.estado_incidencia == "Borrador":
			self.estado_incidencia = "Enviado"