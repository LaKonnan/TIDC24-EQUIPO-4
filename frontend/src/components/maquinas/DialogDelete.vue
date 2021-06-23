<template>
    <div>
        <b-modal ref="delete_modal" id="modal-delete" size="lg" title="ELIMINAR MAQUINA" hide-footer>
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

            <!-- boton eliminar -->
            <p><b>¿Está seguro(a) que desea eliminar la máquina?</b></p>
             <b-button class="normal-button" @click="deleteMaq()">CONFIRMAR</b-button>
        </b-modal>

        <b-modal ref="success_modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
            <center>
                <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
                <p>{{ success_text }}</p>
                <b-button class="dark-button" @click="closeModal()">CERRAR</b-button>
            </center>
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
            success_text: ''
        }
    },

    mounted() {
        // obtener datos de maquina seleccionada
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            console.log('SE MOSTRARA EL MODAL DE UPDATE', bvEvent, modalId)
            
            this.recurso = this.items[0].recurso.N,
            this.patente = this.items[0].patente.S,
            this.nombre = this.items[0].nombre.S,
            this.ubicacion = this.items[0].ubicacion.N
        })
    },

    methods: {
        // eliminar maquina
        deleteMaq() {
            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }

            getAPI.delete('/maquinas/'+ this.recurso,'',options).then(response => {
                console.log('Maquina correctamente eliminada')
                this.$refs.delete_modal.hide()
                this.success_text = 'Maquina '+ this.patente + 'ha sido eliminada con éxito' 
                this.$refs.succes_modal.show()
            })
        },

        closeModal() {
            this.$refs.succes_modal.hide()
        }
        
    }
}
</script>

<style>

</style>