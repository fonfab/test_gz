import {computed, ref} from 'vue';
import {defineStore} from 'pinia';
import {baseUrls} from '@/store/index';
import useRequest from '@/app_core/core/assets/scripts/hooks/requestHook';

import {IReport} from '@/store/types';


const url = baseUrls.main + '/report';

const request = useRequest();

export const useReportStore = defineStore('report', () => {
  const list = ref<IReport[]>([]);
  const isLoading = ref<boolean>(false);

  const getList = computed<IReport[]>(() => list.value);


  const loadList = async (): Promise<IReport[]> => {
    isLoading.value = true;
    return await request.get(url)
        .then((data: IReport[]) => {
          list.value = data;
          return data;
        })
        .finally(() => isLoading.value = false);
  };

  const clearList = () => {
    list.value = [];
  };

  return {
    getList,

    loadList,
    clearList,
  };
});


export default useReportStore;
