const getters = {
  getCurrentCinema (state) {
    return state.currentCinema
  },
  getCinemas (state) {
    return state.cinemas
  },
  getMovies (state) {
    return state.movies
  },
  getCinemaDetails (state) {
    return state.cinemas.find(e => e.id === state.currentCinema)
  },
  getTicketTypes (state) {
    return state.ticketTypes
  },
  getSelectedDate (state) {
    return state.selectedDate
  },
  getMovieDetails (state) {
    return state.movieDetails
  },
  getShowings (state) {
    return state.showings
  }
}

export default getters
