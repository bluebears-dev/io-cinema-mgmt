import axios from 'axios'

const actions = {
  setCurrentCinema ({commit, dispatch}, cinema) {
    commit('SET_CURRENT_CINEMA', cinema)
    dispatch('requestMovies', cinema)
  },
  requestCinemas ({state, commit}) {
    if (state.cinemas.length === 0) {
      return axios.get('cinemas/')
        .then((response) => {
          commit('SET_CINEMAS', response.data)
        })
    }
  },
  requestMovies ({state, commit}) {
    return axios.get(state.currentCinema + '/' + state.selectedDate.date + '/movies')
      .then((response) => {
        commit('SET_MOVIES', response.data)
      })
  },
  requestTicketTypes ({state, commit}) {
    if (state.ticketTypes.length === 0) {
      return axios.get('prices/')
        .then((response) => {
          commit('SET_TICKET_TYPES', response.data)
        })
    }
  },
  requestMovieDetails ({state, commit}, id) {
    return axios.get('movies/' + id)
      .then(response => {
        commit('SET_MOVIE_DETAILS', response.data)
      })
  },
  requestShowings ({state, commit}, id) {
    return axios.get(state.currentCinema + '/' + id + '/' + state.selectedDate.date + '/showings')
      .then(response => {
        commit('SET_SHOWINGS', response.data)
      })
  }
}

export default actions
