<template>
  <span class="label-with-accent">
    <LabelStyled v-for="item in getTextStruct" :key="item"
                 :text="item.text"
                 :color="getProps(item.isAccent, 'color')"
                 :fontFamily="getProps(item.isAccent, 'fontFamily')"
                 :fontSize="getProps(item.isAccent, 'fontSize')"
                 :fontWeight="getProps(item.isAccent, 'fontWeight')"
                 :fontLineHeight="getProps(item.isAccent, 'fontLineHeight')"
                 :fontLetterSpacing="getProps(item.isAccent, 'fontLetterSpacing')"/>
  </span>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {computed} from 'vue';

import LabelStyled from '@/app_core/unit/components_styled/LabelStyled.vue';


interface IProps {
  text: string | number | null,

  // font parameters
  fontFamily?: string,
  fontSize?: number,
  fontWeight?: number,
  fontLineHeight?: number,
  fontLetterSpacing?: number,

  // font parameters accent
  fontFamilyAccent?: string,
  fontSizeAccent?: number,
  fontWeightAccent?: number,
  fontLineHeightAccent?: number,
  fontLetterSpacingAccent?: number,

  // text parameters
  color?: string,
  colorAccent?: string,
}

const props = defineProps<IProps>();

const getTextStruct = computed(() => {
  return props.text
      .split('**').map((item, index) => ({
        text: item,
        isAccent: index % 2 === 1,
      }))
      .filter((item) => item.text !== '');
});


const getProps = (isAccent: boolean, param: string) => {
  const accentParam = param + 'Accent';
  return isAccent ? props[accentParam] ?? props[param] : props[param];
};

</script>
