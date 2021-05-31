<template>
  <div>
      <!-- botones -->
      <div class="buttons">
        <b-button v-b-modal.modal-xl class="normal-button">INGRESAR NUEVO</b-button>
        <b-button class="dark-button">ELIMINAR</b-button>
        <b-button class="disabled-button" disabled>EDITAR</b-button>
        <b-button class="disabled-button" disabled>VER INFORMACIÓN COMPLETA</b-button>
      </div>

      <!-- dialogs CRUD -->
      <dialog-create />
  </div>
</template>

<script>
export default {
  components: {
    'dialog-create': require('@/components/cajas/DialogCreateCaja').default
  }
}
</script>

<style>

</style>