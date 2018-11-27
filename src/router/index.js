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
      component: require('@/views/AppCinemaSelection.vue').default,
      beforeEnter: (to, from, next) => {
        let cinemaCookie = cookie.get('cinema')
        if (cinemaCookie.value == null) {
          next()
        } else {
          next({ name: 'Movies' })
        }
      }
    },
    {
      path: '/repertuar',
      name: 'Movies',
      component: require('@/views/AppCinemaSelection.vue').default,
      props: true
    },
    {
      path: '*',
      redirect: '/repertuar'
    }
  ]
})

// ********** Global Navigation Guards ********** //

router.beforeEach((to, from, next) => {
  let cinemaCookie = cookie.get('cinema')
  if (cinemaCookie.value == null) {
    next(false)
  } else {
    next()
  }
})

export default router
