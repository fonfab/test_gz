<template>
  <div class="footer-navigation">
    <div class="footer-navigation__wrapper">

      <div class="footer-navigation__block">
        <LabelStyled text="Автор проекта: "
                     :fontSize="14"
                     color="gray"/>

        <LabelStyled text="Ильяс Шаехов"
                     :fontSize="14"
                     color="gray"/>
      </div>
      <div class="footer-navigation__block2">
        <img src="../../../public/icons/phone.svg" alt="">
        <LabelStyled text="My phone"
                     :fontSize="14"
                     color="gray"/>

        <img src="../../../public/icons/mail.svg" alt="">
        <LabelStyled text="My email"
                     :fontSize="14"
                     color="gray"/>
      </div>
    </div>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import LabelStyled from '@/app_core/unit/components_styled/LabelStyled.vue';
</script>


<style lang="scss">
.footer-navigation {
  width: 100%;

  background: #FFFFFF;
  border-radius: 20px 20px 0 0;

  z-index: 2;

  &__wrapper {
    max-width: 1280px;
    height: 100%;

    display: grid;
    grid-auto-flow: row;
    grid-row-gap: 36px;

    margin: 0 auto;
    padding: 72px 0;
  }

  &__block {
    display: grid;
    grid-auto-flow: row;
  }

  &__block2 {
    display: grid;
    grid-template-columns: max-content max-content;
    grid-column-gap: 7px;
    align-items: center;
  }
}

</style>
