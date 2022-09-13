<template>
  <div class="search-first">
    <div class="search-first__icon"/>

    <input class="search-first__input"
           type="text"
           placeholder="Что будем искать?">

    <ButtonStyled text="Найти"
                  :fontSize="16"
                  type="main"
                  subtype="main-second"/>
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

.search-first {
  width: 100%;
  margin-top: 16px;
  padding: 16px 16px 16px 24px;

  display: grid;
  grid-template-columns: max-content 1fr max-content;
  grid-column-gap: 16px;
  align-items: center;

  background: linear-gradient(180deg, #E1F5FF 10.94%, #BEE6FF 72.4%);
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);

  border-radius: 50px;

  z-index: 1;

  &__icon {
    width: 32px;
    height: 32px;

    display: flex;
    justify-content: center;
    align-items: center;

    mask: url("../../../public/icons/search.svg");
    background: $text-blue;
  }

  &__input {
    height: 100%;
    padding: 16px 32px;

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
