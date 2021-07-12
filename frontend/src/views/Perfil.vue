<template>
  <div class="content">
    <div class="profile">
      <div class="picture">
        <img :src="$auth.user.picture">
      </div>

      <div class="data1">
        <h2>{{ $auth.user.name }}</h2>
        <p>{{ $auth.user.email }}</p>
      </div>
    </div>

    <div class="data2">
      <pre>{{ JSON.stringify($auth.user, null, 2) }}</pre>
    </div>
    

  </div>
</template>

<script>
  export default {

  }
</script>

<style lang="scss">
  @import '@/components/styles/profile.scss';
</style>