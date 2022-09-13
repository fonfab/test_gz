<template>
  <ButtonComponent :class="[...getClasses, ...getAdditionalClasses]"
                   :disabled="props.disabled"/>
</template>


<script lang="ts">

export const componentName = 'ButtonStyled';
export const componentNameClass = 'button';

export const noClassAttributes = ['disabled'];
export const validators = {
  type: ['main', 'label'] as string[],
  subtype: [
    'main-first', 'main-first-blur', 'main-second', 'main-decline',
    'main-blue',
    'main-green', 'main-green-line',
    'label-green', 'label-black', 'label-blue',
    'label-white', 'label-gray', 'icon',
    'label-icon', 'main-green-blur',
  ] as string[],
  disabled: [true, false] as boolean[],
};

export default {};
</script>


<script setup lang="ts">
import {computed} from 'vue';
import classesFromPropsHook from '@/app_core/core/assets/scripts/hooks/classesFromPropsHook';

import ButtonComponent from '@/app_core/unit/components/ButtonComponent.vue';


interface IProps {
  type?: typeof validators.type[number],
  subtype?: typeof validators.subtype[number],
  disabled?: boolean,
}


const props = defineProps<IProps>();
const {getClasses} = classesFromPropsHook(props,
    componentName, componentNameClass, noClassAttributes, validators);

const getAdditionalClasses = computed(() => [
  props.disabled && `button__subtype__${props.subtype}__disabled`,
]);

</script>

<style lang="scss">
@import '../../../assets/styles/base.scss';

.button {
  &__type {
    &__main {
      padding: 16px 32px;
      border-radius: 54px;

      &:active {
        transform: scale(1);
      }
    }

    &__label {
      width: max-content;
      padding: 0;

      justify-content: inherit;

      border: none;
      border-radius: 0;

      .icon {
        background: none;
      }

      &:hover {
        border: none;
        background: none;

        .icon {
          background: none;
        }
      }

      &:active {
        transform: scale(1);
      }
    }
  }

  &__subtype {
    &__main {
      &-first {
        border: 1px solid $text-blue;

        .label {
          color: $text-blue;
        }

        &:hover {
          background: $text-blue;
          border: 1px solid $text-blue;

          .label {
            color: $white;
          }
        }

        &+.router-link-active {
          pointer-events: none;

          background: $text-blue;
          border: 1px solid $text-blue;

          .label {
            color: $white;
          }
        }
      }

      &-second {
        border: 1px solid $text-blue;
        background: $text-blue;

        .label {
          color: $white;
        }

        .icon {
          background: $white;
        }

        &:hover {
          background: transparent;
          border: 1px solid $text-blue;

          .label {
            color: $text-blue;
          }

          .icon {
            background: $text-blue;
          }
        }
      }

      &-green {
        border: 1px solid #E3FFF4;
        background: #E3FFF4;

        .label {
          color: #0DC895;
        }

        .icon {
          background: #0DC895;
        }

        &__disabled {
          pointer-events: none;

          border: 1px solid #F6F6F6;
          background: #F6F6F6;

          .label {
            color: #B3B3B3;
          }

          .icon {
            background: #B3B3B3;
          }
        }

        &:hover {
          background: #0DC895;
          border: 1px solid #0DC895;

          .label {
            color: white;
          }

          .icon {
            background: white;
          }
        }
      }

      &-blue {
        border: 1px solid #F2F7FC;
        background: #F2F7FC;

        .label {
          color: #0079C2;
        }

        .icon {
          background: #0079C2;
        }

        &__disabled {
          pointer-events: none;

          border: 1px solid #F6F6F6;
          background: #F6F6F6;

          .label {
            color: #B3B3B3;
          }

          .icon {
            background: #B3B3B3;
          }
        }

        &:hover {
          background: #0079C2;
          border: 1px solid #0079C2;

          .label {
            color: white;
          }

          .icon {
            background: white;
          }
        }
      }

      &-red {
        border: 1px solid #FFF5F5;
        background: #FFF5F5;

        .label {
          color: #FC6770;
        }

        .icon {
          background: #FC6770;
        }

        &__disabled {
          pointer-events: none;

          border: 1px solid #F6F6F6;
          background: #F6F6F6;

          .label {
            color: #B3B3B3;
          }

          .icon {
            background: #B3B3B3;
          }
        }

        &:hover {
          background: #FC6770;
          border: 1px solid #FC6770;

          .label {
            color: white;
          }

          .icon {
            background: white;
          }
        }
      }
    }

    &__label {
      &-white {
        .label {
          color: $white;
        }

        .icon {
          background: $white;
        }

        &:hover {
          .label {
            color: $white;
          }

          .icon {
            background: $white;
          }
        }
      }

      &-gray {
        .label {
          color: #D8D8D8;
        }

        .icon {
          background: #D8D8D8;
        }

        &:hover {
          .label {
            color: black;
          }

          .icon {
            background: black;
          }
        }
      }

      &-light-blue {
        .label {
          color: #BEE6FF;
        }

        .icon {
          background: #BEE6FF;
        }

        &:hover {
          .label {
            color: $white;
          }

          .icon {
            background: $white;
          }
        }
      }
    }
  }
}

</style>
