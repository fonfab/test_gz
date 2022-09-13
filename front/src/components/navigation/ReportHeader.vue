<template>
  <div class="report-header">
    <div class="report-header__title">
      <LabelStyled :text="props.title"
                   :fontSize="56"
                   :fontWeight="300"
                   :fontLineHeight="100"
                   color="white"/>

      <div class="report-header__title__separator"/>

      <ButtonStyled href="/"
                    iconUrl="/icons/cross-round.svg"
                    :iconSize="30"
                    type="label"
                    subtype="label-light-blue"/>
    </div>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import LabelStyled from '@/app_core/unit/components_styled/LabelStyled.vue';
import ButtonStyled from '@/app_core/unit/components_styled/ButtonStyled.vue';


interface IProps {
  title: string,
}


const props = defineProps<IProps>();

</script>


<style lang="scss">
.report-header {
  width: 100%;

  display: grid;
  grid-auto-flow: row;
  grid-row-gap: 50px;

  &__title {
    display: grid;
    grid-auto-flow: column;
    grid-template-columns: max-content 1fr max-content;
    grid-column-gap: 32px;
    align-items: flex-end;

    &__separator {
      width: 100%;
      height: 1px;
      margin-bottom: 20px;

      background: white;
    }

    .button {
      margin-bottom: 5px;
    }
  }
}

</style>
