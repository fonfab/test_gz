<template>
  <BaseView>

    <template v-slot:contentHeader>
      <div class="table-view__content-header">
        <ReportHeader :title="props.title"/>
        <ReportActions :createDisabled="selectedRows.length !== 0"
                       :updateDisabled="selectedRows.length !== 1"
                       :deleteDisabled="selectedRows.length < 1"
                       @deleteClick="deleteHandler"/>
      </div>
    </template>

    <template v-slot:content>
      <TableComponent v-model:selectedRows="selectedRows"
                      :headers="getHeaders"
                      :rows="getRows"/>
    </template>

  </BaseView>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, ref} from 'vue';

import {ITableRow, ITableStruct, IId} from '@/store/types';

import BaseView from '@/views/unit/BaseView.vue';
import ReportHeader from '@/components/navigation/ReportHeader.vue';
import ReportActions from '@/components/navigation/ReportActions.vue';
import TableComponent from '@/app_core/unit/components/TableComponent.vue';


interface IProps {
  title: string,
  struct: ITableStruct[],
  data: unknown[],
}

interface IEmits {
  (event: 'deleteList', value: number[]): void
}

const props = defineProps<IProps>();
const emits = defineEmits<IEmits>();

const selectedRows = ref<number[]>([]);


const getHeaders = computed(() => props.struct.map((item) => item.title));

const getRows = computed<ITableRow[]>(() => {
  return props.data.map((item): ITableRow => ({
    id: (item as IId).id,
    items: props.struct.map((structItem) => structItem.value(item)),
  }));
});


const deleteHandler = () => {
  emits('deleteList', selectedRows.value);
};

</script>


<style lang="scss">

.table-view {
  &__content-header {
    display: grid;
    grid-auto-flow: row;
    grid-row-gap: 50px;
  }

  &__content {

  }
}

</style>
