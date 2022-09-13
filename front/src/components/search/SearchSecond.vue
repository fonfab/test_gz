<template>
  <div class="search-second">
    <div class="search-second__icon"/>

    <input class="search-second__input"
           type="text"
           placeholder="Введите запрос">

    <ButtonStyled iconUrl="/icons/settings.svg"
                  :fontSize="16"
                  type="label"
                  subtype="label-gray"/>
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

.search-second {
  width: 100%;
  max-width: 500px;
  padding: 15px 32px;

  display: grid;
  grid-template-columns: max-content 1fr max-content;
  grid-column-gap: 8px;
  align-items: center;

  border: 1px solid #ECECEC;
  border-radius: 50px;

  z-index: 1;

  &__icon {
    width: 23px;
    height: 23px;

    display: flex;
    justify-content: center;
    align-items: center;

    mask: url("../../../public/icons/search.svg");
    mask-size: contain;
    background: #BEE6FF;
  }

  &__input {
    height: 100%;

    font-family: Montserrat, sans-serif;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 125%;

    border-radius: 50px;

    &::placeholder {
      font-family: Montserrat, sans-serif;
      font-size: 16px;
      font-style: normal;
      font-weight: 400;
      line-height: 125%;

      color: $text-gray-2;
    }
  }
}

</style>
