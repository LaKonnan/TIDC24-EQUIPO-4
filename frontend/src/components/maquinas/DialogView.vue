<template>
  <div>
    <b-modal id="modal-view" size="lg" title="ELIMINAR MAQUINA" hide-footer>
        <b-table stacked :items="resume"></b-table>
    </b-modal>
  </div>
</template>

<script>
export default {
    props: ['items'],

    data() {
        return {
            resume: []
        }
    },

    mounted() {
        // obtener datos de maquina seleccionada
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            console.log('SE MOSTRARA EL MODAL DE VIEW', bvEvent, modalId)
            
            if(modalId == 'modal-view') {
                this.resume.push({
                    Recurso: this.items[0].recurso.N,
                    Patente: this.items[0].patente.S,
                    Nombre: this.items[0].nombre.S,
                    Ubicacion: this.items[0].ubicacion.N
                })
            } 
            
        })
    },
}
</script>

<style>

</style>