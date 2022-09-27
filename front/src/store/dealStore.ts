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

  const getList = computed<ICounterparty[]>(() => list.value);


  const loadList = async (): Promise<ICounterparty[]> => {
    return await request.get(url)
        .then((data: ICounterparty[]) => {
          list.value = data;
          return data;
        })
        .finally(() => isLoading.value);
  };

  return {
    getList,

    loadList,
  };
});


export default useDealStore;
