<template>
  <div class="content">
        <!-- titulo -->
        <p class="dark-title">GESTIÓN DE MÁQUINAS Y VEHÍCULOS</p>
        <hr class="hr">

        <!-- tabla de contenidos -->
        <maquinas-table @items="rowItems"/>

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

    methods: {
        rowItems(params) {
            this.items = params
        }
    },

    componentS: {
        'maquinas-table': require('@/components/maquinas/table').default,

    }
}
</script>

<style>

</style>