<template>
    <div>
        <b-modal ref="delete_modal" id="modal-delete" size="lg" title="ELIMINAR MAQUINA" hide-footer>
            <!-- datos de maquina -->
            <b-table stacked :items="resume"></b-table>

            <!-- boton eliminar -->
            <p><b>¿Está seguro(a) que desea eliminar la máquina?</b></p>
             <b-button class="normal-button" @click="deleteMaq()">CONFIRMAR</b-button>
        </b-modal>

        <!-- modal de exito -->
        <modal-success :message="succes_text"/>

        <!-- modal de error -->
        <modal-error :message="error_text" v-on:passData="sendMethod"/>

    </div>

    
</template>

<script>
import { getAPI } from '../axios-api'

export default {
    props: ['items'],

    data() {
        return {
            resume: [],
            success_text: ''
        }
    },

    components: {
        'modal-success': require('@/components/success_error_message/modalSuccess.vue').default,
        'modal-error': require('@/components/success_error_message/modalError.vue').default
    },

    mounted() {
        // obtener datos de maquina seleccionada
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            console.log('SE MOSTRARA EL MODAL DE UPDATE', bvEvent, modalId)
            if(modalId == 'modal-delete') {
                this.resume.push({
                    Recurso: this.items[0].recurso.N,
                    Patente: this.items[0].patente.S,
                    Nombre: this.items[0].nombre.S,
                    Ubicacion: this.items[0].ubicacion.N
                })
            }
        })
    },

    methods: {
        // eliminar maquina
        async deleteMaq() {
            const accessToken = await this.$auth.getTokenSilently()

            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': `Bearer ${accessToken}`
                }
            }

            getAPI.delete('/maquinas/'+ this.recurso,'',options)
                    .then(response => {
                    console.log(response)
                    // mensaje de exito
                    this.success_text = 'Máquina '+ this.patente + 'registrada con éxito'

                    // mostrar modal de éxito
                    this.$bvModal.hide('modal-delete')
                    this.$bvModal.show('success_modal')
                
            }).catch( err => {
                 // mensaje de exito
                this.error_text = 'ERROR: ' + err

                // mostrar modal de éxito
                this.$bvModal.hide('modal-delete')
                this.$bvModal.show('error_modal')
            })
        },
        
        // enviar métodos a componentes
        sendMethod(data) {
            if (data.methodCall) return this[data.methodCall]();
        },

        // en caso de error, desde el modal con el mensaje, regresar al modal crear
        modalBack() {
            this.$bvModal.hide('error_modal')
            this.$bvModal.show('modal-create')
        },
    }
}
</script>

<style>

</style>