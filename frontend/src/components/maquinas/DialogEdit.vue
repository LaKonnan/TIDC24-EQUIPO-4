<template>
    <div>
       <b-modal ref="edit_modal" id="modal-edit" size="xl" title="EDITAR MÁQUINA" hide-footer>
            Recurso
            {{ this.recurso }}
            
            Patente
            <b-form-input v-model="patente"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            
            Nombre
            <b-form-input v-model="nombre"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            
            Ubicación
            <b-form-select  v-model="ubicacion" :options="options" @change="activateButton()" ></b-form-select>

            <b-button class="normal-button" :disabled="button" @click="updateMaq()">ACTUALIZAR</b-button>
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
            recurso: 0,
            patente: '',
            nombre: '',
            ubicacion: 0,
            succes_text: '',
            error_text: '',
            button: true,
            options: []
        }
    },

    components: {
        'modal-success': require('@/components/success_error_message/modalSuccess.vue').default,
        'modal-error': require('@/components/success_error_message/modalError.vue').default
    },

    mounted() {
        // obtener datos de maquina seleccionada
        this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
            console.log('SE MOSTRARA EL MODAL DE EDIT', bvEvent, modalId)
            if (modalId == 'modal-edit') {
                this.recurso = this.items[0].recurso.N,
                this.patente = this.items[0].patente.S,
                this.nombre = this.items[0].nombre.S,
                this.ubicacion = this.items[0].ubicacion.N
            }
        })
    },

    methods: {
        // actualizar maquina
        async updateMaq() {
            const accessToken = await this.$auth.getTokenSilently()
            const data = JSON.stringify({
                recurso: this.recurso,
                patente: this.patente,
                nombre: this.nombre,
                ubicacion: this.ubicacion
            })

            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': `Bearer ${accessToken}`
                }
            }

            getAPI.put('/maquinas/'+ this.recurso, data, options)
                .then(response => {
                    console.log(response)
                    this.succes_text = 'Máquina '+ this.patente + 'actualizada con éxito.'

                    // mostrar modal de éxito
                    this.$bvModal.hide('modal-edit')
                    this.$bvModal.show('success_modal')
            }).catch(err => {
                 // mensaje de exito
                this.error_text = 'ERROR: ' + err

                // mostrar modal de éxito
                this.$bvModal.hide('modal-edit')
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

        activateButton() {
            if(this.patente != '' && this.nombre != '', this.ubicacion != null) {
                this.button = false
            }
        },

        getObras() {
            getAPI.get('/obras',).then(response => {
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
        
    },

    created() {
        this.getObras()
    }
}
</script>

<style>

</style>