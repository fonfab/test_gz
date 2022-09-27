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
];


const counterpartyStore = useCounterpartyStore();


const getList = computed(() => counterpartyStore.getList);


const deleteHandler = (ids: number[]) => {
  counterpartyStore.deleteList(ids);
};


onMounted(() => {
  counterpartyStore.loadList();
});

</script>


<style lang="scss">

</style>
