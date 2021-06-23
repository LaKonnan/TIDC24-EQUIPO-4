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
            succes_text: '',
            button: true,
            options: []
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

    methods: {

        // actualiza maquina
        updateMaq() {
            const data = JSON.stringify({
                recurso = this.recurso,
                patente = this.patente,
                nombre = this.nombre,
                ubicacion = this.ubicacion
            })

            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }

            getAPI.put('/maquinas/'+ this.recurso, data, options).then(response => {
                this.succes_text = 'Máquina '+ this.patente + 'actualizada con éxito.'
                this.$refs.edit_modal.hide()

                // reestablecer datos
                this.recurso = 0
                this.patente = ''
                this.nombre = ''
                this.ubicacion = 0

                this.$refs.success_modal.show()

            })
        },

        closeModal() {
            this.$refs.succes_modal.hide()
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
        getObras()
    }
}
</script>

<style>

</style>