<template>
  <router-view/>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">

</script>


<style lang="scss">
@import "assets/styles/defaults";

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
