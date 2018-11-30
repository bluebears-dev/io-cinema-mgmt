import Vue from 'vue'
import Router from 'vue-router'
import cookie from '../utils/cookie'

Vue.use(Router)

// ******************* Routes ******************* //

const router = new Router({
  routes: [
    {
      path: '/kino',
      name: 'CinemaSelection',
      component: require('@/views/AppCinemaSelection.vue').default
    },
    {
      path: '/repertuar',
      component: require('@/views/AppMovie.vue').default,
      children: [
        {
          path: '',
          name: 'Movies',
          component: require('@/components/AppMovie/MovieList.vue').default
        }
      ]
    },
    {
      path: '/cennik',
      name: 'Pricing'
    },
    {
      path: '/kontakt',
      name: 'Contact'
    },
    {
      path: '/',
      beforeEnter: (to, from, next) => {
        let cinemaCookie = cookie.get('cinema')
        if (to.name !== 'CinemaSelection' && cinemaCookie.value == null) {
          next({name: 'CinemaSelection'})
        } else {
          next({name: 'Movies'})
        }
      }
    }
  ]
})

// ********** Global Navigation Guards ********** //

router.beforeEach((to, from, next) => {
  let cinemaCookie = cookie.get('cinema')
  if (to.name !== 'CinemaSelection' && (cinemaCookie.value == null || cinemaCookie.value === '')) {
    next({name: 'CinemaSelection'})
  } else {
    next()
  }
})

export default router
