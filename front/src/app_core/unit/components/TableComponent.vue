<template>
  <table class="table">
    <tr>
      <th/>
      <th v-for="item in props.headers" :key="item">
        <LabelStyled :text="item"
                     :fontSize="14"
                     :fontWeight="700"
                     location="left"/>
      </th>
    </tr>

    <tr v-for="row in props.rows" :key="row"
        :class="{selected: isSelected(row.id)}"
        @click="selectRow(row.id)">

      <td class="table__check">
        <IconComponent url="/icons/check.svg"
                       type="svg"/>
      </td>

      <td v-for="item in row.items" :key="item">
        <LabelStyled :text="item"
                     :fontSize="14"
                     :fontWeight="400"
                     location="left"/>
      </td>
    </tr>

  </table>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {ref, watch} from 'vue';

import {ITableRow} from '@/store/types';

import LabelStyled from '@/app_core/unit/components_styled/LabelStyled.vue';
import IconComponent from '@/app_core/unit/components/IconComponent.vue';


interface IProps {
  headers: string[],
  rows: ITableRow[],
  selectedRows: number[],
}

interface IEmits {
  (event: 'update:selectedRows', value: number[]): void
}


const props = defineProps<IProps>();
const emits = defineEmits<IEmits>();

const selectedRows = ref<number[]>(props.selectedRows);


const isSelected = (id: number) => selectedRows.value.some((item) => item === id);

const selectRow = (id: number) => {
  if (isSelected(id)) {
    selectedRows.value = selectedRows.value.filter((item) => item !== id);
  } else {
    selectedRows.value.push(id);
  }
};


watch(
    selectedRows,
    (value) => emits('update:selectedRows', value),
    {deep: true},
);

</script>


<style lang="scss">
@import '../../../assets/styles/base';

.table {
  width: 100%;
  border-collapse: collapse;
  //table-layout: fixed;

  &__check {
    width: calc(18px * 2 + 16px);
  }

  tr {
    transition: background 0.2s;

    &:nth-child(2n) {
      background: white;
    }

    &:not(:first-child) {
      cursor: pointer;

      &:hover {
        background: #DEF2FF;
      }
    }

    &+.selected {
      background: #DEF2FF;

      .icon {
        background: #0079C2;
      }
    }

    th {
      position: relative;
      max-width: 150px;
      padding: 18px 18px;

      text-align: left;
      word-wrap: break-word;

      &:not(:first-child):not(:nth-child(2)) {
        &:before {
          content: '';
          position: absolute;
          left: 0;
          top: 8px;
          bottom: 8px;
          width: 1px;

          background: #B9E4FF;
        }
      }
    }

    td {
      max-width: 150px;
      padding: 18px 18px;

      word-wrap: break-word;
    }
  }
}

</style>
