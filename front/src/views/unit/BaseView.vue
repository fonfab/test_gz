<template>
  <div class="base-view">
    <HeaderNavigation/>
    <ContentHeader>
      <slot name="contentHeader"/>
    </ContentHeader>

    <div class="base-view__content">
      <slot name="content"/>
    </div>

    <FooterNavigation/>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import HeaderNavigation from '@/components/navigation/HeaderNavigation.vue';
import ContentHeader from '@/components/navigation/ContentHeader.vue';
import FooterNavigation from '@/components/navigation/FooterNavigation.vue';
</script>


<style lang="scss">
@import "src/assets/styles/base";
.base-view {
  min-height: 100vh;

  display: grid;
  grid-auto-flow: row;
  grid-template-rows: max-content max-content 1fr max-content;

  background: $background-blue;

  &__content {
    width: 100%;
    max-width: 1280px;
    height: 100%;

    margin: 0 auto;
    padding: 70px 0;
  }
}
</style>
