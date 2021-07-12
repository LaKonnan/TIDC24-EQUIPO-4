<template>
    <div>
      <b-modal id="modal-delete" size="xl" title="ELIMINAR OBRA" hide-footer>    
        <b-card-text>
          <b-table stacked :items="resume"></b-table>
        </b-card-text>
        <center>
          <p><b>IMPORTANTE: </b>Una vez eliminada la obra, no podrá ser recuperada.</p>
          <p><b>Para confirmar, escribir el ID de la obra</b></p>
        </center>
        <b-form-input v-model="password" style="text-align: center;" @keyup="activateButton()"></b-form-input>
                
        <b-button  class="button-next dark-button" :disabled="button" @click="deleteObra()">Eliminar Obra</b-button>
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
      obraid:'',
      password:'',
      resume: [],
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
    activateButton() {
      this.button = false
    },

    async deleteObra(){
      const accessToken = await this.$auth.getTokenSilently()

      const options = {
        headers: {
         'Content-Type': 'application/json;charset=UTF-8',
         'Access-Control-Allow-Origin': '*',
         'Authorization': `Bearer ${accessToken}`
        }
      }
      console.log('PASS: '+ this.password + 'OBRA: '+ this.obraid)
     if(this.password == this.obraid){
       getAPI.delete('/obras/'+this.items[0].obraId.S, options)
        .then((res) =>{
          console.log('Datos Eliminados: ', res)
            // mensaje de exito
            this.success_text = 'Obra '+ this.obraid + 'creada con éxito'

            // mostrar modal de éxito
            this.$bvModal.hide('modal-delete')
            this.$bvModal.show('success_modal')

        })
        .catch((err)=>{
          console.log('Error: ', err)
        })
      }else{
        // error
        this.error_text = 'ERROR - El ID es incorrecto'

        // mostrar modal de éxito
        this.$bvModal.hide('modal-delete')
        this.$bvModal.show('error_modal')
      }
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
      this.password = ''
    }
  },

  mounted() {
    this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
      if( modalId == 'modal-delete') {

        // guardar ID de obra
        this.obraid = this.items[0].obraId.S

        // determinar datos de obra
        this.resume.push({
          ID: this.items[0].obraId.S,
          Tipo: this.items[0].tipo.S,
          Encargado: this.items[0].encargado.S,
          Nombre: this.items[0].nombre.S,
          Estado: this.items[0].estado.S
        })

        console.log('SE MOSTRARA EL MODAL DE DELETE', bvEvent, modalId)
      }
    })
  }
}  
  

</script>
 