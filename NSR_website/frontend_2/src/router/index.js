import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/index'
import Explore from '@/views/explore'
import About from '@/views/about'
import Testmap from '@/views/testmap'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'welcome to NSR',
      component: Index
    },
    {
      path: '/explore',
      name: 'Explore',
      component: Explore
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/testmap',
      name: 'test',
      component: Testmap
    }
  ]
})
