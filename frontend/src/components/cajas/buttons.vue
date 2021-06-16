<template>
  <div>
      
      <!-- botones -->
      <div class="buttons">
        <b-button v-b-modal.modal-create class="normal-button">INGRESAR NUEVO</b-button>
        <b-button v-b-modal.modal-delete class="dark-button" >ELIMINAR</b-button>
        <b-button v-b-modal.modal-edit class="normal-button">EDITAR</b-button>
        <b-button v-b-modal.modal-view class="normal-button">VER INFORMACIÓN COMPLETA</b-button>
      </div>

      <!-- dialogs CRUD -->
      <dialog-create />
      <dialog-delete :items="items" />
      <dialog-edit />
      <dialog-view :items="items" />
  </div>
</template>

<script>
export default {
  props: ['items'],
  data() {
    return {
      id: null
    }
  },
  components: {
    'dialog-create': require('@/components/cajas/DialogCreateCaja').default,
    'dialog-delete': require('@/components/cajas/DialogDelete').default,
    'dialog-edit': require('@/components/cajas/DialogEdit').default,
    'dialog-view': require('@/components/cajas/DialogView').default
  },
  
}
</script>

<style>

</style>