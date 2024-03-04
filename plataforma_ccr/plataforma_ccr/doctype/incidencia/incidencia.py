# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
# from frappe.website.website_generato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
from frappe.website.website_generator import WebsiteGenerator

class Incidencia(WebsiteGenerator):
	pass
	# def before_insert(self):
    #     # Verificar si la geolocalización no está establecida
    #     if not self.localizacion_incidencia:
    #         # Obtener la geolocalización actual del navegador
    #         geolocation = self.get_current_geolocation()
    #         if geolocation:
    #             # Establecer la geolocalización en el campo correspondiente
    #             self.localizacion_incidencia = geolocation

    # def get_current_geolocation(self):
    #     try:
    #         # codigo geolocalizacion
	# 		latitud = 37.7749
    #         longitud = -122.4194
    #         return f'{latitud},{longitud}'
    #     except Exception as e:
    #         frappe.log_error(f'Error al obtener geolocalización: {str(e)}', 'Incidencia')
