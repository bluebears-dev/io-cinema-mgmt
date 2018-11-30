const api = [
  {
    cinema: 'Kraków',
    title: 'Jak zdać IO?',
    cover: '/static/bohemian.jpg'
  },
  {
    cinema: 'Kraków',
    title: 'Jak zdać Wzorce?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 'Rzeszów',
    title: 'Jak zdać MISS?',
    cover: '/static/bohemian.jpg'
  },
  {
    cinema: 'Rzeszów',
    title: 'Jak zdać AGH?',
    cover: '/static/bighero.png'
  },
  {
    cinema: 'Rzeszów',
    title: 'Jak zdać AIMO?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 'Warszawa',
    title: 'Jak zdać Prawo?',
    cover: '/static/miserables.jpg'
  },
  {
    cinema: 'Warszawa',
    title: 'Jak zdać PWIR?',
    cover: '/static/bighero.png'
  }
]

const actions = {
  setCurrentCinema ({state, commit, dispatch}, cinema) {
    commit('SET_CURRENT_CINEMA', cinema)
    dispatch('requestMovies', cinema)
  },
  requestMovies ({state, commit}, cinema) {
    let movies = api.filter(v => v.cinema === cinema)
    commit('SET_MOVIES', movies)
  }
}

export default actions
