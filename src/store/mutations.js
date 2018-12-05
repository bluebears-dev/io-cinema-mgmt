const mutations = {
  SET_CURRENT_CINEMA (state, cinema) {
    state.currentCinema = cinema
  },
  SET_CINEMAS (state, cinemas) {
    state.cinemas = cinemas
  },
  SET_MOVIES (state, movies) {
    state.movies = movies
  },
  SET_TICKET_TYPES (state, ticketTypes) {
    state.ticketTypes = ticketTypes
  }
}

export default mutations
