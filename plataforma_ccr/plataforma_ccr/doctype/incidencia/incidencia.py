import frappe
from frappe.website.website_generator import WebsiteGenerator


class Incidencia(WebsiteGenerator):
	def validate(self):
		self.estado_incidencia = 'Enviado'