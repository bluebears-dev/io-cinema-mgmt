import Vue from 'vue'
import Router from 'vue-router'
import cookie from '../utils/cookie'

Vue.use(Router)

// ******************* Routes ******************* //

const toolbar = require('@/components/AppToolbar.vue').default

const router = new Router({
  routes: [
    {
      path: '/kino',
      name: 'CinemaSelection',
      components: {
        default: require('@/views/AppCinemaSelection.vue').default,
        toolbar: require('@/components/AppToolbar/ToolbarWrapper.vue').default
      }
    },
    {
      path: '/repertuar',
      components: {
        default: require('@/views/AppMovie.vue').default,
        toolbar
      },
      children: [
        {
          path: '',
          name: 'Movies',
          components: {
            default: require('@/components/AppMovie/MovieList.vue').default,
            toolbar
          }
        },
        {
          path: ':id',
          name: 'MovieDetails',
          components: {
            default: require('@/components/AppMovie/MovieDetails.vue').default,
            toolbar
          },
          props: {
            default: true,
            toolbar: false
          }
        }
      ]
    },
    {
      path: '/cennik',
      name: 'Prices',
      components: {
        default: require('@/views/AppPrices.vue').default,
        toolbar
      }
    },
    {
      path: '/rezerwuj/:id',
      name: 'BookingForm',
      components: {
        default: require('@/views/AppBookingForm.vue').default,
        toolbar
      },
      props: {
        default: true,
        toolbar: false
      }
    },
    {
      path: '/kontakt',
      name: 'Contact',
      components: {
        default: require('@/views/AppCinema.vue').default,
        toolbar
      }
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
    },
    {
      path: '/404',
      alias: '*',
      name: 'NotFound',
      components: {
        default: require('@/views/AppNotFound.vue').default,
        toolbar
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
