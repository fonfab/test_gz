<template>
  <LabelComponent :class="getClasses"/>
</template>


<script lang="ts">

export const componentName = 'LabelStyled';
export const componentNameClass = 'label';

export const noClassAttributes = [];
export const validators = {
  color: [
    'white', 'black', 'blue', 'red',
    'gray', 'gray-2', 'gray-3', 'gray-4',
    'green', 'green-2',
  ] as Array<string>,
};

export default {};
</script>


<script setup lang="ts">
import classesFromPropsHook from '@/app_core/core/assets/scripts/hooks/classesFromPropsHook';

import LabelComponent from '@/app_core/unit/components/LabelComponent.vue';


interface IProps {
  color?: typeof validators.color[number],
}


const props = defineProps<IProps>();
const {getClasses} = classesFromPropsHook(props,
    componentName, componentNameClass, noClassAttributes, validators);

</script>

<style lang="scss">
@import '../../../assets/styles/base.scss';

.label {
  &__color {
    &__white    { color: $white;        }
    &__black    { color: $black;        }
    &__green    { color: $text-green;   }
    &__green-2  { color: $text-green-2; }
    &__gray     { color: $text-gray;    }
    &__gray-2   { color: $text-gray-2;  }
    &__gray-3   { color: $text-gray-3;  }
    &__gray-4   { color: $text-gray-4;  }
    &__gray-5   { color: $text-gray-5;  }
    &__blue     { color: $text-blue;    }
    &__red      { color: $text-red;     }
  }
}

</style>
