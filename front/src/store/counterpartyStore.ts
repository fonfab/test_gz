import {computed, ref} from 'vue';
import {defineStore} from 'pinia';
import {baseUrls} from '@/store/index';
import useRequest from '@/app_core/core/assets/scripts/hooks/requestHook';


const url = baseUrls.main + '/counterparties';

const request = useRequest();

export const useCounterpartyStore = defineStore('counterparty', () => {
  const list = ref([]);
  const isLoading = ref<boolean>(false);

  const getList = computed(() => list.value);


  const loadList = async () => {
    debugger;
    return await request.get(url)
        .then((data) => {
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


export default useCounterpartyStore;
