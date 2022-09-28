<template>
  <div class="report-actions-second">
    <ButtonStyled text="Обновить данные"
                  type="main"
                  subtype="main-second"
                  @click="renewClick"/>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import ButtonStyled from '@/app_core/unit/components_styled/ButtonStyled.vue';


interface IEmits {
  (event: 'renewClick'): void,
  (event: 'downloadClick'): void,
}


const emits = defineEmits<IEmits>();


const renewClick = () => emits('renewClick');
// const downloadClick = () => emits('downloadClick');

</script>


<style lang="scss">
.report-actions-second {
  width: 100%;
  padding: 48px;

  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: max-content;
  grid-column-gap: 16px;

  background: white;
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);
  border-radius: 20px;
}

</style>
