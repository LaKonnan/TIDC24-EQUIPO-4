<template>
  <div>
      <!-- botones -->
      <div class="buttons-obra">
        <b-button v-b-modal.modal-xlc class="normal-button">NUEVO USUARIO</b-button>
        <b-button v-b-modal.modal-xle class="normal-button" id="btnEditar" :disabled="selectedRow" >EDITAR</b-button>
        <b-button v-b-modal.modal-xld class="dark-button" :disabled="selectedRow">ELIMINAR</b-button>
      </div>

      <!-- dialogs CRUD -->
       <dialog-create :table=table />
       <dialog-delete :table=table :items="items"/>
       <dialog-edit :table=table :items="items"/>
      
  </div>
</template>


<script>

export default {
  props: ['selectedRow','items','table'],
  data() {
    return {
    }
  },
  components: {
    'dialog-create': require('@/components/usuarios/DialogCreate').default,
    'dialog-delete': require('@/components/usuarios/DialogDelete').default,
    'dialog-edit': require('@/components/usuarios/DialogEdit').default
  }
}
</script>
