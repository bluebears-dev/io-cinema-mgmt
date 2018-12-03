import axios from 'axios'

const api = [
  {
    cinema: 1,
    title: 'Jak zdać IO?',
    cover: '/static/bohemian.jpg'
  },
  {
    cinema: 1,
    title: 'Jak zdać Wzorce?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 2,
    title: 'Jak zdać MISS?',
    cover: '/static/bohemian.jpg'
  },
  {
    cinema: 2,
    title: 'Jak zdać AGH?',
    cover: '/static/bighero.png'
  },
  {
    cinema: 2,
    title: 'Jak zdać AIMO?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 3,
    title: 'Jak zdać Prawo?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 3,
    title: 'Jak zdać PWIR?',
    cover: '/static/bighero.png'
  }
]

const actions = {
  setCurrentCinema ({commit, dispatch}, cinema) {
    commit('SET_CURRENT_CINEMA', cinema)
    dispatch('requestMovies', cinema)
  },
  requestCinemas ({state, commit}) {
    if (state.cinemas.length === 0) {
      axios.get('cinema/')
        .then((response) => {
          commit('SET_CINEMAS', response.data)
        })
    }
  },
  requestMovies ({state, commit}) {
    let movies = api.filter(v => v.cinema === state.currentCinema)
    commit('SET_MOVIES', movies)
  }
}

export default actions
