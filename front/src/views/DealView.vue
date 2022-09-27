<template>
  <TableView :title="texts.title"
             :struct="struct"
             :data="getList"/>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, onMounted} from 'vue';
import useDealStore from '@/store/dealStore';

import {IDeal, ITableStruct} from '@/store/types';

import TableView from '@/views/unit/TableView.vue';


const texts = {
  title: 'Сделки',
};


const struct: ITableStruct[] = [
  {
    title: 'Контрагент',
    value: (item) => (item as IDeal).type.name,
  },
  {
    title: 'Дата и время сделки',
    value: (item) => new Date((item as IDeal).deal_date).toLocaleDateString(),
  },
  {
    title: 'Контрагент',
    value: (item) => (item as IDeal).counterparty.name,
  },
  {
    title: 'Пункт поставки',
    value: (item) => (item as IDeal).destination_place.name,
  },
  {
    title: 'Инструмент',
    value: (item) => (item as IDeal).inventory.name,
  },
  {
    title: 'Начало поставки',
    value: (item) => new Date((item as IDeal).start_date).toLocaleDateString(),
  },
  {
    title: 'Конец поставки',
    value: (item) => new Date((item as IDeal).end_date).toLocaleDateString(),
  },
  {
    title: 'Объем, МВт',
    value: (item) => (item as IDeal).amount,
  },
  {
    title: 'Цена, евро / МВт * ч',
    value: (item) => (item as IDeal).cost,
  },
];


const dealStore = useDealStore();


const getList = computed(() => dealStore.getList);


onMounted(() => {
  dealStore.loadList();
});

</script>


<style lang="scss">

</style>
