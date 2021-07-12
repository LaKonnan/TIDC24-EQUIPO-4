<template>
    <div>
      <b-modal ref="create" id="modal-create" size="xl" title="REGISTRAR NUEVA OBRA" hide-footer @hidden="resetForm">
        <b-card-text>
          <!-- ID -->
          <b-form-group label="ID - Recurso">
            <b-form-input 
              v-model="obraid" 
              @keyup="activateButton()" 
              type="number">
            </b-form-input>
          </b-form-group>

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
              :disabled="booleanUsers"
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
            <p><b>Una vez presionado el botón, se registrará la obra en el sistema.</b></p>
          </center>
          <b-button class="button-next normal-button" @click="create()">GUARDAR</b-button>
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
   
  data() {
    return {
      // variables 
      success_text: '',
      error_text: '',
      aux: [],
      users: [],
      rol: '',
      booleanUsers: true,
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
    // habilitar botón para registrar nueva obra
    activateButton(){
      switch(this.tabIndex){
        case 0:
          if(![this.obraid, this.encargado, this.nombre, this.estado, this.tipo].includes(null)) {
            this.btnStep1 = false
            this.step2 = false
          }
        break

        case 1:
          break
        }
      
    },

    // registrar nueva obra
    async create(){
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

      getAPI.post('/obras', data, options)
          .then((res) =>{
            // mensaje de exito
            this.success_text = 'Obra '+ this.obraid + 'creada con éxito'

            this.resetForm()

            // mostrar modal de éxito
            this.$bvModal.hide('modal-create')
            this.$bvModal.show('success_modal')
            
            console.log(res)
          })
          .catch((err)=>{
            console.log('Error: ', err)
          })
    },


    // obtener usuarios
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

    // regresar variables a su estado original
    resetForm() {
      this.aux.splice(0)
      this.users.splice(0)
      this.booleanUsers = true
      this.obraid =''
      this.encargado = ''
      this.nombre = ''
      this.success = false
      this.tabIndex = 2
      this.btnStep1 = true
      this.step2 = true
      this.estado = null
      this.tipo = null
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

}

</script>

