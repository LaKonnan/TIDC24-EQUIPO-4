<template>
  <div>
      <!-- botones -->
      <div class="buttons-obra">
        <b-button v-b-modal.modal-xlc class="normal-button">INGRESAR NUEVO</b-button>
        <b-button v-b-modal.modal-xld class="dark-button">ELIMINAR</b-button>
        <b-button v-b-modal.modal-xle class="disabled-button">EDITAR</b-button>
      
      </div>

      <!-- dialogs CRUD -->
       <dialog-create />
       <dialog-delete />
       <dialog-edit />
      
     
  </div>
</template>

<script>
export default {
  components: {
    'dialog-create': require('@/components/obras/DialogCreateObra').default,
    'dialog-delete': require('@/components/obras/DialogDeleteObra').default,
    'dialog-edit': require('@/components/obras/DialogEditObra').default
  }
}
</script>

<style>

</style>