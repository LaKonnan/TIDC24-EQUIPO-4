<template>
  <div>
      <!-- modal crear -->
       <b-modal ref="create" id="modal-create" size="xl" title="REGISTRAR MÁQUINA" hide-footer>
            Recurso
            <b-form-input v-model="recurso" type="number"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            
            Patente
            <b-form-input v-model="patente"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            
            Nombre
            <b-form-input v-model="nombre"  @keyup="activateButton()" aria-describedby="input-live-feedback2"></b-form-input>
            
            Ubicación
            <b-form-select  v-model="ubicacion" :options="options" @change="activateButton()" ></b-form-select>

            <b-button class="normal-button" :disabled="button" @click="createMaq()">REGISTRAR</b-button>
       </b-modal>

        <!-- modal de exito -->
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
            button: true
        }
    },

    methods: {
        // obtener lista de obras
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

        // registrar nueva maquina
        create() {
           // cofiguracion
            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }

            const data = JSON.stringify({
                tipo: this.recurso,
                patente: this.patente,
                nombre: this.nombre,
                ubicacion: this.ubicacion
            })

            getAPI.post('maquinas', data, options).then(response => {
                this.$refs.create.hide()
                this.success_text = 'Máquina '+ this.patente +' ha sido registrada con éxito.'
                this.$refs.success_modal.show()
            })
        },

        closeModal() {
            this.$refs.success_modal.hide()
        },

        activateButton() {
            if(this.patente != '' && this.nombre != '', this.ubicacion != null) {
                this.button = false
            }
        },
    },


    created() {
        this.getObras()
    }
}
</script>

<style>

</style>