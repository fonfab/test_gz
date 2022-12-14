import {computed, ref} from 'vue';
import {defineStore} from 'pinia';
import {baseUrls} from '@/store/index';
import useRequest from '@/app_core/core/assets/scripts/hooks/requestHook';

import {ICounterparty} from '@/store/types';


const url = baseUrls.main + '/counterparties';

const request = useRequest();

export const useCounterpartyStore = defineStore('counterparty', () => {
  const list = ref<ICounterparty[]>([]);
  const isLoading = ref<boolean>(false);

  const getList = computed<ICounterparty[]>(() => list.value);


  const loadList = async (): Promise<ICounterparty[]> => {
    isLoading.value = true;
    return await request.get(url)
        .then((data: ICounterparty[]) => {
          list.value = data;
          return data;
        })
        .finally(() => isLoading.value = false);
  };

  const deleteList = async (ids: number[]) => {
    isLoading.value = true;
    const requests = ids.map((item) => {
      request.delete(url + '/' + item);
    });

    Promise.all(requests)
        .then(() => {
          list.value = list.value.filter((item) => !ids.includes(item.id));
        })
        .finally(() => isLoading.value = false);
  };

  return {
    getList,

    loadList,
    deleteList,
  };
});


export default useCounterpartyStore;
