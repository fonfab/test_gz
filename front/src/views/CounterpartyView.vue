<template>
  <BaseView>

    <template v-slot:contentHeader>
      <div class="counterparty-view__content-header">
        <ReportHeader :title="texts.title"/>
        <ReportActions/>
      </div>
    </template>

    <template v-slot:content>
      {{getList}}
    </template>

  </BaseView>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed, onMounted} from 'vue';
import useCounterpartyStore from '@/store/counterpartyStore';

import BaseView from '@/views/unit/BaseView.vue';
import ReportHeader from '@/components/navigation/ReportHeader.vue';
import ReportActions from '@/components/navigation/ReportActions.vue';


const texts = {
  title: 'Контрагенты',
};

const counterpartyStore = useCounterpartyStore();


const getList = computed(() => counterpartyStore.getList);

onMounted(() => {
  counterpartyStore.loadList();
});

</script>


<style lang="scss">

.counterparty-view {
  &__content-header {
    display: grid;
    grid-auto-flow: row;
    grid-row-gap: 50px;
  }

  &__content {

  }
}

</style>
