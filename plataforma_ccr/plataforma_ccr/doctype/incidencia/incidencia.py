# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Incidencia(WebsiteGenerator):

	def validate(self):
		# Obtener el valor del campo 'tipo'
		tipo = self.tipo_incidencia

		# Verificar si el tipo es 'Bien'
		if tipo == 'Bien':
			# Si el tipo es 'Bien', hacer que el campo de imagen sea obligatorio
			if not self.img_video_incidencia:
				frappe.throw("Por favor, adjunte una imagen para la incidencia de tipo 'Bien'")
		elif tipo == 'Servicio':
			# Si el tipo es 'Servicio', asegurarse de que el campo de imagen no sea obligatorio
			self.img_video_incidencia = None