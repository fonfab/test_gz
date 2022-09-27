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

import {ICounterparty, ITableStruct} from '@/store/types';

import TableView from '@/views/unit/TableView.vue';


const texts = {
  title: 'Сделки',
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


const dealStore = useDealStore();


const getList = computed(() => dealStore.getList);


onMounted(() => {
  dealStore.loadList();
});

</script>


<style lang="scss">

</style>
