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
  }
}

export default getters
