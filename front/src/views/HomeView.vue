<template>
  <BaseView>

    <template v-slot:contentHeader>
      <div class="home-view__content-header">
        <SearchFirst/>
        <div class="home-view__content-header__items">
          <div class="home-view__content-header__items__wrapper">
            <CardMain v-for="item in struct" :key="item"
                      :title="item.title"
                      :buttonTitle="item.buttonTitle"
                      :buttonHref="item.buttonHref"
                      :colorType="item.colorType"
                      :items="item.items"
                      color="gray-3"/>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:content>
      <div class="home-view__content"/>
    </template>

  </BaseView>
</template>


<script setup lang="ts">
import {EColorType, ICardMainStructItem} from '@/store/types';

import BaseView from '@/views/unit/BaseView.vue';
import SearchFirst from '@/components/search/SearchFirst.vue';
import CardMain from '@/components/navigation/CardMain.vue';


interface IStruct {
  title: string,
  buttonTitle: string,
  buttonHref: string,
  colorType: EColorType,
  items: ICardMainStructItem[],
}


const struct: IStruct[] = [
  {
    title: 'База сделок',
    buttonTitle: 'Изучить',
    buttonHref: '/deal',
    colorType: EColorType.GREEN,
    items: [
      {
        icon: '1',
        text: 'Просмотр сделок',
      },
      {
        icon: '2',
        text: 'Добавление сделок',
      },
      {
        icon: '3',
        text: 'Фильтр по контрагентам',
      },
    ],
  },
  {
    title: 'Отчеты отдела',
    buttonTitle: 'Перейти',
    buttonHref: '',
    colorType: EColorType.BLUE,
    items: [
      {
        icon: '4',
        text: 'Сводный отчет',
      },
      {
        icon: '5',
        text: 'EOD, EOW',
      },
      {
        icon: '6',
        text: 'Сводка MDP и т.д.',
      },
    ],
  },
  {
    title: 'Контрагенты',
    buttonTitle: 'Настроить',
    buttonHref: '/counterparty',
    colorType: EColorType.PURPLE,
    items: [
      {
        icon: '7',
        text: 'Добавление контрагентов',
      },
      {
        icon: '8',
        text: 'Просмотр контрагентов',
      },
      {
        icon: '9',
        text: 'Фильтр по контрагентам',
      },
    ],
  },
];

</script>


<style lang="scss">

.home-view {
  &__content-header {
    display: grid;
    grid-auto-flow: row;
    grid-row-gap: 56px;

    &__items {
      position: relative;

      &__wrapper {
        position: absolute;
        left: 0;
        right: 0;

        display: grid;
        grid-auto-flow: column;
        grid-column-gap: 24px;
      }
    }
  }

  &__content {
    height: 300px;
  }
}

</style>
