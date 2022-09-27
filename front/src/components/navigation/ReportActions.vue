<template>
  <div class="report-actions">
    <SearchSecond/>

    <ButtonStyled text="Создать"
                  type="main"
                  subtype="main-green"
                  iconUrl="/icons/plus-round.svg"
                  iconType="svg"
                  :iconSize="20"
                  :disabled="props.createDisabled"
                  @click="createClick"/>

    <ButtonStyled text="Редактировать"
                  type="main"
                  subtype="main-blue"
                  iconUrl="/icons/pen-round.svg"
                  iconType="svg"
                  :iconSize="20"
                  :disabled="props.updateDisabled"
                  @click="updateClick"/>

    <ButtonStyled text="Удалить"
                  type="main"
                  subtype="main-red"
                  iconUrl="/icons/cross-round.svg"
                  iconType="svg"
                  :iconSize="20"
                  :disabled="props.deleteDisabled"
                  @click="deleteClick"/>
  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import ButtonStyled from '@/app_core/unit/components_styled/ButtonStyled.vue';
import SearchSecond from '@/components/search/SearchSecond.vue';


interface IProps {
  createDisabled: boolean,
  updateDisabled: boolean,
  deleteDisabled: boolean,
}

interface IEmits {
  (event: 'createClick'): void,
  (event: 'updateClick'): void,
  (event: 'deleteClick'): void,
}


const emits = defineEmits<IEmits>();
const props = defineProps<IProps>();


const createClick = () => emits('createClick');
const updateClick = () => emits('updateClick');
const deleteClick = () => emits('deleteClick');

</script>


<style lang="scss">
.report-actions {
  width: 100%;
  padding: 48px;

  display: grid;
  grid-auto-flow: column;
  grid-template-columns: 1fr max-content max-content max-content;
  grid-column-gap: 16px;

  background: white;
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);
  border-radius: 20px;

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
