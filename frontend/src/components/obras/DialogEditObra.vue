<template>
    <div>
        <b-modal ref="edit" id="modal-edit" size="xl" title="EDITAR OBRA" hide-footer>
          <b-card-text>
            <!-- ID -->
            <b-row>
              <b-col>ID</b-col>
              <b-col cols="9" class="mb-2">{{ this.obraid }}</b-col>
            </b-row>

            <!-- Tipo -->
            <b-form-group label="Tipo">
              <b-form-select 
                v-model="tipo" 
                :options="options2" 
                @change="activateButton(); getUsers()">
              </b-form-select>
            </b-form-group>

            <!-- Encargado -->
            <b-form-group label="Encargado">
              <b-form-select
                v-model="encargado"
                :options="users"
                @change="activateButton()"
              >
              </b-form-select>
            </b-form-group>

            <!-- nombre de la obra -->
            <b-form-group label="Nombre">
              <b-form-input 
                v-model="nombre" 
                @keyup="activateButton()">
              </b-form-input>
            </b-form-group>
        
            <!-- estado -->
            <b-form-group label="Estado">
              <b-form-select 
                v-model="estado" 
                :options="options1" 
                @change="activateButton()">
              </b-form-select>
            </b-form-group>

            <center>
              <p><b>Una vez presionado el botón, se actualizará la obra en el sistema.</b></p>
            </center>
            <b-button :disabled="btnEdit" id="btnEdit" class="button-next dark-button" @click="editObra()">GUARDAR</b-button>

          </b-card-text>
        </b-modal>
        <!-- modal de exito -->
        <modal-success :message="succes_text" v-on:passData="sendMethod"/>

        <!-- modal de error -->
        <modal-error :message="error_text" v-on:passData="sendMethod"/>
    </div>
</template>

<script>
import { getAPI } from '../axios-api';


export default {  
  props: ['items'],
  data() {
    return {
      // variables 
      btnEdit: true,
      success_text: '',
      error_text: '',
      users: [],
      aux: [],
      obraid:'',
      encargado: '',
      nombre: '',
      success: false,
      tabIndex: 2,
      btnStep1: true,
      step2: true,
      estado: null,
      tipo: null,

      options1: [
        { value: 'Activa', text: 'Activa'},
        { value: 'Inactiva', text: 'Inactiva'},
        { value: 'Finalizada', text: 'Finalizada' }
      ],

      options2: [
        { value: 'Obra', text: 'Obra'},
        { value: 'Gerencia', text: 'Gerencia'},
        { value: 'Oficina', text: 'Oficina central'}
      ],
    }
  },

  components: {
      'modal-success': require('@/components/success_error_message/modalSuccess.vue').default,
      'modal-error': require('@/components/success_error_message/modalError.vue').default
  },

  methods: {
   activateButton(){
      if(![this.encargado, this.nombre, this.estado, this.tipo].includes(null)) {
        this.btnEdit = false
        }
     },
    
    async editObra(){
      console.log(this.obraid)
      const accessToken = await this.$auth.getTokenSilently()
      const options = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          'Access-Control-Allow-Origin': '*',
          'Authorization': `Bearer ${accessToken}`
          
        }
      }

      const data = JSON.stringify(
        {
          obraId: this.obraid,
          encargado: this.encargado,
          estado: this.estado,
          nombre: this.nombre,
          tipo: this.tipo
        }
      )
      
      getAPI.put('/obras', data, options)
          .then((res) =>{
            console.log(res)
             // mensaje de exito
            this.success_text = 'Obra '+ this.obraid + 'creada con éxito'

            // mostrar modal de éxito
            this.$bvModal.hide('modal-edit')
            this.$bvModal.show('success_modal')
          })
          .catch((err)=>{
            // error
            this.error_text = 'ERROR: ' + err

            // mostrar modal de éxito
            this.$bvModal.hide('modal-edit')
            this.$bvModal.show('error_modal')
          })

    },

    setData() {
      this.tipo = this.items[0].tipo.S
      this.encargado = this.items[0].encargado.S
      this.nombre = this.items[0].nombre.S
      this.estado = this.items[0].estado.S

    },

    async getUsers() {
      if(this.aux.length >= 1){
        this.aux = []
        this.users = []
      }

      const accessToken = await this.$auth.getTokenSilently()

      // obtener lista de usuarios
      getAPI.get('/usuarios', {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      })
      .then(response => {
        this.aux = response.data 
        
        for(var i = 0;  i < this.aux.length; i++) {
          this.users.push({
            value: this.aux[i].user_id,
            text: this.aux[i].name
          })
        }

        this.booleanUsers = false
      })
    },

        // enviar métodos a componentes
    sendMethod(data) {
        if (data.methodCall) return this[data.methodCall]();
    },

    // en caso de error, desde el modal con el mensaje, regresar al modal crear
    modalBack() {
        this.$bvModal.hide('error_modal')
        this.$bvModal.show('modal-delete')
    },

    resetForm() {
      this.obraid = '',
      this.resume.splice(0)
      this.error_text = ''
      this.success_text = ''
    }

  },

  mounted() {
    this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
      if( modalId == 'modal-edit') {

        // guardar ID de obra
        this.obraid = this.items[0].obraId.S

        // obtener lista de usuarios
        this.getUsers()

        // determinar datos de obra
        this.setData()

        console.log('SE MOSTRARA EL MODAL DE EDIT', bvEvent, modalId)
      }
    })
  }
}
    
    

    
  

</script>

