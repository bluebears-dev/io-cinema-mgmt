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
  },
  SET_SELECTED_DATE (state, selectedDate) {
    state.selectedDate = selectedDate
  },
  SET_MOVIE_DETAILS (state, movieDetails) {
    state.movieDetails = movieDetails
  },
  SET_SHOWINGS (state, showings) {
    state.showings = showings
  },
  SET_ROOM (state, room) {
    state.room = room
  },
  ADD_SHOWING (state, showing) {
    if (state.showings && state.showings.findIndex(v => v.id === showing.id) === -1) {
      state.showings.push(showing)
    }
  }
}

export default mutations
