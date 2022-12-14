<template>
  <BaseView>

    <template v-slot:contentHeader>
      <div class="table-view__content-header">
        <ReportHeader :title="props.title"/>
        <ReportActions v-if="props.headerType === 'main'"
                       :createDisabled="selectedRows.length !== 0"
                       :updateDisabled="selectedRows.length !== 1"
                       :deleteDisabled="selectedRows.length < 1"
                       @deleteClick="deleteHandler"/>

        <ReportActionsSecond v-else-if="props.headerType === 'second'"
                             @renewClick="renewHandler"/>

        <template v-else/>
      </div>
    </template>

    <template v-slot:content>
      <TableComponent v-model:selectedRows="selectedRows"
                      :headers="getHeaders"
                      :rows="getRows"
                      :selectDisabled="props.selectDisabled"/>
    </template>

  </BaseView>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, ref} from 'vue';

import {ITableRow, ITableStruct, IId, ITableRowAction} from '@/store/types';

import BaseView from '@/views/unit/BaseView.vue';
import ReportHeader from '@/components/navigation/ReportHeader.vue';
import ReportActions from '@/components/navigation/ReportActions.vue';
import ReportActionsSecond from '@/components/navigation/ReportActionsSecond.vue';
import TableComponent from '@/app_core/unit/components/TableComponent.vue';


interface IProps {
  title: string,
  struct: ITableStruct[],
  data: unknown[],
  selectDisabled: boolean,
  headerType: 'main' | 'second',
}

interface IEmits {
  (event: 'deleteList', value: number[]): void
  (event: 'renewList'): void
}

const props = defineProps<IProps>();
const emits = defineEmits<IEmits>();

const selectedRows = ref<number[]>([]);


const getHeaders = computed(() => props.struct.map((item) => item.title));

const getRows = computed<ITableRow[]>(() => {
  return props.data.map((item): ITableRow => ({
    id: (item as IId).id,
    items: props.struct.filter((structItem) => structItem.type == null || structItem.type === 'text')
        .map((structItem) => structItem.value(item)),
    actions: props.struct.filter((structItem) => structItem.type === 'button')
        .map((structItem): ITableRowAction => ({
          title: structItem.value(item).toLocaleString(),
          href: structItem.href ? structItem.href(item) : '',
        })),
  }));
});


const deleteHandler = () => emits('deleteList', selectedRows.value);
const renewHandler = () => emits('renewList');

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
