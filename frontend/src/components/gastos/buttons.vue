<template>
  <div>
      <!-- botones -->
      <div class="buttons">
        <b-button v-b-modal.modal-xlc class="normal-button">INGRESAR NUEVO GASTO</b-button>
        <b-button v-b-modal.modal-xld class="dark-button" :disabled="selectedRow" >ELIMINAR</b-button>
        <b-button v-b-modal.modal-xle class="normal-button" :disabled="selectedRow" >EDITAR</b-button>
      
      </div>

      <!-- dialogs CRUD -->
       <dialog-create />
       <dialog-delete :items="items"/>
       <dialog-edit :items="items"/>
      
     
  </div>
</template>

<script>
export default {
  props: ['selectedRow','items'],
  data() {
    return {

    }
  },
  components: {
    'dialog-create': require('@/components/gastos/DialogCreate').default,
    'dialog-delete': require('@/components/gastos/DialogDelete').default,
    'dialog-edit': require('@/components/gastos/DialogEdit').default
  }
  
}
</script>