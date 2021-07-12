<template>
  <div>
    <b-modal id="modal-delete" size="lg" title="ELIMINAR CAJA CHICA" ref="modal_delete" hide-footer @hidden="resetData()">
        <!-- datos de caja  -->
        <b-card-text>
            <b-table stacked :items="resume"></b-table>
        </b-card-text>
        
        <!-- mensajes -->
        <center><p>
            <b>IMPORTANTE: </b>Una vez eliminada la caja chica esta no podrá ser recuperada, toda información sobre los gastos efectuados y fechas se perderán. Tanto la caja chica como la caja de combustible serán eliminadas.
        </p></center>

        <p class="warn-text">
            Para confirmar la eliminación de la caja, por favor, ingrese el ID de la caja chica:
        </p>
        
        <!-- input id caja -->
        <b-form-input v-model="id_caja" style="text-align: center;" @keyup="activateButton()" @paste.prevent ></b-form-input>
        <br>

        <!-- boton -->
        <b-button class="normal-button" :disabled="button"  @click="deleteCaja()">ELIMINAR</b-button>
    </b-modal>

    <!-- modal de exito -->
    <modal-success :message="succes_text" v-on:passData="sendMethod"/>

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
            id_caja: '',
            // recibir id de caja seleccionada
            caja: [],
            resume: [],
            button: true,          
        }
    },

    methods: {
        // habilitar botón cuando se ha escrito en el input
        activateButton() {
            if(this.id_caja != '') {
                this.button = false
            }
        },

        // obtener datos de caja seleccionada
        getData() {
            getAPI.get('/cajasChicas/'+ this.items[0].id_caja.S ,)
                .then(response => {
                    this.caja = response.data

                    this.resume.push({
                        ID_caja: this.caja[0].id_caja.S,
                        ID_obra: this.caja[0].id_obra.S,
                        Tipo: this.caja[0].tipo.S,
                        Estado: this.caja[0].estado.S,
                        Fecha_inicio: this.caja[0].fecha_inicio.S,
                        Fecha_termino: this.caja[0].fecha_termino.S,
                        Monto_gastos: this.caja[0].monto_gastos.S,
                        Monto_total: this.caja[0].monto_total.S
                    })
                })
        },

        // Eliminar caja
        async deleteCaja() {
            const accessToken = await this.$auth.getTokenSilently()

            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': `Bearer ${accessToken}`
                }
            }

            if(this.id_caja == this.caja[0].id_caja.S){
                getAPI.delete('/cajasChicas/'+ this.items[0].id_caja.S,'',options)
                    .then(res => {
                        console.log(res)
                        
                        // mensaje de éxito
                        this.success_text = 'Caja chica' + this.items[0].id_caja.S + 'eliminada con éxito'
                        
                        // mostrar modal de éxito
                        this.$bvModal.hide('modal-delete')
                        this.$bvModal.show('success_modal')
                    })
            }else{
                this.error_text = 'ID incorrecto, intente nuevamente'

                // mostrar modal de error
                this.$bvModal.hide('modal-delete')
                this.$bvModal.show('error_modal')
            }
        },

        // en caso de error, desde el modal con el mensaje, regresar al modal eliminar
        modalBack() {   
            this.$bvModal.hide('error_modal')
            this.$bvModal.show('modal-delete')
        },

        // enviar métodos a componentes 
        sendMethod(data) {
            if (data.methodCall) return this[data.methodCall]();
        },

        // dejar variables vacías
        resetData() {
            this.caja = []
            this.resume = []
            this.id_caja = ''
        }
    },

    mounted() {
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            if( modalId == 'modal-delete') {
                this.getData()
                console.log('SE MOSTRARA EL MODAL DE DELETE', bvEvent, modalId)
            }
        })
    }

}
</script>

<style>

</style>