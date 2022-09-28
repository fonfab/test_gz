<template>
  <TableView :title="texts.title"
             :struct="struct"
             :data="getList"
             @deleteList="deleteHandler"/>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, onMounted} from 'vue';
import useCounterpartyStore from '@/store/counterpartyStore';

import {ICounterparty, ITableStruct} from '@/store/types';

import TableView from '@/views/unit/TableView.vue';


const texts = {
  title: 'Контрагенты',
};


const struct: ITableStruct[] = [
  {
    title: 'Контрагент',
    value: (item) => (item as ICounterparty).name,
  },
  {
    title: 'Рейтинг',
    value: (item) => (item as ICounterparty).rating.rating,
  },
  {
    title: 'Сделки',
    type: 'button',
    href: (item) => `/deal?counterparty_id=${(item as ICounterparty).id}`,
    value: () => 'Показать',
  },
];


const counterpartyStore = useCounterpartyStore();


const getList = computed(() => counterpartyStore.getList);


const deleteHandler = (ids: number[]) => {
  counterpartyStore.deleteList(ids);
};


onMounted(() => {
  if (getList.value.length === 0) counterpartyStore.loadList();
});

</script>


<style lang="scss">

</style>
