<template>
  <div class="content">
    <br>

    <!-- resumen -->
    <resume />

    <!-- tabla de contenidos -->
    <table-cajas @items="rowItems"/>

    <!-- botones -->
    <buttons :items="items" />

  </div>
</template>

<script>

export default {
    name: 'cajas',
    data() {
      return {
        items: []
      }
    },
    

    components: {
      'table-cajas': require('../components/cajas/all_table').default,
      'buttons': require('../components/cajas/buttons').default,
      'resume': require('../components/cajas/resumen_global').default
    },

    methods: {
      rowItems(params){
        this.items = params;
      }
    }
}
</script>

<style lang="scss">
  @import '@/components/styles/global.scss';
</style>