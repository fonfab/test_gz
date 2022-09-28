import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import CounterpartyView from '@/views/CounterpartyView.vue';
import DealView from '@/views/DealView.vue';
import ReportView from '@/views/ReportView.vue';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/counterparty',
    name: 'Counterparty',
    component: CounterpartyView,
  },
  {
    path: '/deal',
    name: 'Deal',
    component: DealView,
  },
  {
    path: '/report',
    name: 'report',
    component: ReportView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
