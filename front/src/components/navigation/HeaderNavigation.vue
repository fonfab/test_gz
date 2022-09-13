<template>
  <div class="header-navigation">
    <div class="header-navigation__wrapper">
      <img src="../../../public/icons/logo.svg" alt="">

      <ButtonStyled text="Сделки"
                    href="/deal"
                    :fontSize="16"
                    type="main"
                    subtype="main-first"/>

      <ButtonStyled text="Контрагенты"
                    href="/counterparty"
                    :fontSize="16"
                    type="main"
                    subtype="main-first"/>

      <ButtonStyled text="Отчеты"
                    :fontSize="16"
                    type="main"
                    subtype="main-first"/>
    </div>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import ButtonStyled from '@/app_core/unit/components_styled/ButtonStyled.vue';
</script>


<style lang="scss">
@import "src/assets/styles/base";

.header-navigation {
  width: 100%;

  background: #FFFFFF;
  box-shadow: 0 4px 20px rgba(1, 36, 88, 0.2);

  z-index: 2;

  &__wrapper {
    max-width: 1280px;
    height: 100%;

    display: grid;
    grid-auto-flow: column;
    grid-template-columns: 1fr repeat(3, max-content);
    grid-column-gap: 20px;
    align-items: center;

    margin: 0 auto;
    padding: 30px 0;

    img {
      width: 218px;
      height: 40px;
    }

    .router-link-active {
      pointer-events: none;

      background: $text-blue;
      border: 1px solid $text-blue;

      .label {
        color: $white;
      }
    }
  }
}

</style>
