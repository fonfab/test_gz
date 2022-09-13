<template>
  <div class="content-header">
    <div class="content-header__wrapper">
      <slot/>
    </div>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
</script>


<style lang="scss">
.content-header {
  width: 100%;
  min-height: 360px;

  background: linear-gradient(180deg, rgba(0, 0, 0, 0.138) -14.07%, rgba(0, 0, 0, 0) 41.75%),
  url('../../../public/bg/bg-logo.png') center;
  background-size: cover;

  border-radius: 0 0 20px 20px;

  z-index: 1;

  &__wrapper {
    max-width: 1280px;
    height: 100%;

    margin: 0 auto;
    padding: 50px 0;
  }
}

</style>
