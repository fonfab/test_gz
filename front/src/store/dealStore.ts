import {computed, ref} from 'vue';
import {defineStore} from 'pinia';
import {baseUrls} from '@/store/index';
import useRequest from '@/app_core/core/assets/scripts/hooks/requestHook';

import {ICounterparty} from '@/store/types';


const url = baseUrls.main + '/deals';

const request = useRequest();

export const useDealStore = defineStore('deal', () => {
  const list = ref<ICounterparty[]>([]);
  const isLoading = ref<boolean>(false);
  const counterpartyId = ref<string | number>('');

  const getList = computed<ICounterparty[]>(() => list.value);


  const setCounterpartyId = (id: string | number) => {
    counterpartyId.value = id;
  };

  const loadList = async (): Promise<ICounterparty[]> => {
    let currentUrl = url;

    if (counterpartyId.value) currentUrl += `?counterparty_id=${counterpartyId.value}`;

    return await request.get(currentUrl)
        .then((data: ICounterparty[]) => {
          list.value = data;
          return data;
        })
        .finally(() => isLoading.value);
  };

  const clearList = () => {
    setCounterpartyId('');
    list.value = [];
  };

  return {
    getList,

    setCounterpartyId,
    loadList,

    clearList,
  };
});


export default useDealStore;
