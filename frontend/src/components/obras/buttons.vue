<template>
  <div>
      <!-- botones -->
      <div class="buttons-obra">
        <b-button v-b-modal.modal-xlc class="normal-button">INGRESAR NUEVO</b-button>
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
    'dialog-create': require('@/components/obras/DialogCreateObra').default,
    'dialog-delete': require('@/components/obras/DialogDeleteObra').default,
    'dialog-edit': require('@/components/obras/DialogEditObra').default
  }
  
}
</script>
