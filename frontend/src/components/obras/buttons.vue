<template>
  <div>
    <!-- botones -->
    <div class="buttons-obra">
      <b-button v-b-modal.modal-create class="normal-button">INGRESAR NUEVO</b-button>
      <b-button v-b-modal.modal-delete class="dark-button" @click="openModal('delete')" :disabled="selectedRow">ELIMINAR</b-button>
      <b-button v-b-modal.modal-edit class="normal-button" :disabled="selectedRow">EDITAR</b-button>
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

  components: {
    'dialog-create': require('@/components/obras/DialogCreateObra').default,
    'dialog-delete': require('@/components/obras/DialogDeleteObra').default,
    'dialog-edit': require('@/components/obras/DialogEditObra').default
  },

  methods: {
    openModal(act) {
      switch(act) {
        case 'delete':
          console.log('delete')
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
