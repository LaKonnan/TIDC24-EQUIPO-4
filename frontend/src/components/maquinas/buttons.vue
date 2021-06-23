<template>
  <div>
      
      <!-- botones -->
      <div class="buttons">
        <b-button v-b-modal.modal-create class="normal-button">INGRESAR NUEVO</b-button>
        <b-button v-b-modal.modal-delete class="dark-button" @click="openModal('delete')">ELIMINAR</b-button>
        <b-button v-b-modal.modal-edit class="normal-button" @click="openModal('edit')">EDITAR</b-button>
        <b-button v-b-modal.modal-view class="normal-button" @click="openModal('view')">VER INFORMACIÓN COMPLETA</b-button>
      </div>

      <!-- dialogs CRUD -->
      <dialog-create />
      <dialog-delete :items="items" />
      <dialog-edit :items="items" />
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
    'dialog-create': require('@/components/maquinas/DialogCreateCaja').default,
    'dialog-delete': require('@/components/maquinas/DialogDelete').default,
    'dialog-edit': require('@/components/maquinas/DialogEdit').default,
    'dialog-view': require('@/components/maquinas/DialogView').default
  },

  methods: {
    openModal(act) {
      switch(act) {
        case 'delete':
          this.$root.$emit('bv::show::modal', 'modal-delete')
          break
        
        case 'edit':
          this.$root.$emit('bv::show::modal', 'modal-edit')
          break
        
        case 'view':
          this.$root.$emit('bv::show::modal', 'modal-view')
          break

      }
      
    }
  }
  
}
</script>

<style>

</style>