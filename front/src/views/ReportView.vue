<template>
  <TableView :title="texts.title"
             :struct="struct"
             :data="getList"
             :selectDisabled="true"
             headerType="second"
             @renewList="renewList"/>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, onMounted} from 'vue';
import useReportStore from '@/store/reportStore';

import {IReport, ITableStruct} from '@/store/types';

import TableView from '@/views/unit/TableView.vue';


const texts = {
  title: 'Отчет',
};


const struct: ITableStruct[] = [
  {
    title: 'Рейтинг',
    value: (item) => (item as IReport).rating_name,
  },
  {
    title: 'Объем, тыс. куб. м',
    value: (item) => (item as IReport).amount,
  },
  {
    title: 'Цена, долл. США / тыс. куб. м',
    value: (item) => (item as IReport).cost,
  },
];


const reportStore = useReportStore();


const getList = computed(() => reportStore.getList);


const renewList = () => {
  reportStore.clearList();
  reportStore.loadList();
};


onMounted(() => {
  if (getList.value.length === 0) reportStore.loadList();
});

</script>


<style lang="scss">

</style>
