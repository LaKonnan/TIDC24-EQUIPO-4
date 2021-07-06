<template>
  <div class="content">
      <reglamentoPDF/>
      <subirPDF/>
  </div>
</template>

<script>
  export default {
    components: {
            'reglamentoPDF': require('../components/reglamento/reglamentoPDF.vue').default,
            'subirPDF': require('../components/reglamento/subirPDF.vue').default
    }
  }
</script>