<template>
  <div>
      <!-- botones -->
      <div class="buttons">
        <b-button v-b-modal.modal-create class="normal-button">INGRESAR NUEVO</b-button>
        <b-button v-b-modal.modal-delete class="dark-button">ELIMINAR</b-button>
        <b-button v-b-modal.modal-edit class="normal-button" :disabled="btnEditar" >EDITAR</b-button>
        <b-button class="normal-button" :disabled="btnInfo">VER INFORMACIÓN COMPLETA</b-button>
        <!-- disabled-button -->
      </div>

      <!-- dialogs CRUD -->
      <dialog-create />
      <dialog-delete />
      <dialog-edit />

  </div>
</template>

<script>
export default {
  data() {
    return {
      btnEditar: false,
      btnInfo: false
    }
  },
  components: {
    'dialog-create': require('@/components/cajas/DialogCreateCaja').default,
    'dialog-delete': require('@/components/cajas/DialogDelete').default,
    'dialog-edit': require('@/components/cajas/DialogEdit').default
  }
}
</script>

<style>

</style>