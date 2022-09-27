<template>
  <div class="card-main">
    <LabelStyled :text="props.title"
                 :fontSize="28"
                 color="gray-3"/>


    <div class="card-main__content">
      <template v-for="item in props.items" :key="item">
        <div class="card-main__content__icon"
             :class="['card-main__content__icon-' + item.icon]"/>

        <LabelStyled :text="item.text"
                     :fontSize="18"
                     color="gray-4"/>
      </template>
    </div>

    <div class="card-main__button">
      <ButtonStyled :text="props.buttonTitle"
                    :href="props.buttonHref"
                    type="main"
                    subtype="main-second"
                    iconUrl="icons/arrow.svg"
                    iconType="svg"
                    iconPosition="right"
                    :iconSizeWidth="32"
                    :iconSizeHeight="12"/>
    </div>

    <div class="card-main__image"
         :class="[`card-main__image__type-${props.colorType}`]">

      <div class="card-main__image-1">
        <div class="card-main__image__icon"/>
      </div>

      <div class="card-main__image-2"/>
      <div class="card-main__image-3"/>
    </div>

  </div>
</template>


<script lang="ts">
export default {};
</script>


<script setup lang="ts">
import {EColorType, ICardMainStructItem} from '@/store/types';

import LabelStyled from '@/app_core/unit/components_styled/LabelStyled.vue';
import ButtonStyled from '@/app_core/unit/components_styled/ButtonStyled.vue';


interface IProps {
  title: string,
  buttonTitle: string,
  buttonHref: string,
  colorType: EColorType,
  items: ICardMainStructItem
}

const props = defineProps<IProps>();

</script>


<style lang="scss">
@import "src/assets/styles/base";

.card-main {
  position: relative;
  width: 100%;
  height: 535px;
  padding: 48px;

  display: grid;
  grid-auto-flow: row;
  grid-auto-rows: max-content;
  grid-row-gap: 60px;

  background: #FFFFFF;
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);

  border-radius: 20px;

  z-index: 1;

  &__content {
    display: grid;
    grid-template-columns: max-content 152px;
    grid-auto-rows: 50px;
    grid-column-gap: 18px;
    grid-row-gap: 36px;
    align-items: center;

    &__icon {
      height: 34px;
      width: 34px;
      background: $text-gray-5;
      mask-size: contain;

      &-1 {mask: url("../../../public/icons/main_page/icon_1.svg") no-repeat center;}
      &-2 {mask: url("../../../public/icons/main_page/icon_2.svg") no-repeat center;}
      &-3 {mask: url("../../../public/icons/main_page/icon_3.svg") no-repeat center;}
      &-4 {mask: url("../../../public/icons/main_page/icon_4.svg") no-repeat center;}
      &-5 {mask: url("../../../public/icons/main_page/icon_5.svg") no-repeat center;}
      &-6 {mask: url("../../../public/icons/main_page/icon_6.svg") no-repeat center;}
      &-7 {mask: url("../../../public/icons/main_page/icon_7.svg") no-repeat center;}
      &-8 {mask: url("../../../public/icons/main_page/icon_8.svg") no-repeat center;}
      &-9 {mask: url("../../../public/icons/main_page/icon_9.svg") no-repeat center;}
    }
  }

  &__button {
    display: flex;
    justify-content: flex-end;
  }

  &__image {
    --color-main: #00C3C8;
    --color-second: #00828C;
    --icon: url("../../../public/icons/main_page/icon_3.svg") no-repeat center;

    position: absolute;
    right: 0;
    top: 55%;
    width: 122px;
    height: 148px;

    transform: translateY(-50%);

    &__icon {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 60px;
      height: 76px;

      transform: translate(-50%, -50%);

      mask: var(--icon);
      mask-size: contain;
      background: $white;
    }

    &__type {
      &-green {
        --color-main: #00C3C8;
        --color-second: #00828C;
        --icon: url("../../../public/icons/main_page/icon_3.svg") no-repeat center;
      }

      &-blue {
        --color-main: #50AFF0;
        --color-second: #0079C2;
        --icon: url("../../../public/icons/main_page/icon_10.svg") no-repeat center;
      }

      &-purple {
        --color-main: #AA6EC8;
        --color-second: #8C469B;
        --icon: url("../../../public/icons/main_page/icon_11.svg") no-repeat center;}
    }

    &-1 {
      width: 100%;
      height: 100%;

      background: linear-gradient(120.96deg, var(--color-main) 11.04%, var(--color-second) 86.04%);
      border-radius: 4px 0 0 4px;
    }

    &-2 {
      position: absolute;
      top: 0;
      right: 0;
      width: 99px;
      height: 26px;

      transform: translateY(-100%);

      background: linear-gradient(120.96deg, var(--color-main) 11.04%, var(--color-second) 86.04%);
      border-radius: 4px 0 0 0;
    }

    &-3 {
      position: absolute;
      top: 0;
      right: 0;
      width: 76px;
      height: 26px;

      transform: translateY(-200%);

      background: linear-gradient(120.96deg, var(--color-main) 11.04%, var(--color-second) 86.04%);
      border-radius: 4px 0 0 0;
    }
  }
}

</style>
