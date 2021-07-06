<template>
  <div>
    <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>
    <b-button v-b-modal.modal-xlu class="normal-button">Subir Archivo</b-button>

    <dialog-upload :file=file />
  </div>
</template>

<script>
  export default {
    data() {
      return {
        file: null
      }
    },
  components: {
    'dialog-upload': require('@/components/reglamento/DialogUpload.vue').default
  }
  }
</script>