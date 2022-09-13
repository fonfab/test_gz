<template>
  <span v-html="getText" :class="['label', ...getClasses]"/>
</template>


<script lang="ts">

export const componentName = 'LabelComponent';
export const componentNameClass = 'label';

export const noClassAttributes = ['text', 'toFixedIndex'];

export const validators = {
  fontFamily: [''] as Array<string>,
  fontSize: [10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 48, 56, 64] as Array<number>,
  fontWeight: [100, 200, 300, 400, 500, 600, 700, 800, 900] as Array<number>,
  fontLineHeight: [100, 150, 200] as Array<number>,
  fontLetterSpacing: [0] as Array<number>,

  location: ['left', 'center', 'right'] as Array<string>,
  upperCase: [false, true] as Array<boolean>,
  noWrap: [false, true] as Array<boolean>,
  textDecoration: ['line-through', 'underline', 'none'] as Array<string>,
};

export default {};
</script>


<script setup lang="ts">
import {computed} from 'vue';
import classesFromPropsHook from '@/app_core/core/assets/scripts/hooks/classesFromPropsHook';


interface IProps {
  text: string | number | null,

  // font parameters
  fontFamily?: typeof validators.fontFamily[number],
  fontSize?: typeof validators.fontSize[number],
  fontWeight?: typeof validators.fontWeight[number],
  fontLineHeight?: typeof validators.fontLineHeight[number],
  fontLetterSpacing?: typeof validators.fontLetterSpacing[number],

  // text parameters
  location?: typeof validators.location[number],
  upperCase?: typeof validators.upperCase[number],
  noWrap?: typeof validators.noWrap[number],
  textDecoration?: typeof validators.textDecoration[number],

  toFixedIndex?: number,
}


const props = defineProps<IProps>();
const {getClasses} = classesFromPropsHook(props,
    componentName, componentNameClass, noClassAttributes, validators);


const getText = computed(() => {
  let text = props.text;

  if (text == null) return '';
  if (typeof text === 'number') text = Number(text.toFixed(props.toFixedIndex ?? 2)).toLocaleString();
  if (props.upperCase) text = text.toUpperCase();

  return text;
});

</script>

<style lang="scss">
@import '../../../assets/styles/base.scss';

.label {
  font-family: Montserrat, sans-serif;
  font-style: normal;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;

  text-align: left;
  color: black;

  transition: all 0.2s;

  &__font-family {
  }

  &__font-size {
    &__10 {
      font-size: 10px;
    }

    &__12 {
      font-size: 12px;
    }

    &__14 {
      font-size: 14px;
    }

    &__16 {
      font-size: 16px;
    }

    &__18 {
      font-size: 18px;
    }

    &__20 {
      font-size: 20px;
    }

    &__24 {
      font-size: 24px;
    }

    &__28 {
      font-size: 28px;
    }

    &__32 {
      font-size: 32px;
    }

    &__36 {
      font-size: 36px;
    }

    &__40 {
      font-size: 40px;
    }

    &__48 {
      font-size: 48px;
    }

    &__56 {
      font-size: 56px;
    }

    &__64 {
      font-size: 64px;
    }
  }

  &__font-weight {
    &__100 { font-weight: 100; }
    &__200 { font-weight: 200; }
    &__300 { font-weight: 300; }
    &__400 { font-weight: 400; }
    &__500 { font-weight: 500; }
    &__600 { font-weight: 600; }
    &__700 { font-weight: 700; }
    &__800 { font-weight: 800; }
    &__900 { font-weight: 900; }
  }

  &__text-decoration {
    &__line-through { text-decoration: line-through;  }
    &__underline    { text-decoration: underline;     }
    &__none         { text-decoration: none;          }
  }

  &__font-line-height {
    &__100 { line-height: 100% }
    &__150 { line-height: 150% }
    &__200 { line-height: 200% }
  }

  &__location {
    &__left   { text-align: left;   }
    &__center { text-align: center; }
    &__right  { text-align: right;  }
  }

  &__no-wrap    { white-space: nowrap;        }
  &__upper-case { text-transform: uppercase;  }
}

</style>
