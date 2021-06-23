<template>
  <div>
        <b-modal ref="edit_modal" id="modal-edit" size="lg" title="ELIMINAR MAQUINA" hide-footer>
            <!-- datos de maquina -->
            <b-row>
                <b-col>RECURSO</b-col>
                <b-col>{{ this.recurso }}</b-col>
            </b-row>
            <b-row>
                <b-col>PATENTE</b-col>
                <b-col>{{ this.patente }}</b-col>
            </b-row>
            <b-row>
                <b-col>NOMBRE</b-col>
                <b-col>{{ this.nombre }}</b-col>
            </b-row>
            <b-row>
                <b-col>UBICACIÓN</b-col>
                <b-col>{{ this.ubicacion }}</b-col>
            </b-row>
        </b-modal>
  </div>
</template>

<script>
export default {
    props: ['items'],

    data() {
        return {
            recurso: 0,
            patente: '',
            nombre: '',
            ubicacion: 0,
        }
    },

    mounted() {
        // obtener datos de maquina seleccionada
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            console.log('SE MOSTRARA EL MODAL DE EDIT', bvEvent, modalId)
            
            this.recurso = this.items[0].recurso.N,
            this.patente = this.items[0].patente.S,
            this.nombre = this.items[0].nombre.S,
            this.ubicacion = this.items[0].ubicacion.N
        })
    },
}
</script>

<style>

</style>