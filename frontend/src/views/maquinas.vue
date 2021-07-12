<template>
  <div class="content">
        <!-- tabla de contenidos -->
        <maq-table @items="rowItems"/>

        <!-- botones -->
        <buttons :items="items" />
  </div>
</template>

<script>
export default {
    name: 'maquinas',
    data() {
        return {
            items: []
        }
    },
    
    components: {
        'maq-table': require('@/components/maquinas/table').default,
        'buttons': require('@/components/maquinas/buttons').default,
    },

    methods: {
        rowItems(params) {
            this.items = params
        }
    }
}
</script>

<style lang="scss">
    @import '@/components/styles/global.scss';
</style>