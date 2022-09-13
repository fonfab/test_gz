<template>
  <BaseView>

    <template v-slot:contentHeader>
      <div class="deal-view__content-header">
        <ReportHeader :title="texts.title"/>
        <ReportActions/>
      </div>
    </template>

    <template v-slot:content>

    </template>

  </BaseView>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import BaseView from '@/views/unit/BaseView.vue';
import ReportHeader from '@/components/navigation/ReportHeader.vue';
import ReportActions from '@/components/navigation/ReportActions.vue';


const texts = {
  title: 'Сделки',
};

</script>


<style lang="scss">

.deal-view {
  &__content-header {
    display: grid;
    grid-auto-flow: row;
    grid-row-gap: 50px;
  }

  &__content {

  }
}

</style>
