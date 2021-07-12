<template>
  <div>
      <!-- modal crear -->
       <b-modal ref="create" id="modal-create" size="xl" title="REGISTRAR MÁQUINA" hide-footer>
           <!-- Recurso -->
            <b-form-group label="Recurso">
                <b-form-input v-model="recurso" type="number"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            </b-form-group>
            
            <!-- Patente -->
            <b-form-group label="Patente">
                <b-form-input v-model="patente"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            </b-form-group>

            <!-- Nombre -->
            <b-form-group label="Nombre">
                <b-form-input v-model="nombre"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            </b-form-group>
            
            <!-- Ubicación -->
            <b-form-group label="Ubicación">
                <b-form-select  v-model="ubicacion" :options="options" @change="activateButton()" ></b-form-select>
            </b-form-group>

            <!-- boton -->
            <b-button class="normal-button" :disabled="button" @click="createMaq()">REGISTRAR</b-button>
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
    data() {
        return {
            aux: [],
            recurso: 0,
            patente: '',
            nombre: '',
            ubicacion: null,
            options: [],
            success_text: '',
            error_text: '',
            button: true
        }
    },
    
    components: {
      'modal-success': require('@/components/success_error_message/modalSuccess.vue').default,
      'modal-error': require('@/components/success_error_message/modalError.vue').default
    },

    methods: {
        // obtener lista de obras
        async getObras() {
            const accessToken = await this.$auth.getTokenSilently()

            getAPI.get('/obras', {
                headers: {
                    Authorization: `Bearer ${accessToken}`
                }
            }).then(response => {
                this.aux = response.data

                // asignar datos al select
                for(var i = 0; i < this.aux.length; i++) {
                    this.options.push({ 
                            value: this.aux[i].obraId.S,
                            text: this.aux[i].obraId.S + ' - ' + this.aux[i].nombre.S                          
                        }
                    )
                }
            })
        },

        // registrar nueva maquina
        async create() {
           // cofiguracion
           const accessToken = await this.$auth.getTokenSilently()

            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': `Bearer ${accessToken}`
                }
            }

            const data = JSON.stringify({
                id_maquina: this.recurso,
                patente: this.patente,
                nombre: this.nombre,
                ubicacion: this.ubicacion
            })

            getAPI.post('/maquinas', data, options).then(response => {
                console.log(response)
                // mensaje de exito
                this.success_text = 'Máquina '+ this.patente + 'registrada con éxito'

                // mostrar modal de éxito
                this.$bvModal.hide('modal-create')
                this.$bvModal.show('success_modal')
            }).catch( err => {
                 // mensaje de exito
                this.error_text = 'ERROR: ' + err

                // mostrar modal de éxito
                this.$bvModal.hide('modal-create')
                this.$bvModal.show('error_modal')
            })
        },

        activateButton() {
            if(this.patente != '' && this.nombre != '', this.ubicacion != null) {
                this.button = false
            }
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
    },

    created() {
        this.getObras()
    }
}
</script>

<style>

</style>