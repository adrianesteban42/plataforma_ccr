frappe.ui.form.on('Incidencia1', {
    refresh: function(frm) {
        // Verificar cambios en el campo tipo_incidencia al cargar el formulario y cada vez que cambia
        frm.fields_dict['tipo_incidencia'].$input.on('change', function() {
            // Actualizar la obligatoriedad del campo multimedia_incidencia
            frm.fields_dict['multimedia_incidencia'].df.reqd = frm.doc.tipo_incidencia === 'Servicio';
            frm.refresh_field('multimedia_incidencia');
        });
      
        // Establecer la función para validar la visibilidad del campo multimedia_incidencia
        frm.fields_dict['multimedia_incidencia'].get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    // Aquí, se verifica si el tipo_incidencia es "Servicio"
                    tipo_incidencia: doc.tipo_incidencia === 'Servicio'
                }
            };
        };
    }
});